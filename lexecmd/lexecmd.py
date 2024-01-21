documentation = """----------This is the lexecmd v0.19.0 documentation----------

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
        
Version : 0.19.0
- Added Pokemon dex randomizer
"""

#--------------------Import--------------------#
from random import randint
from colorama import Fore
import pypokedex

""" """ """
from private import todo_list
""" """ """

from helpers import (check_levels, print_greeting, translate, lexhelp,
    alias, print_changelogs, error)

from classes import Color, ExitScript


#--------------------The main functions--------------------#
def main():

    # Call entry functions and compare answers
    def inner_main():
        while True:
            global navigation_level, entry, greetings, temp_greeting
            ans = entry()
            
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
                if ans in end_functions["end_fun_name"]:
                    end_functions["end_fun"][end_functions["end_fun_name"].index(ans)]()
                        
                # Input is already a used values and goes to another level
                else:
                    navigation_level.append(ans)
                    inner_main()
                    
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
            inner_main()
    except ExitScript:
        pass

# Dynamic input function changing with current level
def lexinput():
    u=""
    # Write the current levels
    for i, v in enumerate(navigation_level):
        if i == len(navigation_level) - 1:
            u+= v + ">"
        else:
            u+= v + "/"
    return input(u).lower()

# The entry function, will check 
def entry():
        
    # If check_levels() test passed, will ask the next entry
    if check_levels(navigation_level, correct):
        print_greeting(navigation_level, greetings)
        
        try: 
            # Attempt to translate the input, and ask in a formatted way
            return translate(navigation_level, correct, lexinput())
        
        # The current level doesn't have any correct input available
        # Caused by mistakes in the dictionary 'correct' or unfinished level 
        except KeyError:
            error("Input can't be accepted")
            print(Color.sys_purple + "Exiting",navigation_level[ - 1]+ "\033[39m")
            # Remove the last level as it will create an infinite loop
            del navigation_level[-1]
             
#--------------------End functions--------------------#
# Generate a random activity
def rand_task():
    print("The selected activity will be :",stuck_list[randint(0, len(stuck_list) - 1)])
    ans = input("\nDo you need a random timer? (y)\n").lower()
    
    # Randomise time
    if ans == "y":
        start_rand = int(input("\nWhat is the minimum duration in minutes?\n"))
        end_rand = int(input("\nWhat is the maximum duration in minutes?\n"))
        print("The chosen duration of the activity will be :",randint(start_rand,end_rand),"minutes")
    
def thoughts():
    print("Remember to take time breathing")
    
def rand_dex():
    r=randint(1, 1025)
    pok=pypokedex.get(dex = r)
    print("The chosen pokemon will be",pok.name,"of the pokedex number",r)

#--------------------Dictionaries--------------------#
# List of possible entries
correct = {
    # Level1
    "main":{"adhd":["add"],
            "draw":["drawing"],
            "anxiety":None},
    
    # Level2
    "adhd":{
        "stuck":["stk"],
        "overwhelmed":["ovm","ovwhel"]
            },
    "draw":{
        "idea":None,
        "motivation":["mtv","mtvt",'motiv']
            },
    "anxiety":{
        "talking":["talk"]
        },
    
    # Level3
    "stuck":{
        "rand_task":["task"]
             },
    "overwhelmed":{
        "thoughts":None,
        "noises":None,
        },
    "idea":{
        "pokemon":["pkm"],
        "kup":None,
        },
    "motivation":{
        "sad":None,
        "hard":None
        },
    
    #Level4
    "pokemon":{
        "rand_dex":["dex"],
        "eevee":None
        }
    }

# Greetings for each levels
greetings = {
    # Level1
    "main":"\nHi, what would you need help with?",
    
    # Level2
    "adhd":"\nWhat issue is ADHD causing?",
    "draw":"\nWhat help do you need with drawing?",
    
    # Level3
    "stuck":"\nWould you need a randomized task?",
    "overwhelmed":"\nWhat's making you feeling like that?",
    "idea":"\nWhat kind of idea would you want?",
    "motivation":"\nWhat's making you unmotivated?",
    
    # Level4
    "pokemon":"\nCan you be more precise?"
    }

# Alternate empty greetings
temp_greeting = {k: None for k, v in greetings.items() if v is not None}

# List functions that won't make main() move forward
end_functions = {
    "end_fun":[rand_task,thoughts,rand_dex],
    "end_fun_name":[]
    }
for i in end_functions["end_fun"]:
    end_functions["end_fun_name"].append(i.__name__)
    
stuck_list=[
    "Voice training",
    "Write",
    "Draw",
    "Study",
    "Clean the house",
    "Internal communication",
    "Chat with people",
    "Meditate",
    "Learn Italian",
    "Journaling",
    "Play some games",
    "Python"
    ]

# Keeping track of levels
navigation_level = ["main"]

main()

#To do : 
#add python chat;
# study;
# draw;
# todo+save