import random

class Game:
    def __init__(self, players):
        self.players = players
        self.current_player_index = 0
        self.determine_turn_order()

    # Whoever rolls the highest goes first
    def determine_turn_order(self):
        rolls = {player: self.roll_dice(player) for player in self.players}
        self.players = [player for player, _ in sorted(rolls.items(), key=lambda x: x[1], reverse=True)]
        print(f'\n{self.players[0]} goes first!')

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
            player = self.players[self.current_player_index]
            print(f'\n{player}\'s turn!')
            while double_count < 3:
                (roll, is_double) = self.roll_dice(player)
                if is_double:
                    player.position = (player.position + roll) % 40
                    print(f'You landed on {player.position}')
                    print(f'You rolled a double! Go again')
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
                print(f'{player} landed on {player.position}')
            
            self.current_player_index = (self.current_player_index + 1) % len(self.players)