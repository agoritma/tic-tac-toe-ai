from tic_tac_toe.logic.models import Mark, Move
from tic_tac_toe.logic.models import GameState, Mark, Grid
from functools import partial


def find_best_move(game_sate: GameState) -> Move | None:
    maximizer: Mark = game_sate.current_mark
    bound_minimax = partial(minimax, maximizer=maximizer)
    return max(game_sate.possible_moves, key=bound_minimax)


def minimax(move: Move, maximizer: Mark, choose_highest_score: bool = False) -> int:
    if move.after_state.game_over:
        return move.after_state.evaluate_score(maximizer)
    return (max if choose_highest_score else min)(
        minimax(next_move, maximizer, not choose_highest_score)
        for next_move in move.after_state.possible_moves
    )


if __name__ == "__main__":

    def preview(cells: str) -> None:
        print(cells[:3], cells[3:6], cells[6:], sep="\n")

    game_state = GameState(Grid("XXO O X O"))
    for move in game_state.possible_moves:
        print("Score:", minimax(move, Mark("X")))
        preview(move.after_state.grid.cells)
        print("-" * 10)
