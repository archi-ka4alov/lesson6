# Словарь
my_dict = {'Demian': 1993, 'Artur': 1992, 'Andrey': 1984}
print(my_dict)
print(my_dict['Artur'])
print(my_dict.get('Antuan'))
my_dict.update({'Sergey': 1991,
                'Vasiliy': 1990})
a = my_dict.pop('Sergey')
print(a)
print(my_dict)

# Множество
my_set = {1, 4, 5 , 'Икея', 5, 'Икея', 4, True, 4.5, 3.14, 3.14, 'Олимпиада'}
print(my_set)
my_set.update([(1, 2, 3), 'Флотилия'])
# my_set.add((1, 2, 3))
# my_set.add('Флотилия')
my_set.remove('Икея')
print(my_set)