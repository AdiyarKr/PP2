import pygame, sys
pygame.init()

#түстер
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

#defolt clolor of pen 
color = RED

#clock 
clock = pygame.time.Clock()
FPS = 60

#screen 
wl, wh = 1001, 601
screen = pygame.display.set_mode((wl, wh))
screen.fill(WHITE)#hole scren white

#pen
pen="mouse" #defolt is mouse
last_event=None

pre, cur = None, None
pre_e, cur_e = None, None


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #pen
        if event.type == pygame.KEYDOWN:#егер кейбордттан бірнәрсе басылса
            if event.key == pygame.K_q:
                pen="mouse"#егер q басылса пен мышкаға ауысады
            if event.key == pygame.K_w:
                pen="rectangle"#егер w басылса пен ректангл сызады
            if event.key == pygame.K_e:
                pen="circle"#егер e басылса сөркл сызады 
            if event.key == pygame.K_r:
                pen="Eraser"#егер e басылса ерейсер болады

            #clolor
            if event.key == pygame.K_a:
                color=RED
            if event.key == pygame.K_s:
                color=GREEN
            if event.key == pygame.K_d:
                color=BLUE
            if event.key == pygame.K_f:
                color=BLACK
        
        #draw by mouse
        if pen == "mouse":
            if event.type == pygame.MOUSEBUTTONDOWN:#тінтіуір басылды ма соны тексереді
                pre = pygame.mouse.get_pos()#бастапқы тінтуірдің координатасы
            if event.type == pygame.MOUSEMOTION:#тінтіуір қозғалды ма соны тексереді
                cur = pygame.mouse.get_pos()#тінтіуір қозғалғанан кейінгі координата
            if pre:#егер мышка басылса(мышканын алғашқы кординатссы анықталса)
                pygame.draw.line(screen, color, pre, cur, 1)#сызық сызады бастаппқы точка мен сонғының арасында
                pre = cur#бірінші сызық салынғнан кейін келесі сызық салу үшін бастапқы точка тінтіуір қозғалғанан кейінгіге ауысады 
            if event.type==pygame.MOUSEBUTTONUP:#тітіуірді басқанды тоқтатқанда
                pre=None#бастапқы кордината қайтадан анықталады 
        
        #draw rectangle
        if pen == "rectangle":
            if event.type==pygame.MOUSEBUTTONDOWN:#егер мышка басылса 
                x, y = pygame.mouse.get_pos()#бастапқы кордината
                last_event="press"#тітіуір басылып тұр
            if event.type==pygame.MOUSEBUTTONUP:#тітіуірді баспай тұр
                x1, y1 = pygame.mouse.get_pos()#тітіуірді көтергендегі кордината
                last_event="not press"#тінтіуір басылмай тұр
            if last_event=="not press":#егер тінітуірді басқаны тоқтатылса
                #pygame.draw.rect(screen, color, (int(x), int(y), int(x1)-int(x), int(y1)-int(y) ))#бұл іші боялған тік төрт бұрыш салды
                pygame.draw.line(screen, color, (x, y), (x1, y), 1)
                pygame.draw.line(screen, color, (x,y), (x, y1), 1)
                pygame.draw.line(screen, color, (x, y1), (x1, y1), 1)
                pygame.draw.line(screen, color, (x1, y), (x1, y1), 1)
                last_event=None
        #draw circle
        if pen == "circle":
            if event.type==pygame.MOUSEBUTTONDOWN:#егер мышка басылса
                x, y = pygame.mouse.get_pos()#бастапқы кордината
                last_event="press"#тітіуір басылып тұр
            if event.type==pygame.MOUSEBUTTONUP:#тітіуірді баспай тұр
                x1, y1 = pygame.mouse.get_pos()#тітіуірді көтергендегі кордината
                last_event="not press"#тінтіуір басылмай тұр
            if last_event=="not press":#егер тінітуірді басқаны тоқтатылса
                pygame.draw.circle(screen, color, (((x+x1)//2), ((y+y1)//2)), abs((x1-x)/2))#шеңбер салады
                pygame.draw.circle(screen, WHITE, (((x+x1)//2), ((y+y1)//2)), abs((x1-x)/2)-0.5)#шеңбер ішін тазалайды ақ түске бояю
                last_event=None
        #Eraser
        if pen == "Eraser":
            if event.type == pygame.MOUSEBUTTONDOWN:#тінтіуір басылды ма соны тексереді
                pre_e = pygame.mouse.get_pos()#бастапқы тінтуірдің координатасы
            if event.type == pygame.MOUSEMOTION:#тінтіуір қозғалды ма соны тексереді
                cur_e = pygame.mouse.get_pos()#тінтіуір қозғалғанан кейінгі координата
            if pre_e:
                pygame.draw.line(screen, WHITE, pre_e, cur_e, 10)#қалыңдығы 10 пиксел болатын сызық сызамыз
                pre_e=cur_e
            if event.type == pygame.MOUSEBUTTONUP:
                prev1 = None


    clock.tick(FPS)       
    pygame.display.flip()

