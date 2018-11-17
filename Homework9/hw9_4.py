import sys
import numpy as np
import pandas as pd
import scipy.stats

input = sys.argv[1:]
input = [int(i) for i in input]

print(scipy.stats.norm(input[0], input[1]).pdf(input[2]))
print(scipy.stats.norm(input[0], input[1]).cdf(input[2]))

