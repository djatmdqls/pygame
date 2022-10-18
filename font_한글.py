import pygame as pg

pg.init()

화면가로길이 = 600
화면세로길이 = 600

화면 = pg.display.set_mode((화면가로길이, 화면세로길이))

시스템폰트 = pg.font.Font('img/b.ttf', 50, bold=False, italic=False)
입력폰트 = 시스템폰트.render('안녕하세요', True, (255, 255, 255))
입력폰트사각형 = 입력폰트.get_rect()
입력폰트사각형.center = (300, 300)

화면.blit(입력폰트, 입력폰트사각형)

pg.display.update()

while True:
    for 이벤트 in pg.event.get():
        if 이벤트.type == pg.QUIT:
            quit()