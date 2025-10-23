
lista = list()

for i in range(5):
    n = int (input())
    lista.append(n)
    
menor = lista[0] 
for i in range(5):
    for j in range(i+1, 5):
       if lista[i] < lista[j]:
           aux = lista[i]
           lista[i] = lista[j]
           lista[j] = aux
    
print(lista)