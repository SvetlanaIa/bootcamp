'''Напишите функцию, которая получает на вход поле для игры в крестики-нолики 3х3 в виде двумерного массива и проверяет,
   выиграл ли кто-то, или игра еще идет. Результатом должна быть строка 
   'X wins', '0 wins', 'Draw' (доиграли и ничья), 'Playing: X' (не доиграли и ходит Х), 'Playing: 0' (не доиграли и ходит О), в зависимости от состояния поля. 
   Бонус: поле произвольного размера (5x5 или больше), игра идет до 5 в ряд.'''
 

# Подсчет количества элементов Х(list_elements[0]) и 0(list_elements[1])
def check(board,i,j,list_elements):    
    if board[i][j] == 'X':
        list_elements[0] +=  1
        list_elements[1] = 0    
        return list_elements
    elif board[i][j] == '0':
        list_elements[1] += 1
        list_elements[0] = 0
        return list_elements
    return [0, 0]


# Проверка на выигрыш
def check_win(list_elements):
    if list_elements[0] >= 5:
        return 'X wins'
    if list_elements[1] >= 5:
        return '0 wins'
    return None    


# Анализ матрицы на выигрыш
def result(board,n): 

    # по столбцам и строкам проверяем равенство элементов
    for j in range(n):
        list_elements = [0, 0]   
        list_elements_1 = [0, 0]      
        for i in range(n):      
            list_elements = check(board,i,j,list_elements)
            list_elements_1 = check(board,j,i,list_elements_1)
            for i in list_elements, list_elements_1:
                res=check_win(i)
                if res:
                    return res 
   
    # диагональ правая
    list_elements = [0, 0]   
    for i in range(n):
        list_elements = check(board,i,i,list_elements)
        res = check_win(list_elements)
        if res:
                return res

    # диагональ левая 
    list_elements = [0, 0]   
    for j in range(n-1,0,-1):
        list_elements = check(board,n-j-1,j,list_elements)
        res = check_win(list_elements)
        if res:
                return res   
    return None             


def who_wins(board, n):
    board_list = [j for i in board for j in i]
    X_count = board_list.count('X')
    O_count = board_list.count('0')
    res = result(board, n)    
    if res is None:
        if n % 2 == 0 and X_count == n * n / 2 or n %2 != 0 and X_count == n * n / 2 + 1 :   
            res = 'Draw'
        elif O_count < X_count:
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

board = [ ['X', '0', '0' ,'0', 'X', '0'], ['X', 'X', 'X', '0', 'X', '0'], ['0', '0', 'X','X', '0', 'X'],['0', 'X', '0','X', '0', '0'], ['0', 'X', 'X','0', 'X', '0'], ['X', 'X', '0', 'X', '0', 'X'] ]
print((who_wins(board,6)) == 'X wins')

