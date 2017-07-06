import Hero_Tag_dicts
import Lang_dicts
import Stats
dota = 'dota'
spanish = 'spanish'
unclear = 'unclear'
english = 'english'

#Player class contains everything said by that player in the game and 
#A four-part array representing the language use as three numbers each symbolizing
#how many words in a given language were said by that player, in the form
#[English, Spanish, DoTA, uncategorized]
class Player():
    def __init__(self, chat, lang_profile, l):
      self.c = chat #Dict of chats. Tag is timestamp, content is chat content
      self.lp = lang_profile 
      self.lang = l #Language probably spoken by this player


## Prints out all instances of code-switching w/in the same line. Honestly I 
## took a look at the output and the vaaast majority is just noise, which indicates
## this is a fairly uncommon mode of code switching.
def single_line_switch(entries):
  for player in entries:
    for chat in player.c:
      lang = "unknown"
      newlist = player.c[chat].strip().split(' ')
      newlist = [x.strip("''") for x in newlist]
      for word in newlist:
        if word in Lang_dicts.lang_index:
          w_lang = Lang_dicts.lang_index[word]
          if w_lang == english:
            if lang == "unknown" or lang == "english":
              lang = "english"
            else:
              print(word)
              print(player.c[chat])
          elif w_lang == spanish:
            if lang == "unknown" or lang == "spanish":
              lang = "spanish"
            else:
              print(word)
              print(player.c[chat])

##Given a chat said by a hero, modifies that hero's lang_profile according to
#What is contained in chat
def create_lang_profiles(hero, chat):
  newlist = chat.strip().split(' ')
  newlist = [x.strip("''") for x in newlist]
  for word in newlist:
    if word not in Lang_dicts.lang_index:
      hero.lp['uncat'] += 1
    else:
      word = Lang_dicts.lang_index[word]
      if word == english:
        hero.lp['eng'] += 1
      elif word == spanish:
        hero.lp['spn'] += 1
      elif word == dota:
        hero.lp['dota'] += 1
      else:
        hero.lp['uncat'] += 1
  ##Should go in own function
  if hero.lp['spn'] > 0:
    if hero.lp['eng'] > 0:
      bilingual_percent = bilingual_percentages(hero.lp)
      if bilingual_percent < 0.1:
        if bilingual_percent > 0.01:
          hero.lang = "bilingual"
        else: 
          hero.lang = "spn"
      else:
        hero.lang = 'eng'
    else: hero.lang = "spn"
  elif hero.lp["eng"] > 0:
    hero.lang = "eng"
  elif hero.lp["dota"] > 0:
    hero.lang = "dota"
  elif hero.lp["uncat"] > 0:
    hero.lang = "unknown"



#Gets total word count by language
def get_word_totals(entries):
  lang_tokens = {'eng': 0, 'spn': 0, 'dota': 0, 'uncat': 0, 'cattotal': 0, 'total': 0}
  for game in entries:
    for hero in entries[game]:
      lang_tokens['eng'] += entries[game][hero].lp['eng']
      lang_tokens['spn'] += entries[game][hero].lp['spn']
      lang_tokens['dota'] += entries[game][hero].lp['dota']
      lang_tokens['uncat'] += entries[game][hero].lp['uncat']
      cattotal = entries[game][hero].lp['eng'] + entries[game][hero].lp['spn'] + entries[game][hero].lp['dota']
      lang_tokens['cattotal'] += cattotal
      lang_tokens['total'] += cattotal + entries[game][hero].lp['uncat']
  return lang_tokens

#Gets total speaker count
def get_total_speaker_count(entries):
  speaker_counts = {'total': 0, 'any_dota': 0, 'mono_eng': 0, 'mono_spn': 0, 
                    'mono_dota': 0, 'bilingual_cnt': 0, 'no_lang': 0, 'eng_no_dota_cnt': 0, 
                    'spn_no_dota_cnt': 0, 'bi_no_dota_cnt': 0}
  for game in entries:
    for hero in entries[game]:
      speaker_counts['total'] += 1
      if entries[game][hero].lp['dota'] > 0: ## this is horrible
        speaker_counts['any_dota'] += 1
        if entries[game][hero].lp['eng'] == 0 and entries[game][hero].lp['spn'] == 0:
            speaker_counts['mono_dota'] += 1
        elif entries[game][hero].lp['eng'] > 0 and entries[game][hero].lp['spn'] > 0:
          speaker_counts['bilingual_cnt'] += 1
      elif entries[game][hero].lp['eng'] > 0:
        speaker_counts['eng_no_dota_cnt'] +=1
        if entries[game][hero].lp['spn'] == 0:
          speaker_counts['mono_eng'] += 1
        else: 
          speaker_counts['bilingual_cnt'] += 1
          speaker_counts['bi_no_dota_cnt'] +=1
      elif entries[game][hero].lp['spn'] > 0:
        speaker_counts['mono_spn']+= 1
        speaker_counts['spn_no_dota_cnt'] += 1
      else: 
        speaker_counts['no_lang'] += 1
  return speaker_counts

## Creates a dictionary listing all the games containing those languages
def classify_entries(entries):
  games = {'eng': {}, 'spn': {}, 'dota': {}, 'nolang': {}, 'unknown': {}, 'bilingual':{}}
  for game in entries:
    for player in entries[game]:
        games[entries[game][player].lang][game] = entries[game]
  return games

##Must be called with the result of classify_entries and a list of langs in
##their string representation. Returns all the entries that contain ALL and ONLY 
##the langs get_entries was called with

###COMMENT THIS BETTER ;__;
def get_entries(classified_entries, *langs):
  games = []
  init_lang = langs[0]
  lang_list = langs[1:]
  for game in classified_entries[init_lang]:
    add_game = True
    for lang in classified_entries:
      if lang in langs:
        if game not in classified_entries[lang]:
          add_game = False
      elif game in classified_entries[lang] and lang != "unknown" and lang != "nolang":
        add_game = False
    if add_game:
      games.append(game)
  return games

#returns a list of all the players that speak lang (lang can be "total")
def get_players(entries, lang):
  players = []
  for game in entries:
    for hero in entries[game]:
      if entries[game][hero].lang == lang or lang == "total":
          players.append(entries[game][hero])
  return players


##Returns a negative # if spanish is greater than english, 0 if they are the same, 
##and a positive number if english is greater than spanish.
def bilingual_percentages(lang_profile):
  spanish_percent = Stats.find_percentage('spn', lang_profile)
  english_percent = Stats.find_percentage('eng', lang_profile)
  return english_percent - spanish_percent