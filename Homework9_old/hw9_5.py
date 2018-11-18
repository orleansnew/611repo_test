import sys
import numpy as np
import pandas as pd
import scipy.stats

input = sys.argv[1:]
input = [int(i) for i in input]

def function(x,y):
	squares = [j**2 for j in range(x,y+1)]
	return(sum(squares))

ss = function(input[0],input[1])
print(ss)
