from tic_tac_toe.game.engine import TicTacToe
from tic_tac_toe.logic.models import Mark

from .args import parse_args
from .renderers import ConsoleRenderer


def main() -> None:
    player1, player2 = parse_args()
    TicTacToe(player1, player2, ConsoleRenderer()).play()
