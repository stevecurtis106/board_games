from player import Player
from game import Game

if __name__ == "__main__":
    num_players = None
    players = []

    while True:
        num_players = input("How many people are playing? ")
        if num_players.isdigit():
            num_players = int(num_players)
            if num_players > 1:
                break
            else:
                print("You need at least 2 players to play.")
        else:
            print("Please enter a number.")
    
    for i in range(num_players):
        player_name = input(f"Enter the name of player {i + 1}: ")
        player = Player(player_name)
        players.append(player)

    game = Game(players)
    game.play()