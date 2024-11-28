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
        
    def choose_colour(self):
        print('Bienvenue! Vous êtes le premier joueur !')
        print(self.board)
        chosen_colour = input('Veuillez choisir une couleur, Jaune [J] ou Rouge [R]: ')
        while not type(chosen_colour) == str:
            chosen_colour = input('Veuillez entrer une chaine de caractère ! Pas de chiffres, pas de caractères spéciaux : ')
        self.player_colour = chosen_colour[0].upper() + chosen_colour[1:].lower()

    def play_turn(self):
        print(f'Au tour des {self.player_colour}')
        self.step += 1
        chosen_col = int(self.enter_and_check_col())
        new_pawn = Pawn(id=self.step, colour=self.player_colour, position=chosen_col)
        self.place_pawn_on_board(new_pawn)

    def enter_and_check_col(self):
        chosen_col = input('Dans quelle colonne voulez-vous placer votre pion ? : ') 
        while not isinstance(eval(chosen_col), int) and eval(chosen_col) not in range(1,8): #Checks that the value entered is an integer between 1 and 7
            chosen_col = int(input('Veuillez entrer un chiffre entre 1 et 7: '))
        
        while not ' ' in [self.board.df.loc[i, eval(chosen_col)] for i in self.board.df.index]: #Checks that the colomn contains at least an empty spot
            chosen_col = int(input('La colonne est pleine ! Veuillez en choisir une autre'))
        print('Plaçons le pion.')
        return chosen_col

    def place_pawn_on_board(self, pawn):
        pass

myGame = Game()
