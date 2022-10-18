import pygame as pg

pg.init()

화면가로길이 = 600
화면세로길이 = 600

화면 = pg.display.set_mode((화면가로길이, 화면세로길이))

pg.draw.line(화면, (255, 0, 0), (50, 50), (50, 200), 5)
pg.draw.line(화면, (255, 255, 255), (50, 50), (200, 50), 5)

for i in range(10):
    pg.draw.line(화면, (255, 255, 255), (50, 100+30*i), (200, 100+30*i), 5)
    pg.draw.line(화면, (255, 0, 0), (50+30*i, 50), (50+30*i, 300), 5)

pg.display.update()

while True:
    for 이벤트 in pg.event.get():
        if 이벤트.type == pg.QUIT:
            quit()