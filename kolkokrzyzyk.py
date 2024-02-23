import sys

class Table:
    def __init__(self) -> None:
        
        self.tab =[['-','-','-'],
                    ['-','-','-'],
                    ['-','-','-']]


    def check_win(self) -> bool:
        # check rows 
        for row in self.tab:
            if row[0] == row[1] == row[2] != '-':
                return True
        # check columns
        for i in range(3):
            if self.tab[0][i] == self.tab[1][i] == self.tab[2][i] != '-':
                return True

       #check diagonal
        if self.tab[1][1] == self.tab[0][0] == self.tab[2][2] != '-':
            return True
        if self.tab[1][1] == self.tab[0][2] == self.tab[2][0] != '-':
            return True
        
        
    def print_table(self):
        
        print('*'*20)
        print('            ABC')
        print('          1', ''.join(self.tab[0]))
        print('          2', ''.join(self.tab[1]))
        print('          3', ''.join(self.tab[2]))
        print('*'*20)

    def draw(self):
        counter = 0
        for x in self.tab:
            counter += x.count('-')
        if counter == 0:
            return True
        return False

class Game():
    
    def new_game(self):
        self.table = Table()
    
    def move(self, char):
        self.table.print_table()
        possible_moves = ['A3','A1','A2','B3','B1','B2','C3','C1','C2']
        valid_move = False
        while valid_move != True:
            place = input(f'PODAJ POLE DLA {char}: ')
            place = place.upper()

            if place in possible_moves or place[::-1] in possible_moves:
                if place[0].isalpha():
                    place = place[::-1]
                if place[1] == 'A':
                    x = 0
                elif place[1] == 'B':
                    x = 1
                else:
                    x = 2
                if self.table.tab[int(place[0])-1][x] == '-':
                    self.table.tab[int(place[0])-1][x] = char
                    valid_move = True
                else:
                    print('pole zajęte podaj inne pole')
            else:
                print('zle podaj jeszcze raz')


        if self.table.check_win():
            print(f'!!!!!! {char} - wins  !!!!!')
            self.table.print_table()
            print(f'!!!!!! {char} - wins  !!!!!')
            return True
        
        counter = 0
        for rows in self.table.tab:
            if rows.count('-') == 0:
                counter += 1
        if counter == 3:
            self.table.draw()
        return False
        
def main():

    while True:
        choose = input("""
            1. NOWA GRA

            0. ZAKOŃCZ
                      """)
        
        if choose == '1':
            game = Game()
            game.new_game()
            while True:
                if game.move('x'):
                    break
                if game.move('o'):
                    break
            choose = input('1 - nowa gra \n0 - zakończ grę \n:')


        if choose == '0':
            sys.exit(0)


if __name__ == '__main__':
    main()