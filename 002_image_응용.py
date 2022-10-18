import pygame as pg

pg.init()

화면가로길이 = 600
화면세로길이 = 600

화면 = pg.display.set_mode((화면가로길이, 화면세로길이))

빙수 = pg.image.load('img/a.jpg')
줄어든빙수 = pg.transform.scale(빙수, (100, 100))
돌려진빙수 = pg.transform.rotate(빙수, 45)

돌려진빙수_사각형 = 돌려진빙수.get_rect()
돌려진빙수_사각형.center = (250, 320)

화면.blit(돌려진빙수, 돌려진빙수_사각형)

pg.display.update()

while True:
    for 이벤트 in pg.event.get():
        if 이벤트.type == pg.QUIT:
            quit()