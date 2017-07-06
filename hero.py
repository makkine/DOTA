class Hero():
	def __init__(self, a, l, nc):
		self.avg = a
		self.length = l
		self.n_chats = nc

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
def hero_stats(entries):
	heroes = {}
	for game in entries:
		for player in entries[game]:
			if player in heroes:##Goddamn how do I avoid this
				heroes[player].length += lp_sum(entries[game][player])
				heroes[player].n_chats += len(entries[game][player].c)
			else:
				heroes[player] = Hero(0, lp_sum(entries[game][player]), len(entries[game][player].c))
	for hero in heroes:
		heroes[hero].avg = float("{0:.2f}".format(float(heroes[hero].length) / float(heroes[hero].n_chats)))
	return heroes


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