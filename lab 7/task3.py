import pygame
import sys

pygame.init()
window_width = 400
window_height = 300
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Red ball')
clock = pygame.time.Clock()

x = 47    
y = 47
r = 25
speed = 20
while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                      pygame.quit()
                      sys.exit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT] and x-r-speed>=0: 
                              x = x-speed
                elif keys[pygame.K_RIGHT] and x+r+speed<=window_width: 
                              x = x+speed
                if keys[pygame.K_UP] and y-r-speed>=0: 
                              y = y-speed
                elif keys[pygame.K_DOWN] and y+r+speed<=window_height: 
                              y = y+speed

        window.fill((255, 255, 255)) 

        pygame.draw.circle(window, 'red', (x, y), r)
        
        pygame.display.flip()
        clock.tick(120)
    

pygame.quit()