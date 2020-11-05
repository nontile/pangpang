import pygame

pygame.init()

# FPS
clock = pygame.time.Clock()

# screen size set
screen_width = 480
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gam")
# 2
background = pygame.image.load("D:/workspaces/gam/background.png")
character = pygame.image.load("D:/workspaces/gam/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# coordinate to move
to_x = 0
to_y = 0
character_speed = 0.6

# enemy
enemy = pygame.image.load("D:/workspaces/gam/enemy.png")
enemy_size = character.get_rect().size
enemy_width = character_size[0]
enemy_height = character_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)

# define font
game_font = pygame.font.Font(None, 40)

# Total time
total_time = 10

start_ticks = pygame.time.get_ticks()


running = True
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                to_x += character_speed
            if event.key == pygame.K_UP:
                to_y -= character_speed
            if event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # 경과 시간
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    rest_time = int(total_time - elapsed_time)
    timer = game_font.render(str(rest_time), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    if rest_time < 1:
        print("경과")
        running = False

    pygame.display.update()  # repainting window


pygame.time.delay(2000)

pygame.quit()
