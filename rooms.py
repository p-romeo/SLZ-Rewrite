
class Room():
    def __init__(self, description):
        self.description = description
        self.choices = []

    def add_choice(self, choice_index, player, enemy):
        choice = choice_index
        self.choices.append(choice)

    def interact(self, choice_index, player, enemy):
        pass

class StartingRoom(Room):
    def __init__(self):
        super().__init__("This is the starting room, welcome!")
        self.add_choice("Attack the Enemy")






