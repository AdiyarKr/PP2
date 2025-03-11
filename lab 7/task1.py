import pygame, time
import sys 

pygame.init()
size = (800, 600)
screen = pygame.display.set_mode((size))
pygame.display.set_caption('mickey mouse clock')

back = pygame.image.load('/Users/adiyarkarim/Downloads/back.jpg')
minutes = pygame.image.load('/Users/adiyarkarim/Downloads/minutes.png')
seconds = pygame.image.load('/Users/adiyarkarim/Downloads/seconds.png')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(back ,(0, 0))
    now = time.localtime()
    
    min_angle = 360 - (now.tm_min*6)
    min_rot = pygame.transform.rotate(minutes, min_angle)
    min_pos = ((size[0]-min_rot.get_width())/2, (size[1]-min_rot.get_width())/2) 
    screen.blit(min_rot, min_pos)
     
    sec_angl = 360 - (now.tm_sec*6)
    sec_rot = pygame.transform.rotate(seconds, sec_angl)
    sec_pos = ((size[0]-sec_rot.get_width())/2, (size[1]-sec_rot.get_width())/2)
    screen.blit(sec_rot, sec_pos)

    

    
    pygame.display.flip()

pygame.quit()
sys.exit()