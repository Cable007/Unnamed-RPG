import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Character Movement")

clock = pygame.time.Clock()

x, y = 400, 400
speed = .25
size = 40
vx = 0
vy = 0
dx = 0
dy = 0

running = True
while running:
    # clock.tick(60)
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed() 

    if keys[pygame.K_LEFT]:
        vx = -speed
    elif keys[pygame.K_RIGHT]:
        vx = +speed
    else:
        vx *= 0.7
    
    if keys[pygame.K_UP]:
        vy = -speed
    elif keys[pygame.K_DOWN]:
        vy = speed
    else:
        vy *= 0.7
        
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= speed
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += speed
    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= speed
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += speed

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        dx -= 1
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        dx += 1
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        dy -= 1
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        dy += 1

    # if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
    #     y *= speed  

    x += vx * dt
    y += vy * dt
    x = max(0, min(WIDTH - size, x))
    y = max(0, min(HEIGHT - size, y))



    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (0, 150, 255), (x, y, size, size))
    pygame.display.flip()

pygame.quit()