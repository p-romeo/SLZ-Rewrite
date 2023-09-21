import random
import tkinter as tk
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk


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

class Game:
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

    def game_loop(self):
        self.update_display()

    def attack_enemy(self):
        damage = random.randint(5, 15)
        self.enemy.decrease_health(damage)
        self.update_display()

    def heal_player(self):
        heal = random.randint(10, 20)
        self.player.increase_health(heal)
        self.update_display()

    def update_display(self):
        self.player_health_label.config(text=self.player.display_health())
        self.enemy_health_label.config(text=self.enemy.display_health())

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
            self.update_display()
            self.player_health_label.config(text=f"You drank the potion and restored {heal_amount} health!")
        if effect == "harm":
            damage_amount = random.randint(5, 25)
            self.player.decrease_health(damage_amount)
            self.update_display()
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
game.master.mainloop()