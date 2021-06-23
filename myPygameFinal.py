import os, sys, time, pygame, random, math

os.system('cls')
pygame.init()

WHITE = [255,255,255]
BLACK = [0,0,0]

TitleFont= pygame.font.SysFont("helvetica", 70)  
WordFont=pygame.font.SysFont("helvetica", 50)
LetterFont=pygame.font.SysFont("helvetica",40)

WIDTH = 1000 
HEIGHT = 1000

screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("Asteroids")

Wbox = 30
dist = 10

message = "Level Select"

check = True
while check:
    screen.fill(WHITE)
    text = WordFont.render(message, 1, BLACK)
    screen.blit(text,(500,800))
    pygame.display.update()

    rect1=pygame.Rect(150, 350, Wbox*2,Wbox*2)
    pygame.draw.rect(screen, BLACK, rect1, width=1)
    text = LetterFont.render("Yes", 1, BLACK)
    screen.blit(text, (160 , 350))

    rect2=pygame.Rect(550, 350, Wbox*2,Wbox*2)
    pygame.draw.rect(screen, BLACK, rect2, width=1)
    text = LetterFont.render("No", 1, BLACK)
    screen.blit(text, (560 , 350))

pygame.quit()