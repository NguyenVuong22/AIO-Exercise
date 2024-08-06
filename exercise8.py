import pandas as pd
import numpy as np
data = pd.read_csv("advertising.csv ")
print(data.corr())
