import pygame as pg

pg.init()

화면가로길이 = 600
화면세로길이 = 600

화면 = pg.display.set_mode((화면가로길이, 화면세로길이))
다각형리스트 = [(300, 300), (100, 500), (500, 500)]

pg.draw.polygon(화면, (255, 0, 0), 다각형리스트, 3)

pg.display.update()

while True:
    for 이벤트 in pg.event.get():
        if 이벤트.type == pg.QUIT:
            quit()