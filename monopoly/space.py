class Space():
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name


class Property(Space):
    def __init__(self, name, price, rent_lvl0, rent_lvl1, rent_lvl2, rent_lvl3, rent_lvl4, rent_lvl5, house_cost, color_group):
        super().__init__(name)
        self.price = price
        self.rent_lvl0 = rent_lvl0
        self.rent_lvl1 = rent_lvl1
        self.rent_lvl2 = rent_lvl2
        self.rent_lvl3 = rent_lvl3
        self.rent_lvl4 = rent_lvl4
        self.rent_lvl5 = rent_lvl5
        self.house_cost = house_cost
        self.color_group = color_group
        self.owner = None
        self.houses = 0
        self.mortgaged = False
        self.in_monopoly = False


class Jail(Space):
    def __init__(self, name):
        super().__init__(name)


class Go(Space):
    def __init__(self, name):
        super().__init__(name)


class FreeParking(Space):
    def __init__(self, name):
        super().__init__(name)


class GoToJail(Space):
    def __init__(self, name):
        super().__init__(name)


class Chance(Space):
    def __init__(self, name, description, action):
        super().__init__(name)
        self.description = description
        self.action = action


class CommunityChest(Space):
    def __init__(self, name, description, action):
        super().__init__(name)
        self.description = description
        self.action = action


class Utility(Space):
    def __init__(self, name, price, action):
        super().__init__(name)
        self.price = price
        self.action = action
        self.owner = None


class Railroad(Space):
    def __init__(self, name, price, rent):
        super().__init__(name)
        self.price = price
        self.rent = rent
        self.owner = None


class Tax(Space):
    def __init__(self, name, amount, percentage):
        super().__init__(name)
        self.amount = amount
        self.percentage = percentage