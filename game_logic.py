from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from characters import Player, Enemy
from rooms import StartingRoom


class GameLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Display player and enemy health
        self.player_health_label = Label(text="Player's Health: 100")
        self.enemy_health_label = Label(text="Enemy's Health: 100")

        # Add some labels
        self.add_widget(self.player_health_label)
        self.add_widget(self.enemy_health_label)

        # Create buttons
        self.button1 = Button(text="Attack Enemy", size_hint=(1, 0.2))
        self.button2 = Button(text="Heal Player", size_hint=(1, 0.2))
        self.button3 = Button(text="Next Room", size_hint=(1, 0.2))

        # Load buttons to GUI
        self.add_widget(self.button1)
        self.add_widget(self.button2)
        self.add_widget(self.button3)

        # Create instances of player and enemy
        self.player = Player()
        self.enemy = Enemy()

        # bind the attack button
        self.button1.on_press = self.attack_enemy
        self.button2.on_press = self.heal_player
        #self.button3.on_press = self.next_room

    def update_display(self):
        self.player_health_label.text = f"Player's Health {self.player.health}"
        self.enemy_health_label.text = f"Enemy's Health {self.enemy.health}"

    def attack_enemy(self):
        damage_dealt = self.player.attack(self.enemy)
        self.player.attack(self.enemy)
        self.display_popup(f"You dealt {damage_dealt} damage to the enemy!")
        self.update_display()

    def heal_player(self):
        health_restored = self.player.heal(self.player)
        self.player.heal(self.player)
        self.display_popup(f"You healed {health_restored} health!")
        self.update_display()

    # noinspection PyMethodMayBeStatic
    def display_popup(self, message):
        popup = Popup(title='Game Feedback', content=Label(text=message), size_hint=(0.6, 0.3))
        popup.open()

    #def next_room(self):
