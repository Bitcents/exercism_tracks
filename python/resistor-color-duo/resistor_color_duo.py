# I was tempted to use a dictionary here.
# Given how small the dataset is, however
# I opted for a list based solution instead.
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

def value(colors):
    color1 = None
    color2 = None
    for i in range(len(resistor_colors)):
        if resistor_colors[i] == colors[0]:
            color1 = i
        if resistor_colors[i] == colors[1]:
            color2 = i
    
    if color1 == None or color2 == None:
        raise ValueError('provided color is not valid')
    
    return color1*10 + color2
