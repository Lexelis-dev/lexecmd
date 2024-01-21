documentation = """----------This is the lexecmd v0.19.2 documentation----------

General inputs:
    help -> Display a list of available commands
    alias -> Display a list of alternative names for the available commands
    exit -> Leave  the current level
    fullexit -> Close  the program
    changelogs -> Show the changelogs
        also : changelog, cglg, cgl
    toggle_greetings -> activate or desactivate greetings at each inputs
        also : toggle_greeting, tglgrt
    documentation -> View  this message
        also : lexedoc
        
Version : 0.19.2

- Separated  the program into multiple files
"""

#--------------------Import--------------------#
from random import randint
import colorama
import pypokedex

""" """ """
from private import todo_list
""" """ """

from helpers import (lexinput, entry, check_levels, print_greeting, translate, lexhelp,
    alias, print_changelogs, error, rand_task, thoughts, rand_dex, end_functions_dictionary)
from classes import Color, ExitScript
from variables import correct, greetings, temp_greeting


#--------------------The main functions--------------------#
def main():
    colorama.init()
    # Keeping track of levels
    navigation_level = ["main"]

    # Call entry functions and compare answers
    def inner_main(navigation_level):
        while True:
            global entry, greetings, temp_greeting
            ans = entry(navigation_level, correct, greetings)
            
            # Leaving current level
            if ans == "exit":
                del navigation_level[-1]
                break
            
            # Leaving the program
            elif ans == "fullexit":
                raise ExitScript
                
            # Input is accepted
            elif ans in correct[navigation_level[-1]]:
                
                # Input activates a command
                if ans in end_functions_dictionary["end_fun_name"]:
                    end_functions_dictionary["end_fun"][end_functions_dictionary["end_fun_name"].index(ans)]()
                        
                # Input is already a used values and goes to another level
                else:
                    navigation_level.append(ans)
                    inner_main(navigation_level)
                    
            # User asks for help
            elif ans == "help":
                lexhelp(navigation_level, correct)
            
            # User asks for aliases
            elif ans == "alias":
                alias(navigation_level, correct)
                
            # User asks for changelogs
            elif ans in ("changelogs","changelog","cglg","cgl"):
                print_changelogs()
                
            # User asks for removing greetings
            elif ans in ("toggle_greetings","toggle_greeting","tglgrt"):
                greetings,temp_greeting=temp_greeting,greetings
                
            elif ans in ("documentation","lexedoc"):
                print(documentation)
                
            # Input is found nowhere in our data
            else:
                print("Sorry, but this entry wasn't recognized. Enter 'help' for more information")

    try:
        while True:
            inner_main(navigation_level)
    except ExitScript:
        pass
    


main()

#To do : 
#add python chat;
# study;
# draw;
# todo+save