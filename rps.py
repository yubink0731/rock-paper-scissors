#!/usr/bin/env python3

import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    opponentMove = ""
    myPrevMove = ""

    def __init__(self, name):
        self.name = name

    def name(self):
        return self.name

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.myPrevMove = my_move
        self.opponentMove = their_move


class RandomPlayer(Player):
    def __init__(self):
        self.name = "RandomPlayer"

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def __init__(self):
        self.name = "HumanPlayer"

    def move(self):
        while 1:
            yourMove = input("Enter Your Move (rock, paper, scissors) ? ")
            if yourMove == "quit":
                print("You stopped the game !!! Game Over !")
                exit()
            if yourMove in moves:
                return yourMove

            print("Your input is wrong, enter again !!")


class ReflectPlayer(Player):
    def __init__(self):
        self.name = "ReflectPlayer"

    def move(self):
        return self.opponentMove


class CyclePlayer(Player):
    def __init__(self):
        self.name = "CyclePlayer"

    def move(self):
        if self.myPrevMove == "rock":
            return "paper"
        elif self.myPrevMove == "paper":
            return "scissors"
        elif self.myPrevMove == "scissors":
            return "rock"
        else:
            return random.choice(moves)


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    p1HowManyWon = 0
    p2HowManyWon = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        p1Name = self.p1.name
        p2Name = self.p2.name

        move1 = self.p1.move()
        move2 = self.p2.move()
        didMove1Win = beats(move1, move2)

        if didMove1Win:
            whoWonStatement = p1Name + " Won"
            self.p1HowManyWon = self.p1HowManyWon + 1
        elif move1 == move2:
            whoWonStatement = "Tie"
        else:
            whoWonStatement = p2Name + " Won"
            self.p2HowManyWon = self.p2HowManyWon + 1

        print(f"{p1Name}: {move1}  {p2Name}: {move2} => {whoWonStatement}")
        print(f"Score = {self.p1HowManyWon} : {self.p2HowManyWon}")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
# for round in range(3):
        while abs(self.p1HowManyWon - self.p2HowManyWon) < 3:
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    language = "Python"

# Adding the language variable into a string
    print(f"Hello {language} World!")

    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
