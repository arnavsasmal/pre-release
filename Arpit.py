print('welcome to the slab ordering program')
cchoice = 0
dchoice = 0
slabshape = 0
size = 0
cchoiceconfirmed = 0
dchoiceconfirmed = 0
slabshapeconfirmed = 0
slabshapeconfirmedfinal = 0
sizeconfirmed = 0
sizeconfirmedfinal = 0

while True :
    choice = input("press c to assign a color to the slab;\n press d to define the depth of the slab;\n press s to define the size and shape of the slab;\n press k if you are done\n")
    if choice == "c":
        cchoice = input('type grey if you want the color grey;\n type red for red;\n green for green;\n and if you want a custom color press c\n')
        if cchoice == "grey":
            cchoiceconfirmed = "grey"
        elif cchoice == "red":
            cchoiceconfirmed = "red"
        elif cchoice == "green":
            cchoiceconfirmed = "green"
        elif cchoice == "c":
            cchoiceconfirmed = "custom color"
        else:
            print("invalid input")
    elif choice == "d":
        dchoice = input('what slab depth would you desire 38 or 45? ')
        if dchoice == "38":
            dchoiceconfirmed = "38"
        elif dchoice == "45":
            dchoiceconfirmed = "45"
        else:
            print("invalid input")
    elif choice == "s":
        slabshape = input('what shape of slab would you prefer: square, rectangle or circle')
        if slabshape == "square":
            slabshapeconfirmed = "square"
            slabshapeconfirmedfinal = 1
            size = input("what size would you prefer, 600x600 or 450x450")
            if size == "600x600":
                sizeconfirmed = "600x600"
                sizeconfirmedfinal = 1
            elif size == "450x450":
                sizeconfirmed = "450x450"
                sizeconfirmedfinal = 1
            else:
                print("invalid input")
        elif slabshape == "rectangle":
            slabshapeconfirmed = "rectangle"
            slabshapeconfirmedfinal = 1
            size = input("what size would you prefer 600x700 or 600x450")
            if size == "600x700":
                sizeconfirmed = "600x700"
                sizeconfirmedfinal = 1
            elif size == "600x450":
                sizeconfirmed = "600x450"
                sizeconfirmedfinal = 1
        elif slabshape == "circle" :
            slabshapeconfirmed = "circle"
            slabshapeconfirmedfinal = 1
            size = input("Diameter 300 or 450?")
            if size == "300":
                sizeconfirmed = "300"
                sizeconfirmedfinal = 1
            elif size == "450":
                sizeconfirmed = "450"
                sizeconfirmedfinal = 1
        else:
            print("Invalid input")
    elif choice == "k":
        if cchoiceconfirmed == 0:
            print("you have not assigned a color to the slab yet")
        elif dchoiceconfirmed == 0:
            print("you have not assigned a depth to the slab yet")
        elif slabshapeconfirmedfinal == 0:
            print("you have not assigned the slab shape")
        elif sizeconfirmedfinal == 0:
            print("you have not assigned the size of the slab")
        else:
            print("ok we are good to go")
            print("So here are your slab details \n The color choice is " + str(cchoiceconfirmed))
            print("\n The depth of the slab is " + str(dchoiceconfirmed))
            print("\n The slab shape is " + str(slabshapeconfirmed))
            print("\n The size of the slab is " + str(sizeconfirmed))
            print("Thank you for using the slab selector program!")
            break
    else:
        print("invalid input")


