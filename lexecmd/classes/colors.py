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