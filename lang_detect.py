from __future__ import division ##Division is floating-point by default
import Bilingual
import REPORT
import sys
import getopt
import Lang_dicts


##Will have to fix get_players in bilingual and REPORT after changing lang detection

folders = REPORT.folder_walk()
entries = REPORT.fill_game_entries(folders)

spanish_txt = ""

def classify(entries):
    lang_entries = {'spn': "", 'eng': ""}  ##Entries classified by language spoken
    for game in entries:
        for player in entries[game]:
            for chat in entries[game][player].c:
                language = {'eng': 0, 'spn': 0, 'other': 0, 'tot': 0}
                newlist = entries[game][player].c[chat].strip().split(' ')
                newlist = [x.strip("''") for x in newlist]
                for word in newlist:
                    language['tot'] += 1
                    if word.lower() not in Lang_dicts.lang_index:
                        language['other'] += 1
                    else:
                        word = Lang_dicts.lang_index[word.lower()]
                        if word == "english":
                            language['eng'] += 1
                        elif word == "spanish":
                            language['spn'] += 1
                        else:
                            language['other'] += 1
                if language['other'] < 2 * language['spn']:
                    lang_entries['spn'] += " " + entries[game][player].c[chat][1: -1]
                if language['other'] < 2 * language['eng']:
                    lang_entries['eng'] += " " + entries[game][player].c[chat][1: -1]
    lang_entries['eng'] = lang_entries['eng'][:len(lang_entries['spn'])]
    ##This is the worst thing I've ever done but I guess it'll have to do.
    ##Basically just trims the english chats to be the same length as the spanish chats
    return lang_entries

lang_entries = classify(entries)

##Creates n-grams and sorts by count (most frequent first)
##returns a list of ngrams as tuples, in order of frequency.
##First element of each tuple is the ngram, the second is the percent found in english
##So, for instance ('the', .77) means that 77% of instances of "the" are found in 
##the english block of text. 
##(n-grams are just the text split into n-character blocks, for example:
## (n-g), (-gr), (gra), (ram), (ams), (ms ), (s a), ( ar), (are), (re ))
def ngram(txt, n):
    max = len(txt)
    ngrams = {}

    ##places in dict
    for x in xrange(n, max):
        ngram = txt[x-n : x].lower()
        ngrams[ngram] = 0

    ##counts
    for x in xrange(n, max):
        ngram = txt[x-n : x].lower()
        ngrams[ngram] += 1

    return ngrams


##Should be part of a class or something
eng_grams = ngram(lang_entries['eng'], 3)
spn_grams = ngram(lang_entries['spn'], 3)

sorted_eng = sorted(eng_grams, key = eng_grams.__getitem__, reverse = True)
sorted_spn = sorted(spn_grams, key = spn_grams.__getitem__, reverse = True)

##Value for missing keys
NOT_FOUND = 1000

#Returns delta from standard ngrams. 
##As it is now, however, the LOWEST number represents the most likely language - 
##I've been playing around, and close values suggest heavy DoTA, code-switching, 
##or non-english/spanish samples, which we need to come up with a different way of 
## differentiating between. 
def detect(chat):
    unsorted_ngrams = ngram(chat, 3)
    notfound_count = 0
    ngrams = sorted(unsorted_ngrams, key = unsorted_ngrams.__getitem__, reverse = True)
    probs = {"eng": 0, "spn": 0}
    for ng in ngrams:
        if ng in sorted_eng:
            probs["eng"] += abs(ngrams.index(ng) - sorted_eng.index(ng))
            if ng in spn_grams:
                probs["spn"] += abs(ngrams.index(ng) - sorted_spn.index(ng))
            else:
                probs["spn"] += NOT_FOUND
        elif ng in sorted_spn:
            probs["spn"] += abs(ngrams.index(ng) - sorted_spn.index(ng))
            probs["eng"] += NOT_FOUND  
        else:
            probs["spn"] += NOT_FOUND
            notfound_count += 1
    return probs


def detect_percentages(chat):
    ngrams = ngram(chat, 3)
    probs = {"eng": 0, "spn": 0}
    notfound_count = 0
    for ng in ngrams:
        spn_prob = 1
        eng_prob = 0
        if ng in eng_grams:
            if ng in spn_grams:
                eng_prob = eng_grams[ng] / (eng_grams[ng] + spn_grams[ng])
            else:
                eng_prob = 1
        elif ng not in spn_grams:
            spn_prob = 0
            notfound_count += 1
        probs["eng"] += eng_prob
        probs["spn"] += (spn_prob - eng_prob)
    for lang in probs:
        probs[lang] = probs[lang] / len(ngrams)
    print("Unknown n-grams (a high count probably means the text is not in english or spanish): " + str(notfound_count))
    return probs

## From the command line, the command "py -2 -c "whatever"" will give you the language 
## detection for that line. 
def main(argv):
    opts, args = getopt.getopt(argv, "c:")
    top_N = 200
    arg = "gg xD wp noob"
    for opt, arg in opts:
        if opt == "-c":
            chat = arg
    print("Chat to analyse: " + arg)
    print(detect(arg))
    print(detect_percentages(arg))

if __name__ == "__main__" : main(sys.argv[1:])