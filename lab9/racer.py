import pygame 
import sys
import random, time  
#from pygame.locals import *
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
SPEED=7# player speed 
USER_SPEED=5# enemy spped 
SCORE = 0
coin_score, money_score = 0, 0
pev_money_score=0

pause, end = False, False


way_s = 70 #жолдың жылжу тездігі (макс координата dy) (speed of changing traffic)
dy = 0#жолды жылжытқандағы өзгеріп отыратын y координата 
ch_s = 2#dy өзгеру тездігі 

screen = pygame.display.set_mode((dw,dh))
screen.fill(GREEN)
name = font.render("Street racer", True, BLACK)
screen.blit(name, (15, 150))
game = pygame.display.set_caption('Racer')
#game_over = pygame.image.load('gameover.jpg')
#game_over = pygame.transform.scale(game_over, (dw, dh))
backg = pygame.image.load('/Users/adiyarkarim/Downloads/AnimatedStreet (1).png')





class Player(pygame.sprite.Sprite):#плейер деген спрайттың саб класы 
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('/Users/adiyarkarim/Downloads/Player (1).png')
        self.rect=self.image.get_rect()
        self.rect.center=(160, 520)
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > USER_SPEED:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-USER_SPEED, 0)
        if self.rect.right < dw - USER_SPEED:        
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(USER_SPEED, 0)
        '''if self.rect.top > USER_SPEED:
            if pressed_keys[pygame.K_w]:
                self.rect.move_ip(0, -USER_SPEED)
        if self.rect.bottom < dh - USER_SPEED:        
            if pressed_keys[pygame.K_s]:
                self.rect.move_ip(0, USER_SPEED)'''

    def draw(self):#отвечает за отображение изображения игрока на указанной поверхности 
        screen.blit(self.image, self.rect) 

class  Enemy(pygame.sprite.Sprite):#спрайттың саб класы 
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/adiyarkarim/Downloads/Enemy (1).png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,dw-40), 0)#рандомизированные начальные точки(0-чтобы объект появлялся вверху экрана)
    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)#перемещая объект Enemy вниз на speed пикселей
        if (self.rect.top>600):#top Получение верхней границы прямоугольника y 
            #SCORE += 1#әр машинанның жанынан өткен сайын скор ға +1
            self.rect.top=0#if y=0 -> again 
            self.rect.center = (random.randint(40, dw - 40), 0)
    def draw(self):#отвечает за отображение изображения игрока на указанной поверхности 
        screen.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('/Users/adiyarkarim/Downloads/coin (1).png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(15, 385), -50)
    
    def change_location(self):
        self.rect.center = (random.randint(15, 385), -50)
    
    def move(self):
        self.rect.move_ip(0, USER_SPEED)
        if self.rect.top > 600: self.change_location()
    
    def draw(self):#отвечает за отображение изображения coin на указанной поверхности 
        screen.blit(self.image, self.rect)

class Rubin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('/Users/adiyarkarim/Downloads/rubin.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.change_location()
    
    def change_location(self):
        self.rect.center = (random.randint(15, 385), -3000)#-3000 себебі алыстан келеді сосын сирек шығатын сияқты көрінеді 
    
    def move(self):
        self.rect.move_ip(0, USER_SPEED)
        if self.rect.top > 600: self.change_location()
    
    def draw(self):#отвечает за отображение изображения coin на указанной поверхности 
        screen.blit(self.image, self.rect)



P1 = Player()#создание экземпляра класса
E1 = Enemy()
C = Coin()
R1 = Rubin()


#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C)
all_sprites.add(R1)

money = pygame.sprite.Group()
money.add(C)
money.add(R1)



#Adding a new User event 
#INC_SPEED = pygame.USEREVENT + 1
#pygame.time.set_timer(INC_SPEED, 1000)
'''Это пользовательское событие используется для изменения скорости движения врагов в игре. 
Каждый раз, когда событие INC_SPEED срабатывает (каждую секунду), скорость движения врагов увеличивается на 2 единицы. '''
 

while is_playing:
    FPS.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT or  (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            if pause:
                pause = False
            else:
                pause = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            for entity in all_sprites:
                entity.__init__()#барлық группадан шақрыпады иниитті 
            coin_score, money_score = 0, 0
            SPEED, USER_SPEED = 8, 5
            pause, end = False, False
            dy = 0


    if end or pause:
        pass
    
    else:    
        #анимациялы жол
        screen.blit(pygame.transform.scale(backg, (dw, dh)), (0, dy))
        screen.blit(pygame.transform.scale(backg, (dw, dh)), (0, dy - dh))
        dy = (dy + ch_s) % dh

        '''операция % dh гарантирует, что dy остается в пределах от 
        0 до dh, что позволяет фону двигаться бесконечно вверх'''

        scores = font_small.render(str(coin_score), True, BLACK)
        money_scores = font_small.render(str(money_score), True, BLACK)
        current_speed = font_small.render("Your speed: " + str(USER_SPEED), True, BLACK)
        enemy_speed = font_small.render("Enemy speed: " + str(SPEED), True, BLACK)

        screen.blit(scores, (10, 10))
        screen.blit(money_scores, (365, 10))
        screen.blit(current_speed, (10, 50))
        screen.blit(enemy_speed, (10, 90))

        '''P1.move()
        E1.move()'''
        #screen.fill(WHITE)#әр машинанын артын тазалап отыру қажет ақ қылып 
        '''P1.draw(screen)
        E1.draw(screen)'''

        '''scores = font_small.render(str(SCORE), True, BLACK)
        screen.blit(scores, (10,10))'''

        for entity in all_sprites:
                entity.move()
                entity.draw()



        '''for entity in all_sprites:#группадағы объектің бәрін экранға шығарамыз
            screen.blit(entity.image, entity.rect)
            entity.move()
        
        for coin in coins:
            coin.move()  # койнның қозғалуына жауап береді 
            coin.draw()  # әр койнды салады 
            if pygame.sprite.collide_rect(P1, coin):#ешер койн мен плэйер соғылса
                coin.kill()#койнды жояды
                coin_score += 1
                new_coin = Coin()#жаңа койн қосады 
                coins.add(new_coin)'''
        
        crush_list = pygame.sprite.spritecollide(P1, money, False)#False себебі тру болса біз монейдағы обж шіріп тастаймыз 
        for obj in crush_list:
            if obj == C:
                money_score += 1#койн 1 балл 
                coin_score += 1
                C.change_location()
            elif obj == R1:
                money_score += 3# рубин 3 ббалл 
                R1.change_location()
                
                
        
            
            if money_score >= pev_money_score+10 and money_score > 0:
                SPEED += 1#егер моней скор алдынғыға қарағанда 10 ға көп болса энмемидің жылдамдығын бірге арттырамыз
                pev_money_score=money_score


        if pygame.sprite.spritecollideany(P1, enemies):  

                end = True

                
                pygame.mixer.Sound('/Users/adiyarkarim/Downloads/lab9_racer_crash (1).wav').play()
                time.sleep(1)

                scores = font_small.render("Your Score: " + str(coin_score), True, BLACK)
                money_scores = font_small.render("Your Money: " + str(money_score), True, BLACK)
                
                screen.fill(RED)
                screen.blit(game_over1, (30, 150)) 
                #screen.blit(scores, (30, 350))
                #screen.blit(money_scores, (30, 400))
                
                pygame.display.update()
                    
    pygame.display.flip()
pygame.quit()   