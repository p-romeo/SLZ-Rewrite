from kivy.app import App
import random
from characters import Player, Enemy
from game_logic import GameLayout

class GameApp(App):
    def build(self):
        return GameLayout()

if __name__  == "__main__":
    GameApp().run()
class GameGUI:
    def update_display(self):
        self.player_health_label.config(text=self.Player.display_health())
        self.enemy_health_label.config(text=self.Enemy.display_health())