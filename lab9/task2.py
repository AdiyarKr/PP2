import pygame, sys, math
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
            if event.key==pygame.K_t:
                pen="square"
            if event.key==pygame.K_y:
                pen="right triangle"
            if event.key==pygame.K_u:
                pen="equilateral triangle"
            if event.key==pygame.K_i:
                pen = "rhombus"
            if event.key==pygame.K_o:
                pen = "elips"
            

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

        #square
        #x, y, x1, y1 = 0,0,0,0
        if pen=="square":
            if event.type==pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                last_event="press"
            if event.type==pygame.MOUSEBUTTONUP:
                x1, y1 = pygame.mouse.get_pos()
                last_event="not press"
               
            if last_event=="not press":
                if (x1-x)<=(y1-y):
                    y1=y+(x1-x)#шаршы қабырғалары бірдей болууы үшін 
                else:
                    x1=x+(y1-y)#шаршы қабырғалары бірдей болууы үшін 
    
                pygame.draw.line(screen, color, (x, y), (x1, y),  1)
                pygame.draw.line(screen, color, (x, y),(x, y1) , 1)
                pygame.draw.line(screen, color, (x, y1), (x1, y1), 1)
                pygame.draw.line(screen, color, (x1, y),(x1, y1) , 1)
                    
                
                last_event = None

        if pen == "right triangle":
            if event.type==pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                last_event="press"
            if event.type==pygame.MOUSEBUTTONUP:
                x1, y1 = pygame.mouse.get_pos()
                last_event="not press"
            
            if last_event=="not press":
                
                pygame.draw.line(screen, color, (x, y),(x, y1) , 1)#бірінші қабырғасын саламыз 
                pygame.draw.line(screen, color, (x, y1),(x1, y1) , 1)
                pygame.draw.line(screen, color, (x, y),(x1, y1) , 1)
                last_event=None

        if pen == "equilateral triangle":
            if event.type==pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                last_event="press"
            if event.type==pygame.MOUSEBUTTONUP:
                x1, y1 = pygame.mouse.get_pos()
                last_event="not press"
            
            if last_event=="not press":
                h=y+((math.sqrt(3)*(x1-x))/2)# бұл биіктігі осы биіктік арқылы оренатция жасаймыз табан қабырғасынын жартысы 
                
                pygame.draw.line(screen, color, (x+(x1-x)/2, y), (x, h), 1)
                pygame.draw.line(screen, color, (x+(x1-x)/2, y), (x1, h), 1)
                pygame.draw.line(screen, color, (x1, h), (x, h), 1)
                #pygame.draw.line(screen, color, (x+(x1-x)/2, y), (x+(x1-x)/2, h), 1) #биіктігі
                last_event = None  
        #rhombus
        if pen == "rhombus":
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y =pygame.mouse.get_pos()
                last_event = "press"
            if event.type == pygame.MOUSEBUTTONUP:
                x1, y1 =pygame.mouse.get_pos()
                last_event = "not press"
            if last_event == "not press":
                pygame.draw.line(screen, color, (x, y+(y1-y)/2),(x+(x1-x)/2, y), 1)# төбелерінің коорлинттарын табу үшін 
                pygame.draw.line(screen, color, (x, y+(y1-y)/2),(x+(x1-x)/2, y1), 1)
                pygame.draw.line(screen, color, (x+(x1-x)/2, y1),(x1, y+(y1-y)/2), 1)
                pygame.draw.line(screen, color, (x+(x1-x)/2, y),(x1, y+(y1-y)/2), 1)
                
                
                last_event = None
        if pen == "elips":
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y =pygame.mouse.get_pos()
                last_event = "press"
            if event.type == pygame.MOUSEBUTTONUP:
                x1, y1 =pygame.mouse.get_pos()
                last_event = "not press"
            if last_event == "not press":
                pygame.draw.ellipse(screen, color,(x, y, x1, y1), -1)
                last_event = None
                

    clock.tick(FPS)       
    pygame.display.flip()

