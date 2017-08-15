import Hero_Tag_dicts

#We should be able to: 
# Compare classses against the total (word freq against a total)
# We should be able to compare a hero word freq. against a total
# It would be cool to: compare a hero's word freq. with a tags word freq 

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
def hero_stats(entries, taglist = Hero_Tag_dicts.hero_names):
	heroes = {} 
	heroes['npc_dota_hero_Skrillex'] = Hero(0,0,0, {})
	for game in entries:
		for player in entries[game]:
			heroes["npc_dota_hero_Skrillex"].length += lp_sum(entries[game][player])
			heroes["npc_dota_hero_Skrillex"].n_chats += len(entries[game][player].c)
			if player != "null":
				for t in taglist: 
					if t.startswith("npc_dota_hero_"):
						t = t[14:]
					if t in Hero_Tag_dicts.hero_dict[player]:
						if t in heroes:
							heroes[t].length += lp_sum(entries[game][player])
							heroes[t].n_chats += len(entries[game][player].c)
						else:
							heroes[t] = Hero(0, lp_sum(entries[game][player]), len(entries[game][player].c), {})
						for chat in entries[game][player].c:
							newlist = entries[game][player].c[chat].strip().split(' ')
							newlist = [x.strip("''") for x in newlist]
							for word in newlist:
								if word in heroes[t].chats:
									heroes[t].chats[word] += 1
								else:
									heroes[t].chats[word] = 1
								if word in heroes["npc_dota_hero_Skrillex"].chats:
									heroes["npc_dota_hero_Skrillex"].chats[word] += 1
								else:
									heroes["npc_dota_hero_Skrillex"].chats[word] = 1
	for hero in heroes:
		heroes[hero].avg = float("{0:.2f}".format(float(heroes[hero].length) / float(heroes[hero].n_chats)))
	return heroes




## vekDic is the resulting dictionary from calling hero_stats
## vek is top N words, or words you want to find
## Creates a dictionary ordered by tag which contains pairs, first element is a word, second is its count
def create_list(vekDic, vek, tag_list = Hero_Tag_dicts.hero_names):
	Tg = {}
	for t in tag_list:
		print(t)
		h_at_tag = Hero_Tag_dicts.tag_dict[t] #h_at_tag is a list of heroes for tag 't'
		Tg[t] = [] #Tg is a dictionary, the key is tags, val is a pair, words and count
		for (c, wd) in vek:
			n = 0
			for H in h_at_tag: #h is a individual hero
				H = H[14:]
				if wd in vekDic[H].chats:
					n += vekDic[H].chats[wd] #adding up the word counts for each hero (iteratively, so for each tag)
			Tg[t] += [(wd,n)]
	return Tg

##Same thing but without using top N words, rather using a class of words
def create_list_wclass(vekDic, vek, tag_list = Hero_Tag_dicts.hero_names):
	Tg = {}
	for t in tag_list:
		if t.startswith("npc_dota_hero_"):
			t = t[14:]
		h_at_tag = Hero_Tag_dicts.tag_dict[t] #h_at_tag is a list of heroes for tag 't'
		Tg[t] = [] #Tg is a dictionary, the key is tags, val is a pair, words and count
		for wd in vek:
			n = 0
			for H in h_at_tag: #h is a individual hero
				H = H[14:]
				if wd in vekDic[H].chats:
					n += vekDic[H].chats[wd] #adding up the word counts for each hero (iteratively, so for each tag)
			Tg[t] += [(wd,n)]
	return Tg

## Tg is the result of a call to create_list
## For individual words
def tag_hero_report(vekDic, Tg, vek):
	print('words =')
	for w in vek:
		print(w)
	for t in Tg:
		tot = vekDic[t].length
		rtz = []
		for (wd, cnt) in Tg[t]:
			rt = str(float(cnt)/float(tot))[1:5]
			if len(rt) == 2:
				rt+= '0'
			rtz += [rt]
		print(rtz)
		print(t)
		print('N =', tot)
	print('---------------------------')


##For classes of words
def percentage_report(vekDic, Tg, vek):
	pct = 0
	print('words =')
	for w in vek: 
		print(w)
	for t in Tg:
		tot = vekDic[t].length
		for (wd, cnt) in Tg[t]: 
			pct += cnt
		pct = (float(pct)/float(tot))
		print(pct)
		print(t)
		print("N = ", tot)
	print('---------------------------')