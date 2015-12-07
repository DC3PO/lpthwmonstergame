from sys import exit
	
def frankenstien_room():
	print "You have arrived at the Frankenstien room!"
	print "Do you throw stuff at Frankenstien OR run like heck?"
	
	choice_two = raw_input("> ")
	
	if choice_two == "throw stuff":
		print "Congrats you defeat Frankenstien and exit safely!"
		exit(0)
	elif choice_two == "run like heck":
		print "Your a pansy!! Back to the third room because"
		print "that's where you will run either way!!"
		third_room()
	else:
		print "Type throw stuff OR run like heck."
		frankenstien_room()

def alien_room():
	print "You have arrived at the alien room!"
	print "You get picked up by aliens and probed!"
	print "Congrats!  You are emotionally scared forever! Start over!"
	start()		

def monster_room():
	print "This is the monster room! How many monsters do you see?"
	
	choice = raw_input("> ")
	
	if choice < 5:
		dead("More than that idiot!")
	elif choice > 5:
		print "More than you thought right?!"
		print "Do you go to the Alien room or Frankenstien room?"
		
		choice_one = raw_input("> ")
		
		if choice_one == "alien":
			alien_room()
		elif choice_one == "frankenstien":
			frankenstien_room()
		else:
			print "Type alien or frankenstien, DUMMY!"
			monster_room()
	else:
		print "Type a number!"
		monster_room()
		

def second_room():
	print "There are 3, SCARY, Ghost in here."
	print "How man do you yell at?"
	print "They are SCARY, really!"
	ghost_scary = False
	
	while True:
		choice = raw_input("> ")
		
		if choice == "1":
			print "Come on there's 3 of them! Try again!"
			start()
		elif choice == "2" and not ghost_scary:
			print "I see you, 2 is better than 1!"
			ghost_scary = True
			monster_room()
		elif choice == "3":
			print "You made the obvious choice, congrats!"
			monster_room()
		else:
			print "There are only 3! Try again!"
			second_room()
		

def first_room():
	print "All the workers are in here."
	print "They yell at you and kick you out immediately!"
	print "Go back to the start!"
	start()

def dead(self):
	print "Way to go dummy!"
	start()

def start():
	print "You arrive at a haunted house."
	print "You enter and see a door on the left and one on the right."
	print "Which door do you take??"
	
	choice = raw_input("> ")
	
	if choice == "left":
		first_room()
	elif choice == "right":
		second_room()
	else:
		print "It's a left or right answer!"
		dead("Way to go dummy!")
start()
