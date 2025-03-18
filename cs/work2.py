advice = "nothing needed"
colour = input("Insert the colour: ")
size = input("Insert the size: ")
shape = input("Insert the shape: ")
position = input("Insert the position: ")

if colour == "yellow":
    advice = "nitrogen"

elif colour == "brown":
    if size == "small":
        advice = "phosphorous"

    elif size == "normal":
        advice = "potassium"

elif shape == "cracked":
    advice = "calcium fertiliser"

elif colour == "yellow" and position == "tips":
    advice = "magnesium fertiliser"