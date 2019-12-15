#!/usr/bin/env python
# coding: utf-8

# In[2]:


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
bg.blit(font.render("Score: ", True, (0,0,0), (255,255,255)), (50,50))

#亞統
image = pg.image.load("C:\\Users\kevin\Desktop\德克斯特.jpg").convert()
image = pg.transform.scale(image, (64,64))
ball = image
rect = ball.get_rect()
rect.center = (750,450)                 
clock = pg.time.Clock()

#trash can
can = pg.image.load("C://Users/kevin/Desktop/trash_with_liner.jpg").convert()
can = pg.transform.scale(can, (128,128))
can_rect = can.get_rect()
can_rect.center = (random.randint(100,850),856)



# GAME

score = 0
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
                    SCORE = "Score: " + str(score)
                    text = font.render(SCORE, True, (0,0,0), (255,255,255))
                    bg.blit(text, (50,50))
                    screen.blit(bg, (0,0))
                    screen.blit(ball, rect.topleft) 
                    screen.blit(can, can_rect.topleft)
                    pg.display.update()
                    can_rect.center = (random.randint(100,850),856)

########################################################################################

pg.quit()        


# In[15]:


score


# In[ ]:




