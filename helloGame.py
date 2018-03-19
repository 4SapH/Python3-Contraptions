import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()

is_blue = True
x, y = 30, 30
width, height = 30, 30


while not done:
    screen.fill((0, 0, 0))
    if is_blue: color = (0, 128, 255)
    else: color = (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, x+width, y+height))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
        if event.type == pygame.QUIT or \
           (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = True
    x, y = x+1, y+1
    pygame.display.flip()
    clock.tick(60)
