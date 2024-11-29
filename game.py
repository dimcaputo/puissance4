from board import *
from pawn import *

class Game:
    '''Class Game starts a game, contains the game play'''
    def __init__(self):
        self.board = Board()
        self.ongoing = True
        self.step = 0
        self.choose_colour()
        while self.ongoing:
            self.play_turn()
        self.display_winner()
        while input('Voulez vous jouer à nouveau? [Y]: ') == 'Y' or input('Voulez vous jouer à nouveau? [Y]: ') == 'y':
            new_game = Game()

        
    def choose_colour(self):
        print('Bienvenue! Vous êtes le premier joueur !\n')
        print(self.board)
        chosen_colour = input('\nVeuillez choisir une couleur, Jaune [J] ou Rouge [R]: ')
        while not (chosen_colour == 'J' or chosen_colour == 'R'):
            chosen_colour = input('\nVeuillez entrer J ou R : ')
        self.player_colour = chosen_colour

    def play_turn(self):
        if self.player_colour == 'J':
            print('\nAu tour des jaunes')
        else:
            print('\nAu tour des rouges')
        self.step += 1
        chosen_col = int(self.enter_and_check_col())
        empty_spot = self.find_empty_spot(chosen_col)
        new_pawn = Pawn(id=self.step, colour=self.player_colour, position=(empty_spot,chosen_col))
        self.place_pawn_on_board(new_pawn)
        self.check_if_finished(new_pawn)
        if self.ongoing:
            self.change_player()

    def enter_and_check_col(self):
        chosen_col = input('\nDans quelle colonne voulez-vous placer votre pion ? : ') 
        stop = False
        while stop == False:
            try:
                chosen_col = int(chosen_col)
                if 0 < chosen_col <= 7:
                    try:
                        if ' ' in [self.board.df.loc[i, chosen_col] for i in self.board.df.index]:
                            stop = True
                        else:
                            raise ValueError
                    except:
                        chosen_col = input('\nLa colonne est pleine ! Veuillez en choisir une autre: ')
                else:
                    raise ValueError
            except:
                chosen_col = input('\nVeuillez entrer un chiffre entre 1 et 7: ')
        return chosen_col

    def find_empty_spot(self, col):
        list_value_series = list(self.board.df[col].values)
        for i in range(len(list_value_series)-1, -1, -1):
            if list_value_series[i] == ' ':
                return i+1

    def place_pawn_on_board(self, pawn):
        print('\nPlaçons le pion.')
        self.board.df.loc[pawn.get_position()[0], pawn.get_position()[1]] = pawn.get_colour()
        print(self.board)

    def change_player(self):
        if self.player_colour == 'J':
            self.player_colour = 'R'
        else:
            self.player_colour = 'J'

    def check_if_finished(self, pawn):
        is_finished = self.check_if_winner(pawn) or self.check_if_full()
        if is_finished:
            self.ongoing = not is_finished

    def check_if_winner(self, pawn):
        dict_counts = self.find_neighbours(pawn)
        for k,v in dict_counts.items():
            if len(v) >= 4:
                return True

    def check_if_full(self):
        if len(Pawn.list_of_pawns) == 42:
            bool_full = True
        else:
            bool_full = False
        return bool_full

    def display_winner(self):
        if self.check_if_full():
            print("\nToo bad! Nobody won! :'(")
        else:
            if self.player_colour == 'J':
                print('\nBravo !! Les jaunes ont gagné !')
            else:
                print('\nBravo !! Les rouges ont gagné !')

    def find_neighbours(self, pawn):
        dict_direction = {'horizontale':[(0,y) for y in [-1,1]], 
                          'verticale':[(x,0) for x in [-1,1]], 
                          'diagonale_croissante':[(x,y) for x in [-1,1] for y in [-1,1] if x == y],
                          'diagonale_decroissante':[(x,y) for x in [-1,1] for y in [-1,1] if x != y]}
        dict_count_direction = {k:[] for k in dict_direction.keys()}
        for key in dict_direction.keys():
            for item in dict_direction[key]:
                dict_count_direction[key].extend(self.find_neighbours_in_one_direction(pawn, item, pawn.get_colour(), [pawn]))
            dict_count_direction[key] = list(set([x for x in dict_count_direction[key] if not x == None]))
        return dict_count_direction
        
    def find_neighbours_in_one_direction(self, pawn, tup, colour, lst_temp:list):
        ind,col = pawn.get_position()[0] + tup[0], pawn.get_position()[1] + tup[1]
        new_pawn = Pawn.get_pawn_from_location((ind,col))
        if isinstance(new_pawn, Pawn) and new_pawn.get_colour() == pawn.get_colour():
            lst_temp.append(new_pawn)
            self.find_neighbours_in_one_direction(new_pawn, tup, new_pawn.get_colour(), lst_temp)
        return lst_temp
            

if __name__ == '__main__':
    myGame = Game()
