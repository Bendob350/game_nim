import pygame

pygame.init()
W, H = 800, 400
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Nim Game")
font = pygame.font.SysFont(None, 48)


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

def draw_difficulty_selection():
    btn_w, btn_h = 200, 60
    spacing = 20
    total_h = 3 * btn_h + 2 * spacing
    start_y = (H - total_h) // 2

    buttons = []
    labels = ['easy', 'medium', 'hard']
    for i, label in enumerate(labels):
        rect = pygame.Rect(
            (W - btn_w)//2,
            start_y + i*(btn_h + spacing),
            btn_w, btn_h
        )
        buttons.append((rect, label))

    while True:
        screen.fill((30, 30, 30))
        for rect, label in buttons:
            pygame.draw.rect(screen, (70,70,200), rect, border_radius=8)
            txt = font.render(label.capitalize(), True, (255,255,255))
            txt_r = txt.get_rect(center=rect.center)
            screen.blit(txt, txt_r)

        pygame.display.flip()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                for rect, label in buttons:
                    if rect.collidepoint(ev.pos):
                        return label  # exit menu
                    
def draw_menu_selection():
    btn_w, btn_h = 500, 100
    spacing = 40
    total_h = 3 * btn_h + 2 * spacing
    start_y = (H - total_h) // 2 + spacing
    start_x = (W - btn_w) // 2

    buttons = []
    labels = ['New Game', 'Resume Last Game']
    for i, label in enumerate(labels):
        rect = pygame.Rect(
            start_x,
            start_y + i*(btn_h + spacing),
            btn_w, btn_h
        )
        buttons.append((rect, label))

    while True:
        screen.fill((30, 30, 30))
        for rect, label in buttons:
            pygame.draw.rect(screen, (70,70,200), rect, border_radius=8)
            txt = font.render(label, True, (255,255,255))
            txt_r = txt.get_rect(center=rect.center)
            screen.blit(txt, txt_r)

        pygame.display.flip()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                for rect, label in buttons:
                    if rect.collidepoint(ev.pos):
                        return label  # exit menu

def draw_new_game_selection(tried_loading_game=False):
    btn_w, btn_h = 500, 100
    spacing = 40
    total_h = 2 * btn_h + spacing
    start_y = (H - total_h) // 2 + spacing
    start_x = (W - btn_w) // 2

    buttons = []
    labels = ['H VS AI', 'H VS H']
    for i, label in enumerate(labels):
        rect = pygame.Rect(
            start_x,
            start_y + i*(btn_h + spacing),
            btn_w, btn_h
        )
        buttons.append((rect, label))

    while True:
        screen.fill((30, 30, 30))
        for rect, label in buttons:
            pygame.draw.rect(screen, (70,70,200), rect, border_radius=8)
            txt = font.render(label, True, (255,255,255))
            txt_r = txt.get_rect(center=rect.center)
            screen.blit(txt, txt_r)

        if tried_loading_game:
            txt = font.render("No saved game found!", True, (255, 0, 0))
            txt_r = txt.get_rect(center=(W // 2, 0.2 * H))
            screen.blit(txt, txt_r)

        pygame.display.flip()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                for rect, label in buttons:
                    if rect.collidepoint(ev.pos):
                        return label  # exit menu