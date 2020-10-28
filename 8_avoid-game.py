import random
import pygame
###################################################################
# 1.기본설정

# Initialize
pygame.init()

# screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Title
pygame.display.set_caption("Gam")

# FPS
clock = pygame.time.Clock()
###################################################################

# 캐릭터
background = pygame.image.load("D:/workspaces/gam/background.png")
character = pygame.image.load("D:/workspaces/gam/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

enemy = pygame.image.load("D:/workspaces/gam/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0

to_x = 0
to_y = 0
character_speed = 10

running = True
while running:
    dt = clock.tick(30)

    # 2.이벤트 처리(키보드 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3.캐릭터 위치정의
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_LEFT:
                to_x -= character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                to_x = 0

    character_x_pos += to_x
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += 10
    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    # 4. 충돌처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print(f"character_left:{character_rect.left}, character_top:{character_rect.top}")
        print(f"enemy_left:{enemy_rect.left}, enemy_top:{enemy_rect.top}")
        print("충돌 했습니다.")
        running = False

    # 5. 화면 그리기
    screen.blit(background, (0, 0))

    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update()  # repainting window


pygame.time.delay(1000)

pygame.quit()
