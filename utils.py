def centerWin(window, width: int, height: int) -> str:
    """
    Returns the correct position to center the window by the .wmgeometry()
    method from Tkinter, according to the window's dimensions provided through the
    parameters and the user's screen size.

    This function, >yet<, does consider the MS Windows' taskbar size. So the window
    doesn't get perfectly centered.

    :param window: The target window object you instantiated using Tk(), in which you want to be centered.
    :param width: Width of the window you are creating.
    :param height: Height of the window you are creating.
    :return: str(), with the following standard: widthxheight+x+y
    """




    userScreenWidth = window.winfo_screenwidth()
    userScreenHeight = window.winfo_screenheight()


    correctX = userScreenWidth // 2 - width // 2
    correctY = userScreenHeight // 2 - height // 2

    return f"{width}x{height}+{correctX}+{correctY}"



def isnumber(possibleNumber: str) -> bool:
    """I have no idea why this ain't a thing yet..."""

    try:
        float(possibleNumber)
    except:
        return False
    else:
        return True

def popString(string: str) -> str:
    """As if you could use .pop() in strings"""

    string = string[:-1]
    return string