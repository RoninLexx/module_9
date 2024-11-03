first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# first_result = (len(f) - len(s) for f in first for s in second if len(f) != len(s))  # запишите генераторную сборку, которая высчитывает разницу длин строк
# из списков first и second, если их длины не равны
first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))
# тоже, но из списка, попарно объединённого соответвенно индексам [0] с [0], [1] с [1] и т.д.
second_result = (len(f) == len(s) for f in first for s in second if first.index(f) == second.index(s) )

print(list(first_result))
print(list(second_result))

# вроде как то так