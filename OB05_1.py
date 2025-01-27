# пинг-понг для 2 игроков

import pygame as p
import random

p.init()

def reset_ball (player):
    if player == 2:
        image_rect.x = 890
        image_rect.y = right_rect_y + 50
    elif player == 1:
        image_rect.x = 60
        image_rect.y = left_rect_y + 50


def move_ball():
    global ball_speed_x, ball_speed_y
    image_rect.x += ball_speed_x
    image_rect.y += ball_speed_y
    global left_score
    global right_score
    global ball_active
    global player_move

    if image_rect.top <= 0 or image_rect.bottom >= windows_size[1]:
        ball_speed_y = -ball_speed_y

    if image_rect.colliderect(left_rect) or image_rect.colliderect(right_rect):
        ball_speed_x = -ball_speed_x

    if image_rect.left <= 0:
        right_score += 1
        ball_active = False
        player_move = 2
        reset_ball(player_move)
    elif image_rect.right >= windows_size[0]:
        left_score += 1
        ball_active = False
        player_move = 1
        reset_ball(player_move)

windows_size = (1000, 600)
screen = p.display.set_mode(windows_size)
p.display.set_caption("Пинг-понг для 2 игроков")

image = p.image.load("ping_pong_ball.png")
image_rect = image.get_rect()

speed = 5
ball_speed_x = 5
ball_speed_y = 3

left_rect_x = 50
left_rect_y = 100
left_rect_width = 10
left_rect_height = 150
left_rect = p.Rect(left_rect_x, left_rect_y, left_rect_width, left_rect_height)
color = (255, 255, 255)

right_rect_x = 940
right_rect_y = 100
right_rect_width = 10
right_rect_height = 150
right_rect = p.Rect(right_rect_x, right_rect_y, right_rect_width, right_rect_height)

ball_active = False
player_move = random.randint(1,2)
reset_ball(player_move)
left_score = 0
right_score = 0


run = True
while run:
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
    if ball_active:
        move_ball()

    keys = p.key.get_pressed()
    if keys[p.K_UP] and left_rect_y > 0:
        left_rect_y -= speed
        left_rect = p.Rect(left_rect_x, left_rect_y, left_rect_width, left_rect_height)
        if ball_active == False and player_move == 1:
            image_rect.x = left_rect_x + 10
            image_rect.y = left_rect.y + 50
            reset_ball(player_move)
    elif keys[p.K_DOWN] and left_rect_y < 450:
        left_rect_y += speed
        left_rect = p.Rect(left_rect_x, left_rect_y, left_rect_width, left_rect_height)
        if ball_active == False and player_move == 1:
            image_rect.x = left_rect_x + 10
            image_rect.y = left_rect.y + 50
            reset_ball(player_move)



    if event.type == p.MOUSEMOTION:
        mouseX, mouseY = p.mouse.get_pos()
        mouseX = 940
        new_mouse_y = mouseY

        if mouseY < 0:
            mouseY = 0
        elif mouseY > 450:
            new_mouse_y = 450

        right_rect_x = 940
        right_rect_y = new_mouse_y
        right_rect = p.Rect(right_rect_x, right_rect_y, right_rect_width, right_rect_height)
        if ball_active == False and player_move == 2:
            image_rect.x = right_rect_x - 50
            image_rect.y = right_rect.y + 50
        elif ball_active == False and player_move == 1:
            image_rect.x = left_rect_x + 10
            image_rect.y = left_rect.y + 50



    key1 = p.key.get_pressed()
    if key1[p.K_SPACE] and player_move == 1:
        ball_active = True
    elif p.mouse.get_pressed()[0] and player_move == 2:
        ball_active = True

    screen.fill((0,0,0))
    screen.blit(image, image_rect)
    p.draw.rect(screen, color, left_rect)
    p.draw.rect(screen, color, right_rect)

    font = p.font.Font(None, 74)
    left_score_text = font.render(str(left_score), True, color)
    right_score_text = font.render(str(right_score), True, color)
    screen.blit(left_score_text, (250, 10))
    screen.blit(right_score_text, (730, 10))

    p.display.flip()
p.quit()