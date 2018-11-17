import sys
import numpy as np
import pandas as pd

np.random.seed(0)

df = pd.DataFrame(np.random.randn(20,5),columns=list('ABCDE'))

print(df.mean())
