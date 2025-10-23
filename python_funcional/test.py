

def tail(l1):
    return l1[1:]

def init(l1):
    return l1[:-1]

def head(l1):
    return l1[0]

def last(l1):
    return l1[-1]

def tamanhoLista(l1):
    if(l1 == []):
        return 0
    else:
        return 1 + tamanhoLista(tail(l1))
    
def concatlistas(l1, l2):
    if(l1 == [] and l2 == []):
        return []
    elif(l1 == []):
        return concatlistas(l2, [])
    else:
        return [head(l1)] + concatlistas(tail(l1),l2)
    
print(concatlistas([1,2],[3,4]))

def pertenceLista(x,lista):
    if (tamanhoLista(lista) == 0):
        return False
    elif (x == head(lista)):
        return True
    else:
        return pertenceLista(x,tail(lista))
    
print(pertenceLista(1,[1,2,3,4]))

def uniaolistas(l1,l2):
    if(l1 == [] and l2 == []):
        return []
    elif(l1 == []):
        return uniaolistas(l2,[])
    elif pertenceLista(head(l1),tail(l1)) or pertenceLista(head(l2),tail(l2)):
        return uniaolistas(tail(l1), l2)
    else:
        return [head(l1) + uniaolistas(tail(l1), l2)]
    
print(uniaolistas([1,2],[1,2,3,4]))

# Q10

def listaMaiores(l1,n):
    if(l1 == []):
        return []
    elif(head(l1) > n):
        return listaMaiores(tail(l1), n)
    else:
        return listaMaiores(tail(l1),n)
    
def invertelista(lista):
    if (lista == []):
        return []
    else:
        return concatlistas(invertelista(tail(lista)), [head(lista)])
    
def geraPalindromo (lista):
    return concatlistas(lista,invertelista(lista))

def ehPrimoAuxiliar(a, b):
    if b == 1:
        return True
    elif (a % b == 0):
        return False
    else:
        return ehPrimoAuxiliar(a, b-1)

def ehPrimo(n):
    if n == 1:
        return False
    else:
        return ehPrimoAuxiliar(n,n-1)
    
def consoantlist(l1,l2):
    if (l1 == [] and l2 == []):
        return True
    if (l1)

