#Author : Kenzhi Wong
#This program aims to create an algorithmic pattern design using python's turtle module. The program consists of three different patterns.

import turtle


#Input file name
while True:
    a = input("Please enter your file input : ")
    try:
        inputfile = open(a,"r")
        break
    except FileNotFoundError:
        print("File could not be found")


try:
    #Basic Pattern Function

    def normal_circle():
        turtle.circle(70)

    def square(x):
        turtle.forward(x)
        for i in range(3):
            turtle.left(90)
            turtle.forward(x)
        turtle.left(90)

    #Inspired from YouTube Kartik Agarwal Channel
    def crystal(x):
        turtle.forward(x)
        turtle.left(60)
        turtle.forward(x)
        turtle.left(120)
        turtle.forward(x)
        turtle.left(60)
        turtle.forward(x)
        turtle.left(120)

    #Own Creation
    def enneagon(x): #Enneagon is 9 sided polygon
        turtle.forward(x)
        for i in range (8):
            turtle.left(40)
            turtle.forward(x)
        turtle.left(60)





    #Iteration Pattern Function

    #Inspired from YouTube Kartik Agarwal Channel
    def crystal_pattern():
        for i in range (8):
            for j in range (8): #have to be 8
                crystal(5+i*5)
                turtle.left(45)#have to be 45

    #Own Creation
    def circle_pattern():
        for i in range (100):
            turtle.circle(30)
            turtle.left(10)

    #Own Creation
    def enneagon_pattern():
        for i in range (100):
            enneagon(23)
            turtle.left(10)




    #Main Program Input
    print("Running program")
    dict ={}
    i = 0
    #User wish the program to display all the three patterns.
    if a == "Data1.txt":
        for lines in inputfile:
            alist = lines.split()
            if i<=5:
                dict[i] = alist[0]
                i += 1
            elif i>5:
                dict[i] = alist[0:2]
                i += 1
    #User wish to display exactly one pattern.     
    elif a == "Data2.txt":
        for lines in inputfile:
            alist = lines.split()
            if i <= 4:
                dict[i] = alist[0]
                i += 1
            elif i>4:
                dict[i] = alist[0:2]
                i += 1
    #User wish to display two out of the three patterns provided.
    elif a == "Data3.txt":
        for lines in inputfile:
            alist = lines.split()
            if i <= 6:
                dict[i] = alist[0]
                i += 1
            elif i > 6:
                dict[i] = alist[0:2]
                i += 1       
    turtle.bgcolor(dict[0])
    turtle.pensize(1)
    turtle.tracer(False)



    #Main program: Outer Circle
    def OuterSheetsCircle():
        i = -560 #Let i be the x-coordinate
        j = -420 #Let j be the y-coordinate
        while j <= 280:
            for count in range (1,7): #Let count be the row
                while i <= 630:  
                    turtle.penup()
                    turtle.setposition (i,j)
                    turtle.pendown()
                    turtle.color(dict[1])
                    normal_circle()
                    i += 280
                if count % 2 != 0:
                    i = -560+140
                elif count %2 == 0:
                    i = -560-2*140
                j += 140
    OuterSheetsCircle()
                
    #Main program: Outer Square
    def OuterSheetsSquare():
        i = -490+3 #Let i be the x-coordinate
        j = -420+3 #Let j be the y-coordinate
        while j <= 280:
            for count in range (1,7): #Let count be the row
                while i <= 630:  
                    turtle.penup()
                    turtle.setposition (i,j)
                    turtle.pendown()
                    turtle.color(dict[2])
                    square(134)
                    i = i + 4*70
                if count % 2 != 0:
                    i = -490+3-140
                elif count %2 == 0:
                    i = -490+3-2*140
                j += 140
    OuterSheetsSquare()





    #Main program iteration pattern

    #Displaying all the three patterns.
    def FirstModel():
        for a in range(6,63+1,3):
            turtle.penup()
            turtle.setposition(int(dict[a][0]),int(dict[a][1]))
            turtle.pendown()
            turtle.color(dict[3])
            circle_pattern()
        for b in range(7,64+1,3):
            turtle.penup()
            turtle.setposition(int(dict[b][0]),int(dict[b][1]))
            turtle.pendown()
            turtle.color(dict[4])
            crystal_pattern()
        for c in range(8,65+1,3):
            turtle.penup()
            turtle.setposition(int(dict[c][0]),int(dict[c][1]))
            turtle.pendown()
            turtle.color(dict[5])
            enneagon_pattern()
    if a == "Data1.txt":
        FirstModel()

    #Displaying exactly one pattern.
    def SecondModel():
        for a in range (5,64+1):
            turtle.penup()
            turtle.setposition(int(dict[a][0]),int(dict[a][1]))
            turtle.pendown()
            turtle.color(dict[3])
            if dict[4] == "Pattern_1":
                circle_pattern()
            elif dict[4] == "Pattern_2":
                crystal_pattern()
            elif dict[4] == "Pattern_3":
                enneagon_pattern()
    if a == "Data2.txt":
        SecondModel()

    #Displaying two out of three patterns only.
    def ThirdModel():
        for a in range (7,60+1,2):
            turtle.penup()
            turtle.setposition(int(dict[a][0]),int(dict[a][1]))
            turtle.pendown()
            turtle.color(dict[3])
            if dict[5] == "Pattern_1":
                circle_pattern()
            elif dict[5] == "Pattern_2":
                crystal_pattern()
            elif dict[5] == "Pattern_3":
                enneagon_pattern()
        for b in range (8,61+1,2):
            turtle.penup()
            turtle.setposition(int(dict[b][0]),int(dict[b][1]))
            turtle.pendown()
            turtle.color(dict[4])
            if dict[6] == "Pattern_1":
                circle_pattern()
            elif dict[6] == "Pattern_2":
                crystal_pattern()
            elif dict[6] == "Pattern_3":
                enneagon_pattern()
    if a == "Data3.txt":
        ThirdModel()

except:
    print("Program reads an error. Please refer to the manual.")

