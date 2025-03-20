import pygame 
import sys
import random, time  
from pygame.locals import *
#from pygame.sprite import Group #позволяет нам использовать функции и переменные в модуле pygame.locals

pygame.init()
FPS = pygame.time.Clock()

is_playing, lose = True, False

# Түстер
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#текст жазуға шрифт 
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

game_over1 = font.render("Game Over", True, BLACK)

#background = pygame.image.load("AnimatedStreet.png")#жолды қосу 


dw = 400
dh = 600
SPEED=5
SCORE = 0
coin_score = 0

way_s = 70 #жолдың жылжу тездігі (макс координата dy) (speed of changing traffic)
dy = 0#жолды жылжытқандағы өзгеріп отыратын y координата 
ch_s = 2#dy өзгеру тездігі 

screen = pygame.display.set_mode((dw,dh))

pygame.display.set_caption('Racer')
game_over = pygame.image.load('/Users/adiyarkarim/Downloads/gameover.jpg')
game_over = pygame.transform.scale(game_over, (dw, dh))
backg = pygame.image.load('/Users/adiyarkarim/Downloads/AnimatedStreet.png')



class Player(pygame.sprite.Sprite):#плейер деген спрайттың саб класы 
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('/Users/adiyarkarim/Downloads/Player.png')
        self.rect=self.image.get_rect()
        self.rect.center=(160, 520)
    def move(self):
        pressed_keys=pygame.key.get_pressed()
        
        '''if pressed_keys[K_UP]:
            self.rect.move_ip(0,-5)#бұл суретті қозғалтады екі мән қабылдайды x y бойынша координаттар
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)'''

        if self.rect.left>0:#игрок не сможет покинуть экран.
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < dw:#игрок не сможет покинуть экран.       
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
    def draw(self, surface):#отвечает за отображение изображения игрока на указанной поверхности 
        surface.blit(self.image, self.rect) 

class  Enemy(pygame.sprite.Sprite):#спрайттың саб класы 
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('/Users/adiyarkarim/Downloads/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,dw-40), 0)#рандомизированные начальные точки(0-чтобы объект появлялся вверху экрана)
    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)#перемещая объект Enemy вниз на speed пикселей
        if (self.rect.top>600):#top Получение верхней границы прямоугольника y 
            SCORE += 1#әр машинанның жанынан өткен сайын скор ға +1
            self.rect.top=0#if y=0 -> again 
            self.rect.center = (random.randint(40, dw - 40), 0)
    def draw(self, surface):#отвечает за отображение изображения игрока на указанной поверхности 
        surface.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('/Users/adiyarkarim/Downloads/coin.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, dw - 30), random.randint(30, dh - 130))
    
    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > dh:
            self.rect.top = 0
            self.rect.center = (random.randint(30, dw - 30), 0)
    
    def draw(self):#отвечает за отображение изображения coin на указанной поверхности 
        screen.blit(self.image, self.rect)

P1 = Player()
E1 = Enemy()
C = Coin()

#Creating Sprites Groups
enemies = pygame.sprite.Group()#Создает группу спрайтов для врагов
enemies.add(E1)
all_sprites = pygame.sprite.Group()#Создает группу спрайтов для всех объектов в игре, включая игрока и врагов.
all_sprites.add(P1)
all_sprites.add(E1)

coins = pygame.sprite.Group()
coins.add(C)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
'''Это пользовательское событие используется для изменения скорости движения врагов в игре. 
Каждый раз, когда событие INC_SPEED срабатывает (каждую секунду), скорость движения врагов увеличивается на 2 единицы. '''
 

while is_playing:
    FPS.tick(60)
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
            
    #анимациялы жол
    screen.blit(pygame.transform.scale(backg, (dw, dh)), (0, dy))
    screen.blit(pygame.transform.scale(backg, (dw, dh)), (0, dy - dh))
    dy = (dy + ch_s) % dh

    '''операция % dh гарантирует, что dy остается в пределах от 
    0 до dh, что позволяет фону двигаться бесконечно вверх'''

    '''P1.move()
    E1.move()'''
    #screen.fill(WHITE)#әр машинанын артын тазалап отыру қажет ақ қылып 
    '''P1.draw(screen)
    E1.draw(screen)'''

    scores = font_small.render(str(SCORE), True, BLACK)
    screen.blit(scores, (10,10))

    for entity in all_sprites:#группадағы объектің бәрін экранға шығарамыз
        screen.blit(entity.image, entity.rect)
        entity.move()
    
    for coin in coins:
        coin.move()  # койнның қозғалуына жауап береді 
        coin.draw()  # әр койнды салады 
        if pygame.sprite.collide_rect(P1, coin):#ешер койн мен плэйер соғылса
            coin.kill()#койнды жояды
            coin_score += 1
            new_coin = Coin()#жаңа койн қосады 
            coins.add(new_coin)


    #егер плэйер эмемимен соғысса
    if pygame.sprite.spritecollideany(P1, enemies):#бұл жол машиналар соғылды ма соны анықтайды,егер соғылса тру, spritecollideany(обычным спрайт, группой спрайтов)
        lose = True

    #энеми соғысқанда дыбыс шығу үшін
    if lose:
          pygame.mixer.Sound('crash.wav').play()
          #time.sleep(0.5)

    #game_over
    while lose:
        FPS.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        time.sleep(2)
        screen.fill(RED)#егер соғылса қызыл болады экран 
        screen.blit(game_over1, (30,250))
        pygame.display.flip()

   
    
    final_score_text = font_small.render(f'Coins:{coin_score}', True, 'black')#используется для отображения текста на поверхности
    screen.blit(final_score_text, (300, 10))

    pygame.display.flip()
pygame.quit()   