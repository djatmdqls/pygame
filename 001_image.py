import pygame as pg

pg.init()

화면가로길이 = 600
화면세로길이 = 600

화면 = pg.display.set_mode((화면가로길이, 화면세로길이))

빙수 = pg.image.load('img/a.jpg')
줄어든빙수 = pg.transform.scale(빙수, (100, 100))

화면.blit(줄어든빙수, (100, 100), pg.Rect(0, 0, 400, 270))

pg.display.update()

while True:
    for 이벤트 in pg.event.get():
        if 이벤트.type == pg.QUIT:
            quit()