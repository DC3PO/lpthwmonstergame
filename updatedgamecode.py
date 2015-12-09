# I figured out the problem.  This is the new code I have decided to use 
# and now the function works just fine.

def monster_room():
	print "This is the monster room! How many monsters do you see?"
	
	try:
		choice = int(raw_input("> "))
	except ValueError:
		print "Type a number!"
		monster_room()
	
	if choice < int(5):
		print "There are more than that! It's a haunted house!"
		monster_room()
	elif choice >= int(5):
		print "More than you thought right?!"
		print "Do you go to the Alien room or Frankenstein room?"
		
		choice_one = raw_input("> ")
		
		if choice_one == "alien":
			alien_room()
		elif choice_one == "frankenstein":
			frankenstein_room()
		else:
			print "Type alien or frankenstein, DUMMY!"
			monster_room()
	else:
		print "Type a number!"
		monster_room()
