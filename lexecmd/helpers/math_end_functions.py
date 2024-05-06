from math import (
    pi, e, # Constants
    ceil, floor, fabs, log, log10,
    acos, asin, atan, cos, sin, tan, # Trigonometric
    acosh, asinh, atanh, cosh, sinh, tanh # Hyperbolic
    )
from math import factorial as fact
from math import degrees as deg
from math import radians as rad

from .cli_functions import error

def calculator():
    while True:
        try:
            ans = input()
            if ans == "exit":
                break
            
            if ans == "help":
                print(
                f"Constants: pi, e\n"
                f"Trigonometric: cos, sin, tan, acos, asin, atan\n"
                f"Hyperbolic: cosh, sinh, tanh, acosh, asinh, atanh\n"
                f"Others: ceil, floor, fabs, log, log10\n"
                )
            
            else:
                result = eval(ans)
                print(f"{result}")
                _=result
            
            
        except SyntaxError:
            error("SyntaxError")
        except NameError:
            error("NameError")
        except ValueError:
            error("ValueError")
        except TypeError:
            error("TypeError")
            
def converter():
    while True:
        try:
            ans = input()
            if ans == "exit":
                break
            
            if ans == "help":
                print(
                f"Constants: pi, e\n"
                f"Trigonometric: cos, sin, tan, acos, asin, atan\n"
                f"Hyperbolic: cosh, sinh, tanh, acosh, asinh, atanh\n"
                f"Others: ceil, floor, fabs, log, log10\n"
                )
            
            else:
                converting(ans)
            
        except SyntaxError:
            error("SyntaxError")
        except NameError:
            error("NameError")
        except ValueError:
            error("ValueError")
        except TypeError:
            error("TypeError")

def converting(ans):
    og_value = ans.split()
    if len(og_value) == 3:
        x = float(og_value[0])
        prefixe = og_value[1]
        unit = og_value[2]
        
    if len(og_value) == 2:
        x = float(og_value[0])
        prefixe = None
        unit = og_value[1]
        
    if prefixe:
        for i in prefixes:
            if prefixe in i:
                actual_value = x * i[2]
    else:
        actual_value = x

    for key in units.keys():
        for unit_list in units[key]:
            if unit in unit_list:
                results = []
                
                a = unit_list[0][0]
                if len(unit_list[0]) > 1:
                    b = unit_list[0][1]
                    if len(unit_list[0]) == 3:
                        c = unit_list[0][2]
                    else:
                        c = 0
                else:
                    b = 0
                    c = 0
                    
                # Convert the selected unit in the SI unit
                SI_x = (actual_value-b) / a - c
                
                for unit_list in units[key]:
                    
                    a = unit_list[0][0]
                    if len(unit_list[0]) > 1:
                        b = unit_list[0][1]
                        if len(unit_list[0]) == 3:
                            c = unit_list[0][2]
                        else:
                            c = 0
                    else:
                        b = 0
                        c = 0
                        
                    unit_symbol = unit_list[1]
                    
                    new_value = (SI_x+c) * a + b
                    results.append(str(round(new_value, 11)) + unit_symbol)
                break
    print(results)
    
units = {
    "s" : [
        [[1], "s", "second", "seconds"],
        [[1/60], "min", "minute", "minutes"],
        [[1/3600], "h", "hour", "hours"],
        [[1/86400], "d", "day", "days"],
        [[1/604800], "w", "week", "weeks"],
        [[1/31557600], "y", "year", "years"]
        ],
    "m" : [
        [[1], "m", "metre", "metres", "meter", "meters"],
        [[39.3701], "in", "inch", "inches", "″", '"'],
        [[1/9460730472580.8], "ly", "lightyear", "lightyears"],
        [[1/149597870700], "au", "astronomicalunit"],
        [[10**10], "Å", "angstrom", "ångström"]
        ],
    "kg" : [
        [[1], "kg", "kilogram", "kilograms"]
        ],
    "K" : [
        [[1], "K", "Kelvin", "Kelvins"],
        [[9/5, +32, -273.15], "F", "°F", "Fahrenheit"],
        [[1, 0, -273.15], "C", "°C", "Celsius"],
        ]
}
    
prefixes = [    # TODO
    ["quetta", "Q", 10**30],
    ["ronna", "R", 10**27],
    ["yotta", "Y", 10**24],
    ["zetta", "Z", 10**21],
    ["exa", "E", 10**18],
    ["peta", "P", 10**15],
    ["tera", "T", 10**12],
    ["giga", "G", 10**9],
    ["mega", "M", 10**6],
    ["kilo", "k", 10**3],
    ["hecto", "h", 10**2],
    ["deca", "da", 10**1],
    ["", "", 10**0],
    ["deci", "d", 10**-1],
    ["centi", "c", 10**-2],
    ["mili", "m", 10**-3],
    ["micro", "μ", 10**-6],
    ["nano", "n", 10**-9],
    ["pico", "p", 10**-12],
    ["femto", "f", 10**-15],
    ["atto", "a", 10**-18],
    ["zepto", "z", 10**-21],
    ["yocto", "y", 10**-24],
    ["ronto", "r", 10**-27],
    ["quecto", "q", 10**-30]
]