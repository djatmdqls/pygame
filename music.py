import pygame as pg

pg.init()

화면가로길이 = 600
화면세로길이 = 600

화면 = pg.display.set_mode((화면가로길이, 화면세로길이))

pg.mixer.music.load('img/c.mp3')
pg.mixer.music.play()

pg.display.update()

while True:
    for 이벤트 in pg.event.get():
        if 이벤트.type == pg.QUIT:
            quit()