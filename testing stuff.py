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
fontThree = pygame.font.SysFont("Comic Sans MS", 30)
fontFour = pygame.font.SysFont("Courier New Bold", 30)
fontFive = pygame.font.SysFont("Arial", 75)


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
northamerica = False
europe = False
australia = False
africa = False
southamerica = False
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
numAntidote = -1

#menu and death screen 
menuScreen = pygame.image.load ("menu.png")
end1 = pygame.image.load("end1.png")
end2 = pygame.image.load("end2.png")
end3 = pygame.image.load ("end3.png")
end4 = pygame.image.load ("end4.png")
end5 = pygame.image.load ("end5.png")
end = [end1,end2,end3,end4,end5]

#sound effects
DEATH = pygame.mixer.Sound ("DUN DUN DUN.wav")
DEATH.set_volume(1)
YAY = pygame.mixer.Sound("YAY.wav")
YAY.set_volume(1)
SAD = pygame.mixer.Sound ("sadtrombone.mp3")
SAD.set_volume(0.9)
SCREAM = pygame.mixer.Sound ('scream.mp3')
SCREAM.set_volume(1)
#map
mapPic = pygame.image.load("map.png")
pinpoint = pygame.image.load("pinpoint.png")

#gameplay variables
life = 0
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
background = pygame.image.load("africaBackground.png")

thang = pygame.image.load ("thang.png")

gameWindow.blit (pygame.transform.scale(background, (4800,1800)), (-1600,-1200) )

numAntidote = 3
#menu
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
#end loop



pygame.display.update()
pygame.time.delay(10000)





#-----------------------------------------------------

#player 2

#-------Main Movement--------------------------------


    
pygame.quit()


