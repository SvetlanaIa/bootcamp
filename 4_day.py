'''Напишите функцию, которая получает на вход поле для игры в крестики-нолики 3х3 в виде двумерного массива и проверяет,
   выиграл ли кто-то, или игра еще идет. Результатом должна быть строка 
   'X wins', '0 wins', 'Draw' (доиграли и ничья), 'Playing: X' (не доиграли и ходит Х), 'Playing: 0' (не доиграли и ходит О), в зависимости от состояния поля. 
   Бонус: поле произвольного размера (5x5 или больше), игра идет до 5 в ряд.'''
 

def result(board_list,n):    
    # по столбцам проверяем равенство элементов
    for j in range(n):
        sum_X = 0
        sum_O = 0        
        for i in range(j,n*n,n):
            if board_list[i] == 'X':
                sum_X += 1
                sum_O = 0
                if sum_X >= 5:
                    return 'X wins'
            elif board_list[i] == '0':
                sum_O += 1
                sum_X = 0
                if sum_O >= 5:
                    return '0 wins'
            else:
                break

    # построчно проверяем равенство элементов       
    for j in range(0,n*n,n):
        sum_X = 0
        sum_O = 0
        
        for i in range(j,n+j):
            if  board_list[i] == 'X':
                sum_X += 1
                sum_O = 0
                if sum_X >= 5:
                    return 'X wins'
                    
            elif board_list[i] == '0':
                sum_O += 1
                sum_X = 0 
                if sum_O >= 5:
                    return '0 wins'
                   
            else:
                break

    # диагональ правая
    index = 0
    while index < n * n:
        sum_X = 0
        sum_O = 0        
        if board_list[index] == 'X':
            sum_X += 1
            sum_O = 0
            if sum_X >= 5:
                    return 'X wins'
        if board_list[index] == '0':
            sum_O += 1
            sum_X = 0
            if sum_O >= 5:
                return '0 wins'    
        index = index + n + 1    

    # диагональ левая    
    index = n - 1
    while index < n * (n-1):
        sum_X = 0
        sum_O = 0        
        if board_list[index] == 'X':
            sum_X += 1
            sum_O = 0
            if sum_X >= 5:
                    return 'X wins'
        if board_list[index] == '0':
            sum_O += 1
            sum_X = 0
            if sum_O >= 5:
                return '0 wins'    
        index = index + n - 1

    # ничья
    if n % 2 == 0 and board_list.count('X') == n * n / 2 or n %2 != 0 and board_list.count('X') == n * n / 2 + 1 :   
        return 'Draw'

    return None             


def who_wins(board, n):
    board_list = [j for i in board for j in i]
    X_count = board_list.count('X')
    O_count = board_list.count('0')
    res = result(board_list, n)    
    if res is None:
        if O_count < X_count:
            res = 'Playing: 0'
        else: 
            res = 'Playing: X' 
    return res


board = [ ['0', ' ', ' ',' ',' ',' '], [' ', 'X', 'X',' ',' ',' '], [' ', ' ', ' ',' ',' ',' '], [' ', ' ', ' ',' ',' ',' '], [' ', ' ', ' ',' ',' ',' '], [' ', ' ', ' ',' ',' ',' '] ]
print((who_wins(board,6))== 'Playing: 0')

board = [ ['0', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 'X', 'X', ' ', ' ', ' ', ' '], ['0', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ',' ',' ',' ',' '], [' ', ' ', ' ',' ',' ',' ',' '], [' ', ' ', ' ',' ',' ',' ',' '], [' ', ' ', ' ',' ',' ',' ',' '] ]
print((who_wins(board,7)) == 'Playing: X')

board = [ ['0', '0', ' ', ' ', ' ', ' '], ['0', 'X', 'X', 'X', 'X', 'X'], ['0', ' ', ' ', ' ', ' ', ' '],['0', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' '] ]
print((who_wins(board,6)) == 'X wins')

board = [ ['0', 'X', '0', '0', '0', 'X'], ['0', 'X', 'X', 'X', 'X', '0'], ['X', 'X', '0', '0', '0', '0'], ['0', 'X', '0', 'X', '0', 'X'], ['0', 'X', '0', 'X', '0', 'X'], ['0', 'X', '0', 'X', '0', 'X'] ]
print((who_wins(board,6)) == 'X wins')

board = [ ['0', 'X', '0' ,'0', 'X', '0'], ['X', 'X', 'X', '0', 'X', '0'], ['X', '0', '0','X', '0', 'X'],['0', 'X', '0','0', 'X', '0'], ['0', 'X', 'X','0', 'X', '0'], ['X', 'X', '0', 'X', '0', 'X'] ]
print((who_wins(board,6)) == 'Draw')

