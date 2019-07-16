slabcolouroptions = {"grey", "red", "green", "custom"}
slabdepthoptions = {38, 45}
slabshapeoptions = {"square", "rectangle", "round"}
slabsizeoptions = {"600x600", "450x450", "600x700", "600x450", "300", "450"}
print("Please follow the steps to design the type of slab that you require...")
while True:
    print("Press:\nC for colour options\nD for depth options\nS for size and shape options")
    print("Press 'A' when done")
    Optionchoice = input().lower()
    if Optionchoice == "c":
        print("What colour of slab would you like?")
        print("The options are:\nGrey\nRed\nGreen")
        print("Type 'custom' if you would like a custom colour")
        slabcolour = input().lower()
        while True:
            if slabcolour == "grey":
                print("Colour set to grey")
                break
            elif slabcolour == "red":
                print("Colour set to red")
                break
            elif slabcolour == "green":
                print("Colour set to green")
                break
            elif slabcolour == "custom":
                print("What custom colour would you like?")
                customslabcolour = input().lower()
                print(f"Colour set to {customslabcolour}")
                break
            else:
                print("Invalid input")
                break
    elif Optionchoice == "d":
        print("Choose either depth:\n38mm\n45mm\n")
        slabdepth = input()
        while True:
            if "38" in slabdepth:
                print("Slab depth set to 38mm")
                slabdepth = 38
                break
            elif "45" in slabdepth:
                print("Slab depth set to 45mm")
                slabdepth = 45
                break
            else:
                print("Invalid input")
                break
    elif Optionchoice == "s":
        print("What is the shape that you require?")
        print("All sizes are in millimeters")
        print("The available shapes are:\nSquare\nRectangle\nRound")
        slabshape = input().lower()
        while True:
            if slabshape == "square":
                print("Choose a size")
                print("The available sizes are:\n600x600\n450x450")
                slabsize = input()
                if "600" in slabsize:
                    print("Slab shape set to square")
                    slabsize = "600x600"
                    print("Slab size set to 600mmX600mm")
                    break
                elif "450" in slabsize:
                    print("Slab shape set to square")
                    slabsize = "450x450"
                    print("Slab size set to 450mmX450mm")
                    break
                else:
                    print("Invalid input")
                    break
            elif slabshape == "rectangle":
                print("Choose a size")
                print("The available sizes are:\n600x600\n450x450")
                slabsize = input()
                if "700" in slabsize:
                    print("Slab shape set to rectangle")
                    slabsize = "600x700"
                    print("Slab size set to 600mmX700mm")
                    break
                elif "450" in slabsize:
                    print("Slab shape set to rectangle")
                    slabsize = "600x450"
                    print("Slab size set to 600mmx450mm")
                    break
                else:
                    print("Invalid input")
                    break
            elif slabshape == "round":
                print("Choose a diameter")
                print("The available diameters are:\n300mm\n450mm")
                slabsize = input()
                if "300" in slabsize:
                    print("Slab shape set to round")
                    slabsize = "300"
                    print("Slab diameter set to 300mm")
                    break
                if "450" in slabsize:
                    print("Slab shape set to round")
                    slabsize = "450"
                    print("Slab diameter set to 450mm")
                    break
            else:
                print("Invalid input")
                break
    elif Optionchoice == "a":
            if slabcolour not in slabcolouroptions:
                print("Please recheck the colour options")

            elif slabdepth not in slabdepthoptions:
                print(print("Please recheck the depth options"))

            elif slabshape not in slabshapeoptions:
                print("Please recheck the shape options")

            elif slabsize not in slabsizeoptions:
                print("Please recheck slabsize")
            else:
                print("Your chosen options are:")
                print(f"Slab Colour: {slabcolour.capitalize()}\nSlab Depth: {slabdepth}mm\nSlab Shape: {slabshape.capitalize()}\nSlab Size: {slabsize}mm")
                print("Do you want to change anything?")
                print("Yes or no?")
                alteroptions = input().lower()
                if "y" in alteroptions:
                    print("")
                else:
                    print("Okay moving on then:")
                    break
    else:
        print("Invalid input")