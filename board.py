import pandas as pd

class Board:
    '''Create the board for our game'''
    def __init__(self):
        self.df = pd.DataFrame(index=list(range(1,7)), columns=list(range(1,8))).fillna(' ')
        self.create_dict()

    def create_dict(self):
        '''Crée une un dictionnaire contenant une liste avec le nom des colonnes espacés correctement et une liste de separateur et enregistre dans le dico'''    
        #Crée la liste contenant le nom des colonnes
        self.dico_board = {}
        lst_for_names = ['    ']
        for name in '1234567':
            lst_for_names.append(name)
            lst_for_names.append('   ')
        self.dico_board['name_col'] = lst_for_names

        #Crée une liste a utiliser comme séparateur de lignes et enregistre dans le dico
        lst_for_sep = ['  +']
        for i in range(7):
            lst_for_sep.append('---+')
        self.dico_board['sep'] = lst_for_sep

    def __str__(self):
        #Crée une liste pour chaque ligne numérotée et enregistre dans le dico
        for i in self.df.index:
            lst_for_row = []
            lst_for_row.append(f'  |')
            for j in self.df.columns:
                if self.df.loc[i,j] == 'J':
                    lst_for_row.append('\033[33m' + ' ' + u'\u263B' + ' ' + '\033[0m')
                elif self.df.loc[i,j] == 'R':
                    lst_for_row.append('\033[31m' + ' ' + u'\u263B' + ' ' + '\033[0m')
                else:
                    lst_for_row.append(self.df.loc[i,j]*3)
                lst_for_row.append('|')
            self.dico_board[i] = lst_for_row
        
        #Crée un string pour imprimer le board
        str_to_print = ''.join(self.dico_board['name_col']) + '\n' + ''.join(self.dico_board['sep'])
        for i in range(1,7):
            str_to_print += '\n' + ''.join(self.dico_board[i]) + '\n' + ''.join(self.dico_board['sep'])
        return str_to_print

    def colour_pawns(self, v, list_colour):
        if v == 'J':
            return f'color: {list_colour[0]}'
        else:
            return f'color: {list_colour[1]}'

