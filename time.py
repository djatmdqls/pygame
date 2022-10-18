import pygame as pg

pg.init()

화면가로길이 = 600
화면세로길이 = 600

화면 = pg.display.set_mode((화면가로길이, 화면세로길이))

흰색 = (255, 255, 255)
파랑색 = (0, 0, 255)

원위치 = [50, 50]

시계 = pg.time.Clock()

while True:
    화면.fill(흰색)

    흐른시간 = 시계.tick(10) / 1000

    원위치[0] += 100 * 흐른시간
    if 원위치[0] > 570:
        원위치[0] = 50

    표시활성위치 = (원위치[0], 원위치[1])
    pg.draw.circle(화면, 파랑색, 표시활성위치, 20)

    pg.display.update()

    for 이벤트 in pg.event.get():
        if 이벤트.type == pg.QUIT:
            quit()
