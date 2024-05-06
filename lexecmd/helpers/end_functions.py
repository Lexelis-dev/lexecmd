import random
import pypokedex
from time import time

from .cli_functions import error
from .math_end_functions import calculator, converter

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
    
def converting_time(time_left):
    ignoring=True
    converted_time = ""
    unit=["s","m","h"]
    new_time = time_left // (60**2 * 24)
    if new_time !=0:
        time_left -= new_time * (60**2 * 24)
        converted_time += f"{new_time}d "
        ignoring = False
        
    for i in reversed(range(3)):
        new_time = time_left // 60**i % 60
        if new_time != 0 or ignoring!=True:
            time_left -= new_time * 60**i
            converted_time += f"{new_time}{unit[i]} "
            ignoring = False
    return converted_time
    
def show_todo():
    try:
        with open("../private/private_todo_list.md", "r") as file:
            # Read the file and store it in a list
            content = file.read()
            content = content.split("\n=\n")
            
        for i, j in enumerate(content):
            imp, diff, time_created, item = j.split("§§")
            time_since = int(time()) - int(time_created)
            converted_time = converting_time(time_since)
            print(f"- {i}° | {imp}! | {diff}# | {converted_time}| {item}")
            
    except FileNotFoundError:
        error("Private todo list file not found.")
        
def add_todo():
    try:
        with open("../private/private_todo_list.md", "r") as file:
            # Read the file and store it in a list
            content = file.read()
        content = content.split("\n=\n")
        ans = input("What item do you want to add to the list?\n")
        importance = input("How important is the item?\n")
        difficulty = input("What is its difficulty?\n")
        current_time = int(time())
        
        new_content = f"{importance}§§{difficulty}§§{current_time}§§{ans}"
        all_content = "\n=\n".join(content + [new_content])
        
        with open("../private/private_todo_list.md", "w") as file:
            file.write(all_content)
            
    except FileNotFoundError:
        error("Private todo list file not found.")
        
def del_todo():
    try:
        with open("../private/private_todo_list.md", "r") as file:
            # Read the file and store it in a list
            content = file.read()
        content = content.split("\n=\n")
        ans = int(input())
        
        print(f"Removing :\n{content[ans]}")
        del content[ans]
        new_content = "\n=\n".join(content)
        
        with open("../private/private_todo_list.md", "w") as file:
            file.write(new_content)
            
    except FileNotFoundError:
        error("Private todo list file not found.")
        
def dice():
    ans = int(input("d"))
    print(f"You rolled a {random.randint(0, ans)}")

# List functions that won't make main() move forward
end_functions_dictionary = {
    "end_fun":[rand_task, thoughts, rand_dex, show_todo, add_todo, del_todo,
               dice, calculator, converter],
    "end_fun_name":[]
    }
for i in end_functions_dictionary["end_fun"]:
    end_functions_dictionary["end_fun_name"].append(i.__name__)