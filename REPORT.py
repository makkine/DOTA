import os
import os.path
import Bilingual
import Stats
import Hero_Tag_dicts
import Lang_dicts
from collections import defaultdict
import time
import sys
import hero
import getopt
import prestige

begin_millis = int(round(time.time() * 1000))

#Command line stuff to code:
#Finding data for a word
#Printing hero info or lang info

#Returns an array containing all the files in folders ending with "_Parsed"
def folder_walk():
  parsed = []
  d = os.path.abspath(os.path.join('./', os.pardir))
  for subdir, dirs, files in os.walk(d):
	for dirname in dirs:
		if dirname.endswith('_Parsed') or dirname.endswith('_parsed'):
			parsed += [dirname]
  return parsed

#Game_entries is a dictionary, tag is each game id, content is dictionary where 
#tag is player name, content is a player type
def fill_game_entries(folders):
	game_entries = {}
	d = os.path.abspath(os.path.join('./', os.pardir))
	for p in folders:
		for subdir, dirs, files in os.walk(d+'\\'+p):
			for filename in files:
				game_entries[filename] = {}
				onefile = open(d+'\\'+p+'/'+filename, 'r')
				for line in onefile:
					aslist = line.strip().split(',')
					### this really sucks but I can't think of a better way to do it :(
					if aslist[0] == 'chat':
						if aslist[2] not in game_entries[filename]:
							game_entries[filename][aslist[2]] = Bilingual.Player({}, {'eng': 0, 'spn': 0, 'dota': 0, 'uncat': 0}, "nolang")
						else:
							game_entries[filename][aslist[2]].c[aslist[1]] = aslist[3]
	return game_entries

def lang_profiles(entries):
  for game in entries:
   for hero in entries[game]:
	for chat in entries[game][hero].c:
	  Bilingual.create_lang_profiles(entries[game][hero], entries[game][hero].c[chat])

### This is a function that looks in various dictionaries (English monolingual 
## and Spanish monolingual). You put the word you want to search for in this form
## '[word]' as the input to the function and it returns a count for that word in each dict.  
def search_for_word(searchword, mono_spn_wthCounts, mono_eng_wthCounts, complete_wthCounts, totals):
  for (c,w) in mono_spn_wthCounts:
	if w == searchword:
	  print('number of times %s is said in Spanish: ' % searchword + str(c))
	  print ('%s makes up ' % searchword + str(100 * (float("{0:.4f}".format(float(c) / float(totals['spn']))))) + '% of the total spanish tokens')
  for (c,w) in mono_eng_wthCounts:
	if w == searchword:
	  print ('number of times %s is said in English: ' % searchword + str(c))
	  print ('%s makes up ' % searchword + str(100 * (float("{0:.4f}".format(float(c) / float(totals['eng']))))) + '% of the total English tokens')     
  for (c,w) in complete_wthCounts:
	if w == searchword:
	  print ('number of times %s is said overall: ' % searchword + str(c))
	  print ('%s makes up ' % searchword + str(100 * (float("{0:.4f}".format(float(c) / float(totals['total']))))) + '% of the total tokens')

##Finds and prints all chats in category containing "lang" (so you can print all
## entries categorized as "english" with spanish or dota words. Set as "total" to 
## get all the chats)
def print_chats(entries, lang):
  for item in entries:
	if lang == "total" or item.lp[lang] > 0:
	  for chat in item.c:
		print(item.c[chat])

#Prints the language of all the players in a list of games
def print_speaker_makeup(entries):
  for game in entries:
	print(game)
	# print(game + ":")
	# sys.stdout.write(entries[game][player].lang + " ")
	# print("")

def total_chats(entries):
  total = 0
  for game in entries:
	for hero in entries[game]:
	  total += len(entries[game][hero].c)
  return total

##Main method
def main(argv):
  folders = folder_walk()
  entries = fill_game_entries(folders)
  lang_profiles(entries)

  ##Lang entries
  total_lang_entries = Bilingual.get_players(entries, 'total')
  spn_lang_entries = Bilingual.get_players(entries, 'spn')
  eng_lang_entries = Bilingual.get_players(entries, 'eng')
  bilingual_lang_entries = Bilingual.get_players(entries, 'bilingual')
  dota_lang_entries = Bilingual.get_players(entries, 'dota')
 
  #Prints out instances of code-switching w/in the same line
  # Bilingual.single_line_switch(total_lang_entries)

  ##Totals
  speaker_counts = Bilingual.get_total_speaker_count(entries)
  word_totals = Bilingual.get_word_totals(entries)

  ##Command line stuff
  ##Running py -2 REPORT.py -n 700 -w "peru" returns the stats for "peru"
  ##in the top 700 words. Avoid placing -n after -w for the time being.
  opts, args = getopt.getopt(argv, "w:n:")
  top_N = 200
  for opt, arg in opts:
	if opt == "-n":
	  top_N = int(arg)
	if opt == "-w":
	  spn_dict = Stats.find_top_N_words(spn_lang_entries, top_N, "spanish")
	  eng_dict = Stats.find_top_N_words(eng_lang_entries, top_N, "english")
	  total_dict = Stats.find_top_N_words(total_lang_entries, top_N, "total")
	  search_for_word(arg, spn_dict, eng_dict, total_dict, word_totals)


  ##Other required variables
  classified_entries = Bilingual.classify_entries(entries)

  eng_freq = Stats.lang_frequency_by_speaker_category(eng_lang_entries)
  eng_prcnt = Stats.find_percentage('dota', eng_freq)

  spn_freq = Stats.lang_frequency_by_speaker_category(spn_lang_entries)
  spn_prcnt = Stats.find_percentage('dota', spn_freq)

  biling_freq = Stats.lang_frequency_by_speaker_category(bilingual_lang_entries)
  biling_freq_dota = Stats.find_percentage('dota', biling_freq)
  biling_freq_eng = Stats.find_percentage('eng', biling_freq)
  biling_freq_spn = Stats.find_percentage('spn', biling_freq)

  h_stats = hero.hero_stats(entries)

  ##############
  # SPEAKER INFO
  ##############
  print('--------------------------------------------------------------')
  print('Total number of speakers: ' + str(speaker_counts['total']))
  print('Total number of DJ users: ' + str(speaker_counts['any_dota']))
  print('English speakers who speak no dota: ' + str(speaker_counts['eng_no_dota_cnt']))
  print('Spanish speakers who speak no dota: ' + str(speaker_counts['spn_no_dota_cnt']))
  print('Bilingual speakers who speak no dota: ' + str(speaker_counts['bi_no_dota_cnt']))
  # print('English Speakers: ' + str(speaker_counts['mono_eng']))
  # print('Spanish Speakers: ' + str(speaker_counts['mono_spn']))
  # print('Bilinguals: ' + str(speaker_counts[bilingual_cnt]))
  # print('Dota only: ' + str(speaker_counts[mono_dota]))
  # print('No lang: ' + str(speaker_counts[no_lang]))

  ####################
  ##### TOKEN INFO ###
  ####################
  print('Total Tokens: ' + str(word_totals['total']))
  print('Total English Tokens: ' + str(word_totals['eng']))
  print('Total Spanish Tokens: ' + str(word_totals['spn']))
  print('Total Dota Tokens: ' + str(word_totals['dota']))
  print('Total Uncategorized Tokens: ' + str(word_totals['uncat']))
  print('Total Categorized Tokens: ' + str(word_totals['cattotal']))

  ###################
  # LANGUAGE INFO ###
  ###################
  print('You speak english?')
  print('How much Eng you use brah?: ' + str(eng_freq['eng']))
  print('How much Dotes you use brah?: ' + str(eng_freq['dota']))
  print('How much uncategorized, brah?: ' + str(eng_freq['uncat']))
  print('What percentage Dota? brah?: ' + str(eng_prcnt))
  print('-------------------------------------')

  print('yo hablo espanol?')
  print('how much spanish you use hermano? ' + str(spn_freq['spn']))
  print('how much dotes you use hermano? ' + str(spn_freq['spn']))
  print('how much uncategorized, hermano?: ' + str(spn_freq['uncat']))
  print('What percentage Dota? hermano?: ' + str(spn_prcnt))
  print('--------------------------------------')

  print('yo hablo both?')
  print('how much english do you use?: ' + str(biling_freq['eng']))
  print('how much spanish you use hermano? ' + str(biling_freq['spn']))
  print('how much dotes you use hermano? ' + str(biling_freq['dota']))
  print('how much uncategorized, hermano?: ' + str(biling_freq['uncat']))
  print('What percentage Dota? hermano?: ' + str(biling_freq_dota))
  print('What percentage of English?: ' + str(biling_freq_eng))
  print('What percentage of Spanish?: ' + str(biling_freq_spn))
  print('---------------------------------------')

  #####################
  ## TOP WORDS INFO ###
  #####################
  ###This section of reporting gives you the most frequent words for each 
  ###category of speaker Total, English, Spanish, bilingual, Dota
  # top_N = 50
  # print('DATA FOR ALL SPEAKERS')
  # print('cutoff N =',top_N)
  # def print_top_words(lang_entries, top_N, lang):
  #   vek = Stats.find_top_N_words(lang_entries, top_N, lang)
  #   for(w, c) in vek:
  #     sys.stdout.write("('")
  #     sys.stdout.write(str(c))
  #     sys.stdout.write("', ")
  #     sys.stdout.write(str(w))
  #     sys.stdout.write(") ")
  # NOTE: Third parameter is the full name of the lang, not "spn", "eng", etc.
  # print('Top words in English:')
  # print_top_words(eng_lang_entries, top_N, "english")

  ####################
  ## CHAT PRINTING ###
  ####################
  # print("BILINGUAL CHATS")
  # print_chats(bilingual_lang_entries, "total")
  # print("ENGLISH CHATS")
  # print_chats(eng_lang_entries, "total")
  # print("SPANISH CHATS")
  # print_chats(spn_lang_entries, "Total")


  #######################
  ### GAMES BY LANGUAGE #
  #######################
  #print('English games: ' + str(Bilingual.get_entries(classified_entries, "eng")))
  Eng_n_spn = Bilingual.get_entries(classified_entries, "eng", "spn")
  print('English and Spanish only: ' + str(Eng_n_spn))
  #print('----------------------------------------')
 # print('Bilingual only: ' + str(Bilingual.get_entries(classified_entries, "bilingual")))
  print_speaker_makeup(Eng_n_spn)


  ##########################
  ## CHAT AND GAME COUNTS ##
  ##########################
  # number_of_games = len(entries)            
  # number_of_chats = total_chats(entries)
  # average_chats_per_game = float("{0:.2f}".format(float(number_of_chats) / float(number_of_games)))
  # # # print('Number of chats: ' + str(number_of_chats))
  # # print('Number of games: ' + str(number_of_games))
  # # print 'Average chats per game: ' + str(average_chats_per_game)

  #################
  # HERO AVERAGES #
  #################


  ##########################
  # SPEAKER MAKEUP REPORTS #
  ##########################
  #print_speaker_makeup(total_lang_entries)


  ############
  # KDA, MMR #
  ############
  # print("Total mentions of kda in English:" + str(prestige.ex_amounts(eng_lang_entries, '\d+/\d+')))
  # print("Total mentions of mmr in English:" + str(prestige.ex_amounts(eng_lang_entries, '\d0{3}|\dk')))

if __name__ == "__main__" : main(sys.argv[1:])
  
# average_chat_length = "{0:.2f}".format(float(total_chat_length) / float(total_chats))
  
# compare_hero_total = {}
# for h,n in average_by_hero.items():
#   compare_hero_total[h] = "{0:.2f}".format(float(average_by_hero[h]) - float(average_chat_length))
  
  
# compare_tag_total = {}
# for h,n in average_by_tag.items():
#   compare_tag_total[h] = "{0:.2f}".format(float(average_by_tag[h]) - float(average_chat_length))

  
# compare_hero_tag = {}
# for t,h in tag_dict.items():
#   for hero in h:
#     compare_hero_tag[hero+'- '+t] = "{0:.2f}".format(float(average_by_hero[hero]) - float(average_by_tag[t]))

	
# compare_tag_hero = {}
# for t,h in tag_dict.items():
#   for hero in h:
#     compare_tag_hero[t+'- '+hero] = "{0:.2f}".format(float(average_by_hero[hero]) - float(average_by_tag[t]))
	
# compare_hero_tag_keys = sorted(compare_hero_tag.keys())   
# compare_tag_hero_keys = sorted(compare_tag_hero.keys())
####COMMENTED OUT WHILE I'M FIXING LENGTH SHIT 

#------------------------------------------
#This starts the reporting section, uncomment a section to get the report
#--------------------------------------------

#----------------------------------------
#COMPARISON SECTION
#------------------------------------------


# print '---------------------------------'
# print 'Hero Average compared to tag average, sorted by tag'
# print '------------------------------------'
# for item in compare_tag_hero_keys:
  # print item + ': ' + str(compare_tag_hero[item])



# print '---------------------------------'
# print 'Hero Average compared to tag average, sorted by hero'
# print '------------------------------------'
# for item in compare_hero_tag_keys:
  # print item + ': ' + str(compare_hero_tag[item])

# print '---------------------------------'
# print 'Hero Average compared to overall average'
# print '------------------------------------'
# for item in compare_hero_total:
  # print item + ': ' + str(compare_hero_total[item])


# print '---------------------------------'
# print 'Tag Average compared to overall average'
# print '------------------------------------'
# for item in compare_tag_total:
  # print item + ': ' + str(compare_tag_total[item])
  
  
  
#------------------------------------------------
#RAW DATA SECTION
#---------------------------------------------------- 
  

# print '---------------------------------'
# print 'Overall Statistics'
# print '---------------------------------'
# print 'total chats: ' + str(total_chats)

# print 'total chat length: ' + str(total_chat_length)

# print 'average chat length: ' + str(average_chat_length)


#-----------------------------------------
# REPORT BY TAG
#-----------------------------------------

# print '------------------------------------'
# print 'Chats by Tag'
# print '------------------------------------'
# for item in chats_by_tag:
  # print item + ': ' + str(chats_by_tag[item])
  
# print '------------------------------------'
# print 'Length by Tag'
# print '------------------------------------'
# for item in length_by_tag:
  # print item + ': ' + str(length_by_tag[item])
  
# print '------------------------------------'
# print 'Average by Tag'
# print '------------------------------------'
# for item in average_by_tag:
  # print item + ': ' + str(average_by_tag[item])
  

#-------------------------------------------
# REPORT BY HERO
#--------------------------------------------

# print '------------------------------------'
# print 'Chats by Hero'
# print '------------------------------------'
# for item in chats_by_hero:
  # print item + ': ' + str(chats_by_hero[item])
  
# print '------------------------------------'
# print 'Length by Hero'
# print '------------------------------------'
# for item in length_by_hero:
  # print item + ': ' + str(length_by_hero[item])
  
# print '------------------------------------'
# print 'Average by Hero'
# print '------------------------------------'
# for item in average_by_hero:
  # print item + ': ' + str(average_by_hero[item])

end_millis = int(round(time.time() * 1000))
print(str(end_millis - begin_millis))