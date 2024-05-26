#!/usr/bin/python3

import Team


if __name__ == "__main__":
    player1 = Team.FootballPlayer("John", "Doe", "QB")
    player1.determine_jersey_number()
    print(f"Player: {player1.get_first_name()} {player1.get_last_name()}, Position: {player1.get_position()}, Jersey Number: {player1.get_jersey_number()}")

    player2 = Team.FootballPlayer("Jane", "Doe", "WR")
    player2.determine_jersey_number()
    print(f"Player: {player2.get_first_name()} {player2.get_last_name()}, Position: {player2.get_position()}, Jersey Number: {player2.get_jersey_number()}")
