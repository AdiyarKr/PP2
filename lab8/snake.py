import pygame as pg 
from random import  randrange
import time

pg.init()

w= 800
h=800
fps= 6
level=0
step = 40 
screen = pg.display.set_mode((w, h))
pg.display.set_caption('Snake')
is_running, lose = True, False
clock = pg.time.Clock()
score = pg.font.SysFont("Verdana", 20)
surf = pg.Surface((390, 390), pg.SRCALPHA)#гэйм оверді главный экран бетіне қою үшін(сурет үстіне сурет қою)
bg = pg.image.load("/Users/adiyarkarim/Downloads/back.png")
bg = pg.transform.scale(bg, (w, h))
gameover = pg.image.load("/Users/adiyarkarim/Downloads/gameover.jpg")
gameover = pg.transform.scale(gameover, (390, 390))

class Food:
    def __init__(self):
        #әр 40 пиксел ішінде фуд координаталарын анықтайды 
        self.x = randrange(0, w, step)
        self.y = randrange(0, h, step)
        self.pic = pg.image.load("/Users/adiyarkarim/Downloads/food (2).png")

    def draw(self):
        screen.blit(self.pic, (self.x, self.y))

    def draw2(self):
        self.x = randrange(0, w, step)
        self.y = randrange(0, h, step)

class Snake:
    def __init__(self):
        self.speed = step#снэйк step пикселге қозғалып отырады
        self.body = [[360, 360]] #басының бастапқы кординаталары
        self.dx = 0
        self.dy = 0
        self.score = 0
        self.color = 'blue'
    
    def move(self, events):
        for event in events:
            if event.type == pg.KEYDOWN: #клав басылды ма соны тексері 
                if event.key == pg.K_LEFT and self.dx == 0: #сол жаққа жылжу басылғанда ол оңға жылжымауы керек(бұл жерде снэйк y бойынша қозғалып жатыр, ал егер олай болмасаол солға немесе оңға қозғалуда керісінше бағытта қозғала алмайды )
                    self.dx = -self.speed
                    self.dy = 0#y бойынша жылжымайды
                if event.key == pg.K_RIGHT and self.dx == 0:#оң жаққа жылжу басылғанда ол солға жылжымауы керек
                    self.dx = self.speed
                    self.dy = 0#y бойынша жылжымайды
                if event.key == pg.K_UP and self.dy == 0:#жоғары жылжып жатқанда төмен жылжымас үшін
                    self.dx = 0#x бойынша жылжымайды
                    self.dy = -self.speed
                if event.key == pg.K_DOWN and self.dy == 0:#төмен жылжып жатқанда жоғары жылжымас үшін
                    self.dx = 0#x бойынша жылжымайды
                    self.dy = self.speed

        #снэйктің басынан басқасын осындай кординатларға жылжытамыз
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0] 
            self.body[i][1] = self.body[i - 1][1]

        #снэйк басын жылжытамыз клав тан басылған сайын 
        self.body[0][0] += self.dx 
        self.body[0][1] += self.dy 

    def draw(self):
        for part in self.body:
            pg.draw.rect(screen, self.color, (part[0], part[1], step, step))#step x step шаршы салады part[0], part[1] осы точкаларда 
    
    #снэйк фуд жегенін тексереміз
    def collide_food(self, f:Food):
        if self.body[0][0] == f.x and self.body[0][1] == f.y: #егер снэйк басының координаталары фудпен сәйкес келсе скоре бірге арттырамыз
            self.score += 1
            self.body.append([900, 900]) 
    
    #гэйм овер егер снэйк басы өзінің денесімен соғылса 
    def self_collide(self):
        global is_running
        if self.body[0] in self.body[1:]: #егер денесінің координаталары басымен сәйкес келсе 
            lose = True #гэйм овер

    
    def check_food(self, f:Food): 
        if [f.x, f.y] in self.body: #фуд снэйк басына тиді ма соны тексереді 
            f.draw2() #фуд қайта саламыз 


class Wall:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.pic = pg.image.load("/Users/adiyarkarim/Downloads/wall1.png")


    def draw(self):
        screen.blit(self.pic, (self.x, self.y))

#снэйк пен фудқа объэкт жасаймыз
s = Snake()
f = Food()

while is_running:
    clock.tick(fps)
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            is_running = False
        
    screen.blit(bg, (0, 0))

    
    my_walls = open(f'wall{level}.txt', 'r').readlines() #әр жолды жеке лист ретінде оқиды
    walls = []
    for i, line in enumerate(my_walls): #әр жолмен жүгіріп өтеміз
        for j, each in enumerate(line): #әр элеметтпен жүріп өтеміз
            if each == "+":#егер ол + қа тең болса 
                walls.append(Wall(j * step, i * step)) #сол i мен j координаталарын степқа көбейтеміз координатдан пиксел жасағымыз келеді 

    #класстардың методтарын шақырамыз
    f.draw()
    s.draw()
    s.move(events) #UP DOWN keft right басылуы евентс
    s.collide_food(f)
    s.self_collide()
    s.check_food(f)

    #скор және левлді экранға шығарамыз 
    counter = score.render(f'Score: {s.score}', True, 'black')
    #render сурет бетіне жазу жазу үшін қоладнылады (score = pg.font.SysFont("Verdana", 20) осындай болып жазылады)
    screen.blit(counter, (50, 50))
    l = score.render(f'Level: {level}', True, 'black')
    screen.blit(l, (50, 80))

    #келесі кезеңге өту үшін шарт 
    if s.score == 3:
        level += 1 #егер скоре 3 ке тең болғанда левелді бірге арттырамыз 
        level %= 3 
        fps += 2 #жылдамдықты арттырамыз
        s.score = 0 #келесі левелге жаңа скор
        # Останавливаем движение змейки на 5 секунд
        s.dx = 0
        s.dy = 0
        time.sleep(2)

        # После ожидания, возобновляем движение змейки
        s.dx = s.speed  # Например, движение вправо
        s.dy = 0

    #wallдарды экранға шығрамыз
    for wall in walls:
        wall.draw()
        if f.x == wall.x and f.y == wall.y: #егер фуд wallмен координатасымен беттссе фудты қайта саламыз
            f.draw2()

        if s.body[0][0] == wall.x and s.body[0][1] == wall.y: #гэйм овер егер снэйк денесі валллға тисе 
            lose = True

    #цикл 'game_over'
    while lose:
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_running = False
                lose = False   
        surf.blit(gameover, (0, 0))
        screen.blit(surf, (200, 200))
        cntr = score.render(f'Your score is {s.score}', True, 'black')
        screen.blit(cntr, (320, 500))
        l = score.render(f'Your level is {level}', True, 'black')
        screen.blit(l, (322, 520))
        pg.display.flip()

    pg.display.flip()
pg.quit()