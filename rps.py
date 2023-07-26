import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def __init__(self):
        self.my_move = None
        self.their_move = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RockPlayer(Player):
    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.move_index = 0

    def move(self):
        move = moves[self.move_index]
        self.move_index = (self.move_index + 1) % 3
        return move


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Enter your move (rock/paper/scissors) "
                         "or 'quit' to end the game: ").lower()
            if move in moves:
                return move
            elif move == 'quit':
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

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

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
    player_strategies = [RockPlayer(), RandomPlayer(), ReflectPlayer(),
                         CyclePlayer()]
    p1 = HumanPlayer()
    p2 = random.choice(player_strategies)
    game = Game(p1, p2)
    game.play_game()
