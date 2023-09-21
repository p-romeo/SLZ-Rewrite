from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import random

class Character:
    def __init__(self, initial_health=100):
        self.health = initial_health
        self.has_gun = False

    def decrease_health(self, amount):
        """Decrease the character's health by an amount"""
        self.health -= amount
        self.health = max(0, self.health)  # prevents health from going below 0

    def increase_health(self, amount):
        self.health += amount  # increases health by amount
        self.health = min(100, self.health)

    def display_health(self):
        return f"Character's health: {self.health}"

    def attack(self, target):
        damage = random.randint(5,15)
        target.decrease_health(damage)
        return damage

class Player(Character):
    def __init__(self, initial_health=100):
        super().__init__(initial_health)
        self.broken_legs = False
        self.inventory = []

    def break_legs(self):
        self.broken_legs = True

    def heal_legs(self):
        self.broken_legs = False

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def has_item(self, item):
        return item in self.inventory

    def open_door(self):
        if self.has_item("key"):
            messagebox.showinfo("Congrats", "You Opened a Door")
        else:
            messagebox.showinfo("Oops!", "You need a key to do that!")

    def get_key(self):
        self.add_to_inventory("key")

    def pickup_gun(self):
        self.has_gun = True
        self.add_to_inventory("gun")

class Enemy(Character):
    def __init__(self, initial_health=100):
        super().__init__(initial_health)
        self.is_stunned = False

    def pickup_gun(self):
        self.has_gun = True

    def stun(self):
        self.is_stunned = True

    def stun_recovery(self):
        self.is_stunned = False

class GameLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        #Display player and enemy health
        self.player_health_label = Label(text="Player's Health: 100")
        self.enemy_health_label = Label(text="Enemy's Health: 100")

        #Add some labels
        self.add_widget(self.player_health_label)
        self.add_widget(self.enemy_health_label)

        #Create buttons
        self.button1 = Button(text="Attack Enemy", size_hint=(1,0.2))
        self.button2 = Button(text="Heal Player", size_hint=(1,0.2))
        self.button3 = Button(text="Next Room", size_hint=(1,0.2))

        #Load buttons to GUI
        self.add_widget(self.button1)
        self.add_widget(self.button2)
        self.add_widget(self.button3)

        #Create instances of player and enemy
        self.player = Player()
        self.enemy = Enemy()

        #bind the attack button
        self.button1.on_press = self.attack_enemy

    def update_display(self):
        self.player_health_label.text = f"Player's Health {self.player.health}"
        self.enemy_health_label.text = f"Enemy's Health {self.enemy.health}"

    def attack_enemy(self, *args):
        damage_dealt = self.player.attack(self.enemy)
        self.player.attack(self.enemy)
        self.display_popup(f"You dealt {damage_dealt} damage to the enemy!")
        self.update_display()


    def display_popup(self, message):
        popup = Popup(title='Game Feedback',content=Label(text=message),size_hint=(0.6,0.3))
        popup.open()




class GameApp(App):
    def build(self):
        return GameLayout()

if __name__  == "__main__":
    GameApp().run()
class GameGUI:
    def update_display(self):
        self.player_health_label.config(text=self.Player.display_health())
        self.enemy_health_label.config(text=self.Enemy.display_health())




'''class Game:
    def __init__(self):
        # init game window
        self.open_door_button = None
        self.turn_around_button = None
        self.next_room_button = None
        self.drink_button = None
        self.leave_button = None
        self.image_label = None
        self.potion_image = None
        self.master = tk.Tk()
        self.master.title("SLZ - The Game")

        # init players
        self.player = Player()
        self.enemy = Enemy()

        # build gui
        self.player_health_label = tk.Label(self.master, text=self.player.display_health())
        self.enemy_health_label = tk.Label(self.master, text=self.enemy.display_health())

        # pack gui for display
        self.player_health_label.pack(pady=10)
        self.enemy_health_label.pack(pady=10)

        # placeholder button - to be replaced later for progression
        self.button1 = tk.Button(self.master, text="Attack Enemy", command=self.attack_enemy)
        self.button2 = tk.Button(self.master, text="Heal Player", command=self.heal_player)

        self.button1.pack(pady=10)
        self.button2.pack(pady=10)

        # add button to start potion encounter
        self.button3 = tk.Button(self.master, text="Inspect Potion", command=self.potion_encounter)
        self.button3.pack(pady=10)

    def attack_enemy(self):
        damage = random.randint(5, 15)
        self.enemy.decrease_health(damage)
        GameGUI.update_display()


    def heal_player(self):
        heal = random.randint(10, 20)
        self.player.increase_health(heal)
        GameGUI.update_display()

    def potion_encounter(self):

        # remove old buttons
        # presents options
        self.button1.config(text="Drink Potion", command=self.drink_potion)
        self.button2.config(text="Take Potion", command=self.take_potion)

        # displays potion image
        image = Image.open('potion.jpg')
        self.potion_image = ImageTk.PhotoImage(image)
        self.image_label = tk.Label(self.master, image=self.potion_image)
        self.image_label.pack(pady=10)

    def drink_potion(self):
        # drinks the potion, random effects
        effect = random.choice(["heal", "harm"])
        if effect == "heal":
            heal_amount = random.randint(10, 20)
            self.player.increase_health(heal_amount)
            GameGUI.update_display()
            self.player_health_label.config(text=f"You drank the potion and restored {heal_amount} health!")
        if effect == "harm":
            damage_amount = random.randint(5, 25)
            self.player.decrease_health(damage_amount)
            GameGUI.update_display()
            self.enemy_health_label.config(text=f"You drank the potion and took {damage_amount} points of damage!")

    def take_potion(self):

        self.player.add_to_inventory("Potion")
        # player takes potion, added to inventory
        self.image_label.pack_forget()
        # potion image is removed

        # reset the buttons
        self.button1.config(text="Attack Enemy", command=self.attack_enemy)
        self.button2.config(text="Heal Player", command=self.heal_player)
        self.button3.config(text="Next Room", command=self.door_encounter)

        messagebox.showinfo("Inventory", f"You now have {self.player.inventory} in your inventory.")

    def door_encounter(self):

        # present door options
        self.button1.config(text="Try to Open Door", command=self.try_door)
        self.button2.config(text="Kick the door", command=lambda: self.player.decrease_health(random.randint(1, 6)))

    def try_door(self):
        self.player.open_door()


game = Game()
game.master.mainloop()'''