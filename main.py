# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame #importing pygame
from constants import * #importing the constent so you get it too

pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return  #it says this is out of function but it isn't
    pygame.display.fill(000000)    
    pygame.display.flip()
print ("Starting Asteroids!")
print (f"Screen width: {SCREEN_WIDTH}")
print (f"Screen height: {SCREEN_HEIGHT}")
if __name__ == "__name__":
    main()