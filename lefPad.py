def lefPad(string: str, ch: str, size: int) -> str | int:
    """
    -----This is a joke-----
    Version of rjust of python

    The js version of this function almost break the internet
    """
    if (not isinstance(string, str) or not isinstance(ch, str) or 
        not isinstance(size, int) or len(ch) != 1):
        return -1
    return (ch * (size - 1)) + string

assert lefPad("B", "*", 3) == "**B" 
assert lefPad("B", "**", 3) == -1
assert lefPad("B", "*", 1) == "B"
assert lefPad(1, "*", 1) == -1

