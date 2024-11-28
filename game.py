from board import Board
from pawn import Pawn

class Game:
    '''Class Game starts a game, contains the game play'''
    def __init__(self):
        self.board = Board()
        self.ongoing = True
        self.step = 0
        self.choose_colour()
        while self.ongoing:
            self.play_turn()
            self.change_player()
        
    def choose_colour(self):
        print('Bienvenue! Vous êtes le premier joueur !')
        print(self.board)
        chosen_colour = input('Veuillez choisir une couleur, Jaune [J] ou Rouge [R]: ')
        while not (chosen_colour.upper() == 'J' or chosen_colour.upper() == 'R'):
            chosen_colour = input('Veuillez entrer J ou R : ')
        self.player_colour = chosen_colour

    def play_turn(self):
        print(f'Au tour des {self.player_colour}')
        self.step += 1
        chosen_col = int(self.enter_and_check_col())
        empty_spot = self.find_empty_spot(chosen_col)
        new_pawn = Pawn(id=self.step, colour=self.player_colour, position=(empty_spot,chosen_col))
        self.place_pawn_on_board(new_pawn, chosen_col)
        self.check_if_end()
        

    def enter_and_check_col(self):
        chosen_col = input('Dans quelle colonne voulez-vous placer votre pion ? : ') 
        while not isinstance(eval(chosen_col), int) and eval(chosen_col) not in range(1,8): #Checks that the value entered is an integer between 1 and 7
            chosen_col = int(input('Veuillez entrer un chiffre entre 1 et 7: '))
        
        while not ' ' in [self.board.df.loc[i, eval(chosen_col)] for i in self.board.df.index]: #Checks that the colomn contains at least an empty spot
            chosen_col = int(input('La colonne est pleine ! Veuillez en choisir une autre'))
        return chosen_col

    def find_empty_spot(self, col):
        list_value_series = list(self.board.df[col].values)
        for i in range(len(list_value_series)-1, -1, -1):
            if list_value_series[i] == ' ':
                return i

    
    def place_pawn_on_board(self, pawn, col):
        print('Plaçons le pion.')
        pass


    def change_player(self):
        if self.player_colour == 'J':
            self.player_colour = 'R'
        else:
            self.player_colour = 'J'

    def check_if_end(self):
        pass
myGame = Game()
