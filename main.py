from kivy.app import App
from characters import Player, Enemy
from game_logic import GameLayout

class GameApp(App):
    def build(self):
        return GameLayout()

if __name__ == "__main__":
    GameApp().run()