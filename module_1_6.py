my_dict = {'Nata':1982,"Egor":1980,"Kate":2010,'Vlad':1959}
print('Dict:',my_dict)
print('Existing value:',my_dict['Nata'])
print('Not existing value:',my_dict.get('Vera','Такого имени нет')) #вывод значения по несуществующему ключу без ошибки
my_dict.update({'Sasha': 1984, 'Lena': 2024}) #добавить еще две пары ключ:значение
a = my_dict.pop('Kate') #вынуть значение из словаря в переменную
print('Deleted value:',a)
print('Modified dictionary:',my_dict)

my_set = {1,6,3,1,7,'yes','no','no',2}
print('Set:',my_set)
my_set.add(9)
my_set.add('ok') #добавление двух уникальных элементов
my_set.discard('no') #удаление элемента
print('Modified set:',my_set)