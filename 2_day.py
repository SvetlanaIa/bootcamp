''' Если объект в списке встречается несколько раз, то нужно перед ним написать сколько, а в конце добавить "s" (2 cows), 
а если встречается только один - то добавить артикль "an" перед словами, начинающимися на гласные (a,e,i,o,u - an apple),
 или "a" перед согласными (a pig). Все объекты нужно связать с помощью "and"
  сортировать в предложении объекты по убыванию количества (больше всего объектов вначале): ’2 cows and a pig and an apple’'''

def count_things(words):
    vowels = ('a', 'e', 'o', 'i', 'u', 'y')
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
    return ' and '.join(result)

# при сортировке элементы с одинаковым количеством постоянно меняют последовательность ( т.к. для формирования количества использую set, нужно переписать код,
# что бы последовательность ввода и вывода не изменялась?)
print(count_things(['pig', 'cow', 'apple', 'cow']))
print(count_things (['pig'] + ['onion'] + ['apple']*14 + ['cow']*19 + ['table']*2))

