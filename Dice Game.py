"""A Dice Game"""
import random


class DiceGameFramework:
    def __init__(self, num_of_players=2):

        print(f'This is a 2 player game.')
        self.num_of_players = num_of_players

        name_of_players = []
        self.name_of_players = name_of_players
        # this uses the number of players, to get the names of the players. it then appends the names to the empty list
        for num in range(1, self.num_of_players + 1):
            players = input(f'Enter player {num} here: ')
            name_of_players.append(players.title())

        num_of_dice = int(input('Do you want to use 1 die or 2 dice? Enter the number here: '))
        if num_of_dice == 1:
            choice_of_num_of_dice = f'You are using 1 die.'
        elif num_of_dice == 2:
            choice_of_num_of_dice = f'You are using 2 dice.'
        # this ensures that the player enters a correct value
        else:
            print('Enter a correct value!')
        print(choice_of_num_of_dice)
        self.num_of_dice = num_of_dice

        num_of_rounds = int(input('How many rounds do you want to play? Enter the number here: '))
        self.num_of_rounds = num_of_rounds

        die = [1, 2, 3, 4, 5, 6]
        self.die = die

        ties = 0
        self.ties = ties


# this class inherits the attributes from DiceGameFramework and uses them for the game
class PlayGame(DiceGameFramework):
    def __init__(self):
        super().__init__()

        # gets the first player from the list above, and assigns it to this variable
        player1 = self.name_of_players[0]
        self.player1 = player1

        # gets the second player from the list above, and assigns it to this variable
        player2 = self.name_of_players[1]
        self.player2 = player2

        # creates a list to store all the outcomes of the game
        self.name_of_players[0] = []
        # creates a list to store all the outcomes of the game
        self.name_of_players[1] = []

        # keeps track of the scores
        player1_score = 0
        self.player1_score = player1_score

        # keeps track of the scores
        player2_score = 0
        self.player2_score = player1_score

        # in the event that a tie occurs, thos variable keeps track of it
        ties = 0
        self.ties = ties

    def getScore(self):
        # loops through the number of rounds
        for num in range(1, self.num_of_rounds + 1):
            if self.num_of_dice == 1:
                # gats a random value from the 'die list'
                rolledDie = random.choice(self.die)
                # appends/'adds' the result to the the empty list above
                self.name_of_players[0].append(rolledDie)
            elif self.num_of_dice == 2:
                # uses two dice in rder to satisfy the players' request
                rolledDie = random.choice(self.die), random.choice(self.die)
                # appends/'adds' the result to the the empty list above
                self.name_of_players[0].append(rolledDie)
            else:
                print('Choose either 1 or 2!')
        for num in range(1, self.num_of_rounds + 1):
            if self.num_of_dice == 1:
                # gats a random value from the 'die list'
                rolledDie = random.choice(self.die)
                # appends/'adds' the result to the the empty list above
                self.name_of_players[1].append(rolledDie)
            elif self.num_of_dice == 2:
                # uses two dice in rder to satisfy the players' request
                rolledDie = random.choice(self.die), random.choice(self.die)
                # appends/'adds' the result to the the empty list above
                self.name_of_players[1].append(rolledDie)
            else:
                # this serves as a second line of defense for errors. you can't be too sure lol
                print('Choose either 1 or 2!')
        # returns the complete list, after all the rounds
        print(self.name_of_players[0], self.name_of_players[1])

        # checks , and updates the scores
        for i in range(self.num_of_rounds):
            if self.name_of_players[0][i] > self.name_of_players[1][i]:
                print([self.name_of_players[0][i], self.name_of_players[1][i]], f'{self.player1}!')
                self.player1_score += 1
            elif self.name_of_players[0][i] < self.name_of_players[1][i]:
                print([self.name_of_players[0][i], self.name_of_players[1][i]], f'{self.player2}!')
                self.player2_score += 1
            else:
                print([self.name_of_players[0][i], self.name_of_players[1][i]], f'You tie!')
                self.player2_score += 0
                self.player1_score += 0
                self.ties += 1
        # checks too see who won, and returns the scores
        if self.player1_score > self.player2_score:
            print(
                f'The score is  {self.player1_score} : {self.player2_score}. There were {self.ties} ties. {self.player1} won!')
        elif self.player1_score < self.player2_score:
            print(
                f'The score is  {self.player1_score} : {self.player2_score}. There were {self.ties} ties. {self.player2} won!')
        else:
            print(
                f'The score is  {self.player1_score} : {self.player2_score}. There were {self.ties} ties. {self.player1} and {self.player2} you tie!')
        return


PlayGame().getScore()