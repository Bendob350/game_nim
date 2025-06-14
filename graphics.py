import pygame

pygame.init()
W, H = 800, 400
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Nim Game")


def draw_piles(piles, selected_pile=None):
    screen.fill((240, 240, 240))
    pile_h = H // len(piles)
    stick_w = 20
    clickable = []

    for i, count in enumerate(piles):
        y0 = i * pile_h
        total_width = count * stick_w
        x_start = (W - total_width) // 2
        for j in range(count):
            x = x_start + j * stick_w
            y = y0 + (pile_h - (pile_h // 2)) // 2
            rect = pygame.Rect(x, y + 7, stick_w - 4, pile_h // 2)
            color = (200, 50, 50)
            pygame.draw.rect(screen, color, rect)
            clickable.append((rect, (i, j + 1)))

    pygame.display.flip()
    return clickable