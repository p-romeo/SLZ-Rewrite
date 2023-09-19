import random
import tkinter as tk
from PIL import Image, ImageTk


class Player:
    def __init__(self, initial_health=100):
        self.health = initial_health
        self.has_gun = False
        self.broken_legs = False
        self.inventory = []

    def decrease_health(self, amount):
        """Decrease the players health by an amount"""
        self.health -= amount
        self.health = max(0, self.health)  # prevents health from going below 0

    def increase_health(self, amount):
        self.health += amount  # increases health by amount
        self.health = min(100, self.health)

    def display_health(self):
        return f"Players health: {self.health}"

    def pickup_gun(self):
        self.has_gun = True

    def break_legs(self):
        self.broken_legs = True

    def heal_legs(self):
        self.broken_legs = False

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def has_item(self, item):
        return item in self.inventory

    def open_door(self):
        #placeholder
        pass



class Enemy:
    def __init__(self, initial_health=100):
        self.health = initial_health
        self.has_gun = False
        self.is_stunned = False

    def decrease_health(self, amount):
        self.health -= amount
        self.health = max(0, self.health)

    def increase_health(self, amount):
        self.health += amount
        self.health = min(100, self.health)

    def display_health(self):
        return f"Enemy's Health: {self.health}"

    def pickup_gun(self):
        self.has_gun = True

    def stun(self):
        self.is_stunned = True

    def stun_recovery(self):
        self.is_stunned = False


class Game:
    def __init__(self):
        # init game window
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
        self.attack_button = tk.Button(self.master, text="Attack Enemy", command=self.attack_enemy)
        self.heal_button = tk.Button(self.master, text="Heal Player", command=self.heal_player)

        self.attack_button.pack(pady=10)
        self.heal_button.pack(pady=10)

        # add button to start potion encounter
        self.potion_button = tk.Button(self.master, text="Inspect Potion", command=self.potion_encounter)
        self.potion_button.pack(pady=10)

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
        self.heal_button.pack_forget()
        self.attack_button.pack_forget()
        self.potion_button.pack_forget()

        # presents options
        self.drink_button = tk.Button(self.master, text="Drink Potion", command=self.drink_potion, width=20, height=10)
        self.leave_button = tk.Button(self.master, text="Leave Potion", command=self.leave_potion, width=20, height=10)

        self.drink_button.pack(pady=10)
        self.leave_button.pack(pady=10)

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

    def leave_potion(self):

        # player leaves the potion, boring fucks
        self.image_label.pack_forget()
        self.leave_button.pack_forget()
        self.drink_button.pack_forget()
        self.player_health_label.config(text="You Left the Potion")
        # reset the buttons
        self.attack_button.config(text="Attack Enemy", command=self.attack_enemy)
        self.heal_button.config(text="Heal Player", command=self.heal_player)

        self.attack_button.pack(pady=10)
        self.heal_button.pack(pady=10)
        self.potion_button.pack(pady=10)


game = Game()
game.master.mainloop()

'''
master = tk.Tk()
tex = tk.Text(master=master)
tex.pack(side=tk.RIGHT)
global path
path = 0
str1 = "Open the door"
str2 = "Walk away"
gun = False
global photo
canvas = tk.Canvas(master, bg='white', width=1, height=1)
global health
global otherHealth
health = 100
otherHealth = 100


def win():
    canvas.delete(l.background)
    l.background = PhotoImage(file='./win.gif')
    l.create_image(100, 100, image=l.background, anchor='nw')
    canvas.pack(side=tk.TOP)
    b.config(text="You won!")
    b.config(command=lost)
    c.config(text="You won!")
    c.config(command=lost)
    d.config(text="You won!")
    d.config(command=lost)
    master.update()


def fight():
    canvas.delete(l.background)
    l.background = PhotoImage(file='./sh.gif')
    l.create_image(100, 100, image=l.background, anchor='nw')
    canvas.pack(side=tk.TOP)
    global health
    global otherHealth
    while health > 0 and otherHealth > 0:
        b.config(text="Stab him")
        b.config(command=stab)
        c.config(text="Shoot him")
        c.config(command=shoot)
        d.config(text="Strangle him")
        d.config(command=strangle)
        d.pack()
        master.update()
        if health < 0:
            tex.insert(tk.END, "You have fallen victim to actual cannibal Shia LaBeouf!")
            away()
            break
            master.destroy()
        elif otherHealth < 0:
            tex.insert(tk.END, "You have won! Congrats!")
            win()
            break
            master.destroy()


def shoot():
    global health
    global otherHealth
    chance = random.randint(10, 30)
    otherHealth = otherHealth - chance
    chance2 = random.randint(0, 10)
    health = health - chance2
    int(health)
    tex.insert(tk.END, "You shot Shai Lebouf and dealt ")
    tex.insert(tk.END, chance)
    tex.insert(tk.END, " damage!\nYou have taken ")
    tex.insert(tk.END, chance2)
    tex.insert(tk.END, " damage from Shai Lebouf!")
    tex.insert(tk.END, "You have ")
    tex.insert(tk.END, health)
    tex.insert(tk.END, “ health
    remaining.\n”)
    tex.insert(tk.END, "Shai Lebouf has ")
    tex.insert(tk.END, otherHealth)
    tex.insert(tk.END, “ health
    remaining.\n”)

    def stab():
        global health
        global otherHealth
        chance = random.randint(10, 20)
        otherHealth = otherHealth - chance
        chance2 = random.randint(10, 30)
        health = health - chance2
        int(health)
        tex.insert(tk.END, "You stabbed Shai Lebouf and dealt ")
        tex.insert(tk.END, chance)
        tex.insert(tk.END, " damage!\nYou have taken ")
        tex.insert(tk.END, chance2)
        tex.insert(tk.END, " damage from Shia Lebouf!")
        tex.insert(tk.END, "You have ")
        tex.insert(tk.END, health)
        tex.insert(tk.END, “ health
        remaining.\n”)
        tex.insert(tk.END, "Shai Lebouf has ")
        tex.insert(tk.END, otherHealth)
        tex.insert(tk.END, “ health
        remaining.\n”)

        def strangle():
            global health
            global otherHealth
            chance = random.randint(10, 20)
            otherHealth = otherHealth - chance
            chance2 = random.randint(10, 40)
            health = health - chance2
            int(health)
            tex.insert(tk.END, "You strangle Shia Lebouf and deal")
            tex.insert(tk.END, chance)
            tex.insert(tk.END, " damage to him!\nYou have taken ")
            tex.insert(tk.END, chance2)
            tex.insert(tk.END, " damage from Shai Lebouf!")
            tex.insert(tk.END, "You have ")
            tex.insert(tk.END, health)
            tex.insert(tk.END, “ health
            remaining.\n”)
            tex.insert(tk.END, "Shai Lebouf has ")
            tex.insert(tk.END, otherHealth)
            tex.insert(tk.END, “ health
            remaining.\n”)

            def lost():
                master.destroy()

            def window2():
                canvas.delete(l.background)
                l.background = PhotoImage(file='./window.gif')
                l.create_image(100, 100, image=l.background, anchor='nw')
                canvas.pack(side=tk.TOP)
                tex.insert(tk.END, "You take the gun. \n")
                tex.see(tk.END)
                b.config(text="Use the gun to shoot the lock on the window and go through.")
                b.config(command=fight)
                c.config(text="Walk away")
                c.config(command=away)
                master.update()

            def fridge():
                canvas.delete(l.background)
                l.background = PhotoImage(file='./gun.gif')
                l.create_image(100, 100, image=l.background, anchor='nw')
                canvas.pack(side=tk.TOP)
                tex.insert(tk.END, "You found a gun in the fridge. \n")
                tex.see(tk.END)
                b.config(text="Take gun")
                b.config(command=window2)
                c.config(text="Leave the gun")
                c.config(command=door)
                master.update()

            def window():
                canvas.delete(l.background)
                l.background = PhotoImage(file='./blood.gif')
                l.create_image(100, 100, image=l.background, anchor='nw')
                canvas.pack(side=tk.TOP)
                tex.insert(tk.END, "You try to climb through the window but slip and fall onto glass shards. \n")
                tex.see(tk.END)
                b.config(text="Try to stop the bleeding")
                b.config(command=away)
                c.config(text="Lie there and regret life")
                c.config(command=away)
                master.update()

            def door():
                canvas.delete(l.background)
                l.background = PhotoImage(file='./fridge.gif')
                l.create_image(100, 100, image=l.background, anchor='nw')
                canvas.pack(side=tk.TOP)
                tex.insert(tk.END, "You go to the kitchen. \n")
                tex.see(tk.END)
                b.config(text="Go through the window")
                b.config(command=window)
                c.config(text="Open the fridge")
                c.config(command=fridge)
                master.update()

            def away():
                canvas.delete(l.background)
                l.background = PhotoImage(file='./youdied.gif')
                l.create_image(100, 100, image=l.background, anchor='nw')
                canvas.pack(side=tk.TOP)
                tex.insert(tk.END, "You have died! \n")
                tex.see(tk.END)
                b.config(text="You lost")
                b.config(command=lost)
                c.config(text="You lost")
                c.config(command=lost)
                d.config(text="You lost")
                d.config(command=lost)
                master.update()

            b = Button(master, text=str1, command=door)
            c = Button(master, text=str2, command=away)
            d = Button(master, text="", command=lost)
            l = tk.PhotoImage(file="door.gif")
            # obj1 = canvas.create_text(250, 10, text='Simulation ',font=('verdana', 16, 'bold')

            l = Canvas(master)
            l.pack(expand=YES, fill=BOTH)
            l.background = PhotoImage(file='./door.gif')
            l.create_image(100, 100, image=l.background, anchor='nw')
            canvas.pack(side=tk.TOP)

            b.pack()
            c.pack()

            mainloop()
            
'''
