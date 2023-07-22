import random

moves = ['rock', 'paper', 'scissors']
"""
the Player class does not have any specific use or functionality in my code.
It serves as a parent class for other player classes,
but it does not provide any unique methods or attributes.

Since the Player class does not have any significant functionality,
I remove it without affecting the rest of the code.
The child classes directly inherit from object,
which is the default behavior in Python,
so there's no explicit need to have the empty Player class.
"""
# class Player:
#     def move(self):
#         return 'rock'

#     def learn(self, my_move, their_move):
#         pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer:
    def move(self):
        return random.choice(moves)


class HumanPlayer:
    def move(self):
        while True:
            move = input("Enter your move (rock/paper/scissors)"
                         f" or 'quit' to end the game: ").lower()
            if move in moves:
                return move
            elif move.lower() == 'quit':
                return 'quit'
            else:
                print("Invalid move. Please try again.")


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0

    def play_round(self):
        move1 = self.p1.move()
        if move1 == 'quit':
            print("Game ended by player.")
            print(f"Final scores - Player 1: {self.score_p1}, "
                  f"Player 2: {self.score_p2}")
            if self.score_p1 > self.score_p2:
                print("Player 1 wins the game!")
            elif self.score_p1 < self.score_p2:
                print("Player 2 wins the game!")
            else:
                print("It's a tie!")
            exit()

        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        if move1 == move2:
            print("It's a tie!")
        elif beats(move1, move2):
            print("Player 1 wins!")
            self.score_p1 += 1
        else:
            print("Player 2 wins!")
            self.score_p2 += 1

    def play_game(self):
        print("Game start!")
        round_num = 0
        while round_num < 3 or abs(self.score_p1 - self.score_p2) < 3:
            print(f"Round {round_num + 1}:")
            self.play_round()
            round_num += 1

        print("Game over!")
        print(f"Final scores - Player 1: {self.score_p1}, "
              f"Player 2: {self.score_p2}")

        if self.score_p1 > self.score_p2:
            print("Player 1 wins the game!")
        elif self.score_p1 < self.score_p2:
            print("Player 2 wins the game!")
        else:
            print("It's a tie!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
