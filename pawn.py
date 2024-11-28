class Pawn:
    list_of_pawns = []
    '''Represent the pawns used during the game'''
    def __init__(self, id:int, colour:str, position:tuple, is_on_board=False):
        self.set_id(id)
        self.set_colour(colour)
        self.set_position(position)
        self.set_is_on_board(is_on_board)
        Pawn.list_of_pawns.append(self)

    def set_id(self, id):
        self.__id = id

    def set_colour(self, colour):
        self.__colour = colour

    def set_position(self, position):
        self.__col = position[1]
        self.__row = position[0]
    
    def set_is_on_board(self, is_on_board):
        self.__is_on_board = is_on_board

    def get_id(self):
        return self.__id
    
    def get_colour(self):
        return self.__colour
    
    def get_position(self):
        return self.__row, self.__col
    
    def get_is_on_board(self):
        return self.__is_on_board