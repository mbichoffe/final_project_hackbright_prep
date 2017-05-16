''' Where in the World is Carmen Santiago(Hackbright Prep final project from Marina Bichoffe)
The goal of this game is to track around the world and arrest a villain from E.V.I.L., a criminal organization led by Carmen Santiago. 
The player, a special agent from the ACME Detective Agency, is alerted that a stupefying theft has been committed. She will receive a brief 
with information about the case and a deadline. She has the mission to find and arrest the criminal. In order to make an arrest the player 
must have a warrant, and it must be the right warrant.

The player will be transported to the scene of the crime, where she will complete tasks in order to find clues to infer the suspect's next 
destination and to create an arrest warrant describing the guilty party's attributes. The chase around the world continues until the player 
has collected enough evidence to determine the culprit. When the player reaches her final destination where the villain is going to pass off 
the loot to Carmen, she has to arrest the villain.'''

import datetime
from datetime import date, time, datetime, timedelta
import sys 
from beautifultable import BeautifulTable

case_start_date = datetime.today()
#sets starting date for the game from which deadline will be calculated

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

######DATE########

def current_date(date_today, travel_time):
	'''Calculates the passage of time by adding travel time to current date
	Arguments:
	date_today: current date in the game 
	travel_time: amount of time it takes to reach the chosen destination on travel menu
	Returns: 
	Current date on arrival at destination'''
	
	d = date_today
	t = timedelta(hours = travel_time)
	date_today = d + t
	print date_today.strftime('%B %d, %I:%M '' %p')
	return date_today


def deadline(current_date):
	'''Calculates the players' deadline to complete the mission by adding 5 days to the
	date the case started'''
	case_closed_deadline = case_start_date + timedelta(days = 5)
	return case_closed_deadline.strftime('%B, %d, %I:%M '' %p')

	

def brief():
	'''Prints current case brief with crime information and deadline
	Arguments: 
	none
	Returns:
	none'''

	print '\n\t\t\t***FLASH***\n\t\t\t-----------'
 
	print '''\n\nNational Treasure stolen from Florence's Uffizi Gallery Museum
 
	\nThe Treasure has been identified as the painting 'The Birth of Venus', by Botticelli.
 
	\nYour assignment: 
	\nTrack the thief from Florence to her hideout and arrest her!

	\n\nYou must apprehend the thief by {}.
 
	\nGood luck, Rookie {}'''.format(deadline(case_start_date),username)


#######TRAVEL######
def travel_menu():
	'''Prints list with destinations and respective time of flight
	Arguments: 
	None
	Returns:
	int: new city and travel time'''
	#print welcome to Employee Travel Service

	travel_table = BeautifulTable()
	#creates a new table 
	travel_table.column_headers = ['Destination', 'Flight Duration']
	for destination, ttime in game_data.keys():
		travel_table.append_row([destination, ttime])
	travel_table.append_column('Flight #', ['1711', '1931'])
	print travel_table

	travel_choice =(raw_input('What is your next destination? (Type city name)')).title
	




######OPTIONS######

def menu_options():
	'''Gives the player the option to review the brief, return to main menu or quit the game
	Arguments:
	None
	Returns:
	int: the users'menu choice''' 

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

def execute_repl(current_city):
    """Execute the repl loop for the control structure of the program. 

    Arguments:
        current_city
    Returns:
        None
    """
#add warrant within execute_repl outside the while loop, inside execute_repl and takes city and warrant

    while True:
    	#print current time
    	print('Current Location: {}'.format(current_city))

    	current_date(new_date,0)
    	
    	choice = game_main_menu()

    	if choice == 'O':
    		#options submenu
    		menu_options()

    	elif choice == 'T':
    		#print list of cities dict.keys() 
    		travel_menu()

    		current_city = "vatican"

    	elif choice == 'I':
    		#needs current city 
    		print 'I ran investigate'
    	elif choice == 'D':
    		print 'I ran data'

    	else: 
    		print 'Invalid choice'


print '''\
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
		WHERE IN THE WORLD IS CARMEN SANTIAGO?
		    A Mystery Exploration Game
						 	
		        By Marina Bichoffe

		    Hackbright Prep Final Project

		            May 2017
                                 				
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'''

raw_input('')
#pauses the script until the user presses Enter

print'''\n\n\n\t\t\tINTRODUCTION\n\t\t\t------------'''

print'\n\n\nThe Chase is On...'

print'''\n\n\n\tIn this game, you are a rookie detective for the Acme Detective Agency, who are known for 
bringing down the most elusive and dangerous criminals in the world.
It's your first day on the job, and Carmen Santiago and her Evil Villains International League (E.V.I.L). 
have once again made sensational headlines in the newspaper.

\n\tFor more than five years, Carmen and her gang of felons had managed to stockpile 
the world's most valuable treasures, while outwitting every crime expert from 
New York to Sydney. 
Now they've struck again. And you, the newest employee of the Acme Detective Agency, 
have been given the near-impossible assignment of tracking them down.'''

raw_input('\n\n\n\nPress enter to continue')

print '''\n\n\t\t\tYour Assignment\n\t\t\t---------------'''

print'''\n\n\n\tThe thief is making a few stops around the world, before meeting with Carmen 
to pass off the loot.  Your job is to track him or her down, using clues you unearth along the way. 
\nClues can point to the city itself or the country in which the city is located. Clues can  
also point out to some of the culprit's characteristics. There are 5 possible suspects, 
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

execute_repl(start_city)







