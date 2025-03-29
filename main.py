# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame #importing pygame
from constants import * #importing the constent so you get it too

def main():
    pygame.init()

    
    clock = pygame.time.Clock()
    timer = 60


    dt = 0
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  
        screen.fill("black")    
        pygame.display.flip()
        dt = (clock.tick(timer))/1000
        

        
        
print ("Starting Asteroids!")
print (f"Screen width: {SCREEN_WIDTH}")
print (f"Screen height: {SCREEN_HEIGHT}")
if __name__ == "__main__":
    main()