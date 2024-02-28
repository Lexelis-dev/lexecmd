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

def converter():
    pass