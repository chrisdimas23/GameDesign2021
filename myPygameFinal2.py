import os, sys, time, pygame, random, math

os.system('cls')
pygame.init()

WHITE = [255,255,255]
BLACK = [0,0,0]

TitleFont= pygame.font.SysFont("helvetica", 70)  
WordFont=pygame.font.SysFont("helvetica", 50)
LetterFont=pygame.font.SysFont("helvetica",40)

WIDTH = 1000
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("Asteroids")

Wbox = 30
dist = 10

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

def level1():
    display_message("You are in level 1")
def level2():
    display_message("You are in level 2")
def level3():
    display_message("you are in level 3")
def scores():
    display_message("score function")
 
while True:
    game_Init("Level Select")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 