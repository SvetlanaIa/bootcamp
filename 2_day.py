'''19 cows, 14 apples, 2 tables, a pig and an onion'''

def count_things(words):
    vowels = ('a', 'e', 'o', 'i', 'u')
    words_set = set(words)   
    res = [[i,words.count(i)] for i in words_set]
    res.sort(key = lambda x: -x[1])
    result = []
    for i in res:
        if  i[1] > 1:
            i[0] = str(i[0]) + 's'
            result.append(' '.join([str(i[1]),i[0]]))
        else:            
            if i[0][0] in vowels:
                i[0] = 'an ' + i[0]
            else:
                i[0] = 'a ' + i[0]
            result.append(i[0])
    if len(words_set) > 1:
        return ', '.join(result[:-1]) + ' and ' + result[-1]
    return result[0]

# при сортировке элементы с одинаковым количеством постоянно меняют последовательность ( т.к. для формирования количества использую set, нужно переписать код,
# что бы последовательность ввода и вывода не изменялась?)
print(count_things(['pig', 'cow', 'apple', 'cow']))
print(count_things (['pig'] + ['onion'] + ['apple']*14 + ['cow']*19 + ['table']*2))

