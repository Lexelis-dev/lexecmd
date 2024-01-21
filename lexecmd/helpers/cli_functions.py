from classes import Color

# Check if the levels are correct
def check_levels(navigation_level, correct):
    check = True
    
    # Check if the input is correct for every levels
    for i in range(len(navigation_level) - 1):
        if navigation_level[i + 1] in correct.get(navigation_level[i], {}):
            check = True
            
        # A level is considered incorrect
        else:
            error("Levels unordered")
            check = False
            break
    return check

# Print a greeting before asking for input
def print_greeting(navigation_level, greetings):
    
        try:
            if greetings[navigation_level[len(navigation_level) - 1]] != None:
                # Attempt to print the gretting for the current level
                print(str(greetings[navigation_level[len(navigation_level) - 1]]))
            
        except KeyError:
            error("Greeting not found")
        
# Translate a user input
def translate(navigation_level, correct, ans):
    
    # Go through every possible current answers
    for i in correct[navigation_level[-1]]:
        try :
            
            # Input is found within the lists to translate
            if ans in correct[navigation_level[-1]][i]:
                return i
                break
        # Input isn't found in said lists, can still be a correct input
        except TypeError:
            continue 
    return ans

# Give a list of possible entries
def lexhelp(navigation_level, correct):
    try:
        print("\nHere is the list of entries possible:\n", ", ".join(sorted((correct[navigation_level[-1]]))))
    
    except KeyError:
        error("Help list not found")
        
# Give a list of aliases
def alias(navigation_level, correct):
    
    temp_alias = {k: v for k, v in correct[navigation_level[-1]].items() if v is not None}
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