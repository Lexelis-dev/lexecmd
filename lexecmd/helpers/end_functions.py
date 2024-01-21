import random
import pypokedex

from .cli_functions import error

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

# Generate a random activity
def rand_task():
    print("The selected activity will be :",stuck_list[random.randint(0, len(stuck_list) - 1)])
    ans = input("\nDo you need a random timer? (y)\n").lower()
    
    # Randomise time
    if ans == "y":
        while True:
            try:
                start_rand = int(input("\nWhat is the minimum duration in minutes?\n"))
                end_rand = int(input("\nWhat is the maximum duration in minutes?\n"))
                break
            except ValueError:
                error("Please enter a valid integer")
        try:
            print("The chosen duration of the activity will be :",random.randint(start_rand,end_rand),"minutes")
        except ValueError:
            print("The chosen duration of the activity will be :",random.randint(end_rand,start_rand),"minutes")
    
def thoughts():
    print("Remember to take time breathing")
    
def rand_dex():
    r=random.randint(1, 1025)
    pok=pypokedex.get(dex = r)
    print("The chosen pokemon will be",pok.name,"of the pokedex number",r)

# List functions that won't make main() move forward
end_functions_dictionary = {
    "end_fun":[rand_task,thoughts,rand_dex],
    "end_fun_name":[]
    }
for i in end_functions_dictionary["end_fun"]:
    end_functions_dictionary["end_fun_name"].append(i.__name__)