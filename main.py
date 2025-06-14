import random
import copy
from dbmanagement import *
from graphics import *

def is_over(piles):
    for p in piles:
        if p != 0:
            return False
    return True

def valid_moves(piles):
    moves = []
    for i, count in enumerate(piles):
        for k in range(1, count + 1):
            moves.append((i, k))
    return moves

def apply_move(piles, move):
    pile_idx, remove_count = move
    piles[pile_idx] -= remove_count

def minimax(piles, human_turn):
    if is_over(piles):
        return (+1 if human_turn else -1), None
    if human_turn:
        best_score, best_move = +float('inf'), None
    else:
        best_score, best_move = -float('inf'), None

    for move in valid_moves(piles):
        new_p = piles.copy()
        apply_move(new_p, move)
        score, _ = minimax(new_p, not human_turn)
        if human_turn:
            if score < best_score:
                best_score, best_move = score, move
        else:
            if score > best_score:
                best_score, best_move = score, move
        if best_score == (+1 if not human_turn else -1):
            break

    return best_score, best_move

def compute_ai_move(piles,difficulty = 'easy'):
    if difficulty == 'easy':
        return random.choice(valid_moves(piles))

    if difficulty == 'medium':
        if random.random() < 0.5:
            return random.choice(valid_moves(piles))

    _, mv = minimax(piles, human_turn=False)
    return mv




def main():
    mode = draw_menu_selection()
    if mode == 'Resume Last Game':
        loaded = load_last_unfinished()
        if loaded:
            p1_type, p2_type, current_player, piles = loaded
        else:
            mode = draw_new_game_selection(True)
            if mode == 'H VS AI':
                loaded = None
                p1_type = 'Human'
                p2_type = 'AI'
                DIFFICULTY = draw_difficulty_selection()
            elif mode == 'H VS H':
                loaded = None
                p1_type = 'Human'
                p2_type = 'Human'
            current_player = 1 if random.choice([True, False]) else 2
            piles = [1, 3, 5, 7]
    else:
        mode = draw_new_game_selection()
        if mode == 'H VS AI':
            loaded = None
            p1_type = 'Human'
            p2_type = 'AI'
            DIFFICULTY = draw_difficulty_selection()
        else:
            loaded = None
            p1_type = 'Human'
            p2_type = 'Human'
        current_player = 1 if random.choice([True, False]) else 2
        piles = [1, 3, 5, 7]
    selected_pile = None

    running = True
    while running:
        clickable = draw_piles(piles, selected_pile)

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False

            elif ev.type == pygame.MOUSEBUTTONDOWN:
                if (p1_type == 'Human' and current_player == 1) or (p2_type == 'Human' and current_player == 2) and not is_over(piles):
                    for rect, move in clickable:
                        if rect.collidepoint(ev.pos):
                            apply_move(piles, move)
                            selected_pile = None
                            current_player = 1 if current_player == 2 else 2
                            save_unfinished_game(p1_type, p2_type, current_player, piles)
                            break

        if (p1_type == 'AI' and current_player == 1) or (p2_type == 'AI' and current_player == 2) and not is_over(piles):
            move = compute_ai_move(piles, DIFFICULTY if (p2_type == 'AI' or p1_type == 'AI') else 'easy')
            apply_move(piles, move)
            current_player = 1 if current_player == 2 else 2
            save_unfinished_game(p1_type, p2_type, current_player, piles)

        if is_over(piles):
            winner = "player 1" if current_player == 2 else "player 2"
            print(f"\nGame over! {winner} wins!")
            running = False
            save_finished_game(p1_type, p2_type, 1 if winner == "player 1" else 2)
            clear_saved_games()

    pygame.quit()
    clear_finished_games()


if __name__ == "__main__":
    main()
