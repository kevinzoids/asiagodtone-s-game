#!/usr/bin/env python
# coding: utf-8



import pygame as pg, random, math
pg.init()

#設定視窗背景
width, height = 1500, 920                      
screen = pg.display.set_mode((width, height))  
font = pg.font.SysFont("simhei", 100)
pg.display.set_caption("asiagodtone's game")         
bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((255,255,255))
text = font.render("Press Left Click Button to start game!", True, (0,0,0), (255,255,255))
bg.blit(text, (50,50))

#亞統
ball = pg.image.load("德克斯特.jpg").convert()
ball = pg.transform.scale(ball, (64,64))
rect = ball.get_rect()
rect.center = (750,450)                 
clock = pg.time.Clock()

#trash can
can = pg.image.load("trash_with_liner.jpg").convert()
can = pg.transform.scale(can, (128,128))
can_rect = can.get_rect()
can_rect.center = (random.randint(100,850),856)



# GAME

score = 0
running = True
playing = True  #開始時球不能移動
throwing = False
stop = True
timerON = False
timer = [pg.time.get_ticks(), pg.time.get_ticks()]
timeUse = timer[-1] - timer[0]
while running:
    clock.tick(60)  #每秒執行30次
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            buttons = pg.mouse.get_pressed()
            
            if buttons[0]:          #按滑鼠左鍵後球可移動
                playing = True
                throwing = False
                stop = True
                timerON = True

        elif event.type == pg.MOUSEBUTTONUP:
            playing = False
            throwing = True
            stop = False
            
########################################################################################
    if timerON == True:
        timer[-1] = pg.time.get_ticks()
        timeUse = timer[-1] - timer[0]
        #text = font.render("Press Left Click Button to start game!", True, (255,255,255), (255,255,255))
        bg.blit(text, (50,50))
        screen.blit(bg, (0,0))
        SCORE = "Score: " + str(score) + " "
        text = font.render(SCORE, True, (0,0,0), (255,255,255))
        TIME = font.render("Time: " + str(timeUse/1000)+" sec  ", True, (0,0,0), (255,255,255))
        bg.blit(TIME, (50,150))
        bg.blit(text, (50,50))
        screen.blit(bg, (0,0))
        screen.blit(ball, rect.topleft) 
        screen.blit(can, can_rect.topleft)
        pg.display.update()
    else:
        timer[0] = pg.time.get_ticks()
            
            
            
#######################################################################################
    if playing == True:
        mouses = pg.mouse.get_pos()  #取得滑鼠坐標
        rect.centerx = mouses[0]     #移動滑鼠
        rect.centery = mouses[1]-30
        screen.blit(bg, (0,0))
        screen.blit(ball, rect.topleft)
        screen.blit(can, can_rect.topleft)
        pg.display.update()
#######################################################################################
    if throwing == True:
        t = 0
        while rect.centery<887:
            t += 1        
            clock.tick(40)
            if stop == False:
                rect.centerx = mouses[0]
                rect.centery = mouses[1]+0.5*t**2
                screen.blit(bg, (0,0))
                screen.blit(ball, rect.topleft)
                screen.blit(can, can_rect.topleft)
                pg.display.update() 
                if rect.centery>887 and rect.centerx > can_rect.centerx-32 and rect.centerx < can_rect.centerx+32:
                    stop = True
                    throwing = False
                    rect.centerx = mouses[0]
                    rect.centery = 888
                    score += 1
                    SCORE = "Score: " + str(score) + " "
                    text = font.render("Press Left Click Button to start game!", True, (255,255,255), (255,255,255))
                    bg.blit(text, (50,50))
                    screen.blit(bg, (0,0))
                    text = font.render(SCORE, True, (0,0,0), (255,255,255))
                    TIME = font.render("Time: " + str(timeUse/1000)+" sec  ", True, (0,0,0), (255,255,255))
                    bg.blit(TIME, (50,150))
                    bg.blit(text, (50,50))
                    screen.blit(bg, (0,0))
                    screen.blit(ball, rect.topleft) 
                    screen.blit(can, can_rect.topleft)
                    pg.display.update()
                    can_rect.center = (random.randint(100,850),856)
                    
                    timerON = False
########################################################################################




pg.quit()        


