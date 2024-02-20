import sys

class Table:
    def __init__(self) -> None:
        
        self.tab =[['-','-','-'],
                    ['-','-','-'],
                    ['-','-','-']]


    def check_win(self) -> bool:
        
        chars = ['x','o']
        result = self.tab

        for char in chars:
            if char in result[0] or char in result[1] or char in result[2]:

                for x in result:

                    if x.count(char) == 3:

                        return True
                i = 0
                for _ in range(3):

                    if self.tab[0][i] == char and self.tab[1][i] == char and self.tab[2][i] == char:
                        return True
                    i += 1
                if self.tab[1][1] == char:
                    if self.tab[0][0] == char and self.tab[2][2] == char:
                        return True
                    if self.tab[2][0] == char and self.tab[0][2] == char:
                        return True
        
        for x in result:
            if '-' not in x:
                return 

        return False

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
        ver = False
        while ver != True:
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
                    ver = True
                else:
                    print('pole zajęte podaj inne pole')
            else:
                print('zle podaj jeszcze raz')


        if self.table.check_win():
            print(f'!!!!!! {char} - wins  !!!!!')
            self.table.print_table()
            print(f'!!!!!! {char} - wins  !!!!!')
            return True
        
        if self.table.draw():
            self.table.print_table()
            print('ITS A DRAW, TRY AGAIN')

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


        if choose == '0':
            sys.exit(0)


if __name__ == '__main__':
    main()