import pygame

# cores
WHITE = (255, 255, 255)
GRAY = (30, 30, 30)


def menu_scene(screen):
    screen.fill(GRAY)

    font_title = pygame.font.SysFont(None, 64)
    font_menu = pygame.font.SysFont(None, 36)

    title = font_title.render("MEU RPG", True, WHITE)

    start = font_menu.render("ENTER - Iniciar Combate", True, WHITE)
    shop = font_menu.render("S - Loja", True, WHITE)
    quit_game = font_menu.render("ESC - Sair", True, WHITE)

    screen.blit(title, (280, 160))
    screen.blit(start, (260, 300))
    screen.blit(shop, (260, 350))
    screen.blit(quit_game, (260, 400))
