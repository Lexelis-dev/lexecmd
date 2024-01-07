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
from random import *
from colorama import Fore
import pypokedex

#--------------------Classes--------------------#
# Colors for print()
class Color :
    sys_red = [145, 32, 49]
    sys_purple = [161, 141, 181]
    
# vars() create a dictionary of every values stored in the class
# {k: v .... } creates a new dictionary, here with only the keys that don't have '__' at the beginning of their name
    # k is the key, and v the value
# for k, v in.... loops for each values and keys of the dictionary
# .items() gives the dictionary values as a tuple
for i in {k: v for k, v in vars(Color).items() if not k.startswith('__')}:
    
    # setattr(object, attribute, value assigned) replace the value of an object
    # {} will prepare each affected formatting; .format() will replace those values by an unpacked values of the attributes
    setattr(Color, i, "\x1b[38;2;{};{};{}m".format(*getattr(Color, i)))


# Used to fully exit the script  
class ExitScript(Exception):
    pass


#--------------------The main functions--------------------#
def main():

    # Call entry functions and compare answers
    def inner_main():
        while True:
            global L, entry, greetings, temp_greeting
            ans = entry()
            
            # Leaving current level
            if ans == "exit":
                del L[-1]
                break
            
            # Leaving the program
            elif ans == "fullexit":
                raise ExitScript
                
            # Input is accepted
            elif ans in correct[L[-1]]:
                
                # Input activates a command
                if ans in end_functions["end_fun_name"]:
                    end_functions["end_fun"][end_functions["end_fun_name"].index(ans)]()
                        
                # Input is already a used values and goes to another level
                else:
                    L.append(ans)
                    inner_main()
                    
            # User asks for help
            elif ans == "help":
                lexhelp()
            
            # User asks for aliases
            elif ans == "alias":
                alias()
                
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
    for i in range(len(L)):
        if i == len(L) - 1:
            u+= L[i] + ">"
        else:
            u+= L[i] + "/"
    return input(u).lower()

# The entry function, will check 
def entry():
        
    # If check_levels() test passed, will ask the next entry
    if check_levels():
        print_greeting()
        
        try: 
            # Attempt to translate the input, and ask in a formatted way
            return translate(lexinput())
        
        # The current level doesn't have any correct input available
        # Caused by mistakes in the dictionary 'correct' or unfinished level 
        except KeyError:
            error("Input can't be accepted")
            print(Color.sys_purple + "Exiting",L[ - 1]+ "\033[39m")
            # Remove the last level as it will create an infinite loop
            del L[-1]
          
# Check if the levels are correct
def check_levels():
    check = True
    
    # Check if the input is correct for every levels
    for i in range(len(L) - 1):
        if L[i + 1] in correct.get(L[i], {}):
            check = True
            
        # A level is considered incorrect
        else:
            error("Levels unordered")
            check = False
            break
    return check

# Print a greeting before asking for input
def print_greeting():
    
        try:
            if greetings[L[len(L) - 1]] != None:
                # Attempt to print the gretting for the current level
                print(str(greetings[L[len(L) - 1]]))
            
        except KeyError:
            error("Greeting not found")
        
# Translate a user input
def translate(ans):
    
    # Go through every possible current answers
    for i in correct[L[-1]]:
        try :
            
            # Input is found within the lists to translate
            if ans in correct[L[-1]][i]:
                return i
                break
        # Input isn't found in said lists, can still be a correct input
        except TypeError:
            continue 
    return ans

# Give a list of possible entries
def lexhelp():
    try:
        print("\nHere is the list of entries possible:\n", ", ".join(sorted((correct[L[-1]]))))
    
    except KeyError:
        error("Help list not found")
        
# Give a list of aliases
def alias():
    
    temp_alias = {k: v for k, v in correct[L[-1]].items() if v is not None}
    if temp_alias != {}:
        print("\nHere is the list of aliases")
    else:
        print("There is no current aliases")
    for i in sorted(temp_alias):
        print(str(i)+":",", ".join(sorted(temp_alias[i])))
    
# Print changelogs_lexecmd.md
def print_changelogs():
    # Open the "changelog.md" file in read mode
    try:
        with open("changelogs_lexecmd.md", "r") as changelog_file:
            # Read the file and store it
            changelog_content = changelog_file.read()
        
        # Print the content of the changelog file
        print(changelog_content,"\n")
    except FileNotFoundError:
        error("Changelogs file not found.")
        

# Write an error message
def error(message):
    print("\n" + Color.sys_red + "Lexerror " + Color.sys_purple + message + "\033[39m")
    
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
L = ["main"]

main()

#To do : 
#add python chat;
# study;
# draw;
# todo+save