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


running = True
while running:
    dt = clock.tick(30)

    # 2.이벤트 처리(키보드 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3.캐릭터 위치정의

    # 4. 충돌처리

    # 5. 화면 그리기

    pygame.display.update()  # repainting window


pygame.time.delay(2000)

pygame.quit()
