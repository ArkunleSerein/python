# exo 10.5
# Créer une fonction nommée `compare()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoie une valeur de type `int`
# - renvoie 1 si `a` est plus grand que `b`
# - renvoie -1 si `a` est plus petit que `b`
# - renvoie 0 si `a` et `b` sont égaux
# Appelez la fonction et affichez le résultat

# réponse 10.5

import random

a = round(random.uniform(1.0, 1.1), 2)
b = round(random.uniform(1.0, 1.1), 2)

print(f"a = {a}")
print(f"b = {b}")

def compare(a: float, b: float) -> int:
        if a > b:
                return 1
        if a < b:
                return -1
        elif a == b:
                return 0
        
result = compare(a, b)
print(result)