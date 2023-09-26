import random
import game_logic


class Character:
    def __init__(self, initial_health):
        self.broken_legs_damage = None
        self.broken_legs = None
        self.health = None
        self.has_gun = None

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
        damage = random.randint(5, 15)
        target.decrease_health(damage)
        return damage

    def heal(self, target):
        restored = random.randint(1, 10)
        target.increase_health(restored)
        return restored

    def fix_legs(self, broken_legs):
        self.broken_legs = False
        game_logic.GameLayout.display_popup("Awesome you fixed your legs, unfortunately that is all you fixed.")

    def break_legs(self, broken_legs):
        self.broken_legs = True
        self.broken_legs_damage = 0.5 * self.health
        self.health = self.health - self.broken_legs_damage
        game_logic.GameLayout.display_popup(
            f"Oops! You just broke your legs and lost {self.broken_legs_damage} health. "
            f"Nice job.")


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
