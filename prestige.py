import re

##Given a lang_entries to look in and the regex expression to match, returns
##The total count of instances of that expression in the string. 
def ex_amounts(entries, regex):
	ex = re.compile(regex)
	total = 0
	for player in entries:
		### FOR DEBUG - PRINTS ALL CHATS W MENTIONS OF KDA, MMR
		for chat in player.c:
		# 	arr = ex.findall(player.c[chat])
		# 	if len(arr) > 0:
		# 		print(player.c[chat])
			total += len(ex.findall(player.c[chat]))
	return total
