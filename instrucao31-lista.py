#
# Desempacotando listas
# *_ separa o restante em uma lista diferente
#
lst1 = ['Mamão', 'Laraja', 'Limão', 'Goiaba', 'Tangerina']
#
it1, it2, it3, it4, it5 = lst1
lt1, lt2, lt3, *_ = lst1
#
print(f'\n it1, it2, it3, it4, it5 = lst1: it3= {it3}\n')
print(lt2, lt3)
