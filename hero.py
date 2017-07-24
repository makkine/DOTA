import Hero_Tag_dicts

#We should be able to: 
# Compare classses against the total (word freq against a total)
# We should be able to compare a hero word freq. against a total
# It would be cool to: compare a hero's word freq. with a tags word freq 


##########################################
## DOESN'T MATCH OLD VALUES - STILL IN DEBUGGING!!!! AVOID USE FOR THE TIME BEING

class Hero():
	def __init__(self, a, l, nc, c):
		self.avg = a
		self.length = l
		self.n_chats = nc
		self.chats = c ##Dict of words w word counts


class Tag():
	def __init__(self, l, nc):
		self.avg = a
		self.length = l
		self.n_chats = nc

#Returns the total words spoken in all the chats of a Player type. 
def lp_sum(player):
	total = 0
	for lang in player.lp:
		total += player.lp[lang]
	return total

# Creates an dict of Hero classes and initializes their average, length
# and chat_n fields. Length contains the total length of chats spoken by the 
# hero, average is the average length of the hero's chats, and chat_n is the 
# number of chats. dict tags are the hero names
# Also initializes their chats. 
# 'npc_dota_hero_Skrillex' is a catch-all for all chats by all heroes
def hero_stats(entries):
	heroes = {}
	heroes["npc_dota_hero_Skrillex"] = Hero(0, 0, 0, {})
	for game in entries:
		for player in entries[game]:
			if player in heroes:##Goddamn how do I avoid this
				heroes[player].length += lp_sum(entries[game][player])
				heroes[player].n_chats += len(entries[game][player].c)
			else:
				heroes[player] = Hero(0, lp_sum(entries[game][player]), len(entries[game][player].c), {})
			heroes["npc_dota_hero_Skrillex"].length += lp_sum(entries[game][player])
			heroes["npc_dota_hero_Skrillex"].n_chats += len(entries[game][player].c)
			for chat in entries[game][player].c:
					newlist = entries[game][player].c[chat].strip().split(' ')
					newlist = [x.strip("''") for x in newlist]
					for word in newlist:
						if word in heroes[player].chats:
							heroes[player].chats[word] += 1
						else:
							heroes[player].chats[word] = 1
						if word in heroes["npc_dota_hero_Skrillex"].chats:
							heroes["npc_dota_hero_Skrillex"].chats[word] += 1
						else:
							heroes["npc_dota_hero_Skrillex"].chats[word] = 1
	for hero in heroes:
		heroes[hero].avg = float("{0:.2f}".format(float(heroes[hero].length) / float(heroes[hero].n_chats)))
	return heroes


## vekDic is the resulting dictionary from calling hero_stats
## vek is top N words
## Creates a dictionary ordered by tag which contains pairs, first element is a word, second is its count
def create_list(tag_list, vekDic, vek):
	Tg = {}
	for t in tag_list:
		h_at_tag = Hero_Tag_dicts.tag_dict[t] #h_at_tag is a list of heroes for tag 't'
		Tg[t] = [] #Tg is a dictionary, the key is tags, val is a pair, words and count
		for (c, wd) in vek:
			n = 0
			for H in h_at_tag: #h is a individual hero
				if wd in vekDic[H].chats:
					n += vekDic[H].chats[wd] #adding up the word counts for each hero (iteratively, so for each tag)
			Tg[t] += [(wd,n)]
	return Tg


## Tg is the result of a call to create_list
def tag_hero_report(Tg, vek):
	print 'words =',
	for w in vek:
		print w
	for t in Tg:
		tot = sum([c for (wd, c) in Tg[t]])
		rtz = []
		for (wd, cnt) in Tg[t]:
			rt = str(float(cnt)/float(tot))[1:5]
			if len(rt) == 2:
				rt+= '0'
			rtz += [rt]
		print rtz 
		print t
		print 'N =', tot
	print '---------------------------'

##Basically same as hero_stats ... maybe there's a better way to do this, then?
###STILL BROKEN!!!
# def tag_stats: 
# 	for t,h in tag_dict.items():
# 		if t not in length_by_tag:
# 			length_by_tag[t] = 0
# 		if t not in chats_by_tag:
# 			chats_by_tag[t] = 0
# 	for hero in h:
# 		if t not in length_by_tag:
# 			length_by_tag[t] = length_by_hero[hero]
# 		if t not in chats_by_tag:
# 			chats_by_tag[t] = chats_by_hero[hero]