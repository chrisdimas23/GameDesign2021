import os, sys, time, pygame, random, math

os.system('cls')
pygame.init()

gameWords= ['python','java','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware']
word=random.choice(gameWords)

dropX = (random.randint(100,900))

score = 0

WHITE = [255,255,255]
BLACK = [0,0,0]
red=[200,25,0]

TitleFont= pygame.font.SysFont("helvetica", 70)  
WordFont=pygame.font.SysFont("helvetica", 50)
LetterFont=pygame.font.SysFont("helvetica",40)

WIDTH = 1000
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("Asteroids")

x = 10
y = 10
Wbox = 30
dist = 10

AS = pygame.image.load("spacePictures/asteroid.jpg")

clock = pygame.time.Clock()

text = ""
input_active = True
run = True

def game_Init(message):  
    BG=pygame.image.load("spacePictures/space1.webp")  
    screen.blit(BG, (0,0))
    text = WordFont.render(message, 1, WHITE)
    screen.blit(text,(365,80))

    rect1=pygame.Rect(430, 220, Wbox*5,Wbox*2)
    pygame.draw.rect(screen, WHITE, rect1, width=1)
    text = LetterFont.render("Level 1", 1, WHITE)
    screen.blit(text, (443 , 230))
 
    rect2=pygame.Rect(430, 390, Wbox*5,Wbox*2)
    pygame.draw.rect(screen, WHITE, rect2, width=1)
    text = LetterFont.render("Level 2", 1, WHITE)
    screen.blit(text, (443, 400))
    
    rect3=pygame.Rect(430, 560, Wbox*5,Wbox*2)
    pygame.draw.rect(screen, WHITE, rect3, width=1)
    text = LetterFont.render("Level 3", 1, WHITE)
    screen.blit(text, (443, 570))

    rect4=pygame.Rect(430, 730, Wbox*5,Wbox*2)
    pygame.draw.rect(screen, WHITE, rect4, width=1)
    text = LetterFont.render("Exit", 1, WHITE)
    screen.blit(text, (470, 740))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx,my= pygame.mouse.get_pos()
            if rect1.collidepoint((mx,my)):
                #call main function
                level1()
            if rect2.collidepoint((mx,my)):
                level2()
            if rect3.collidepoint((mx,my)):
                level3()
            if rect4.collidepoint((mx,my)):
                display_message("goodbye!!")
                pygame.quit()
                sys.exit()
        pygame.display.update() 
 
def display_message(message):
    pygame.time.delay(500)
    screen.fill(WHITE)
    text = WordFont.render(message, 1, BLACK)
    screen.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)

def textBox():
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                input_active = True
                text = ""
            elif event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_RETURN:
                    print(text)
                    text = text[:-999]
                elif event.key == pygame.K_BACKSPACE:
                    text =  text[:-1]
                else:
                    text += event.unicode

            screen.blit(BG, (0,0))
            text_surf = WordFont.render(text, True, (WHITE))
            screen.blit(text_surf, (100,100))
            pygame.display.flip()
            pygame.display.update()


x=100
y=10
m=490
n=10
wBox=20
hBox=20
xBox=20
zBox=20
BG=pygame.image.load("spacePictures/space1.webp")

pygame.time.delay(500)
rect_1=pygame.Rect(dropX, y, wBox, hBox)
rect_2=pygame.Rect(dropX, y, wBox, hBox)
rect_3=pygame.Rect(dropX, y, wBox, hBox)

speed=1
speed2=3/2
speed3=2
jump = 10

pygame.display.update()

def level1():
    check = True
    while check:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                check = False
        pygame.draw.rect(screen, red, rect_1)
        pygame.display.update()
        rect_1.y += speed
        screen.blit(BG, (0,0))
        pygame.display.update()
        if rect_1.y > HEIGHT - hBox: break
def level2():
    check = True
    while check:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                check = False
        pygame.draw.rect(screen, red, rect_2)
        pygame.display.update()
        rect_2.y += speed2
        screen.blit(BG, (0,0))
        pygame.display.update()
        if rect_2.y > HEIGHT - hBox: break
def level3():
    check = True
    while check:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                check = False
        pygame.draw.rect(screen, red, rect_3)
        pygame.display.update()
        rect_3.y += speed3
        screen.blit(BG, (0,0))
        pygame.display.update()
        if rect_3.y > HEIGHT - hBox: break
def scores():
    display_message("score function")

while True:
    game_Init("Level Select")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 