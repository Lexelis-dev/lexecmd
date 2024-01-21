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
    
def show_todo():
    try:
        with open("../private/private_todo_list.md", "r") as file:
            # Read the file and store it in a list
            content = file.read()
            content = content.split("\n")
        for i, j in enumerate(content):
            print(f"- [{i}] {j}")
            
    except FileNotFoundError:
        error("Private todo list file not found.")
        
def add_todo():
    with open("../private/private_todo_list.md", "r") as file:
        # Read the file and store it in a list
        content = file.read()
    content = content.split("\n")
    ans = input("What item do you want to add to the list?\n")
    new_content = "\n".join(content + [ans])
    with open("../private/private_todo_list.md", "w") as file:
        file.write(new_content)

# List functions that won't make main() move forward
end_functions_dictionary = {
    "end_fun":[rand_task, thoughts, rand_dex, show_todo, add_todo],
    "end_fun_name":[]
    }
for i in end_functions_dictionary["end_fun"]:
    end_functions_dictionary["end_fun_name"].append(i.__name__)