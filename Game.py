from operator import truediv
from turtle import pos
import pygame
from pygame.locals import *
from tokenize import String
import random

pygame.init()

bg = pygame.image.load('Highway.png')
imgSize=(350,600)
bg = pygame.transform.scale(bg,imgSize)
bg2 = pygame.transform.scale(bg,imgSize)
bgY=0
bgY2=-600

mt = pygame.image.load('Motorcycle.png')
mtSize = (100,100)
mt = pygame.transform.scale(mt,mtSize)
posX=125
posY=500

st = pygame.image.load('shot.png')
stSize=(100,100)
st=pygame.transform.scale(st,stSize)
shotArray=[]

bmt = pygame.image.load('BadMotorcycle.png')
bmt = pygame.transform.scale(bmt,mtSize)
bmtArray=[]

bst = pygame.image.load('BadShot.png')
bst=pygame.transform.scale(bst,stSize)
bstArray=[]

font = pygame.font.Font('freesansbold.ttf', 20)
slow = font.render('[Dont drive so fast]', True, (0,255,255))

sc=pygame.display.set_mode((350,600))
pygame.display.set_caption("Rogue Base")
timeDecorred=0
op= True
while op:
    timeDecorred+=1
    sc.blit(bg2,(0,bgY2))
    sc.blit(bg,(0,bgY))
    sc.blit(mt,(posX,posY))
    pygame.time.delay(50)

    if timeDecorred%60==0:
        mX=random.randint(0,350)
        bmtArray.append([mX,0])

    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        posY-=3
    if key[pygame.K_DOWN]:
        posY+=3
    if key[pygame.K_LEFT]:
        posX-=3
    if key[pygame.K_RIGHT]:
        posX+=3
    if key[pygame.K_SPACE]:
        shotArray.append([posX,posY-50])
        

    if posX<-25:
        posX=-25
    if posX>275:
        posX=275
    if posY<400:
        posY=400
        if timeDecorred%10<8:
            sc.blit(slow,(90,200))
    if posY>500:
        posY=500

    bgY+=3
    bgY2+=3
    if bgY>600:
        bgY=-600
    if bgY2>600:
        bgY2=-600
    for shot in shotArray:
        if shot[1]<-25:
            shotArray.pop(0)
        shot[1]-=5
        for i in range(0,len(bmtArray)-1):
            if (shot==bmtArray[i]):
                bmtArray.pop(i)
                print("explodiu")
        sc.blit(st,(shot[0],shot[1]))
    for enemie in bmtArray:
        if timeDecorred%20==0:
            x=random.randint(0,1)
            y=random.randint(0,1)
        if x==0:
            enemie[0]-=3
        else:
            enemie[0]+=3
        if y==0:
            enemie[1]-=3
        else:
            enemie[1]+=3
        if enemie[0]<-25:
            enemie[0]=-25
        if enemie[0]>275:
            enemie[0]=275
        if enemie[1]<0:
            enemie[1]=0
        if enemie[1]>300:
            enemie[1]=300
        sc.blit(bmt,(enemie[0],enemie[1]))
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            op=False

pygame.quit()