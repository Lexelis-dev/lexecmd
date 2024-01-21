# List of possible entries
correct = {
    # Level1
    "main":{"adhd":["add"],
            "draw":["drawing"],
            "anxiety":None,
            "todo":None
    },
    
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
    "todo":{
        "show_todo":["show"],
        "add_todo":["add"]
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
    "todo":" ",
    
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

def toggle_greetings():
    global greetings, temp_greeting
    greetings, temp_greeting = temp_greeting, greetings