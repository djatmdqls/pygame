import os
import pygame

pygame.init()

가로 = 640
세로 = 480
화면 = pygame.display.set_mode((가로, 세로))
clock = pygame.time.Clock()

pygame.display.set_caption("게임 이름")

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "img")

배경 = pygame.image.load(os.path.join(image_path, "bgbg.png"))

stage = pygame.image.load(os.path.join(image_path, "st.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

char = pygame.image.load(os. path.join(image_path, "charr.png"))
char_size = char.get_rect().size
char_width = char_size[0]
char_height = char_size[1]
char_x_pos = (가로 / 2) - (char_width / 2)
char_y_pos = 세로 - char_height - stage_height

char_to_x = 0
char_speed = 5

weapon = pygame.image.load(os.path.join(image_path, "wp.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

weapons = []
weapon_speed = 10

ball_images = [
    pygame.image.load(os.path.join(image_path, "bl1.png")),
    pygame.image.load(os.path.join(image_path, "bl2.png")),
    pygame.image.load(os.path.join(image_path, "bl3.png")),
    pygame.image.load(os.path.join(image_path, "bl4.png"))]

ball_speed_y = [-18, -15, -12, -9]

balls = []

balls.append({
    "pos_x" : 50,
    "pos_y" : 50,
    "img_idx" : 0,
    "to_x" : 3,
    "to_y" : -6,
    "init_spd_y": ball_speed_y[0]})

weapon_to_remove = -1
ball_to_remove = -1

game_font = pygame.font.Font(None, 40)
total_time = 13
start_ticks = pygame.time.get_ticks()
game_result = "Game Over"

running = True
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                char_to_x -= char_speed
            elif event.key == pygame.K_RIGHT:
                char_to_x += char_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = char_x_pos + (char_width / 2) - (weapon_width / 2)
                weapon_y_pos = char_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                char_to_x = 0

    char_x_pos += char_to_x

    if char_x_pos < 0:
        char_x_pos = 0
    elif char_x_pos > 가로 - char_width:
        char_x_pos = 가로 - char_width

    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons]
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        if ball_pos_x < 0 or ball_pos_x > 가로 - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1

        if ball_pos_y >= 세로 - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else:
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

    char_rect = char.get_rect()
    char_rect.left = char_x_pos
    char_rect.top = char_y_pos

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y
        if char_rect.colliderect(ball_rect):
            running = False
            break

        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx
                ball_to_remove = ball_idx

                if ball_img_idx < 3:
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    small_ball_rect = ball_images[ball_img_idx].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]

                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2),
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2),
                        "img_idx" : ball_img_idx + 1,
                        "to_x" : -3,
                        "to_y" : -6,
                        "init_spd_y": ball_speed_y[ball_img_idx + 1]})
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2),
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2),
                        "img_idx" : ball_img_idx + 1 ,
                        "to_x" : 3,
                        "to_y" : -6,
                        "init_spd_y": ball_speed_y[ball_img_idx + 1]})
                break

    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1
    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    if len(balls) == 0:
        game_result = "Mission Complete"
        running = False

    화면.blit(배경, (0, 0))
    for weapon_x_pos, weapon_y_pos in weapons:
        화면.blit(weapon, (weapon_x_pos, weapon_y_pos))
    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        화면.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))
    화면.blit(stage, (0, 세로 - stage_height))
    화면.blit(char, (char_x_pos, char_y_pos))

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (255, 255, 255))
    화면.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0:
        game_result = "Time Over"
        running = False

    pygame.display.update()

msg = game_font.render(game_result, True, (255, 255, 0))
msg_rect = msg.get_rect(center=(int(가로 / 2), int(세로 / 2)))
화면.blit(msg, msg_rect)
pygame.display.update()

pygame.time.delay(2000)

pygame.quit()