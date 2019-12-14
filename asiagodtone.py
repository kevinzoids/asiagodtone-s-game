#!/usr/bin/env python
# coding: utf-8


import pygame as pg, random, math
pg.init()

#設定視窗背景
width, height = 1500, 920                      
screen = pg.display.set_mode((width, height))   
pg.display.set_caption("asiagodtone's game")         
bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((255,255,255))

#亞統
image = pg.image.load("德克斯特.jpg")
image.convert()
image = pg.transform.scale(image, (64,64))
ball = image
rect = ball.get_rect()
rect.center = (750,450)                 
clock = pg.time.Clock()


#關閉程式的程式碼

running = True
playing = True  #開始時球不能移動
throwing = False
stop = True
while running:
    clock.tick(30)  #每秒執行30次
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            buttons = pg.mouse.get_pressed()
            if buttons[0]:          #按滑鼠左鍵後球可移動
                playing = True
                throwing = False
                stop = True
        elif event.type == pg.MOUSEBUTTONUP:
            playing = False
            throwing = True
            stop = False
#######################################################################################
    if playing == True:
        mouses = pg.mouse.get_pos()  #取得滑鼠坐標
        rect.centerx = mouses[0]     #移動滑鼠
        rect.centery = mouses[1]
        screen.blit(bg, (0,0))
        screen.blit(ball, rect.topleft) 
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
                pg.display.update() 
                if rect.centery>887:
                    stop = True
                    rect.centerx = mouses[0]
                    rect.centery = 888
                    screen.blit(bg, (0,0))
                    screen.blit(ball, rect.topleft) 
                    pg.display.update()
            else:
                stop = True
                rect.centerx = mouses[0]
                rect.centery = 888
                screen.blit(bg, (0,0))
                screen.blit(ball, rect.topleft) 
                pg.display.update()
##############################################################################################
pg.quit()        

