import pygame
import random
import math
from pygame import mixer

mixer.init()
pygame.init()

mixer.music.load("bgm2.mp3")
mixer.music.play(-1)

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('Space Shooter Game')
icon=pygame.image.load('icon.jpg')
pygame.display.set_icon(icon)

background=pygame.image.load('bg11.jpg')
spaceshipimg=pygame.image.load('player.png')

enemyimg=[]
enemyX=[]
enemyY=[]
enemyspeedX=[]
enemyspeedY=[]

no_of_enemys=6

for i in range(no_of_enemys):


    enemyimg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(0,150))
    enemyspeedY.append(40)
    enemyspeedX.append(-1)

bulletimg=pygame.image.load('bullet.png')
check=False
bulletX=387
bulletY=480
    
 
spaceshipiX=370 
spaceshipiY=480


changeX=0
changeY=0
speed=1.5
score=0
level=1

def gameover():
    font_gameover=pygame.font.SysFont("Arial",65,"bold")
    font_img=font_gameover.render(f"GAME OVER",True,"white")
    
    font_resume=pygame.font.SysFont("Arial",32,"bold")
    resume_img=font_resume.render(f"press 'R' to resume",True,"white")
    quit_img=font_resume.render(f"press 'Q' to Quit",True,"white")
    over=True
    while over:
        screen.blit(background,(0,0))
        screen.blit(font_img,(200,250))
        
        screen.blit(resume_img,(500,0))
        screen.blit(quit_img,(500,30))
        
    
        
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_r:
                        for j in range(no_of_enemys):
                            enemyY[j]=15
                        over=False
                        running=True
                elif event.key==pygame.K_q:
                        over=False
                        running=False
                
    
                    
            
        gamelevel()
        score_text()
        pygame.display.update()
    return running


def gamestart():
    font_start=pygame.font.SysFont("Arial",50,"bold")
    img=font_start.render("Press 'S' To Start",True,"white")
    screen.blit(img,(220,250))

def score_text():
    font=pygame.font.SysFont("Arial",32,'bold')
    img=font.render(f"score:{score}",True,"white")
    screen.blit(img,(10,30))

def gamelevel():
    font_level=pygame.font.SysFont("Arial",32,"bold")
    img=font_level.render(f"Level:{level}",True,"white")
    screen.blit(img,(10,0))

# def gameresume():
#     font_resume=pygame.font.SysFont("Arial",32,"bold")
#     img=font_resume.render(f"press 'R' to resume",True,"white")
#     imgs=font_resume.render(f"press 'Q' to Quit",True,"white")
#     screen.blit(img,(500,0))
#     screen.blit(imgs,(500,30))


running=True
def startpage():
    start=True
    while start:
        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event. type==pygame.QUIT:
                start=False
                running=False

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_s:
                    start=False
        gamestart()
        pygame.display.update()             



startpage()

while running:

    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event. type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:

            if event.key==pygame.K_LEFT:
                changeX=-speed
            if event.key==pygame.K_RIGHT:
                changeX=speed
            # if event.key==pygame.K_UP:
                # changeY=-speed
            # if event.key==pygame.K_DOWN:
                # changeY=speed
            if event.key==pygame.K_SPACE:
                if check is False:
                    bulletsound=mixer.Sound("laser2.mp3")  
                    bulletsound.play()
                    check=True
                    bulletX=spaceshipiX+15
                    # print("Fire")
        if event.type==pygame.KEYUP:
            changeX=0
            changeY=0


    spaceshipiX+=changeX
    spaceshipiY+=changeY
    if spaceshipiX<=0:
        spaceshipiX=0

    if spaceshipiY<=0:
        spaceshipiY=0

    if spaceshipiX>=736:
        spaceshipiX=736
    if spaceshipiY>=530:
        spaceshipiY=530
    
    for i in range(no_of_enemys):
        if enemyY[i]>=420:
            for j in range(no_of_enemys):
                enemyY[j]=2000
            ret=gameover()
            if ret==False:
                running=False
            break
        enemyX[i]+=enemyspeedX[i]
        if enemyX[i]<=0:
            enemyspeedX[i]=1
            enemyY[i]+=enemyspeedY[i]
        if enemyX[i]>=736: 
            enemyspeedX[i]=-1
            enemyY[i]+=enemyspeedY[i]

        
        distance=math.sqrt(math.pow(bulletX-enemyX[i],2)+math.pow(bulletY-enemyY[i],2))
        if distance<40 and bulletX>(enemyX[i]-10) and bulletX<(enemyX[i]+40):
            explosion=mixer.Sound("explosion.mp3")
            explosion.play()
            bulletY=480
            check=False
            enemyX[i]=random.randint(0,736)
            enemyY[i]=random.randint(30,150)
            score+=1
            
        screen.blit(enemyimg[i],(enemyX[i],enemyY[i]))
        if score>=20:
            level+=1
            score=0

    if bulletY<=0:
        bulletY=490
        check=False

    

    
    
    if check is True:
        screen.blit(bulletimg,(bulletX,bulletY))
        bulletY-=2

    screen.blit(spaceshipimg,(spaceshipiX,spaceshipiY ))   
    gamelevel()
    score_text()
    pygame.display.update()



