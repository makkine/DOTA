import Bilingual
import REPORT
import Lang_dicts

##Will have to fix get_players in bilingual and REPORT after changing lang detection

##Add - lowercase, get rid of numbers, we just want words, words words ...

folders = REPORT.folder_walk()
entries = REPORT.fill_game_entries(folders)
spn_lang_entries = Bilingual.get_players(entries, 'spn')
eng_lang_entries = Bilingual.get_players(entries, 'eng')

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
##returns a list of ngrams in order of frequency
def ngram(txt, n):
    max = len(txt)
    ngrams = {}

    ##places in dict
    for x in xrange(n, max):
        ngram = txt[x-n : x]
        ngrams[ngram] = 0

    ##counts
    for x in xrange(n, max):
        ngram = txt[x-n : x]
        ngrams[ngram] += 1

    return sorted(ngrams, key = ngrams.__getitem__, reverse = True)

eng_grams = ngram(lang_entries['eng'], 3)
spn_grams = ngram(lang_entries['spn'], 3)

##Value for missing keys
NOT_FOUND = 1000

###Given a chat, returns percentage probabilities for lang groups
###as a tuple
def detect(chat):
    ngrams = ngram(chat, 3)
    probs = {"eng": 0, "spn": 0}
    for ng in ngrams:
        if ng in eng_grams:
            probs["eng"] += abs(ngrams.index(ng) - eng_grams.index(ng))
        else:
            probs["spn"] += NOT_FOUND
        if ng in spn_grams:
            probs["spn"] += abs(ngrams.index(ng) - spn_grams.index(ng))
        else:
            probs["spn"] += NOT_FOUND
    return probs


print(detect("MANES MI SUPPORT TIENE MALESTRON Y MALLAS NO JODAN REPORT PLEASE"))