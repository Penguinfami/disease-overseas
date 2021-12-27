#Final Game.py
#January 18 2019
#Christine and Melody
#Final Project

import pygame
pygame.init()
import time

import random
from random import randint

# display variables
WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0,0,0)
CYAN = (0, 255,255)
BROWN = (168, 42,42)
GRAY = (190,190,190)
LIGHTGREEN = (144,238,144)
LIGHTGRAY = (169,169,169)
WHITE = (255,255,255)
YELLOW = (255,252,0)
DARKBLUE = (0,18,117)

gameWindow = pygame.display.set_mode ((800,600))
fontOne = pygame.font.SysFont("Courier New Bold", WIDTH*HEIGHT/10000)
fontTwo = pygame.font.SysFont("Courier New Bold", WIDTH*HEIGHT/14000)
fontThree = pygame.font.SysFont("Courier New Bold", 40)
fontFour = pygame.font.SysFont("Courier New Bold", 30)
fontFive = pygame.font.SysFont("Arial", 75)
fontSix = pygame.font.SysFont("Courier New Bold", WIDTH*HEIGHT/9500)


#obstacle dodging variables
playerX = 60
playerY = HEIGHT*3/4
x2 = 700
y2 = 0
x3 = 800
y3 = 0
x4 = 600
y4 = 50
left = False
left4 = True
backgroundx = 0
backgroundy = 0
plane1 = pygame.image.load ("plane1.png")
plane2 = pygame.image.load ("plane2.png")
plane3 = pygame.image.load ("plane3.png")
plane4 = pygame.image.load ("plane4.png")
plane5 = pygame.image.load ("plane5.png")
plane6 = pygame.image.load ("plane6.png")
plane = [plane1,plane2,plane3,plane4,plane5,plane6]
virus1 = pygame.image.load ("virusOne.png")
virus2 = pygame.image.load ("virusTwo.png")
virus3 = pygame.image.load ("virusThree.png")
virus4 = pygame.image.load ("virusFour.png")
virus5 = pygame.image.load ("virusFive.png")
virus = [virus1,virus2,virus3,virus4,virus5]
numVirus1 = virus1
numVirus2 = virus2
numVirus3 = virus3
player = plane1
heart = pygame.image.load("heart.png")

#treasure chest
openChest = pygame.image.load("openChest.png")
closedChest = pygame.image.load ("closedChest.png")
chestY = 490
chestX = 1700
chest = closedChest
playerplane = pygame.image.load("playerplane.png")

#jumping obstacles
jump = False
jumpHeight = 9
playerRun = pygame.image.load ("PersonRun.png")
playerSide = pygame.image.load ("Person side.png")
playerRun2 = pygame.image.load ("PersonRun2.png")

#continents
asia = False
antartica = False
northAmerica = False
europe = False
australia = False
africa = False
southAmerica = False
numContinent = 0
asiaC = 1
antarticaC = 2
northamericaC = 3
europeC = 4
oceaniaC = 5
africaC = 6
southamericaC = 7
chosencontinents = [asiaC,antarticaC,northamericaC,europeC,oceaniaC,africaC, southamericaC]

#antidotes
blueAntidote = pygame.image.load ("blueP.png")
greenAntidote = pygame.image.load("greenP.png")
redAntidote = pygame.image.load("redP.png")
yellowAntidote = pygame.image.load("yellowP.png")
antidotes = [blueAntidote,greenAntidote,redAntidote,yellowAntidote]
numAntidote = 0

#menu and death screen 
menuScreen = pygame.image.load ("menu.png")
end1 = pygame.image.load("end1.png")
end2 = pygame.image.load("end2.png")
end3 = pygame.image.load ("end3.png")
end4 = pygame.image.load ("end4.png")
end5 = pygame.image.load ("end5.png")
end = [end1,end2,end3,end4,end5]
menuBackground = pygame.image.load("caution.png")

#sound effects
DEATH = pygame.mixer.Sound ("DUN DUN DUN.wav")
DEATH.set_volume(1)
YAY = pygame.mixer.Sound("YAY.wav")
YAY.set_volume(1)
SAD = pygame.mixer.Sound ("sadtrombone.wav")
SAD.set_volume(1)
SCREAM = pygame.mixer.Sound ('scream.wav')
SCREAM.set_volume(1)
pygame.mixer.music.load ("Lounge Game1.wav") 
pygame.mixer.music.play(-1) 
#map
mapPic = pygame.image.load("map.png")
pinpoint = pygame.image.load("pinpoint.png")
thang = pygame.image.load ("thang.png")


#gameplay variables
life = 1
menu = True
newOne = False
newOne2 = False
newOne3 = False
gameRun = True
instructions = False
menuDisplay = True
run = False
run2 = False
deathScreen = False
instructionsScreen = False
nextButton = False
play = False
mapScreen = False
victoryScreen = False
creditScreen = False


#the game
while gameRun == True:
    #menu
    while menu == True:
        if menuDisplay == True and play == False:
            gameWindow.fill (BROWN)

            menuBackground = pygame.image.load("caution.png")
            gameWindow.blit (menuBackground, (0,0))

            menuDrawing = pygame.image.load ("menuDrawing.png")
            gameWindow.blit (menuDrawing, (0,0))

            font1 = pygame.font.SysFont ("Courier New Bold", 80)
            graphics = font1.render ("Disease", 0, WHITE)
            gameWindow.blit (graphics, (295, 40))

            font2 = pygame.font.SysFont ("Courier New Bold", 60)
            graphics = font2.render ("Overseas", 0, WHITE)
            gameWindow.blit (graphics, (295, 100))

            font3 = pygame.font.SysFont ("Courier New Bold", 3)
            graphics = font2.render ("Play", 0, WHITE)
            gameWindow.blit (graphics, (290, 400))

            font4 = pygame.font.SysFont ("Courier New Bold", 3)
            graphics = font2.render ("Instructions", 0, WHITE)
            gameWindow.blit (graphics, (290, 440))

            font5 = pygame.font.SysFont ("Courier New Bold", 3)
            graphics = font2.render ("Exit", 0, WHITE)
            gameWindow.blit (graphics, (290, 480))
            pygame.display.update()
            
        #choosing from menu  
        for event in pygame.event.get():
            (mouseX, mouseY) = pygame.mouse.get_pos()   
            mouse = pygame.mouse.get_pressed()
        if mouseX >= 290 and mouseX<= 290 + 100 and mouseY <= 400 + 40 and mouseY >= 400 and menuDisplay == True:
            font3 = pygame.font.SysFont ("Courier New Bold", 3)
            graphics = font2.render ("Play", 0, YELLOW)
            gameWindow.blit (graphics, (290, 400))
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                play = True
                menuDisplay = False
                random.shuffle(chosencontinents)
            #generating the continents
                for i in range (4):
                    if chosencontinents [i] == asiaC:
                        print "asia"
                        asiaC = True
                    elif chosencontinents [i] == antarticaC:
                        print "antartica"
                        antarticaC = True
                    elif chosencontinents [i] == northamericaC:
                        print "northamerica"
                        northamericaC = True
                    elif chosencontinents [i] == europeC:
                        print "europe"
                        europeC = True
                    elif chosencontinents [i] == oceaniaC:
                        print "oceania"
                        oceaniaC = True
                    elif chosencontinents [i] == africaC:
                        print "africa"
                        africaC = True
                    elif chosencontinents [i] == southamericaC:
                        print "southamerica"
                        southamericaC = True
                #end for
                        pygame.display.update()
                    pygame.display.update()
        if(mouseX>= 290 and mouseX<= 290+250 and mouseY <=440+40 and mouseY >= 440 and menuDisplay == True and play == False):
            graphics = font2.render ("Instructions", 0, YELLOW)
            gameWindow.blit (graphics, (290, 440))
            if event.type == pygame.MOUSEBUTTONDOWN:
                instructions = True
                gameWindow = pygame.display.set_mode ((880,640))
                instructionsScreen = True
                menuDisplay = False
        #end elif
        if (mouseX >= 290 and mouseX <= 290+90 and mouseY <= 480+40 and mouseY>=490 and menuDisplay == True and play == False):
            graphics = font2.render ("Exit", 0, YELLOW)
            gameWindow.blit (graphics, (290, 480))
            if (event.type == pygame.MOUSEBUTTONDOWN ):
                gameRun = False
                menu = False
                play = False
        #end elif
                
        #starting the game        
        if  play == True:
            menu = False
            run = True
            mapScreen = True

            
            #Introduction: A thousand years ago...
            intro = pygame.image.load("intro.png")
            gameWindow.blit(intro, (0, 0))
            #------------------------------------------------------
            font1 = pygame.font.SysFont ("Courier New Bold", 40)
            graphics = font1.render("Thousands of years ago...", 0, WHITE)
            gameWindow.blit(graphics, (330, 560))

            pygame.display.update()
            pygame.time.delay(5000)

            #Slide 2: Epidemic disease
            pygame.draw.rect(gameWindow, GRAY, (0, 0, 800, 600), 0)
            #-------------------------------------------------------
            firstImg = pygame.image.load("grave.png")
            gameWindow.blit(firstImg, (0,0))
            #-------------------------------------------------------
            secImg = pygame.image.load("poison.png")
            gameWindow.blit(secImg, (40, 280))
            #-------------------------------------------------------
            font2 = pygame.font.SysFont ("Courier New Bold", 30)
            graphics = font2.render("An epidemic disease that spread throughout Europe killed millions of people", 0, WHITE)
            gameWindow.blit(graphics, (20, 280))
            #-------------------------------------------------------
            font3 = pygame.font.SysFont ("Courier New Bold", 30)
            graphics = font3.render("The disease was called 'the Silent Killer' and was spread through tiny rodents", 0, WHITE)
            gameWindow.blit(graphics, (15, 570))

            pygame.display.update()
            pygame.time.delay(5000)

            #Slide 4: Antidote remedy 
            pygame.draw.rect(gameWindow, GRAY, (0, 0, 800, 600), 0)
            #----------------------------------------------------------
            fourthImg = pygame.image.load("potion.png")
            gameWindow.blit(fourthImg, (-50,20))
            #----------------------------------------------------------
            font5 = pygame.font.SysFont ("Courier New Bold", 30)
            graphics = font5.render("Humanity was able to find the 4 antidotes to cure the past deadly disease", 0, WHITE)
            gameWindow.blit(graphics, (40, 20))
            
            pygame.display.update()
            pygame.time.delay (5000)

            #Slide 3: Modern day
            thirdImg = pygame.image.load("moderncity.png")
            gameWindow.blit(thirdImg, (0,0))
            #--------------------------------------------------------
            font4 = pygame.font.SysFont ("Courier New Bold", 30)
            graphics = font4.render("Years later, the disease has recurred and is spreading at double the speed", 0, WHITE)
            gameWindow.blit(graphics, (35, 570))

            pygame.display.update()
            pygame.time.delay (5000)

            #Slide 5: Planet
            fifthImg = pygame.image.load("planet.png")
            gameWindow.blit(fifthImg, (0,0))
            #----------------------------------------------------------
            font6 = pygame.font.SysFont ("Courier New Bold", 30)
            graphics = font6.render("However, over the years the antidotes have been scattered", 0, WHITE)
            gameWindow.blit(graphics, (90,10))
            #----------------------------------------------------------
            font7 = pygame.font.SysFont("Courier New Bold", 30)
            graphics = font7.render("Humanity has forgotten the exact location of each antidote", 0, WHITE)
            gameWindow.blit(graphics, (100, 570))

            pygame.display.update()
            pygame.time.delay (5000)

            #Slide 6: Plane drawing
            planeBackground = pygame.image.load("planebackg.png")
            gameWindow.blit(planeBackground, (0,0))
            #----------------------------------------------------------
            sixthImg = pygame.image.load("plane.png")
            gameWindow.blit(sixthImg, (30,200))
            #----------------------------------------------------------
            font8 = pygame.font.SysFont ("Courier New Bold", 27)
            graphics = font8.render ("You will be travelling by plane, however...", 0, WHITE)
            gameWindow.blit(graphics, (7, 520))
            #----------------------------------------------------------
            font9 = pygame.font.SysFont ("Courier New Bold", 27)
            graphics = font9.render("your plane only has enough fuel to bring you to 4 different continents of your choosing", 0, WHITE)
            gameWindow.blit(graphics, (7, 550))

            pygame.display.update()
            pygame.time.delay (5000)

            #Final slide: World 
            seventhImg = pygame.image.load("world.png")
            gameWindow.blit(seventhImg, (0,0))
            #-----------------------------------------------------------
            font10 = pygame.font.SysFont ("Courier New Bold", 40)
            graphics = font10.render ("You are the only hope to save humanity", 0, WHITE)
            gameWindow.blit(graphics, (130, 570))
        #end if

        #main menu    

        #end if
            
        if instructions == True:
            
            gameWindow.fill (BLACK)


            # Background

            backG = pygame.image.load ("4.jpeg")

            gameWindow.blit(backG, (0, 0))



            # Instruction border

            pygame.draw.rect(gameWindow, BLUE, (20, 10, 840, 460), 3)


            # Instruction line

            pygame.draw.line(gameWindow, YELLOW, (0, 90), (20, 90), 3)

            pygame.draw.line(gameWindow, YELLOW, (0, 200), (20, 200), 3)

            pygame.draw.line(gameWindow, YELLOW, (0, 250), (20, 250), 3)




            # Back button

            pygame.draw.rect(gameWindow, BLUE, (50, 550, 70, 50), 3)

            pygame.draw.line(gameWindow, BLUE, (0, 580), (50, 580), 3)


            font1 = pygame.font.SysFont ("Courier New Bold", 100)

            graphics = font1.render ("Instructions", 0, YELLOW)

            gameWindow.blit(graphics, (250, 50))


            font2 = pygame.font.SysFont ("Courier New Bold", 20)

            graphics = font2.render ("An epidemic disease has taken over the world and you are the only hope!", 0, WHITE)

            gameWindow.blit (graphics, (30, 130))


            font3 = pygame.font.SysFont ("Courier New Bold", 30)

            graphics = font3.render ("Here's the catch...", 0, YELLOW)

            gameWindow.blit(graphics, (30, 180))


            font4 = pygame.font.SysFont ("Courier New Bold", 20)

            graphics = font4.render ("* You have", 0, WHITE)

            gameWindow.blit(graphics, (30, 220))


            font5 = pygame.font.SysFont ("Courier New Bold", 20)

            graphics = font5.render ("5 out of 7 chances to choose the 4 correct continents containing the 4 different antidotes.", 0, YELLOW)

            gameWindow.blit(graphics, (102, 220))


            font6 = pygame.font.SysFont ("Courier New Bold", 20)

            graphics = font6.render ("* You have", 0, WHITE)

            gameWindow.blit(graphics, (30, 250))


            font7 = pygame.font.SysFont ("Courier New Bold", 20)

            graphics = font7.render ("30 lives to complete the mission", 0, YELLOW)

            gameWindow.blit(graphics, (102, 250))


            font8 = pygame.font.SysFont ("Courier New Bold", 20)

            graphics = font8.render ("* Once all chances and/or lives are lost, you have failed to save humanity", 0, WHITE)

            gameWindow.blit(graphics, (30, 280))


            font9 = pygame.font.SysFont ("Courier New Bold", 20)

            graphics = font9.render ("To select a continent, use the mouse to click a pinpoint", 0, WHITE)

            gameWindow.blit(graphics, (30, 370))


            font10 = pygame.font.SysFont ("Courier New Bold", 20)

            graphics = font10.render ("Use the arrow keys to move your character and dodge the obstacles", 0, WHITE)

            gameWindow.blit(graphics, (30, 400))


            font11 = pygame.font.SysFont ("Courier New Bold", 20)

            graphics = font11.render ("Object: Retrieve all 4 antidotes to cure the pandemic disease ", 0, WHITE)

            gameWindow.blit(graphics, (30, 500))


            font12 = pygame.font.SysFont ("Courier New Bold", 30)

            graphics = font12.render ("How to play", 0, YELLOW)

            gameWindow.blit(graphics, (30, 330))


            font13 = pygame.font.SysFont ("Courier New Bold", 30)

            graphics = font12.render ("Exit", 0, YELLOW)

            gameWindow.blit(graphics, (65, 565))



            #cursor

            mouseCursor = pygame.image.load ("cursor.png")

            gameWindow.blit(mouseCursor, (430, 350))


            #arrow keys

            arrowK = pygame.image.load("arrowkeys.png")

            gameWindow.blit(arrowK, (490, 350))


            #blue antidote


            gameWindow.blit(blueAntidote, (670, 140))


            #green antidote


            gameWindow.blit(greenAntidote, (690, 140))


            #red antidote


            gameWindow.blit(redAntidote, (710, 140))


            #yellow antidote


            gameWindow.blit(yellowAntidote, (730, 140))


            while instructions == True:

                for event in pygame.event.get():

                    mouse = pygame.mouse.get_pressed()

                    (mouseX, mouseY) = pygame.mouse.get_pos()

                    if event.type == pygame.MOUSEBUTTONDOWN and mouseX >= 50 and mouseX <= 50 + 70 and mouseY >= 550 and mouseY <= 550 + 50:

                        exit = True
                        instructionScreen = False
                        instructions = False
                        menuDisplay = True
                        gameWindow = pygame.display.set_mode ((800,600))
                    #end if
                        
                    pygame.display.update()
               #end for     
            # end while

            
            for event in pygame.event.get():
                mouse = pygame.mouse.get_pressed()
                (mouseX, mouseY) = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN and mouseX>= 530 and mouseX<= 750 and mouseY <=300+110 and mouseY >= 300:
                    instructions = False
                    menuDisplay = True

        pygame.display.update()
    #end if
        
    while mapScreen == True:
        gameWindow = pygame.display.set_mode ((800,600))

        #Map
        gameWindow.blit(mapPic, (0, 0))
        #North America
        gameWindow.blit(pinpoint, (150, 200))
        #Africa
        gameWindow.blit(pinpoint, (390, 300))
        #South America
        gameWindow.blit(pinpoint, (235, 390))
        #Europe
        gameWindow.blit(pinpoint, (403, 140))
        #Asia
        gameWindow.blit(pinpoint, (600, 150))
        #Australia
        gameWindow.blit(pinpoint, (650, 402))
        #Antartica
        gameWindow.blit(pinpoint, (395, 550))


        for event in pygame.event.get():
            mouse = pygame.mouse.get_pressed()
            (mouseX, mouseY) = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and mouseX >= 150 and mouseX <=150 + 20 and mouseY >=200 and mouseY <= 200 + 20:
                run = True
                africa = False
                northAmerica = True
                southAmerica = False
                europe = False
                asia = False
                australia = False
                antartica = False
                mapScreen = False 
                background = pygame.image.load("northAmericaBackground.png")
            #end if
            if event.type == pygame.MOUSEBUTTONDOWN and mouseX >= 390 and mouseX <= 390 + 20 and mouseY >= 300 and mouseY <= 300 + 20:
                run = True
                northAmerica = False
                southAmerica = False
                europe = False
                asia = False
                australia = False
                antartica = False
                mapScreen = False
                africa = True
                background = pygame.image.load("africaBackground.png")
            #end if
            if event.type == pygame.MOUSEBUTTONDOWN and mouseX >= 235 and mouseX <= 235 + 20 and mouseY >= 390 and mouseY <= 390 + 20:
                run = True
                northAmerica = False
                africa = False
                europe = False
                asia = False
                australia = False
                antartica = False
                mapScreen = False
                southAmerica = True
                background = pygame.image.load("southAmericaBackground.png")
            #end if
            if event.type == pygame.MOUSEBUTTONDOWN and mouseX >= 403 and mouseX <= 403 + 20 and mouseY >= 140 and mouseY <= 140 + 20:
                run = True
                northAmerica = False
                southAmerica = False
                africa = False
                asia = False
                australia = False
                antartica = False
                mapScreen = False
                europe = True
                background = pygame.image.load("europeBackground.png")
            #end if
            if event.type == pygame.MOUSEBUTTONDOWN and mouseX >= 600 and mouseX <= 600 + 20 and mouseY >= 150 and mouseY <= 150 + 20:
                run = True
                northAmerica = False
                southAmerica = False
                africa = False
                europe = False
                australia = False
                antartica = False
                mapScreen = False
                asia = True
                background = pygame.image.load("asiaBackground.png")
            #end if
            if event.type == pygame.MOUSEBUTTONDOWN and mouseX >= 650 and mouseX <= 650 + 20 and mouseY >= 402 and mouseY <= 402 + 20:
                run = True
                northAmerica = False
                southAmerica = False
                europe = False
                africa = False
                asia = False
                antartica = False
                mapScreen = False
                australia = True
                background = pygame.image.load("australiaBackground.png")
            #end if
            if event.type == pygame.MOUSEBUTTONDOWN and mouseX >= 395 and mouseX <= 395 + 20 and mouseY >= 550 and mouseY <= 550 + 20:
                run = True
                northAmerica = False
                southAmerica = False
                europe = False
                asia = False
                australia = False
                africa = False
                mapScreen = False
                antartica = True
                background = pygame.image.load("antarticaBackground.png")
            #end if
            pygame.display.update()
    #end while
    if (asia == True and asiaC == True) or (antartica == True and antarticaC == True) or (northAmerica == True and northamericaC == True) or (europe == True and europeC == True) or (australia == True and oceaniaC == True) or (africa == True and africaC == True) or (southAmerica == True and southamericaC == True):
        correctContinent = True
        numAntidote = numAntidote + 1
        print "YAS"
    else:
        correctContinent = False
        print "NOP"
    #end if

    #numContinent
    numContinent = numContinent + 1
    start = 0
    pygame.display.update()

    #on plane
    if (run == True and numContinent < 5) :
        pygame.mixer.music.load ("Intro Screen.mp3") 
        pygame.mixer.music.play(-1)
    while run == True and numContinent < 5:
        for frame in range (6):
            gameWindow.blit(background, (backgroundx,backgroundy))
            if correctContinent == True:
                gameWindow.blit (chest, (chestX,chestY))
            #end if

                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                #end if
            #end for
                    
            #arrow keys
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and playerX > 30:
                playerX -= WIDTH/(60)
            #end if
            if keys[pygame.K_RIGHT] and playerX <WIDTH - 160:
                playerX += WIDTH/(60)
            #end if
            if keys[pygame.K_UP] and playerY > 20:
                playerY -= HEIGHT/(60)
            #end if
            if keys [pygame.K_DOWN] and playerY < HEIGHT - 64-20:
                playerY += HEIGHT/(60)
            #end if
            player = plane[frame]
            
            if (playerX+10 > x2+10 -130 and playerX+20 < x2 + 90 and playerY+15 < y2+ 90 and playerY+15 > y2-30):
                newOne = True
                newOne2 = True
                newOne3 = True
                SCREAM.play()
                pygame.time.delay(2000)
                life = life +1
            else:
                newOne = False
            #end if
                
            #collision
            if (playerX+10 > x3+10 -130 and playerX+20 < x3 + 100 and playerY +15 < y3+ 90 and playerY+15 > y3-30):
                newOne = True
                newOne2 = True
                newOne3 = True
                SCREAM.play()
                pygame.time.delay(2000)
                life = life + 1
            else:
                newOne2 = False
            #end if
                #collision    
            if (playerX > x4 + 10 -130 and playerX+20 < x4 + 100 and playerY+15 < y4+ 90 and playerY+15 > y4-30):
                newOne = True
                newOne2 = True
                newOne3 = True
                SCREAM.play()
                pygame.time.delay(2000)
                life = life + 1
            else:
                newOne3 = False
            #end if
                
            if (x2 < 0  and left == False)or(x2 > WIDTH and left == True) :            
                newOne = True
            #end if


            if (x4 < 0  and left4 == False) or (x4 > WIDTH and left4 == True):            
                newOne3 = True
            #end if

            #obstacles
            if newOne == True:
                direction = randint (1,2)
                numVirus1 = virus[randint (0,4)]
                y2 = randint (0,HEIGHT-100)
                if direction == 1:
                    x2=0-100
                    left = True
                else:
                    x2 = WIDTH
                    left = False
                #end if
            #end if
            if newOne2 == True:
                y3 = -100
            #end if
            if newOne3 == True:
                y4 = randint (1,HEIGHT-100)
                direction = randint (1,2)
                numVirus3 = virus[randint (0,4)]
                if direction == 1:
                    x4=0-100
                    left4 = True
                else:
                    x4 = WIDTH
                    left4 = False
                #end if
            #end if
            if (y3 > HEIGHT):            
                x3 = randint (1,WIDTH)
                y3 = 0-300
                numVirus2 = virus[randint (0,4)]
            #end if
                
            #background moving
            if backgroundx > -1000:
                backgroundx -= 0.5*(WIDTH/400)
                chestX -= 0.5*(WIDTH/400)
                                        

            else:
                #treasure stuffs
                newOne = False
                newOne2 = False
                newOne3 = False
                mapScreen = True
                play = True
                if correctContinent == True:
                    if (playerX + 130 > chestX and playerX+10 < chestX + 88 and playerY + 55 > chestY and backgroundx <= -1000):
                        chest = openChest
                    #end if
                    if chest == openChest:
                        gameWindow.blit(antidotes[numAntidote-1],(chestX-30, chestY-70))
                        nextButton = True
                        if asia == True:
                            asiaC == False
                        elif (antartica == True):
                            antartica == False
                        elif (northAmerica == True):
                            northamericaC = False
                        elif southAmerica == True:
                            southamericaC = False
                        elif (europe == True):
                            europeC == False
                        elif (australia == True):
                            australiaC = False
                        elif (africa == True):
                            africaC = False
                        #end if
                        pygame.draw.rect (gameWindow,RED,(80-8,80-8,400,45),0)
                        graphics = fontThree.render("You found an antidote!", 0,BLACK)
                        gameWindow.blit(graphics,(80,80))
                        YAY.play()
                    #end if

                elif (correctContinent == False):
                    start = time.clock()
                    if start >3:
                        pygame.draw.rect (gameWindow,RED,(80-8,80-8,400,45),0)
                        graphics = fontThree.render("There is nothing here...", 0,BLACK)
                        gameWindow.blit(graphics,(80,80))
                        nextButton = True
                        SAD.play()
                    #end if
                #end if
                        
            #direction
            if left4 == False:
                x4-= WIDTH/(75)
            elif (left4 == True):
                x4+= WIDTH/(75)
            if left == False:
                x2-= WIDTH/(65)
            elif (left == True):
                x2+= WIDTH/(65)
            y3 += HEIGHT/(80)

            #chest
        
    
            
            #player and viruses
            if nextButton == False:
                gameWindow.blit (numVirus3, (x4,y4))
                gameWindow.blit(numVirus1,(x2,y2))
                gameWindow.blit(numVirus2,(x3,y3))
            #end if
                
            gameWindow.blit(player,(playerX,playerY))
            gameWindow.blit(heart,(playerX + 45, playerY + 27))
            graphics = fontFour.render(" = "+str(30-life),0,BLACK)
            gameWindow.blit(graphics, (playerX + 60, playerY + 27))
            pygame.display.update()
            pygame.time.delay(5)
            
        #NEXT    
        while nextButton == True:
            pygame.draw.rect(gameWindow, BROWN,(30, 500,180,80),0)
            graphics = fontFive.render("NEXT", 0,BLACK)
            gameWindow.blit(graphics,(40,495))
            for event in pygame.event.get(): #choosing an option
                mouse = pygame.mouse.get_pressed()
                (mouseX, mouseY) = pygame.mouse.get_pos()
            if mouseX >= 30 and mouseX<= 30+180 and mouseY <= 500+80 and mouseY >= 500 and nextButton == True:
                pygame.draw.rect(gameWindow, YELLOW,(30, 500,180,80),0)
                graphics = fontFive.render("NEXT", 0,BLACK)
                gameWindow.blit(graphics,(40,495))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    run = False
                    print "YO"
                    nextButton = False
                #end if
            #end if
        #end for
            pygame.display.update()
        #end while
            
        pygame.display.update()
        pygame.time.delay(5)
        
        #DEATH
        if life > 30:
            pygame.mixer.music.stop()
            for i in range (5):
                pygame.display.set_mode((800,600),pygame.FULLSCREEN)
                gameWindow.blit(end[i],(0,0))
                if i == 4:
                    DEATH.play()
                pygame.display.update()
                pygame.time.delay(4000)
            #end for
            run = False
            gameWindow.fill (BLACK)
            graphics = fontOne.render("THE END", 0,YELLOW)
            gameWindow.blit(graphics,(300,200))
            creditScreen = True
            pygame.display.update()
            pygame.time.delay(3000)
            menu = True
        #end if
    #end while
        
    #on foot

    while run2 == True:
        for frame in range (6):
            
            #background
            gameWindow.blit (background, (backgroundx, backgroundy))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run2 = False
                #end if
            #end for
        #end for
    

            #chest
            if correctContinent == True:
                gameWindow.blit(closedChest, (chestX,chestY))
            

            #collision 
            if (playerX-5 >= x2-50 and playerX-5 < x2+90 and playerY-5 > y2 -50 and playerY-5 < y2 + 90):
                life = life + 1
                SCREAM.play()
                pygame.time.delay(2000)
                newOne = True
                newOne2 = True
                newOne3 = True
                jump = False
                jumpHeight = 9
                playerY= HEIGHT*3/4
            #end if
                

            if  (playerX-5 >= x3+10 -50 and playerX-5 < x3+90 and playerY > y3 -50 and playerY < y3 + 90):
                life = life + 1
                SCREAM.play()
                newOne = True
                newOne2 = True
                jump = False
                jumpHeight = 9
                playerY= HEIGHT*3/4
                pygame.time.delay(2000)
            #end if
                
            if x2 < 0 and left == False:
                newOne = True
            #end if
                
            if (x2 > WIDTH and left == True):
                newOne = True
            #end if

            #newOne loop
            if newOne == True:
                direction = randint (1,2)
                numVirus1 = virus[randint(0,4)]
                if direction == 1:
                    x2=-200
                    left = True
                else:
                    x2 = WIDTH+100
                    left = False
                newOne = False
            #end if
                
            if newOne2 == True or (y3>HEIGHT):
                x3 = randint (1, WIDTH-90)
                y3 = -200
                numVirus2 = virus[randint(0,4)]
                newOne2 = False
            #end if

            #running animation
            if frame <=2:            
                player = playerRun
            elif (frame<=4):
                player = playerSide
            else:
                player = playerRun2


            #moving background     
            if backgroundx > -1000 and life <31:
                backgroundx -= 0.5*(WIDTH/300)
                chestX -= 0.5*(WIDTH/380)


            else:
                if correctContinent == True:
                    if (playerX + 50 > chestX and playerX+10 < chestX + 88 and playerY + 45 > chestY and backgroundx <= -1000):
                        chest = openChest
                        run = False
                    #end if
                    if chest == openChest:
                        gameWindow.blit(antidotes[numAntidote-1],(chestX-30, chestY-70))
                        nextButton = True
                        if asia == True:
                            asiaC == False
                        elif (antartica == True):
                            antartica == False
                        elif (northAmerica == True):
                            northamericaC = False
                        elif southAmerica == True:
                            southamericaC = False
                        elif (europe == True):
                            europeC == False
                        elif (australia == True):
                            australiaC = False
                        elif (africa == True):
                            africaC = False
                        #end if
                        pygame.draw.rect (gameWindow,RED,(80-8,80-8,400,45),0)
                        graphics = fontThree.render("You found an antidote!", 0,BLACK)
                        gameWindow.blit(graphics,(80,80))
                        YAY.play()
                    #end if
                #end if

                #theres nothing here...
                elif (correctContinent == False):
                    start = time.clock()
                    if start >3:
                        pygame.draw.rect (gameWindow,RED,(80-8,80-8,400,45),0)
                        graphics = fontThree.render("There is nothing here...", 0,BLACK)
                        gameWindow.blit(graphics,(80,80))
                        nextButton = True
                        SAD.play()
                    #end if
                #end if

                    
                

            #movement of viruses
            y3 += HEIGHT/50
            if left == False:
                x2-= WIDTH/(55)
            elif (left == True):
                x2+= WIDTH/(55)

            #player and obstacles
            if frame <2:            
                player = playerRun
            elif (frame<=4):
                player = playerSide
            else:
                player = playerRun2

            gameWindow.blit(player,(playerX,playerY))
            gameWindow.blit(numVirus1,(x2,y2))
            gameWindow.blit(numVirus2,(x3,y3))
            graphics = fontSix.render("Lives left: "+str(30-life),0,YELLOW)
            gameWindow.blit(graphics, (400-2, 100-2))
            graphics = fontOne.render("Lives left: "+str(30-life),0,BLACK)
            gameWindow.blit(graphics, (400, 100))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and playerX >5:
                playerX -= 20        
            elif( keys[pygame.K_RIGHT] and playerX <WIDTH-60):
                playerX += 20
                
            #jump
            if jump == True:
                if jumpHeight > -10:
                    fall = 1
                    if jumpHeight < 0:
                        fall = -1
                    playerY -= (jumpHeight**2) * 0.5 * fall * (HEIGHT/500)
                    jumpHeight -= 1
                else:
                    jump = False
                    jumpHeight = 9
            else:
                if keys[pygame.K_UP] and jump == False:
                    jump = True
                #end if
                
            pygame.display.update()
            pygame.time.delay(2)
            
        while nextButton == True:
            pygame.draw.rect(gameWindow, BROWN,(30, 500,180,80),0)
            graphics = fontFive.render("NEXT", 0,BLACK)
            gameWindow.blit(graphics,(40,495))
            for event in pygame.event.get(): #choosing an option
                mouse = pygame.mouse.get_pressed()
                (mouseX, mouseY) = pygame.mouse.get_pos()
            if mouseX >= 30 and mouseX<= 30+180 and mouseY <= 500+80 and mouseY >= 500 and nextButton == True:
                pygame.draw.rect(gameWindow, YELLOW,(30, 500,180,80),0)
                graphics = fontFive.render("NEXT", 0,BLACK)
                gameWindow.blit(graphics,(40,495))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    run2 = False
                    print "YO"
                    nextButton = False
                    
                #end if
            pygame.display.update()

            #end if
        #end for
        pygame.display.update()
    #end while
            
        #DEATH
        if life > 30:
            pygame.mixer.music.stop()
            for i in range (5):
                pygame.display.set_mode((800,600),pygame.FULLSCREEN)
                gameWindow.blit(end[i],(0,0))
                if i == 4:
                    DEATH.play()
                pygame.display.update()
                pygame.time.delay(4000)
            #end for
            run2 = False
            menu = True
            gameWindow.fill (BLACK)
            graphics = fontOne.render("THE END", 0,YELLOW)
            gameWindow.blit(graphics,(300,200))
            creditScreen = True
            pygame.display.update()
            pygame.time.delay(3000)
        #end if

    #after 4 continents        
    if numContinent == 4 and numAntidote < 4 and life <31:
        pygame.mixer.music.load ("Defense Line.mp3") 
        pygame.mixer.music.play(-1)
        gameWindow.blit (pygame.transform.scale(background, (3600,1200)), (-800,-600) )
        gameWindow.blit(playerplane, (0,0))
        pygame.draw.rect (gameWindow, RED,(45, 95,730,30),0)
        graphics = fontTwo.render("Your plane is out of fuel, but you haven't found all the antidotes.", 0,BLACK)
        gameWindow.blit(graphics, (50, 100))
        pygame.draw.rect (gameWindow, RED,(45, 195,700,30),0)
        graphics = fontTwo.render("Your only option is to travel on foot instead.", 0,BLACK)
        gameWindow.blit(graphics, (50, 200))
        pygame.display.update()
        pygame.time.delay(4000)
        pygame.draw.rect (gameWindow, RED,(45, 295,700,30),0)
        graphics = fontTwo.render("But time is running out. You only have time to travel to one", 0,BLACK)
        gameWindow.blit(graphics, (50, 300))
        pygame.draw.rect (gameWindow, RED,(45, 345,500,30),0)
        graphics = fontTwo.render("more continent before all the infected die.", 0,BLACK)
        gameWindow.blit(graphics, (50, 350))
        pygame.display.update()
        pygame.time.delay(4000)
        run2 = True
        run = False
        mapScreen = True
        chestY = 420
        pygame.display.update()
    #end if

    #not enough antidotes
    elif (numContinent == 5 and numAntidote !=4 and life <31):
        pygame.mixer.music.load ("Lounge Game1.wav") 
        pygame.mixer.music.play(-1)
        gameWindow.blit (pygame.transform.scale(background, (4800,1800)), (-1600,-1200) )
        gameWindow.blit(thang, (0,0))
        pygame.draw.rect (gameWindow, RED,(400, 100,370,50),0)
        pygame.draw.rect (gameWindow, RED,(400, 200,370,50),0)
        graphics = fontThree.render("You were only able to find " , 0,BLACK)
        gameWindow.blit(graphics, (400+5, 100+5))
        graphics = fontThree.render(str(numAntidote) + " out of the 4 antidotes..." , 0,BLACK)
        gameWindow.blit(graphics, (400+5, 200+5))
        for i in range (numAntidote):
            gameWindow.blit (pygame.transform.scale(antidotes[i], (900,900)), (i*135 -133,42) )
            pygame.display.update()
        #end if
        pygame.time.delay(4000)
        gameWindow.fill (BLACK)
        graphics = fontOne.render("Now there is no cure.", 0,YELLOW)
        gameWindow.blit(graphics,(300,200))
        pygame.time.delay(2000)
        graphics = fontOne.render("THE END", 0,YELLOW)
        gameWindow.blit(graphics,(300,200))
        menu = True
        creditScreen = True
        pygame.display.update()
        pygame.time.delay(3000)
    #end if

    #win
    elif (numAntidote == 4 and life <31):
        pygame.mixer.music.load ("Lounge Game1.wav") 
        pygame.mixer.music.play(-1)
        menu = True

        victoryScreen = True

        #Picture of winning screen 
        win = pygame.image.load("win1.png")
        gameWindow.blit(win, (0,0))

        #---------------------------------------------------------
        #---------------------------------------------------------
        #Font for winning screen 
        font1 = pygame.font.SysFont ("Courier New Bold", 70)
        graphics = font1.render("Victory!", 0, WHITE)
        gameWindow.blit(graphics, (190, 85))

        #-----------------------------------------------------------

        font2 = pygame.font.SysFont ("Courier New Bold", 30)
        graphics = font2.render("You have successfully", 0, WHITE)
        gameWindow.blit(graphics, (170, 370))

        #----------------------------------------------------------

        font3 = pygame.font.SysFont ("Courier New Bold", 30)
        graphics = font3.render("attained all four antidotes", 0, WHITE)
        gameWindow.blit(graphics, (150, 390))

        #----------------------------------------------------------

        font4 = pygame.font.SysFont ("Courier New Bold", 30)
        graphics = font4.render("and saved humanity!", 0, WHITE)
        gameWindow.blit(graphics, (170, 410))

        #-----------------------------------------------------------
        #-----------------------------------------------------------

        #Exit button shape
        pygame.draw.rect (gameWindow, LIGHTGREEN, (170, 440, 218, 30), 0)

        #sound
        YAY.play()

        #Font for exit button 
        font5 = pygame.font.SysFont ("Courier New Bold", 50)
        graphics = font5.render ("Exit", 0, WHITE)
        gameWindow.blit(graphics, (240, 440))
        pygame.display.update()
        pygame.time.delay(1000)

        #Mouse movement to go back to the menu
        while victoryScreen == True:
            for event in pygame.event.get():
                mouse = pygame.mouse.get_pressed()
                (mouseX, mouseY) = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN and mouseX >= 170 and mouseX <= 170 + 218 and mouseY >= 440 and mouseY <= 440 + 30:
                    gameWindow.fill (BLACK)
                    graphics = fontOne.render("THE END", 0,YELLOW)
                    gameWindow.blit(graphics,(300,200))            
                    pygame.display.update()
                    pygame.time.delay(3000)
                    exit = True
                    victoryScreen = False
                    creditScreen = True
                #end if
                pygame.display.update()
            pygame.display.update()
        #end while
        pygame.display.update()
    #end if

    if creditScreen == True:
        gameWindow = pygame.display.set_mode((WIDTH, 620))
        gameWindow.blit (menuBackground, (0,0))


        #----------------------------------------------------------------
        #Animation Credits
        font1 = pygame.font.SysFont ("Courier New Bold", 40)
        graphics = font1.render ("Animation Credits", 0, YELLOW)
        gameWindow.blit (graphics, (270, 0))

        font2 = pygame.font.SysFont ("Courier New Bold", 30)
        graphics = font2.render ("Melody and Christine", 0, WHITE)
        gameWindow.blit (graphics, (290, 30))

        #----------------------------------------------------------------
        #Picture Credits
        font3 = pygame.font.SysFont ("Courier New Bold", 40)
        graphics = font2.render ("Picture Credits", 0, YELLOW)
        gameWindow.blit (graphics, (300, 60))

        font4 = pygame.font.SysFont ("Courier New Bold", 30)
        graphics = font4.render ("https://www.google.com/search?rlz=1C1GGRV_enCA822CA822&biw=", 0, WHITE)
        gameWindow.blit (graphics, (0, 80))

        font5 = pygame.font.SysFont ("Courier New Bold", 30)
        graphics = font5.render("1920&bih=949&tbm=isch&sa=1&ei=4A4QXLD3I6XRjwTY-KiICA&q=sprite", 0, WHITE)
        gameWindow.blit (graphics, (0, 110))

        font6 = pygame.font.SysFont ("Courier New Bold", 30)
        graphics = font6.render("+characters&oq=sprite+characters&gs_l=img.3..0j0i5i30l3j0i8i10", 0, WHITE)
        gameWindow.blit (graphics, (0, 130))

        font7 = pygame.font.SysFont ("Courier New Bold", 30)
        graphics = font7.render("i30j0i8i30j0i24.4187.8671..8808...6.0..0.98.1511.23......1....1", 0, WHITE)
        gameWindow.blit (graphics, (0, 150))

        font8 = pygame.font.SysFont ("Courier New Bold", 30)
        graphics = font8.render("..gws-wiz-img.......0i67j0i10j0i10i67j0i5i10i30j0i10i24.Png_09q", 0, WHITE)
        gameWindow.blit (graphics, (0, 170))

        font9 = pygame.font.SysFont ("Courier New Bold", 30)
        graphics = font9.render("WTNg&safe=active&ssui=on#imgrc=zWZOb39RzHYxLM:", 0, WHITE)
        gameWindow.blit (graphics, (0, 190))

        font10 = pygame.font.SysFont ("Courier New Bold", 30)
        graphics = font10.render ("http://oil-rig-explosions.com/wp-content/uploads/2018/0", 0, WHITE)
        gameWindow.blit (graphics, (0, 210))

        font11 = pygame.font.SysFont ("Courier New Bold", 30)
        graphics = font11.render ("9/wallpaper-map-of-the-world-contemporary-design-glowing-", 0, WHITE)
        gameWindow.blit (graphics, (0, 230))
                                 
        font12 = pygame.font.SysFont ("Courier New Bold", 30)
        graphics = font12.render ("world-map-wallpaper-digital-art-wallpapers-322.jpg", 0, WHITE)
        gameWindow.blit (graphics, (0, 250))

        font13 = pygame.font.SysFont ("Courier New Bold", 30)                        
        graphics = font13.render ("https://www.google.com/search?q=pinpoint&rlz=1C1GGRV", 0, WHITE)
        gameWindow.blit (graphics, (0, 270))
                                 
        font14 = pygame.font.SysFont ("Courier New Bold", 30)                        
        graphics = font14.render("enCA831CA831&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiGg7nq", 0, WHITE)
        gameWindow.blit (graphics, (0, 290))
                                
        font15 = pygame.font.SysFont ("Courier New Bold", 30)                        
        graphics = font15.render ("h_PfAhXwj4MKHS-MCQMQ_AUIDigB&biw=1920&bih=949&safe=active", 0, WHITE)
        gameWindow.blit (graphics, (0, 310))
                                 
        font16 = pygame.font.SysFont ("Courier New Bold", 30)                        
        graphics = font16.render ("&ssui=on#imgrc=ApnYlm51UvHniM:", 0, WHITE)
        gameWindow.blit (graphics, (0, 330))

        font17 = pygame.font.SysFont ("Courier New Bold", 30)
        graphics = font17.render ("http://pngimg.com/download/43353", 0, WHITE)
        gameWindow.blit (graphics, (0, 350))

        font18 = pygame.font.SysFont ("Courier New Bold", 30)
        graphics = font18.render ("https://stickeroid.com/uploads/pic/fx0n217l-full/67b4bc67bcaa0f3cc2cec2d4e8b0146c88a8b754.png", 0, WHITE)
        gameWindow.blit (graphics, (0, 370))

        font19 = pygame.font.SysFont ("Courier New Bold", 30)
        graphics = font19.render ("https://imgkid.com/cold-virus-cells.shtml", 0, WHITE)
        gameWindow.blit (graphics, (0, 390))
                                 
                                 
        #-----------------------------------------------------------------
        #Sound Credits
        font20 = pygame.font.SysFont ("Courier New Bold", 40)
        graphics = font20.render ("Sound Credits", 0, YELLOW)
        gameWindow.blit (graphics, (270, 420))

        font21 = pygame.font.SysFont ("Courier New Bold", 30)
        graphics = font21.render ("http://www.orangefreesounds.com/wilhelm-scream/", 0, WHITE)
        gameWindow.blit (graphics, (0, 450))


        font21 = pygame.font.SysFont ("Courier New Bold", 30)
        graphics = font21.render ("http://www.orangefreesounds.com/wilhelm-scream/", 0, WHITE)
        gameWindow.blit (graphics, (0, 470))

        font21 = pygame.font.SysFont ("Courier New Bold", 30)
        graphics = font21.render ("https://www.myinstants.com/instant/sad-trombone/", 0, WHITE)
        gameWindow.blit (graphics, (0, 490))
        pygame.display.update()
        pygame.time.delay(1000)

        font21 = pygame.font.SysFont ("Courier New Bold", 30)
        graphics = font21.render ("http://soundbible.com/2103-1-Person-Cheering.html", 0, WHITE)
        gameWindow.blit (graphics, (0, 510))

        font21 = pygame.font.SysFont ("Courier New Bold", 30)
        graphics = font21.render ("http://www.orangefreesounds.com/dun-dun-dun-sound-effect-brass/", 0, WHITE)
        gameWindow.blit (graphics, (0, 530))

        graphics = font21.render ("https://www.dl-sounds.com/royalty-free/defense-line/", 0, WHITE)
        gameWindow.blit (graphics, (0, 550))

        graphics = font21.render ("https://www.dl-sounds.com/royalty-free/intro-screen/", 0, WHITE)
        gameWindow.blit (graphics, (0, 570))

        graphics = font21.render ("https://www.dl-sounds.com/royalty-free/lounge-game1/", 0, WHITE)
        gameWindow.blit (graphics, (0, 590))
        
        creditScreen = False
        pygame.display.update()
        pygame.time.delay(10000)
    #end if
                
    #new game
    if menu == True:
        numAntidote = 0
        menuDisplay = True
        life = 0
        mapScreen = False
        play = False
        asiaC = 1
        antarticaC = 2
        northamericaC = 3
        europeC = 4
        oceaniaC = 5
        africaC = 6
        southamericaC = 7
        numContinent = 0
        chosencontinents = [asiaC,antarticaC,northamericaC,europeC,oceaniaC,africaC, southamericaC]
        pygame.mixer.music.load ("Lounge Game1.wav") 
        pygame.mixer.music.play(-1)         
        
    #end if
    pygame.display.update()

                    
    #new level
    backgroundx = 0
    pygame.time.delay(2000)
    playerX = 300
    playerY= HEIGHT*3/4
    newOne = True
    newOne2 = True
    newOne3 = True
    y2 = HEIGHT*3/4 - 40
    WIDTH = 800
    HEIGHT = 600
    left = False
    chest = closedChest
    chestX = 1700
    nextButton = False
    gameWindow = pygame.display.set_mode ((WIDTH,HEIGHT))                
    pygame.display.update()
#end while

pygame.display.update()


    
pygame.quit()


