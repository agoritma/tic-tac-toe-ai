from abc import ABC, abstractmethod

from tic_tac_toe.logic.models import GameState


class Renderer(ABC):
    @abstractmethod
    def render(self, game_state: GameState) -> None:
        """Render the current game state"""
