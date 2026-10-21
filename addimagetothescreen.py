import pygame

pygame.init()

screen_width, screen_length = 500, 500

display_surface = pygame.display.set_mode((screen_width, screen_length))

pygame.display.set_caption('The rainbow tiger in the cosmos')
bg = pygame.transform.scale(pygame.image.load('space.jpg').convert(), (screen_width,screen_length))

tyger = pygame.transform.scale(pygame.image.load('rainbowtiger.png').convert_alpha(), (200,200))

window = tyger.get_rect(center = (screen_width // 2,screen_length // 2 - 30))

text = pygame.font.Font(None,36).render('Tyger', True, pygame.Color('White'))

text_rect = text.get_rect(center = (screen_width // 2, screen_length // 2 + 110))

def gameloop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False

        display_surface.blit(bg, (0,0))
        display_surface.blit(tyger, window)
        display_surface.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    gameloop()