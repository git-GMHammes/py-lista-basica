#
# Desempacotando listas
# *_ separa o restante em uma lista diferente
#
lst1 = ['Mamão', 'Laraja', 'Limão', 'Goiaba', 'Tangerina']
#
lis1, lis2, lis3, lis4, lis5 = lst1
lt1, lt2, lt3, *_ = lst1
#
print(lis3)
print(lt2, lt3)
