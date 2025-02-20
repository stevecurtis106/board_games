import random
from space import Go, Property, CommunityChest, Chance, Jail, Utility, Railroad, Tax, FreeParking, GoToJail

class Game:
    def __init__(self, players):
        self.players = players
        self.current_player_index = 0
        self.determine_turn_order()
        self.create_board()

    # Whoever rolls the highest goes first
    def determine_turn_order(self):
        rolls = {player: self.roll_dice(player) for player in self.players}
        self.players = [player for player, _ in sorted(rolls.items(), key=lambda x: x[1], reverse=True)]
        print(f'\n{self.players[0]} goes first!')

    def create_board(self):
        self.board = [
            Go('Go'),
            Property('Mediterranean Avenue', 60, 2, 10, 30, 90, 160, 250, 50, 'brown'),
            CommunityChest('Community Chest', 'Advance to Go', 'advance_to_go'),
            Property('Baltic Avenue', 60, 4, 20, 60, 180, 320, 450, 50, 'brown'),
            Tax('Income Tax', 200, 0),
            Railroad('Reading Railroad', 200, 25),
            Property('Oriental Avenue', 100, 6, 30, 90, 270, 400, 550, 50, 'light blue'),
            Chance('Chance', 'Advance to Go', 'advance_to_go'),
            Property('Vermont Avenue', 100, 6, 30, 90, 270, 400, 550, 50, 'light blue'),
            Property('Connecticut Avenue', 120, 8, 40, 100, 300, 450, 600, 50, 'light blue'),
            Jail('Jail'),
            Property('St. Charles Place', 140, 10, 50, 150, 450, 625, 750, 100, 'pink'),
            Utility('Electric Company', 150, 'electric_company'),
            Property('States Avenue', 140, 10, 50, 150, 450, 625, 750, 100, 'pink'),
            Property('Virginia Avenue', 160, 12, 60, 180, 500, 700, 900, 100, 'pink'),
            Railroad('Pennsylvania Railroad', 200, 25),
            Property('St. James Place', 180, 14, 70, 200, 550, 750, 950, 100, 'orange'),
            CommunityChest('Community Chest', 'Advance to Go', 'advance_to_go'),
            Property('Tennessee Avenue', 180, 14, 70, 200, 550, 750, 950, 100, 'orange'),
            Property('New York Avenue', 200, 16, 80, 220, 600, 800, 1000, 100, 'orange'),
            FreeParking('Free Parking'),
            Property('Kentucky Avenue', 220, 18, 90, 250, 700, 875, 1050, 150, 'red'),
            Chance('Chance', 'Advance to Illinois Avenue', 'advance_to_illinois'),
            Property('Indiana Avenue', 220, 18, 90, 250, 700, 875, 1050, 150, 'red'),
            Property('Illinois Avenue', 240, 20, 100, 300, 750, 925, 1100, 150, 'red'),
            Railroad('B. & O. Railroad', 200, 25),
            Property('Atlantic Avenue', 260, 22, 110, 330, 800, 975, 1150, 150, 'yellow'),
            Property('Ventnor Avenue', 260, 22, 110, 330, 800, 975, 1150, 150, 'yellow'),
            Utility('Water Works', 150, 'water_works'),
            Property('Marvin Gardens', 280, 24, 120, 360, 850, 1025, 1200, 150, 'yellow'),
            GoToJail('Go to Jail'),
            Property('Pacific Avenue', 300, 26, 130, 390, 900, 1100, 1275, 200, 'green'),
            Property('North Carolina Avenue', 300, 26, 130, 390, 900, 1100, 1275, 200, 'green'),
            CommunityChest('Community Chest', 'Advance to Boardwalk', 'advance_to_boardwalk'),
            Property('Pennsylvania Avenue', 320, 28, 150, 450, 1000, 1200, 1400, 200, 'green'),
            Railroad('Short Line', 200, 25),
            Chance('Chance', 'Advance to Boardwalk', 'advance_to_boardwalk'),
            Property('Park Place', 350, 35, 175, 500, 1100, 1300, 1500, 200, 'dark blue'),
            Tax('Luxury Tax', 75, 0),
            Property('Boardwalk', 400, 50, 200, 600, 1400, 1700, 2000, 200, 'dark blue')
        ]

    # Rolls 2 six-sided dice
    def roll_dice(self, player):
        input(f'{player} - press enter to roll the dice.')
        die_1 = random.randint(1, 6)
        die_2 = random.randint(1, 6)

        if die_1 + die_2 == 8 or die_1 + die_2 == 11:
            print(f'You rolled an {die_1 + die_2}!')
        else:
            print(f'You rolled a {die_1 + die_2}!')

        return (die_1 + die_2, die_1 == die_2)


    def play(self):
        while True:
            double_count = 0
            roll = None
            player = self.players[self.current_player_index]
            print(f'\n{player}\'s turn!')
            while double_count < 3:
                (roll, is_double) = self.roll_dice(player)
                if is_double:
                    player.position = (player.position + roll) % 40
                    print(f'{player} landed on {self.board[player.position]}. Go again!')
                    double_count += 1
                else:
                    break
            # 3 doubles in a row, go to jail
            if double_count == 3:
                player.position = 10
                player.in_jail = True
                print(f'{player} rolled 3 doubles in a row - go to jail')
            else:
                player.position = (player.position + roll) % 40
                print(f'{player} landed on {self.board[player.position]}')

            
            self.current_player_index = (self.current_player_index + 1) % len(self.players)