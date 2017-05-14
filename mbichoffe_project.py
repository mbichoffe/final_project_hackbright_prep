''' Where in the World is Carmen Santiago(Hackbright Prep final project from Marina Bichoffe)
The goal of this game is to track around the world and arrest a villain from E.V.I.L., a criminal organization led by Lauren Sandi Eggo. 
The player, a special agent from the ACME Detective Agency, is alerted that a stupefying theft has been committed. She will receive a brief with information about the case and a deadline. She has the mission to find and arrest the criminal. In order to make an arrest the player must have a warrant, and it must be the right warrant.

The player will be transported to the scene of the crime, where she will complete tasks in order to find clues to infer the suspect's next destination and to create an arrest warrant describing the guilty party's attributes. The chase around the world continues until the player has collected enough evidence to determine the culprit. When the player reaches her final destination where the villain is going to pass off the loot to Lauren, she has to arrest the villain."""
'''
import datetime
from datetime import date, time, datetime, timedelta




def current_date(date_today, travel_time):
	'''Calculates the passage of time by adding travel time to current date'''
	
	d = date_today
	t = timedelta(hours = travel_time)
	date_today = d + t
	
	print date_today.strftime('%B, %d, %I:%M '' %p')
	return date_today

# def review_brief:

# 	print '''\n''


# print '''\
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# 		WHERE IN THE WORLD IS CARMEN SANTIAGO?
# 		    A Mystery Exploration Game
						 	
# 		        By Marina Bichoffe

# 		    Hackbright Prep Final Project

# 		            May 2017
                                 				
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'''

# raw_input('')
# #pauses the script until the user presses Enter

# print'''\n\n\n\t\t\tINTRODUCTION\n\t\t\t------------'''

# print'\n\n\nThe Chase is On...'

# print'''\n\n\n\tIn this game, you are a rookie detective for the Acme Detective Agency, who are known for 
# bringing down the most elusive and dangerous criminals in the world.
# It's your first day on the job, and Carmen Santiago and her Evil Villains International League (E.V.I.L). 
# have once again made sensational headlines in the newspaper.

# \n\tFor more than five years, Carmen and her gang of felons had managed to stockpile 
# the world's most valuable treasures, while outwitting every crime expert from 
# New York to Sydney. 
# Now they've struck again. And you, the newest employee of the Acme Detective Agency, 
# have been given the near-impossible assignment of tracking them down.'''

# raw_input('\n\n\n\nPress enter to continue')

# print '''\n\n\t\t\tYour Assignment\n\t\t\t---------------'''

# print'''\n\n\n\tThe thief .  Your job
# is to track him or her down around the world, using clues you unearth along the way. 
# Clues can point to the city itself or the country in which the city is located. Clues can  
# also point out to some of the culprit's characteristics. There are 5 possible suspects, 
# any one of whom could be the thief.
# \n\tYou can only arrest the criminal when you have a warrant, and it must be the right 
# warrant.
# \nWork quickly.  You have only a limited amount of time to solve the case.  The Crime Computer 
# will let you know what your deadline is. 
# \n'''

# print '''\n\n\n\nLet's get started!\n\n\n\n'''

# raw_input('\n\n\n\nPress enter to continue')
# print ('\n\n')

# from pyfiglet import Figlet
# #import figlet fonts - figlet.org
# f = Figlet(font='roman')
# print f.renderText('ACME')
# #print ACME with roman font on Figlet

# f = Figlet(font='straight')
# print f.renderText('Detective Agency')
# #print Detective Agency with straight font on Figlet

#every time 
print '\nSan Francisco, CA'
current_date(datetime.today(),0)



#remember to update these numbers (suspects and cities)
# import sys, os

print'\n\n\n###Acme Computer###'

print '\n\n64 Ram System'

print '\n\n>login'

print '\nDetective at keyboard, please identify yourself:\n\n'

username = raw_input('')








