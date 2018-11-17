import sys
import numpy as np

input = sys.argv[1:]
input = [int(i) for i in input]
lista = [1,6,9,8,14]


lista.extend(input)
print(lista)
print(len(lista))
lista.sort()
print(lista)
