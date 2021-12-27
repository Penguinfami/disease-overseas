from random import randint
import pygame
pygame.init()
WIDTH = 800
HEIGHT = 600

#------------Colours------------------------
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0,0,0)
CYAN = (0, 255,255)
BROWN = (168, 42,42)
GRAY = (190,190,190)
LIGHTGREEN = (144,238,144)
LIGHTGRAY = (169,169,169)

#-------------------------------------------

screenWidth = 800


gameWindow = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption(("TESTING GAME"))

font1 = pygame.font.SysFont("Courier New Bold", WIDTH*HEIGHT/10000)

end1 = pygame.image.load("end1.png")
end2 = pygame.image.load("end2.png")
end3 = pygame.image.load ("end3.png")
end4 = pygame.image.load ("end4.png")
end5 = pygame.image.load ("end5.png")
end = [end1,end2,end3,end4,end5]
pygame.mixer.music.load ("DUN DUN DUN.wav")
#-----------------------------------------------------

COLOUR = [RED, GREEN, BLUE, BLACK, BROWN, GRAY, LIGHTGREEN, LIGHTGRAY]
menu = True

pygame.display.update()
#-------Main Movement--------------------------------
for i in range (5):
    pygame.display.set_mode((800,600),pygame.FULLSCREEN)

    gameWindow.blit(end[i],(0,0))
    if i == 4:
        pygame.mixer.music.play()
    pygame.display.update()
    pygame.time.delay(4000)
#-----------------------------------------------------
pygame.display.update()
pygame.time.delay(3000)
pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.update()


#-----------------------------------------------------

#player 2

#-------Main Movement--------------------------------


    
pygame.quit()
