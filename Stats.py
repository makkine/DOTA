# -*- coding: utf-8 -*-

import Hero_Tag_dicts
import sys
import Lang_dicts
import nltk
from nltk.stem.snowball import SpanishStemmer
from nltk.stem.snowball import EnglishStemmer

##Stats.py finds word vectors, average chat length, word counts

### This is an attempt to find the vector over all data
def fill_words(entries):
    complete_dict = {}
    for item in entries:
        for hero in entries[item]:
            aslist = []
            aslist += entries[item][hero].c
            j = ','.join(aslist)
            words = j.split(' ')
            for line in words:
                word = line.strip().split(',')
                for i in word:
                    word = i.split(',')
                    word = str(word).replace('\'', '')
                    word = word.replace('"', '')
                    if len(word) > 0:
                        if word not in complete_dict:
                            complete_dict[word] = 0
                        complete_dict[word] += 1
    return complete_dict

##Lang Dictionary
class Lang_Dictionary():
    def __init__(self, dictionary, lang):
        self.d = dictionary
        self.l = lang

##This is horribly circular but here's nmy thought for language detection:
## - Detect chat language by using existing top 1000 words, then lemmatize accordingly
## - idk wtf to do w single-line switch, probably just ignore.
## - Once top 1000 lemmas have been categorized, re-categorize speakers accordingly.


# give counts for the the top N most frequent
##players must be players that speak language
def find_top_N_words(lang_entries, top_N, lang):
    dictionary = Lang_Dictionary({}, lang)
    for player in lang_entries:
        for chat in player.c:
            language = {'eng': 0, 'spn': 0, 'other': 0, 'tot': 0}
            sentence = player.c[chat]
            newlist = player.c[chat].strip().split(' ')
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
            if language['other'] < 2 * (language['spn'] + language['eng']):
               print(sentence)
               if language['spn'] > language['eng']:
                   print("SPANISH")
                   stemmer = SpanishStemmer()
               else:
                   print("ENGLISH")
                   stemmer = EnglishStemmer()
            aslist = []
            aslist += sentence
            sentence =""
            j = ''.join(aslist)
            words = j.split(' ')
            for line in words:
                line = str(line).replace('\'', '')
                line = line.replace('""', '')
                line = line.replace('"', '')
                if len(line) > 0:
                    if language["other"] < 2 * (language['spn'] + language["eng"]):
                        sentence += stemmer.stem(line.encode(sys.stdout.encoding, errors = 'replace')) + " "
                        print(sentence)
                    ##INEFFICIENT - looking through dictionary each time?
                    if line.lower() not in dictionary.d:
                        dictionary.d[line.lower()] = 0
                    dictionary.d[line.lower()] += 1

    ###wthCounts is a list of the word and its count
    wthCounts = []
    for(w,c) in dictionary.d.iteritems():
        wthCounts += [(c,w)]
    ##wc is the wthCounts list only sorted
    wc = sorted(wthCounts, reverse=True)
    return wc[:top_N]


##Returns a [english, spanish, DoTA, uncategorized] for all words in speaker category
def lang_frequency_by_speaker_category(lang_entries):
    lang_breakdown = {'eng': 0, 'spn': 0, 'dota': 0, 'uncat': 0}
    for item in lang_entries:
        lang_breakdown['eng'] += item.lp['eng']
        lang_breakdown['spn'] += item.lp['spn']
        lang_breakdown['dota'] += item.lp['dota']
        lang_breakdown['uncat'] += item.lp['uncat']
    return lang_breakdown

#finds the percentage of lang1 words in lang2 speakers (dota in english,
# dota in spanish, spanish in bilingual, etc ...)
# lang1 must be a string in 'eng', 'spn', etc format, lang2 is the result of a
# call to lang_frequency_by_speaker_category
def find_percentage(lang1, lang2):
    total = float(lang2['eng'] + lang2['spn'] + lang2['dota'] + lang2['uncat'])
    return(float("{0:.2f}".format(float(lang2[lang1])/ total)))

#topw is top 10 or whatever words
##### Creates a CSV file with the top 10 words as fields, then
## Lists the # of instances of each word per player. Also has
## fields for relevant hero stats
def csv(entries, topw):
    ret = "uniqID, gender, difficulty, role, " + topw[0][1] #String to be returned
    dict = {}
    dict[topw[0][1]] = 0
    for (count, word) in topw[1:]:
        ret+= ",{0}".format(word)
        dict[word] = 0
    dict["total"] = 0
    ret += ", total words, total chats\n"
    for game in entries:
        for player in entries[game]:
            if player != "null":
                chatn = 0
                uniqname = game + "-" + player
                htype = entries[game][player].type
                ret += uniqname + ", " + htype[0]+ ", "  + htype[2]+ ", " + htype [1]
                for word in dict:
                    dict[word] = 0
                for chat in entries[game][player].c:
                    chatn += 1
                    newlist = entries[game][player].c[chat].strip().split(' ')
                    newlist = [x.strip("''") for x in newlist]
                    for word in newlist:
                        if word in dict:
                            dict[word] += 1
                        dict["total"] += 1
                for word in dict:
                    ret += ", {0}".format(dict[word])
                ret += ", " + str(chatn) + "\n"
    return ret

## Creates a CSV file with the game name, number of spanish, bilingual,
## DoTA and english players as fields.
# def csv_games(entries):
#     ret = "game, spanish, english, bilingual, DoTA, none, other, total\n"
#     players = [0,0,0,0,0,0,0]
#     for game in entries:
#         for player in entries[game]:
#             players[6] += 1
#             if



                ######OLD_CODE

                # top_N = 200 # give counts for the the top N most frequent

                # ###vek is a list of the top_N words (no counts)
                # bilingual_vek = [wd for (cnt,wd) in bilingual_wc[:top_N]]
                # chatDict = {}

                # total_chats = 0
                # total_chat_length = 0
                # length_by_hero = {}
                # chats_by_hero = {}
                # average_by_hero = {}

                # langdic = defaultdict(list)
                # hero_entries = defaultdict(list)
                # game_entries = {} # a dictionary whose keys are gameids (filenames) and the value is a list of all the things
                # game_entries_with_heronames = {} #The same dictionary as above only with the hero names included before the chats
                # #said during that game

                # chats_per_game = {}

                # word_finder_cnt = 0