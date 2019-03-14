import pygame #bring in the module
import time, sys, csv, Auth,math,random,Automaton224
pygame.init() #initialize pygame
pygame.font.init()

print("Welcome, Player!!! This is the Python Shell, and it is only for developer use. \nPlease enjoy the game, and let us know what you think at feedback@gmail.com")
print("The 'Add Song' option is only for developer use, please don't use it")
print("Look alive to see what's going on behind the scenes")

window = pygame.display.set_mode((800,480)) #Set the size of the game's window

pygame.display.set_caption("SynthEpic") #Set the caption for the game window (top left on bar)
vol = pygame.mixer.music.set_volume(0.6)#sets volume


#Image Loads
bg = pygame.image.load('newscreen.png') #start screen
socis = pygame.image.load('socisinfo.png')
bg2 = pygame.image.load('page 1.png')#screen, song 1's screen
scrn3 = pygame.image.load('page 2.png') #screen, song 2's screen
devscrn = pygame.image.load('Synthep add screen.png')#devscreen
bg3 = pygame.image.load('page 3.png')#song 3's screen
bg4 = pygame.image.load('page 4.png')
bg5 = pygame.image.load('page 5.png')
bg6 = pygame.image.load('page 6.png')
bg7 = pygame.image.load('page 7.png')
bg8 = pygame.image.load('page 8.png')
bg9 = pygame.image.load('page 9.png')
bg10 = pygame.image.load('page 10.png')
bg11 = pygame.image.load('page 11.png')
bg12 = pygame.image.load('page 12.png')
bg13 = pygame.image.load('page 13.png')
bg14 = pygame.image.load('page 14.png')
bg15 = pygame.image.load('page 15.png')
bg16 = pygame.image.load('page 16.png')
bg17 = pygame.image.load('page 17.png')


key = Auth.key
store = Auth.fresh

clock = pygame.time.Clock()

class cursor(object):
    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y 
        self.width = width
        self.height = height
        self.vel = vel

        self.starterx = 270 #cursor is next to start
        self.startery = 336  # cursor is next to start

        self.hitright = 395

        self.secondx = 255 #cusor is nect to add
        self.secondy = 365 #cursor is next to add

        self.change = 0

        self.pagenum = 0

        
    def drawCursor(self,window):
     window.blit(bg,(0,0)) #fill the background with the picture
     pygame.draw.rect(window,(111, 92, 255),(self.x, self.y, self.width, self.height))
        
    def drawScreen2(self, window): #screen for song 1
        window.blit(bg2,(0,0))
        pygame.display.update()

    def drawScreen3(self, window): #screen for song 2
        window.blit(scrn3,(0,0))
        pygame.display.update()

    def drawAddScreen(self, window): #screen for developers
        window.blit(devscrn,(0,0))
        pygame.display.update()

    def drawInfoScreen(self, window): #screen for developers
        window.blit(socis,(0,0))
        pygame.display.update()   

    def update(self, window):
        window.blit(bg,(0,0)) #fill the background with the picture
        cursor.drawCursor(window) #calls draw from cursor object
        pygame.display.update()#updates display to show new cursor position

    #ADD Functions HERE
    def drawScreen4(self, window): #screen for song3
        window.blit(bg3, (0,0))
        pygame.display.update()

    def drawScreen5(self, window): #screen for song4
        window.blit(bg4, (0,0))
        pygame.display.update()

    def drawScreen6(self, window): #screen for song5
        window.blit(bg5, (0,0))
        pygame.display.update()

    def drawScreen7(self, window): #screen for song6
        window.blit(bg6, (0,0))
        pygame.display.update()

    def drawScreen8(self, window): #screen for song7
        window.blit(bg7, (0,0))
        pygame.display.update()

    def drawScreen9(self, window): #screen for song8
        window.blit(bg8, (0,0))
        pygame.display.update()
        
    def drawScreen10(self, window): #screen for song9
        window.blit(bg9, (0,0))
        pygame.display.update()

    def drawScreen11(self, window): #screen for song10
        window.blit(bg10, (0,0))
        pygame.display.update()

    def drawScreen12(self, window): #screen for song11
        window.blit(bg11, (0,0))
        pygame.display.update()

    def drawScreen13(self, window): #screen for song12
        window.blit(bg12, (0,0))
        pygame.display.update()

    def drawScreen14(self, window): #screen for song13
        window.blit(bg13, (0,0))
        pygame.display.update()

    def drawScreen15(self, window): #screen for song14
        window.blit(bg14, (0,0))
        pygame.display.update()

    def drawScreen16(self, window): #screen for song15
        window.blit(bg15, (0,0))
        pygame.display.update()

    def drawScreen17(self, window): #screen for song16
        window.blit(bg16, (0,0))
        pygame.display.update()

    def drawScreen18(self, window): #screen for song17
        window.blit(bg17, (0,0))
        pygame.display.update()


def TakePassword(key):
    passwrd = input('Enter your password: ')
    decrypt = decryptMessage(key,passwrd)
    if decrypt not in store:
        print("Invalid Password!!! Please try again")
    else:
        print("Cleared, access granted")
        print('Loading...')
        time.sleep(1)
        Automaton224.addsong()
        print("Running code synth...writing the song...creating the code...")
        time.sleep(1)
        print("Done! Check output file, and add it into the region. Please come again!")

def redraw():
    window.blit(bg,(0,0)) #fill the background with the picture
    cursor.drawCursor(window) #calls draw from cursor object
    pygame.display.update()#updates display to show new cursor position

def decryptMessage(key, message):

    numOfColumns = int(math.ceil(len(message) / float(key)))

    numOfRows = key

    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    plaintext = [''] * numOfColumns

    column = 0

    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1
        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1
    return ''.join(plaintext)



#main loop
cursor = cursor(270,336, 12, 12,5) #create cursor through class (x pos, y pos, width, height, velocity)
run = True
while run:
    clock.tick(27) #sets a framerate
    #Checking for events

    for event in pygame.event.get(): #this will get a list of events that happen
        if event.type == pygame.QUIT: #Checks if user hits the red X
            run = False

        keys = pygame.key.get_pressed() #gets key presses
        click = pygame.mouse.get_pressed()    

        if keys[pygame.K_DOWN] and cursor.x == cursor.starterx and cursor.y == cursor.startery: #Down arrow key from start
            cursor.y = 365
            cursor.x = 255
            cursor.update(window)
    
        if keys[pygame.K_UP] and cursor.x == cursor.secondx and cursor.y == cursor.secondy: #Up arrow key from add
            cursor.y = 336
            cursor.x = 270
            cursor.update(window)

        if keys[pygame.K_RETURN] and cursor.x == cursor.starterx and cursor.y == cursor.startery: #Press enter on start 
            cursor.change = 1
            cursor.pagenum = 1
            cursor.drawScreen2(window)    

        if keys[pygame.K_ESCAPE]:
            pygame.mixer.music.stop()
            cursor.y = 336
            cursor.x = 270
            cursor.change = 0
            cursor.pagenum = 0

        if keys[pygame.K_RIGHT] and cursor.x == cursor.starterx and cursor.y == cursor.startery: #Right arrow key from start
            cursor.y = 336
            cursor.x = 395
            cursor.update(window)

        if keys[pygame.K_LEFT] and cursor.x == cursor.hitright and cursor.y == cursor.startery: #Left arrow key from socis
            cursor.y = 336
            cursor.x = 270
            cursor.update(window)

        if keys[pygame.K_RETURN] and cursor.x == cursor.hitright and cursor.y == cursor.startery: #Enter on socis
            cursor.drawInfoScreen(window)
            cursor.change = 3
            

        if keys[pygame.K_RIGHT]: #Press right on screen 2
            if cursor.pagenum == 0:
                print("This is the starting page")
            elif cursor.pagenum == 1:
                cursor.drawScreen3(window)
                cursor.pagenum += 1
            elif cursor.pagenum == 2:
                cursor.drawScreen4(window)
                cursor.pagenum += 1
                
            #Add new code below this line
            elif cursor.pagenum == 3: #this is for right arrow key 
                cursor.drawScreen5(window)
                cursor.pagenum += 1
            elif cursor.pagenum == 4: #this is for right arrow key 
                cursor.drawScreen6(window)
                cursor.pagenum += 1
            elif cursor.pagenum == 5: #this is for right arrow key 
                cursor.drawScreen7(window)
                cursor.pagenum += 1
            elif cursor.pagenum == 6: #this is for right arrow key 
                cursor.drawScreen8(window)
                cursor.pagenum += 1
            elif cursor.pagenum == 7: #this is for right arrow key 
                cursor.drawScreen9(window)
                cursor.pagenum += 1
            elif cursor.pagenum == 8: #this is for right arrow key 
                cursor.drawScreen10(window)
                cursor.pagenum += 1
            elif cursor.pagenum == 9: #this is for right arrow key 
                cursor.drawScreen11(window)
                cursor.pagenum += 1
            elif cursor.pagenum == 10: #this is for right arrow key 
                cursor.drawScreen12(window)
                cursor.pagenum += 1
            elif cursor.pagenum == 11: #this is for right arrow key 
                cursor.drawScreen13(window)
                cursor.pagenum += 1
            elif cursor.pagenum == 12: #this is for right arrow key 
                cursor.drawScreen14(window)
                cursor.pagenum += 1
            elif cursor.pagenum == 13: #this is for right arrow key 
                cursor.drawScreen15(window)
                cursor.pagenum += 1
            elif cursor.pagenum == 14: #this is for right arrow key 
                cursor.drawScreen16(window)
                cursor.pagenum += 1
            elif cursor.pagenum == 15: #this is for right arrow key 
                cursor.drawScreen17(window)
                cursor.pagenum += 1
            elif cursor.pagenum == 16: #this is for right arrow key 
                cursor.drawScreen18(window)
                cursor.pagenum += 1
            

        if keys[pygame.K_LEFT]: #Press left on screen 2
            if cursor.pagenum == 1:
                print("Boundary")
            elif cursor.pagenum == 2:
                cursor.drawScreen2(window)
                cursor.pagenum -= 1
            elif cursor.pagenum == 3:
                cursor.drawScreen3(window)
                cursor.pagenum -= 1
            #Add new code below this line
            elif cursor.pagenum == 4: #this is for left arrow key 
                cursor.drawScreen4(window)
                cursor.pagenum -= 1
            elif cursor.pagenum == 5: #this is for left arrow key 
                cursor.drawScreen5(window)
                cursor.pagenum -= 1
            elif cursor.pagenum == 6: #this is for left arrow key 
                cursor.drawScreen6(window)
                cursor.pagenum -= 1
            elif cursor.pagenum == 7: #this is for left arrow key 
                cursor.drawScreen7(window)
                cursor.pagenum -= 1
            elif cursor.pagenum == 8: #this is for left arrow key 
                cursor.drawScreen8(window)
                cursor.pagenum -= 1
            elif cursor.pagenum == 9: #this is for left arrow key 
                cursor.drawScreen9(window)
                cursor.pagenum -= 1
            elif cursor.pagenum == 10: #this is for left arrow key 
                cursor.drawScreen10(window)
                cursor.pagenum -= 1
            elif cursor.pagenum == 11: #this is for left arrow key 
                cursor.drawScreen11(window)
                cursor.pagenum -= 1
            elif cursor.pagenum == 12: #this is for left arrow key 
                cursor.drawScreen12(window)
                cursor.pagenum -= 1
            elif cursor.pagenum == 13: #this is for left arrow key 
                cursor.drawScreen13(window)
                cursor.pagenum -= 1
            elif cursor.pagenum == 14: #this is for left arrow key 
                cursor.drawScreen14(window)
                cursor.pagenum -= 1
            elif cursor.pagenum == 15: #this is for left arrow key 
                cursor.drawScreen15(window)
                cursor.pagenum -= 1
            elif cursor.pagenum == 16: #this is for left arrow key 
                cursor.drawScreen16(window)
                cursor.pagenum -= 1

            elif cursor.pagenum == 17: #this is for left arrow key 
                cursor.drawScreen17(window)
                cursor.pagenum -= 1

            
                
        
        if click[0] == 1 and cursor.pagenum == 1: #Click on page 2 (Song 1's screen)
            SGH1 = pygame.mixer.music.load('Such_Great_Heights_Pi.wav') #loads such great heights
            pygame.mixer.music.play(1) #plays once
            opts = ["Hey! that tickles", "Stop that", "You clicked me", "Input received"]
            choice = random.choice(opts)
            print(choice)

            
            
        elif click[0] == 1 and cursor.pagenum == 2: #Click on page 3 (Song 2's screen)
            MPS = pygame.mixer.music.load('Motion_Picture_Soundtrack_Pi.wav') #loads motion picture soundtrack
            vol = pygame.mixer.music.set_volume(0.7)
            pygame.mixer.music.play(1) #plays once
            opts = ["Hey! that tickles", "Stop that", "You clicked me", "Input received"]
            choice = random.choice(opts)
            print(choice)
        #Add Part 4 of Automaton's Code below here

        elif click[0] == 1 and cursor.pagenum == 3:
            pygame.mixer.music.load('Moonlight_Pi.wav')
            vol = pygame.mixer.music.set_volume(0.6)
            pygame.mixer.music.play(1)
            opts = ['Hey! that tickles', 'Stop that', 'You clicked me', 'Input received']
            choice = random.choice(opts) 
            print(choice)

        elif click[0] == 1 and cursor.pagenum == 4:
            pygame.mixer.music.load('My_Lie_Pi.wav')
            vol = pygame.mixer.music.set_volume(0.8)
            pygame.mixer.music.play(1)
            opts = ['Hey! that tickles', 'Stop that', 'You clicked me', 'Input received']
            choice = random.choice(opts) 
            print(choice)

        elif click[0] == 1 and cursor.pagenum == 5:
            pygame.mixer.music.load('You_Say_Run_Pi.wav')
            vol = pygame.mixer.music.set_volume(0.8)
            pygame.mixer.music.play(1)
            opts = ['Hey! that tickles', 'Stop that', 'You clicked me', 'Input received']
            choice = random.choice(opts) 
            print(choice)

        elif click[0] == 1 and cursor.pagenum == 6:
            pygame.mixer.music.load('Colors_Pi.wav')
            pygame.mixer.music.play(1)
            opts = ['Hey! that tickles', 'Stop that', 'You clicked me', 'Input received']
            choice = random.choice(opts) 
            print(choice)

        elif click[0] == 1 and cursor.pagenum == 7:
            pygame.mixer.music.load('Deep_In_Abyss_Pi.wav')
            pygame.mixer.music.play(1)
            opts = ['Hey! that tickles', 'Stop that', 'You clicked me', 'Input received']
            choice = random.choice(opts) 
            print(choice)

        elif click[0] == 1 and cursor.pagenum == 8:
            pygame.mixer.music.load('Unravel_Pi.wav')
            pygame.mixer.music.play(1)
            opts = ['Hey! that tickles', 'Stop that', 'You clicked me', 'Input received']
            choice = random.choice(opts) 
            print(choice)

        elif click[0] == 1 and cursor.pagenum == 9:
            pygame.mixer.music.load('Glassy_Sky_Pi.wav')
            pygame.mixer.music.play(1)
            opts = ['Hey! that tickles', 'Stop that', 'You clicked me', 'Input received']
            choice = random.choice(opts) 
            print(choice)

        elif click[0] == 1 and cursor.pagenum == 10:
            pygame.mixer.music.load('Wii_Shop_Theme_Pi.wav')
            pygame.mixer.music.play(1)
            opts = ['Hey! that tickles', 'Stop that', 'You clicked me', 'Input received']
            choice = random.choice(opts) 
            print(choice)

        elif click[0] == 1 and cursor.pagenum == 11:
            pygame.mixer.music.load('The_Lion_Sleeps_Tonight_Pi.wav')
            pygame.mixer.music.play(1)
            opts = ['Hey! that tickles', 'Stop that', 'You clicked me', 'Input received']
            choice = random.choice(opts) 
            print(choice)

        elif click[0] == 1 and cursor.pagenum == 12:
            pygame.mixer.music.load('Shadow_Of_The_Day_Pi.wav')
            pygame.mixer.music.play(1)
            opts = ['Hey! that tickles', 'Stop that', 'You clicked me', 'Input received']
            choice = random.choice(opts) 
            print(choice)

        elif click[0] == 1 and cursor.pagenum == 13:
            pygame.mixer.music.load('Never_Gonna_Give_You_Up_Pi.wav')
            pygame.mixer.music.play(1)
            opts = ['Hey! that tickles', 'Stop that', 'You clicked me', 'Input received']
            choice = random.choice(opts) 
            print(choice)

        elif click[0] == 1 and cursor.pagenum == 14:
            pygame.mixer.music.load('Candy_Paint_Pi.wav')
            pygame.mixer.music.play(1)
            opts = ['Hey! that tickles', 'Stop that', 'You clicked me', 'Input received']
            choice = random.choice(opts) 
            print(choice)

        elif click[0] == 1 and cursor.pagenum == 15:
            pygame.mixer.music.load('One_Dance_Pi.wav')
            pygame.mixer.music.play(1)
            opts = ['Hey! that tickles', 'Stop that', 'You clicked me', 'Input received']
            choice = random.choice(opts) 
            print(choice)

        elif click[0] == 1 and cursor.pagenum == 16:
            pygame.mixer.music.load('Despacito_Pi.wav')
            pygame.mixer.music.play(1)
            opts = ['Hey! that tickles', 'Stop that', 'You clicked me', 'Input received']
            choice = random.choice(opts) 
            print(choice)

        elif click[0] == 1 and cursor.pagenum == 17:
            pygame.mixer.music.load('Idontwannabeyouanymore_Pi.wav')
            pygame.mixer.music.play(1)
            opts = ['Hey! that tickles', 'Stop that', 'You clicked me', 'Input received']
            choice = random.choice(opts) 
            print(choice) 


        elif keys[pygame.K_RETURN] and cursor.x == cursor.secondx and cursor.y == cursor.secondy: #Press enter on add 
            cursor.change = 2
            cursor.drawAddScreen(window)
            TakePassword(key)
            
        elif cursor.change == 0: #Return to the home screen
            redraw()

        elif cursor.change == 1: #Hold the Second song screen
            cursor.x = 0
            cursor.y = 0
            
        elif cursor.change == 2: #Hold the Developer Screen
            cursor.drawAddScreen(window)

        elif cursor.change == 3: #Hold the Developer Screen
            cursor.drawInfoScreen(window)


        else:
            redraw()

        
    
    



pygame.quit() #closes the game down


