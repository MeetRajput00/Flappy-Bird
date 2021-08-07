import pygame
import math
import random
pygame.init()
score=0
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Flappy Bird")
logo = pygame.image.load("bird.png")
bg = pygame.image.load("bg.png")
player = pygame.image.load("player.png")
downpipe = pygame.image.load("downpipe.png")
font = pygame.font.SysFont("arial", 32)
pygame.display.set_icon(logo)
tryscore=False
playerX=220
playerYChange=0.1
playerY=230
changeY=0
pipeX=570
pipeY=random.randint(230, 400)
pipeXChange=0.5
def show_score():
    score_txt = font.render("Score: "+str(score), True, (255,255,255))
    screen.blit(score_txt, (10, 10))
def pipe_down(x,y):
    screen.blit(downpipe, (x, y))
def show_player(x,y):
    screen.blit(player, (x, y))
def background():
    screen.blit(bg,(0,0))
def distance(x1,x2,y1,y2):
    dist=math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
    if(dist>60):
        return True
    return False

notcollided=True
running=True
while running:
    screen.fill((0,0,0))
    background()
    show_player(playerX, playerY)
    pipe_down(pipeX, pipeY)
    show_score()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                changeY=playerY
                playerYChange=-1
    pipeX-=pipeXChange
    if(pipeX<=-120):
        pipeX=640
        pipeY=random.randint(230, 400)
    if changeY is not 0:
        if(distance(playerX,playerX,changeY,playerY)):
            playerYChange=1
            changeY=0
    if playerX+64>pipeX and playerX<pipeX+160 and playerY+32>=pipeY:
        notcollided=False
    if tryscore:
        if playerX+64>pipeX and playerX<pipeX+160 and playerY+32<=pipeY:
            score+=1
            tryscore=False
    else:
        if playerX>pipeX+300:
            tryscore=True
    if playerY>=398:
        notcollided=False
    if notcollided:
        if playerYChange>=0:
            playerYChange+=0.03
        else:
            playerYChange-=0.03
        playerY+=playerYChange
    else:
        pipeXChange=0
    pygame.display.update()