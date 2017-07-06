### This is an attempt to find the vector over all data
def fill_words(entries):
  complete_dict = {}
  for item in entries:
    for hero in item:
      aslist = []
      aslist += hero.chat
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

def counts(dictionary):
  complete_wthCounts = []
  complete_tot = 0
  for(w, c) in list(dictionary.items()):
    complete_wthCounts += [(c, w)]
    complete_tot += c
  return complete_wthCounts

##Lang Dictionary
class Lang_Dictionary():
    def __init__(self, dictionary, lang):
        self.d = dictionary
        self.l = lang

# give counts for the the top N most frequent
##NOTE: Speaker_makeup_of_game is called both here and in get_entries, see if you can 
##make it more efficient somehow
#lang must be in the form 'spn', 'eng', 'bilingual', 'dota', etc
def find_top_N_words(dictionary, entries, lang, top_N):
  ##wc is the wthCounts list only sorted
  complete_wc = sorted(counts(dictionary), reverse=True)
  speaker_makeup = speaker_makeup_of_game(entries)
  ###vek is a list of the top_N words (no counts)
  complete_vek = [wd for (cnt, wd) in complete_wc[:top_N]]
  dictionary = Lang_Dictionary({}, lang)
  for game in speaker_makeup:
    if lang in game:
      aslist = []
      aslist += speaker_makeup[game]
      j = ','.join(aslist)
      words = j.split(' ')
      for line in words: 
        word = line.strip().split(',')
        for i in word:
          word = i.split(',')
          word = str(word).replace('\'', '')
          word = word.replace('""', '')
          word = word.replace('"', '')
          if len(word) > 0:
            ##INEFFICIENT - looking through dictionary each time?
            if word not in dictionary.dictionary:
              dictionary.dictionary[word] = 0
            dictionary.dictionary[word] += 1
  return dictionary



######OLD_CODE

###wthCounts is a list of the word and its count              
bilingual_wthCounts = []
bilingual_tot = 0
for (w,c) in list(bilingual_dict.items()):
    bilingual_wthCounts += [(c,w)]
    bilingual_tot += c

##wc is the wthCounts list only sorted
bilingual_wc = sorted(bilingual_wthCounts,reverse=True)

top_N = 200 # give counts for the the top N most frequent

###vek is a list of the top_N words (no counts)
bilingual_vek = [wd for (cnt,wd) in bilingual_wc[:top_N]]
