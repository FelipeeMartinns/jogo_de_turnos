import pygame

WHITE = (255, 255, 255)
GRAY = (30, 30, 30)
GREEN = (50, 200, 50)
RED = (200, 50, 50)


def shop_scene(screen, player, items):
    screen.fill(GRAY)

    font = pygame.font.SysFont(None, 32)

    title = font.render("LOJA", True, WHITE)
    coins = font.render(f"Coins: {player.coins}", True, WHITE)

    sword = font.render("1 - Espada (+5 AD) - 10 coins", True, WHITE)
    staff = font.render("2 - Cajado (+5 AP) - 10 coins", True, WHITE)
    armor = font.render("3 - Armadura (+2 AD / +2 AP) - 5 coins", True, WHITE)
    back = font.render("ESC - Voltar", True, WHITE)

    screen.blit(title, (360, 80))
    screen.blit(coins, (50, 50))
    screen.blit(sword, (200, 200))
    screen.blit(staff, (200, 250))
    screen.blit(armor, (200, 300))
    screen.blit(back, (200, 380))
