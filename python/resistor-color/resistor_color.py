resistor_colors = [
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white",
        ]

def color_code(color):
    global resistor_colors
    for i in range(len(resistor_colors)):
        if resistor_colors[i] == color:
            return i
    raise ValueError('the color does not exist in the color chart')


def colors():
    global resistor_colors
    return resistor_colors
