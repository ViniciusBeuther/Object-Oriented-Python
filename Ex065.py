# LISTA 03
# 6) Crie uma lista de n umeros e remova o primeiro e ultimo elemento
L = [1,2,3,4,5,6,7,8,9,10]
ultimo = len(L)
L.remove(L[0])
L.remove(ultimo)
print('Lista com o primeiro e ultimo elem. removido: ')
print(L)