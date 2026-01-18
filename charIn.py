def charIn(string: str, char: str) -> tuple[bool, list]:
    """
    Determines if a char is in an string and return the position at which the char appears
    
    Params:
    -> string (str): This is the string where search for char is going to happend
    -> char (str): Char that is gooing to be look for
 
    Except:
    -> Return -1 if type of string or char is not str or if char is not a sigle char
    
    Return:
    -> (tuple[bool, list]): It returns True and list of index if char is in string,
    false otherwise.
    """
    if not isinstance(string, str) or not isinstance(char, str) or len(char) != 1:
        return -1
    
    positions = []
    for i, e in enumerate(string):
        if e == char:
            positions.append(i)
    
    return (True, positions) if positions else (False, positions)


#Tests
assert charIn("qraias", "a") == (True, [2, 4])
assert charIn("", "") == -1
assert charIn(1, "b") == -1
assert charIn("kjsdn", [10]) == -1
assert charIn(["a", "b", "c"], "a") == -1
assert charIn("abcde", "f") == (False, [])
assert charIn("bcda", "a") == (True, [3])