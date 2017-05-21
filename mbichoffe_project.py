""" Where in the World is Carmen Santiago(Hackbright Prep final project from Marina Bichoffe)
The goal of this game is to track around the world and arrest a villain from E.V.I.L., a criminal organization led by Carmen Santiago. 
The player, a special agent from the ACME Detective Agency, is alerted that a stupefying theft has been committed. She will receive a brief 
with information about the case and a deadline. She has the mission to find and arrest the criminal. In order to make an arrest the player 
must have a warrant, and it must be the right warrant.

The player will be transported to the scene of the crime, where she will complete tasks in order to find clues to infer the suspect's next 
destination and to create an arrest warrant describing the guilty party's attributes. The chase around the world continues until the player 
has collected enough evidence to determine the culprit. When the player reaches her final destination where the villain is going to pass off 
the loot to Carmen, she has to arrest the villain."""

import datetime
from datetime import date, time, datetime, timedelta
import sys 
from beautifultable import BeautifulTable

case_start_date = datetime.today()
#sets starting date for the game from which deadline will be calculated
travel_time = 0 
date_today = datetime.today()
current_location = 'Florence'
#sets starting location for the game and gets updated with current_location function

game_data = {('Florence', 0): {
'Embassy':
'''Diplomat\n\n
\'I heard her talking business on the phone and she said, "Well, another day, another rupee. 
She mentioned a startup called Paytm.\'''', 

'Street Market': 
'''Peddler\n\n
I didn\'t see anyone but are you interested in buying some candies? It\'s for a good cause.''',
'Sports Club':
'''Barman\n\n
I think saw the person you're looking for. She said she was going to the capital of Karnataka.'''},
('Bengaluru', 12) : {'Foreign Ministry':
 '''\nUnder Secretary\n\n
\'Sources tell me she was planning on visiting a catholic church in the Alps.\''''
 } }
#this dictionary includes the cities and respective travel time as keys, and another dictionary includes the places and clues available on each

Villains = {
'Bessie May Mucho': 
{'Sex': 'Female' ,
'Hair Color' : 'Brown',
'Hobby'  : 'Mountain Climbing',
'Auto': 'Limousine',
'Feature': 'Jewelry'}, 

"""Anita Bath""": 
{"""Sex""": """Female""", 
'Hair Color': 'Blonde', 
'Hobby': 'Limousine', 
'Feature': 'Tattoo'},

 """Ivanna Steele""": 
 {"""Sex""": """Female""" ,
'Hair Color' : 'Red',
'Hobby'  : 'Tennis',
'Auto': 'Denby Roadster',
'Feature': 'Jewelry'},

"""M.T. Pockets""": 
{"""Sex""": """Male""" ,
'Hair Color' : 'Red',
'Hobby'  : 'Mountain Climbing',
'Auto': 'Convertible',
'Feature': 'Tattoo'},

"""Noah Clue""": 
{"""Sex""": """Male""" ,
'Hair Color' : 'Red',
'Hobby'  : 'Croquet',
'Auto': 'Convertible',
'Feature': 'Tattoo'},

"""Perry Syte""": 
{"""Sex""": """Male""" ,
'Hair Color' : 'Red',
'Hobby'  : 'Croquet',
'Auto': 'Convertible',
'Feature': 'Tattoo'},

"""Hardley Worthit""": 
{"""Sex""": """Male""" ,
'Hair Color' : 'Blond',
'Hobby'  : 'Croquet',
'Auto': 'Limousine',
'Feature': 'Limp'}}

Warrant = {
'Sex': None,
'Hair Color': None ,
'Hobby': None ,
'Auto': None ,
'Feature': None ,
}

def brief():
	"""Prints current case brief with crime information and deadline
	Arguments: 
	none
	Returns:
	none"""

	print '\n\t\t\t***FLASH***\n\t\t\t-----------'
 
	print '''\n\nNational Treasure stolen from Florence's Uffizi Gallery Museum
 
	\nThe Treasure has been identified as the painting 'The Birth of Venus', by Botticelli.
 
	\nYour assignment: 
	\nTrack the thief from Florence to her hideout and arrest her!

	\n\nYou must apprehend the thief by {}.
 
	\nGood luck, Rookie {}'''.format(deadline(case_start_date),username)


#######TRAVEL######

def menu_travel():
	'''Prints list with destinations and respective time of flight
	Arguments: 
	None
	Returns:
	int: new city and travel time'''
	#print welcome to Employee Travel Service
	global current_location 
	destinations_times = game_data.keys()
	list_with_destinations = [place[0] for place in destinations_times]
	 #extracts the cities from the (city, time) tuple and creates a list 
	travel_table = BeautifulTable()
	#creates a new table 
	travel_table.column_headers = ['Destination', 'Flight Duration']
	for destination, ttime in game_data.keys():
		travel_table.append_row([destination, ttime])
	travel_table.append_column('Flight #', ['1711', '1931'])
	print travel_table

	users_location = (raw_input('What is your next destination? (Type city name)\n')).title()

	#gets user input on next destination

	if users_location not in list_with_destinations:
		print 'Invalid Choice'
	
	else:
		current_location = users_location#if the location is on the list, prints the destination and updates the variable current_location	
		print 'Your reservations have been confirmed to {} on Flight # . Enjoy the in-flight meal.'.format(current_location)


	print current_location #city

######DATE########

def get_hours_from_dict(game_data):
	'''Gets the current city and returns travel time as an integer
	Arguments: 
	game_data: dictionary
	Returns:
	travel time'''
	global current_location
	global travel_time
	destinations_times = game_data.keys()
	destinations_times = dict(destinations_times)
	travel_time = destinations_times[current_location]
	return travel_time

def current_date(date_now, travel_time):
	'''Calculates the passage of time by adding travel time to current date
	Arguments:
	date_today: current date in the game 
	travel_time: amount of time it takes to reach the chosen destination on travel menu
	Returns: 
	Current date on arrival at destination'''
	global date_today
	d = date_today
	t = timedelta(hours = travel_time)
	date_today = d + t
	print date_today.strftime('%B %d, %I:%M '' %p')
	return date_today


def deadline(current_date):
	'''Calculates the players' deadline to complete the mission by adding 5 days to the
	date the case started'''
	case_closed_deadline = case_start_date + timedelta(days = 3)
	return case_closed_deadline.strftime('%B, %d, %I:%M '' %p')	


######INVESTIGATE########

places_list = 0
clues_list = 0
def menu_investigate():
	'''Gets user's current location and returns three places to be investigated and the clues in it'''
	current_location
	global places_list
	global clues_list
	for x,y in game_data.keys():
		if x == current_location:
			city_places_clues_dict = game_data[x,y]
			places_list = city_places_clues_dict.keys()
			clues_list = city_places_clues_dict.values()
			get_user_input_investigate()

def get_user_input_investigate():
	"""Gets users input for three options of places to investigate or return to main menu"""
	#to do: print title with 'investigate current city'
	#create list with tuples and return the second tuple
	for index, place in enumerate(places_list, 1):
		print '\t{} - {}'.format(index, place)

	investigate_choice = raw_input("\n\nWhich of these places would you like to investigate?\nChoose a number or R = Return to Main Menu\n")
	if investigate_choice.upper() == 'R':
		game_main_menu()
	elif int(investigate_choice) <= len(places_list):
		place_to_investigate = int(investigate_choice)
		print clues_list[(place_to_investigate - 1)]
		get_user_input_investigate()

	else:
		print 'Invalid Choice'
		get_user_input_investigate()
#remove /n/n from the dictionary
		

######OPTIONS######

def menu_options():
	"""Gives the player the option to review the brief, return to main menu or quit the game
	Arguments:
	None
	Returns:
	int: the users'menu choice""" 

	options_menu = '\n\t\tREVIEW BRIEF\t\tQUIT GAME\t\tRETURN TO MAIN MENU\n\t\t-           \t\t-        \t\t -'
	print options_menu
	choice = (raw_input('>')).upper()

	if choice == 'R':
		brief()
	elif choice == 'E':

		game_main_menu()

	elif choice == 'Q':
		#quit
		sys.exit()

####DATA######
def menu_data():
	"""Displays menu with options to view dossiers or add info to Warrant"""

	data_menu = '\n\t\tDOSSIERS\t\tWARRANT\n\t\t-       \t\t-      '
	print data_menu
	choice = (raw_input('>')).upper()

	if choice == 'D':
		#return dossie function
		menu_dossier()

	elif choice == 'W':
		menu_warrant()

	else:
		print 'Invalid Choice'
		menu_data()

def menu_warrant():
##gets user input on warrant info and updates dictionary##
	pass
def menu_dossier():
	"""Returns a list with suspects and gets user input on which dossier she wants to read"""
	print '\n\n\n\t\t\t****ACME Secret E.V.I.L. Dossier**** '

	for villain in sorted(Villains.keys()):
		print '\n\t{}'.format(villain)
	print '\n\n'
	view_dossier = (raw_input('Which dossier would you like to read? (Type full name)\n')).title()
	#maybe add string split and strip
	villain_dossier = Villains.get(view_dossier, 'Invalid Choice')
	if villain_dossier == 'Invalid Choice':
		menu_dossier()
	else:
		print '\n\n\t\t\t{}\'s Dossier'.format(view_dossier)
		for category, description in villain_dossier.items():
			print '{} : {}'.format(category, description)




	
#####GAME MAIN MENU####
def game_main_menu():
	"""Prints current date/location and a menu and asks the user to make a choice.
    Arguments:
    None
    Returns:
    int: the user's menu choice
    """

	print '\n\t\tOPTIONS\t\tTRAVEL\t\tINVESTIGATE\t\tDATA\n\t\t-      \t\t-     \t\t-          \t\t-'

	choice = raw_input('>')
	return choice.upper()

def execute_repl():
    """Execute the repl loop for the control structure of the program. 

    Arguments:
        current_location
    Returns:
        None
    """
    global current_location
#add warrant within execute_repl outside the while loop, inside execute_repl and takes city and warrant

    while True:
    	#print current time
    	print('\n\n\nCurrent Location: {}'.format(current_location))
    	#prints users' current city
    	get_hours_from_dict(game_data) 

    	current_date(date_today, travel_time) 
    	#prints user current date in MM, DD, HH:MM
    	
    	choice = game_main_menu()

    	if choice == 'O':
    		#options submenu
    		menu_options()

    	elif choice == 'T':
    		#print list of cities dict.keys() 
    		menu_travel()	

    	elif choice == 'I':
    		#needs current city 
    		menu_investigate()


    	elif choice == 'D':

    		menu_data()

    	else: 
    		print 'Invalid choice'

####GAME INTRO####

print """\
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
		WHERE IN THE WORLD IS CARMEN SANTIAGO?
		    A Mystery Exploration Game
						 	
		        By Marina Bichoffe

		    Hackbright Prep Final Project

		            May 2017
                                 				
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"""

raw_input('')
#pauses the script until the user presses Enter

print'''\n\n\n\t\t\tINTRODUCTION\n\t\t\t------------'''

print'\n\n\nThe Chase is On...'

print"""\n\n\n\tIn this game, you are a rookie detective for the Acme Detective Agency, who are known for 
bringing down the most elusive and dangerous criminals in the world.
It's your first day on the job, and Carmen Santiago and her Evil Villains International League (E.V.I.L). 
have once again made sensational headlines in the newspaper.

\n\tFor more than five years, Carmen and her gang of felons had managed to stockpile 
the world's most valuable treasures, while outwitting every crime expert from 
New York to Sydney. 
Now they've struck again. And you, the newest employee of the Acme Detective Agency, 
have been given the near-impossible assignment of tracking them down."""

raw_input('\n\n\n\nPress enter to continue')

print '\n\n\t\t\tYour Assignment\n\t\t\t---------------'''

print'''\n\n\n\tThe thief is making a few stops around the world, before meeting with Carmen 
to pass off the loot.  Your job is to track him or her down, using clues you unearth along the way. 
\nClues can point to the city itself or the country in which the city is located. Clues can  
also point out to some of the culprit's characteristics. There are 7 possible suspects, 
any one of whom could be the thief.
\n\tYou can only arrest the criminal when you have a warrant, and it must be the right 
warrant.
\nWork quickly.  You have only a limited amount of time to solve the case.  The Crime Computer 
will let you know what your deadline is. 
\n'''

#remember to update these numbers (suspects and cities)
# import sys, os

print '''\n\n\n\nLet's get started!\n\n\n\n'''

raw_input('\n\n\n\nPress enter to continue')
print ('\n\n')

from pyfiglet import Figlet
#import figlet fonts - figlet.org
f = Figlet(font='roman')
print f.renderText('ACME')
#print ACME with roman font on Figlet

f = Figlet(font='straight')
print f.renderText('Detective Agency')
#print Detective Agency with straight font on Figlet

print '\nSan Francisco, CA'

new_date = current_date(case_start_date,0)

print'\n\n\n###Acme Computer###'

print '\n\n64 Ram System'

print '\n\n>login'

print '\nDetective at keyboard, please identify yourself:\n\n'

username = raw_input('').title()

brief()

start_city = 'Florence'

execute_repl()







