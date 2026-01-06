"""
Rock Paper Scissors Plus – AI Game Referee

This program runs a command-line Rock–Paper–Scissors–Plus game
where a user plays against an AI referee.

Game features:
- Best of 3 rounds
- One-time bomb move per player
- Clear rule enforcement and score tracking
"""

import random
from dataclasses import dataclass

# -------------------- Game State --------------------

@dataclass
class GameState:
    round: int = 1
    user_score: int = 0
    bot_score: int = 0
    user_bomb_used: bool = False
    bot_bomb_used: bool = False

# -------------------- Tools --------------------

def validate_move(move, is_user, state):
    valid_moves = {"rock", "paper", "scissors", "bomb"}

    if move not in valid_moves:
        return False, "Invalid move"

    if move == "bomb":
        if is_user and state.user_bomb_used:
            return False, "User bomb already used"
        if not is_user and state.bot_bomb_used:
            return False, "Bot bomb already used"

    return True, ""

def resolve_round(user_move, bot_move):
    if user_move == bot_move:
        return "draw"

    if user_move == "bomb" and bot_move != "bomb":
        return "user"
    if bot_move == "bomb" and user_move != "bomb":
        return "bot"

    wins = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    if wins[user_move] == bot_move:
        return "user"
    return "bot"

def update_game_state(state, winner, user_move, bot_move):
    if user_move == "bomb":
        state.user_bomb_used = True
    if bot_move == "bomb":
        state.bot_bomb_used = True

    if winner == "user":
        state.user_score += 1
    elif winner == "bot":
        state.bot_score += 1

    state.round += 1

# -------------------- Game Logic --------------------

def explain_rules():
    print("Rules:")
    print("• Best of 3 rounds")
    print("• Moves: rock, paper, scissors, bomb (once per game)")
    print("• Bomb beats everything | Bomb vs Bomb = draw")
    print("• Invalid input wastes the round\n")

def bot_choose(state):
    moves = ["rock", "paper", "scissors"]
    if not state.bot_bomb_used:
        moves.append("bomb")
    return random.choice(moves)

def run_game():
    state = GameState()
    explain_rules()

    while state.round <= 3:
        print(f"--- Round {state.round} ---")
        user_move = input("Your move: ").strip().lower()

        valid, reason = validate_move(user_move, True, state)
        bot_move = bot_choose(state)

        if not valid:
            print(f"Invalid input ({reason}). Round wasted.\n")
            state.round += 1
            continue

        winner = resolve_round(user_move, bot_move)
        update_game_state(state, winner, user_move, bot_move)

        print(f"You played: {user_move}")
        print(f"Bot played: {bot_move}")

        if winner == "draw":
            print("Result: Draw")
        else:
            print(f"Result: {winner.capitalize()} wins the round")

        print(f"Score → You: {state.user_score}, Bot: {state.bot_score}\n")

    print("=== Final Result ===")
    if state.user_score > state.bot_score:
        print("You win the game!")
    elif state.bot_score > state.user_score:
        print("Bot wins the game!")
    else:
        print("The game is a draw!")



run_game()
