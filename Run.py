import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([700, 700])
pygame.display.set_caption("Pokemon Red - By James B")
pygame.display.set_icon(Logo)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()

    