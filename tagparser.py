import os

chatDict = {}

folders_parsed = []
for subdir, dirs, files in os.walk('./'):
    for dirname in dirs:
        if dirname.endswith('_Parsed'):
            # print('yes - '+dirname)
            folders_parsed += [dirname]
        # else:
        #     print('no - '+dirname)

# puts words and their counts into chatDict
# chatDict is a dictionary with the word as index and number of repetitions as value		
for p in folders_parsed: 
    for subdir, dirs, files in os.walk('./'+p):
        for filename in files:
            # print filename
            onefile = open('./'+p+'/'+filename, 'r')
            for line in onefile:
                aslist = line.strip().split(',')
                if aslist[0] == 'chat':
                    # print aslist
                    j = ','.join(aslist[3:])
                    words = j.split(' ')
                    for word in words:
                        word = word.strip("'")
                        if len(word) > 0:
                            if word not in chatDict:
                                chatDict[word] = 0
                            chatDict[word] += 1

#wthCounts is a list of the word and its count							
wthCounts = []
tot = 0
for (w,c) in chatDict.items():
    wthCounts += [(c,w)]
    tot += c

# wc is the wthCounts list only sorted
wc = sorted(wthCounts,reverse=True)

top_N = 18 # give counts for the the top N most frequent

#vek is a list of the top_N words (no counts)
vek = [wd for (cnt,wd) in wc[:top_N]]


# print 'cutoff N =',top_N
# print 'word vek =',vek

#####give counts for the the top N most frequent words
# print '---------------------------'
# for (w,c) in wc[:top_N]:
    # print c,w
# print '---------------------------'



#---------------------------------------------------------------------- 
# vekDic is a dictionary of dictionaries 
# the top level keys are hero_id_strings 
# below that the keys are words in chats
# for each of these the values are counts for that word by that hero
# we added one dummy hero entry: 
# 'npc_dota_hero_Skrillex' is a catch-all for all chats by all heroes
#
# Note that above we are only including the 'top_N' most frequent words 
#---------------------------------------------------------------------- 

vekDic = {}
vekDic['npc_dota_hero_Skrillex'] = {}
for wd in vek: 
    vekDic['npc_dota_hero_Skrillex'][wd] = 0

for p in folders_parsed: 
    for subdir, dirs, files in os.walk('./'+p):
        for filename in files:
            # print filename
            onefile = open('./'+p+'/'+filename, 'r')
            for line in onefile:
                aslist = line.strip().split(',')
                if aslist[0] == 'chat':
                    hero = aslist[2]
                    if hero not in vekDic:
                        vekDic[hero] = {}
                        for wd in vek: 
                            vekDic[hero][wd] = 0
                    j = ','.join(aslist[3:])
                    words = j.split(' ')
                    for word in words:
                        word = word.strip("'")
                        if len(word) > 0:
                            if word in vek: 
                                vekDic[hero][word] += 1
                                vekDic['npc_dota_hero_Skrillex'][word] += 1


# print vekDic

#---------------------------------------------------------------------- 
# hero_dict is a dictionary whose keys are hero_id_tags and whose 
# values are in-game category tags describing attributes of heroes
# 
# tags '1','2','3' = indicators difficulty of play 
# tags 'female', 'male', 'neuter' = presented gender of hero
# tags 'agi', 'int', 'str' = main attribute hero uses 
# the other tags mark in-gagme categories of relevence 
# 
# except for difficulty level and gender and main attribute, tags are not (usually) mutually  
# exclusive and are not used uniformly or exuaustively across heroes
#---------------------------------------------------------------------- 

# h_tags is a list of tags
h_tags = ['1', '2', '3', 
          'female', 'male', 'neuter',
          'agi', 'int', 'str',
          'carry', 'disabler', 'durable', 'escape', 'initiator',  
          'jungler',  'melee',  'nuker', 'pusher', 'ranged', 'support']


hero_dict = {}
hero_dict['npc_dota_hero_antimage'] = ['male', 'melee', 'agi', 'carry', 'escape', 'nuker', '1']
hero_dict['npc_dota_hero_axe'] = ['male', 'melee', 'str', 'initiator', 'durable', 'disabler', 'jungler']
hero_dict['npc_dota_hero_bane'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'durable', '2']
hero_dict['npc_dota_hero_bloodseeker'] = ['male', 'melee', 'agi', 'carry', 'disabler', 'nuker', 'jungler', 'initiator', '1']
hero_dict['npc_dota_hero_crystal_maiden'] = ['female', 'ranged', 'int', 'support', 'disabler', 'nuker', 'jungler', '1']
hero_dict['npc_dota_hero_drow_ranger'] = ['female', 'ranged', 'agi', 'carry', 'disabler', 'pusher', '1']
hero_dict['npc_dota_hero_earthshaker'] = ['male', 'melee', 'str', 'initiator', 'support', 'disabler', 'nuker']
hero_dict['npc_dota_hero_juggernaut'] = ['male', 'melee', 'agi', 'carry', 'pusher', 'escape', '1']
hero_dict['npc_dota_hero_mirana'] = ['female', 'ranged', 'agi', 'carry', 'escape', 'nuker', 'support', 'disabler', '2']
hero_dict['npc_dota_hero_nevermore'] = ['male', 'ranged', 'agi', 'carry', 'nuker', '2']
hero_dict['npc_dota_hero_morphling'] = ['male', 'ranged', 'agi', 'carry', 'escape', 'nuker', 'durable', 'disabler', '3']
hero_dict['npc_dota_hero_phantom_lancer'] = ['male', 'melee', 'agi', 'carry', 'escape', 'nuker', 'pusher', '2']
hero_dict['npc_dota_hero_puck'] = ['female', 'ranged', 'int', 'initiator', 'disabler', 'nuker', 'escape', '2']
hero_dict['npc_dota_hero_pudge'] = ['male', 'melee', 'str', 'initiator', 'durable', 'disabler', 'nuker']
hero_dict['npc_dota_hero_razor'] = ['male', 'ranged', 'agi', 'carry', 'durable', 'nuker', 'pusher', '1']
hero_dict['npc_dota_hero_sand_king'] = ['male', 'melee', 'str', 'initiator', 'escape', 'disabler', 'nuker', 'jungler']
hero_dict['npc_dota_hero_storm_spirit'] = ['male', 'ranged', 'int', 'carry', 'disabler', 'nuker', 'initiator', 'escape', '3']
hero_dict['npc_dota_hero_sven'] = ['male', 'melee', 'str', 'carry', 'durable', 'disabler', 'initiator', 'nuker']
hero_dict['npc_dota_hero_tiny'] = ['male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'nuker', 'pusher', 'durable']
hero_dict['npc_dota_hero_vengefulspirit'] = ['female', 'ranged', 'agi', 'support', 'escape', 'nuker', 'initiator', 'disabler', '1']
hero_dict['npc_dota_hero_windrunner'] = ['female', 'ranged', 'int', 'support', 'disabler', 'nuker', 'carry', 'escape', '2']
hero_dict['npc_dota_hero_zuus'] = ['male', 'ranged', 'int', 'nuker', '1']
hero_dict['npc_dota_hero_kunkka'] = ['male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'nuker', 'durable']
hero_dict['npc_dota_hero_lina'] = ['female', 'ranged', 'int', 'support', 'disabler', 'nuker', 'carry', '1']
hero_dict['npc_dota_hero_lich'] = ['male', 'ranged', 'int', 'support', 'nuker', '1']
hero_dict['npc_dota_hero_lion'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'initiator', '1']
hero_dict['npc_dota_hero_shadow_shaman'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'pusher', 'initiator', '1']
hero_dict['npc_dota_hero_slardar'] = ['male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'durable', 'escape']
hero_dict['npc_dota_hero_tidehunter'] = ['male', 'melee', 'str', 'initiator', 'durable', 'disabler', 'nuker']
hero_dict['npc_dota_hero_witch_doctor'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', '1']
hero_dict['npc_dota_hero_riki'] = ['male', 'melee', 'agi', 'carry', 'escape', 'disabler', '1']
hero_dict['npc_dota_hero_enigma'] = ['male', 'ranged', 'int', 'pusher', 'disabler', 'initiator', 'jungler', '2']
hero_dict['npc_dota_hero_tinker'] = ['male', 'ranged', 'int', 'carry', 'pusher', 'nuker', '2']
hero_dict['npc_dota_hero_sniper'] = ['male', 'ranged', 'agi', 'carry', 'nuker', '1']
hero_dict['npc_dota_hero_necrolyte'] = ['male', 'ranged', 'int', 'carry', 'disabler', 'nuker', 'durable', '1']
hero_dict['npc_dota_hero_warlock'] = ['male', 'ranged', 'int', 'support', 'disabler', 'initiator', '1']
hero_dict['npc_dota_hero_beastmaster'] = ['male', 'melee', 'str', 'initiator', 'durable', 'disabler', 'nuker']
hero_dict['npc_dota_hero_queenofpain'] = ['female', 'ranged', 'int', 'carry', 'escape', 'nuker', '2']
hero_dict['npc_dota_hero_venomancer'] = ['male', 'ranged', 'agi', 'support', 'initiator', 'nuker', 'pusher', 'disabler', '1']
hero_dict['npc_dota_hero_faceless_void'] = ['male', 'melee', 'agi', 'carry', 'escape', 'initiator', 'disabler', 'durable', '2']
hero_dict['npc_dota_hero_skeleton_king'] = ['male', 'melee', 'str', 'initiator', 'support', 'disabler', 'durable', 'carry']
hero_dict['npc_dota_hero_death_prophet'] = ['female', 'ranged', 'int', 'carry', 'disabler', 'nuker', 'pusher', '1']
hero_dict['npc_dota_hero_phantom_assassin'] = ['female', 'melee', 'agi', 'carry', 'escape', '1']
hero_dict['npc_dota_hero_pugna'] = ['male', 'ranged', 'int', 'pusher', 'nuker', '2']
hero_dict['npc_dota_hero_templar_assassin'] = ['female', 'ranged', 'agi', 'carry', 'escape', '2']
hero_dict['npc_dota_hero_viper'] = ['male', 'ranged', 'agi', 'carry', 'durable', 'initiator', 'disabler', '1']
hero_dict['npc_dota_hero_luna'] = ['female', 'ranged', 'agi', 'carry', 'pusher', 'nuker', '1']
hero_dict['npc_dota_hero_dragon_knight'] = ['male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'nuker', 'durable', 'pusher']
hero_dict['npc_dota_hero_dazzle'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', '1']
hero_dict['npc_dota_hero_rattletrap'] = ['male', 'melee', 'str', 'initiator', 'durable', 'disabler', 'nuker']
hero_dict['npc_dota_hero_leshrac'] = ['male', 'ranged', 'int', 'carry', 'disabler', 'nuker', 'support', 'pusher', '1']
hero_dict['npc_dota_hero_furion'] = ['male', 'ranged', 'int', 'carry', 'escape', 'nuker', 'jungler', 'pusher', '2']
hero_dict['npc_dota_hero_life_stealer'] = ['male', 'melee', 'str', 'durable', 'jungler', 'disabler', 'carry', 'escape']
hero_dict['npc_dota_hero_dark_seer'] = ['male', 'ranged', 'int', 'initiator', 'disabler', 'escape', 'jungler', '2']
hero_dict['npc_dota_hero_clinkz'] = ['male', 'ranged', 'agi', 'carry', 'escape', 'pusher', '2']
hero_dict['npc_dota_hero_omniknight'] = ['male', 'melee', 'str', 'durable', 'support', 'nuker']
hero_dict['npc_dota_hero_enchantress'] = ['female', 'ranged', 'int', 'support', 'disabler', 'pusher', 'jungler', 'durable', '2']
hero_dict['npc_dota_hero_huskar'] = ['male', 'ranged', 'str', 'initiator', 'carry', 'durable']
hero_dict['npc_dota_hero_night_stalker'] = ['male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'nuker', 'durable']
hero_dict['npc_dota_hero_broodmother'] = ['female', 'melee', 'agi', 'carry', 'escape', 'nuker', 'pusher', '2']
hero_dict['npc_dota_hero_bounty_hunter'] = ['male', 'melee', 'agi', 'escape', 'nuker', '1']
hero_dict['npc_dota_hero_weaver'] = ['male', 'ranged', 'agi', 'carry', 'escape', '2']
hero_dict['npc_dota_hero_jakiro'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'pusher', '1']
hero_dict['npc_dota_hero_batrider'] = ['male', 'ranged', 'int', 'initiator', 'disabler', 'escape', 'jungler', '2']
hero_dict['npc_dota_hero_chen'] = ['male', 'ranged', 'int', 'support', 'pusher', 'jungler', '3']
hero_dict['npc_dota_hero_spectre'] = ['female', 'melee', 'agi', 'carry', 'escape', 'durable', '2']
hero_dict['npc_dota_hero_doom_bringer'] = ['male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'nuker', 'durable']
hero_dict['npc_dota_hero_ancient_apparition'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', '2']
hero_dict['npc_dota_hero_ursa'] = ['male', 'melee', 'agi', 'carry', 'jungler', 'durable', 'disabler', '1']
hero_dict['npc_dota_hero_spirit_breaker'] = ['male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'durable', 'escape']
hero_dict['npc_dota_hero_gyrocopter'] = ['male', 'ranged', 'agi', 'carry', 'disabler', 'nuker', '1']
hero_dict['npc_dota_hero_alchemist'] = ['male', 'melee', 'str', 'initiator', 'support', 'disabler', 'nuker', 'carry', 'durable']
hero_dict['npc_dota_hero_invoker'] = ['male', 'ranged', 'int', 'carry', 'disabler', 'nuker', 'escape', 'pusher', '3']
hero_dict['npc_dota_hero_silencer'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'carry', 'initiator', '2']
hero_dict['npc_dota_hero_obsidian_destroyer'] = ['male', 'ranged', 'int', 'carry', 'disabler', 'nuker', '2']
hero_dict['npc_dota_hero_lycan'] = ['male', 'melee', 'str', 'carry', 'pusher', 'jungler', 'durable', 'escape', '2']
hero_dict['npc_dota_hero_brewmaster'] = ['male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'nuker', 'durable']
hero_dict['npc_dota_hero_shadow_demon'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'initiator', '2']
hero_dict['npc_dota_hero_lone_druid'] = ['male', 'ranged', 'agi', 'carry', 'pusher', 'jungler', 'durable', '3']
hero_dict['npc_dota_hero_meepo'] = ['male', 'melee', 'agi', 'carry', 'escape', 'nuker', 'disabler', 'initiator', 'pusher', '3']
hero_dict['npc_dota_hero_keeper'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'jungler', '2']
hero_dict['npc_dota_hero_visage'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'pusher', 'durable', '3']
hero_dict['npc_dota_hero_disruptor'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'initiator', '2']
hero_dict['npc_dota_hero_rubick'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', '3']
hero_dict['npc_dota_hero_ogre'] = ['male', 'melee', 'int', 'support', 'disabler', 'nuker', 'durable', 'initiator', '1']
hero_dict['npc_dota_hero_nyx'] = ['male', 'melee', 'agi', 'disabler', 'initiator', 'escape', 'nuker', '2']
hero_dict['npc_dota_hero_naga'] = ['female', 'melee', 'agi', 'carry', 'escape', 'support', 'pusher', 'disabler', 'initiator', '2']
hero_dict['npc_dota_hero_undying'] = ['male', 'melee', 'str', 'nuker', 'support', 'disabler', 'durable', '1']
hero_dict['npc_dota_hero_chaos'] = ['male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'durable', 'pusher', '1']
hero_dict['npc_dota_hero_wisp'] = ['neuter', 'ranged', 'str', 'escape', 'support', 'nuker', '3']
hero_dict['npc_dota_hero_treant'] = ['male', 'melee', 'str', 'initiator', 'support', 'disabler', 'durable', 'escape', '2']
hero_dict['npc_dota_hero_magn'] = ['male', 'melee', 'str', 'initiator', 'disabler', 'nuker', 'escape', '2']
hero_dict['npc_dota_hero_cent'] = ['male', 'melee', 'str', 'initiator', 'nuker', 'disabler', 'durable', 'escape', '1']
hero_dict['npc_dota_hero_slark'] = ['male', 'melee', 'agi', 'carry', 'escape', 'nuker', 'disabler', '1']
hero_dict['npc_dota_hero_shredder'] = ['male', 'melee', 'str', 'nuker', 'durable', 'escape', '2']
hero_dict['npc_dota_hero_medusa'] = ['female', 'ranged', 'agi', 'carry', 'disabler', 'durable', '1']
hero_dict['npc_dota_hero_troll_warlord'] = ['male', 'ranged', 'agi', 'carry', 'pusher', 'disabler', 'durable', '2']
hero_dict['npc_dota_hero_techies'] = ['male', 'ranged', 'int', 'disabler', 'nuker', '2']
hero_dict['npc_dota_hero_abaddon'] = ['male', 'melee', 'str', 'carry', 'support', 'durable', '1']
hero_dict['npc_dota_hero_bristleback'] = ['male', 'melee', 'str', 'initiator', 'carry', 'nuker', 'durable', '1']
hero_dict['npc_dota_hero_abyssal_underlord'] = ['male', 'melee', 'str', 'support', 'disabler', 'nuker', 'durable', 'escape', '2']
hero_dict['npc_dota_hero_legion_commander'] = ['female', 'melee', 'str', 'initiator', 'carry', 'disabler', 'durable', 'nuker', '1']
hero_dict['npc_dota_hero_earth_spirit'] = ['male', 'melee', 'str', 'initiator', 'nuker', 'disabler', 'durable', 'escape', '3']
hero_dict['npc_dota_hero_arc_warden'] = ['neuter', 'ranged', 'agi', 'carry', 'escape', 'nuker', '3']
hero_dict['npc_dota_hero_elder_titan'] = ['male', 'melee', 'str', 'initiator', 'nuker', 'disabler', 'durable', '2']
hero_dict['npc_dota_hero_tusk'] = ['male', 'melee', 'str', 'initiator', 'nuker', 'disabler', '2']
hero_dict['npc_dota_hero_winter_wyvern'] = ['female', 'ranged', 'int', 'support', 'disabler', 'nuker', '2']
hero_dict['npc_dota_hero_ember_spirit'] = ['male', 'melee', 'agi', 'carry', 'escape', 'nuker', 'disabler', 'initiator', '2']
hero_dict['npc_dota_hero_oracle'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'escape', '3']
hero_dict['npc_dota_hero_phoenix'] = ['neuter', 'ranged', 'str', 'initiator', 'support', 'disabler', 'nuker', 'escape', '2']
hero_dict['npc_dota_hero_skywrath_mage'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', '1']
hero_dict['npc_dota_hero_terrorblade'] = ['male', 'melee', 'agi', 'carry', 'pusher', 'nuker', '2']
hero_dict['npc_dota_hero_monkey_king'] = ['male', 'melee', 'agi', 'initiator', 'carry', 'escape', 'disabler', '2']


#---------------------------------------------------------------------- 
# tag_dict is a dictionary whose keys are tags and whose 
# values are lists of heroes that are marked with that tag
#---------------------------------------------------------------------- 

tag_dict = {}

for t in h_tags:
    tag_dict[t] = []
    for (h,tag_list) in hero_dict.items():
        if t in tag_list:
            tag_dict[t] += [h]


# -- uncomment me to display lists of heroes grouped by tags
# for t in h_tags:
    # print '----------------------'
    # print 'TAG:',t
    # for h in sorted(tag_dict[t]):
        # print '    ',h
    # print '\n'
    


# def tag_report(tag_list):
    # generate a report comparing groups of heroes with tags in tag_list
    # to the group of all heroes 
    # for the top_N most frequent words [this parameter is set above]
    # R = []
    # for t in tag_list:
        # h_at_tag = tag_dict[t] #h_at_tag is a list of heroes for tag 't'
        # Tg = [t,[]] #Tg is a list of lists, the first value is tags, then a pair, words and count
        # for wd in vek:
            # n = 0
            # for H in h_at_tag: #h is a individual hero
                # if H in vekDic:
                    # w_ct = vekDic[H][wd] #w_ct is the word count (integer)
                    # n += w_ct #adding up the word counts for each hero (iteratively, so for each tag)
            # Tg[1] += [(wd,n)]
        # R += [Tg] #I think R is a list of lists
    # print 'words =',
    # for w in vek:
        # print w,
    # print 
    # for (t,l) in R:
        # tot = sum([c for (wd,c) in l]) #tot sums all the counts for al heroes
        # rtz = []
        # for (wd,cnt) in l:
            # rt = str(float(cnt)/float(tot))[1:5]
            # if len(rt) == 2:
                # rt += '0'
            # rtz += [rt]
        # print rtz,
        # print t,
        # print 'N =',tot
		

def tag_report(tag_list):
    # generate a report comparing groups of heroes with tags in tag_list
    # to the group of all heroes 
    # for the top_N most frequent words [this parameter is set above]
	Y = [] # top level hero, then words and counts
	R = [] # top level, tag, then words and counts
	
	#This one fleshes out R, the one for type comnparison
	for t in tag_list:
		h_at_tag = tag_dict[t] #h_at_tag is a list of heroes for tag 't'
		Tg = [t,[]] #Tg is a list of lists, the first value is tags, then a pair, words and count
		for wd in vek:
			n = 0
			for H in h_at_tag: #h is a individual hero
				if H in vekDic:
					w_ct = vekDic[H][wd] #w_ct is the word count (integer)
					n += w_ct #adding up the word counts for each hero (iteratively, so for each tag)
			Tg[1] += [(wd,n)]
		R += [Tg] #I think R is a list of lists
	print 'words =',
	for w in vek:
		print w,
	print 
	for (t,l) in R:
		tot = sum([c for (wd,c) in l]) #tot sums all the counts for al heroes
		rtz = []
		for (wd,cnt) in l:
			rt = str(float(cnt)/float(tot))[1:5]
			if len(rt) == 2:
				rt += '0'
			rtz += [rt]
		print rtz,
		print t,
		print 'N =',tot
	print '---------------------------'
	
	#This one fleshes out Y, the one for hero comparison
	for t in tag_list:
		hh_at_tag = tag_dict[t] #h_at_tag is a list of heroes for tag 't'
		for H in h_at_tag: #h is a individual hero
			vek_by_hero = [H,[]]
			if H in vekDic:
				for wd in vek:
					w_ct = vekDic[H][wd] #w_ct is the word count (integer)
					hero_vek = [wd,w_ct]
					vek_by_hero[1] += [(hero_vek)]
				Y += [vek_by_hero]
	#print Y

	
			
		#print rtz_hero,
		#print rtz_type
		#print t,
		#print 'N =',tot
		
print '---------------------------'

def hero_report(tag_list):
	Y = [] # top level hero, then words and counts
	R = [] # top level, tag, then words and counts
	
	#This one fleshes out R, the one for type comnparison
	for t in tag_list:
		h_at_tag = tag_dict[t] #h_at_tag is a list of heroes for tag 't'
		Tg = [t,[]] #Tg is a list of lists, the first value is tags, then a pair, words and count
		for wd in vek:
			n = 0
			for H in h_at_tag: #h is a individual hero
				if H in vekDic:
					w_ct = vekDic[H][wd] #w_ct is the word count (integer)
					n += w_ct #adding up the word counts for each hero (iteratively, so for each tag)
			Tg[1] += [(wd,n)]
		R += [Tg] #I think R is a list of lists
	print 'words =',
	for w in vek:
		print w,
	print 
	
	print '---------------------------'
	
	#This one fleshes out Y, the one for hero comparison
	for t in tag_list:
		hh_at_tag = tag_dict[t] #h_at_tag is a list of heroes for tag 't'
		for H in h_at_tag: #h is a individual hero
			vek_by_hero = [H,[]]
			if H in vekDic:
				for wd in vek:
					w_ct = vekDic[H][wd] #w_ct is the word count (integer)
					hero_vek = [wd,w_ct]
					vek_by_hero[1] += [(hero_vek)]
				Y += [vek_by_hero]
	
	
	for (t,l) in Y:
		tot_hero = sum([c for (wd,c) in l]) #tot sums all the counts for each hero
		rtz_hero = []
		for (wd,cnt) in l:
			rt_hero = str(float(cnt)/float(tot_hero))[1:5]
			if len(rt_hero) == 2:
				rt_hero += '0'
			rtz_hero += [rt_hero]
			
		print rtz_hero,
		print t
	for (q,p) in R:
		tot_type = sum([c for (wd,c) in p]) #tot sums all the counts for al heroes
		rtz_type = []
		for (wd,cnt) in p:
			rt_type = str(float(cnt)/float(tot_type))[1:5]
			if len(rt_type) == 2:
				rt_type += '0'
			rtz_type += [rt_type]
	
	
	print rtz_type,
	print q



# tag_report(['male','female'])

# print '---------------------------'                
# tag_report(['1','2','3'])

# print '---------------------------'    
# tag_report(['agi', 'int', 'str'])

print 'this is the tag report'
tag_report(['carry', 'disabler', 'durable', 'escape', 'initiator', 'jungler',  'melee',  'nuker', 'pusher', 'ranged', 'support'])

print 'this is the hero report'
hero_report(['carry', 'disabler', 'durable', 'escape', 'initiator', 'jungler',  'melee',  'nuker', 'pusher', 'ranged', 'support'])
# print '---------------------------'    
#hero_report(['carry'])#, 'disabler', 'durable', 'escape', 'initiator',  
            # 'jungler',  'melee',  'nuker', 'pusher', 'ranged', 'support'])