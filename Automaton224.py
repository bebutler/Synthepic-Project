

def addsong():
    print("Hello and welcome to the prgram that writes code so you don't have to")
    print("Thank you for using the Automaton Service")

    screennum = int(input("Please enter the song number: "))
    filename = input("Please enter the picture's filename: ")
    songname = input("Plese enter the song's filename: ")
    print("Make sure you've already made the screen's background image, and song, and added them to the directory")

    print("Preparing to write your code")

    file = open("code.txt", "w")


 
    right = screennum + 1

    left = right - 1

    file.write("\n Part 1-------\n")
    file.write("bg"+ str(screennum) + " = pygame.image.load('"+ filename + "')\n")

    print("Declared Variables")

    file.write("\n Part 2-------\n")
    file.write("def drawScreen" + str(screennum + 1) +
           "(self, window): #screen for song" + str(screennum) + "\n" +
           "window.blit(bg" + str(screennum)  + ", (0,0))\n"
           "pygame.display.update()\n\n")

    print("Done writing Function")

    file.write("\n Part 3-------\n")
    file.write("elif cursor.pagenum == " + str(screennum -1)
           + ": #this is for right arrow key \n"
           + "cursor.drawScreen" + str(right) + "(window)\n"
           + "cursor.pagenum += 1 \n")
    print("Finished Right Check")


    file.write("elif cursor.pagenum == " + str(screennum)
           + ": #this is for left arrow key \n"
           + "cursor.drawScreen" + str(left) + "(window)\n" + "cursor.pagenum -= 1 \n")

    print("Finished Left Check")

    file.write("\n Part 4-------\n")
    file.write("elif click[0] == 1 and cursor.pagenum == " + str(screennum)
           + ":\n" + "pygame.mixer.music.load('"+songname+"')\n" +
           "pygame.mixer.music.play(1)\n" +
           "opts = ['Hey! that tickles', 'Stop that', 'You clicked me', 'Input received']" +
            "\nchoice = random.choice(opts) \n" +
            "print(choice)")

    print("Finished Click Check")

    file.close()

           
           
           
           

        
