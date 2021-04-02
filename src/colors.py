def get_colors():
    """ Returns the all colors supported """
    return {
        "[GREEN]": "\033[32m",
        "[YELLOW]": "\033[33m",
        "[BG-GREEN]": "\033[42m",
        "[RED]": "\033[91m",
        "[ENDC]": "\033[0m",
        "[BOLD]": "\033[1m"
    }


def get_color(name):
    """
    Returns the code of color according parameter.
    If there is not color, returns None
    """
    colors = get_colors()
    return colors[name] if name in colors else None
