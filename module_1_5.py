immutable_var = (1, True, 'apple',[1,True,89])
print(immutable_var)
#immutable_var[1]=False ошибка т.к. сам элемент кортежа неизменяем
immutable_var[3][2]=69 # элементы внутри изменяемых элементов кортежа (списков) можно менять
immutable_var[3][1]=False
print(immutable_var)

mutable_list = [24, 'coconut',False, 'peach']
print(mutable_list)
mutable_list[0]=True
mutable_list[2]='banana'
print(mutable_list)