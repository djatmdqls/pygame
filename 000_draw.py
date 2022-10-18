import pygame as pg

pg.init()

화면가로길이 = 600
화면세로길이 = 600

화면 = pg.display.set_mode((화면가로길이, 화면세로길이))
사각형 = pg.Rect(300, 300, 50, 50)

pg.draw.rect(화면, (255, 0, 0), (50, 50, 50, 50))
pg.draw.rect(화면, (255, 255, 255), (100, 200, 200, 100), 20)
pg.draw.rect(화면, (0, 0, 255), 사각형, 5)

pg.display.update()

while True:
    for 이벤트 in pg.event.get():
        if 이벤트.type == pg.QUIT:
            quit()