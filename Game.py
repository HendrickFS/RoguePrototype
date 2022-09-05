from operator import truediv
from turtle import pos
import pygame
from pygame.locals import *
from tokenize import String
import random

pygame.init()

bg = pygame.image.load('Highway.png')
imgSize = (350, 600)
bg = pygame.transform.scale(bg, imgSize)
bg2 = pygame.transform.scale(bg, imgSize)
bgY = 0
bgY2 = -600

mt = pygame.image.load('Motorcycle.png')
mtSize = (100, 100)
mt = pygame.transform.scale(mt, mtSize)
tmt = pygame.transform.rotate(mt, 90)
posX = 125
posY = 500
hp = pygame.image.load('hp.png')
health = [[20, 570], [42, 570], [64, 570]]

st = pygame.image.load('shot.png')
stSize = (100, 100)
st = pygame.transform.scale(st, stSize)
shotArray = []
charged = True

bmt = pygame.image.load('BadMotorcycle.png')
bmt = pygame.transform.scale(bmt, mtSize)
bmtArray = []

bst = pygame.image.load('BadShot.png')
bst = pygame.transform.scale(bst, stSize)
bstArray = []

font = pygame.font.Font('freesansbold.ttf', 20)
font2 = pygame.font.Font('freesansbold.ttf', 30)
slow = font.render('[Dont drive so fast]', True, (0, 255, 255))
over = font2.render('[GAME OVER]', True, (0, 255, 255))
press = font.render('<Press SPACE to play again>', True, (0, 255, 255))

sc = pygame.display.set_mode((350, 600))
pygame.display.set_caption("Rogue Base")
timeDecorred = 0
gameOver = False
op = True
while op:
    pygame.time.delay(50)
    timeDecorred += 1
    if gameOver:
        bstArray = []
        bmtArray = []
        shotArray = []
        sc.blit(bg2, (0, bgY2))
        sc.blit(bg, (0, bgY))
        sc.blit(tmt, (posX, posY))
        sc.blit(over, (90, 300))
        sc.blit(press, (50, 350))
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            gameOver = False
            health = [[20, 570], [42, 570], [64, 570]]

    if not gameOver:
        sc.blit(bg2, (0, bgY2))
        sc.blit(bg, (0, bgY))
        sc.blit(mt, (posX, posY))
        if not charged:
            if timeDecorred % 10 == 0:
                charged = True

        if timeDecorred % 100 == 0:
            mX = random.randint(0, 350)
            bmtArray.append([mX, 0, 0])
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            posY -= 3
        if key[pygame.K_DOWN]:
            posY += 3
        if key[pygame.K_LEFT]:
            posX -= 3
        if key[pygame.K_RIGHT]:
            posX += 3
        if key[pygame.K_SPACE] and charged:
            charged = False
            shotArray.append([posX, posY-50])

        if posX < -25:
            posX = -25
        if posX > 275:
            posX = 275
        if posY < 400:
            posY = 400
            if timeDecorred % 10 < 8:
                sc.blit(slow, (90, 200))
        if posY > 500:
            posY = 500
        bgY += 8
        bgY2 += 8
        if bgY > 600:
            bgY = -600
        if bgY2 > 600:
            bgY2 = -600
        for shot in shotArray:
            if shot[1] < -25:
                shotArray.pop(0)
            shot[1] -= 5
            sc.blit(st, (shot[0], shot[1]))
        for enemie in bmtArray:
            if timeDecorred % 20 == 0:
                x = random.randint(0, 1)
                y = random.randint(0, 1)
            if x == 0:
                enemie[0] -= 3
            else:
                enemie[0] += 3
            if y == 0:
                enemie[1] -= 3
            else:
                enemie[1] += 3
            if enemie[0] < -25:
                enemie[0] = -25
            if enemie[0] > 275:
                enemie[0] = 275
            if enemie[1] < 0:
                enemie[1] = 0
            if enemie[1] > 300:
                enemie[1] = 300
            sc.blit(bmt, (enemie[0], enemie[1]))
            for shot in shotArray:
                if (shot[0]+50 >= enemie[0]+30 and shot[0]+50 <= enemie[0]+70) and (shot[1]+50 >= enemie[1] and shot[1]+50 <= enemie[1]+100):
                    try:
                        bmtArray.remove(enemie)
                        shotArray.remove(shot)
                    except:
                        print("error")
            enemie[2] += 1
            if enemie[2] % 50 == 0:
                bstArray.append([enemie[0], enemie[1]+50])

        for eShot in bstArray:
            eShot[1] += 5
            sc.blit(bst, (eShot[0], eShot[1]))
            for shot in shotArray:
                if (shot[0]+50 >= eShot[0]+30 and shot[0]+50 <= eShot[0]+70) and (shot[1]+50 >= eShot[1] and shot[1]+50 <= eShot[1]+100):
                    try:
                        bstArray.remove(eShot)
                        shotArray.remove(shot)
                    except:
                        print("error")
            if (posX+50 >= eShot[0]+30 and posX+50 <= eShot[0]+70) and (posY+50 >= eShot[1] and posY+50 <= eShot[1]+100):
                try:
                    bstArray.remove(eShot)
                    health.pop(len(health)-1)
                except:
                    print("error")
            if eShot[1]>600:
                bstArray.pop(0)
        for h in health:
            sc.blit(hp, (h[0], h[1]))
        if health == []:
            gameOver = True

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            op = False

pygame.quit()
