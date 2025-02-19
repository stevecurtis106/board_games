class Player:
    def __init__(self, name):
        self.name = name
        self.money = 1000
        self.position = 0
        self.properties = []
        self.jail_cards = 0
        self.in_jail = False
        self.turns_in_jail = 0

    def __str__(self):
        return self.name
    

    
    