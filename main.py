import random
import copy

def is_over(piles):
    return all(p == 0 for p in piles)

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
        new_piles = piles.copy()
        apply_move(new_piles, move)
        score, _ = minimax(new_piles, not human_turn)

        if human_turn:
            if score < best_score:
                best_score, best_move = score, move
        else:
            if score > best_score:
                best_score, best_move = score, move

        if best_score == (+1 if not human_turn else -1):
            break

    return best_score, best_move

def compute_ai_move(piles):
    _, move = minimax(piles, human_turn=False)
    return move
def play_console(initial_piles):
    piles = initial_piles.copy()
    human_player = random.choice([True, False])

    while not is_over(piles):
        print("\nPiles:", piles)
        if human_player: # Human turn
            try:
                pile = int(input(f"Choose a pile (1–{len(piles)}): "))
                count = int(input(f"How many to remove from pile {pile}? "))
                move = (pile - 1, count)
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                move = None
                continue
        else:# AI turn
            move = compute_ai_move(piles)
            print(f"AI removes {move[1]} from pile {move[0]+1}")
        
        if move in valid_moves(piles):
            apply_move(piles, move)
            human_player = not human_player
        else:
            print("Invalid move—try again.")

    winner = "Human" if not human_player else "AI"
    print(f"\nGame over! {winner} wins!")

if __name__ == "__main__":
    play_console([1, 3, 5, 7])
