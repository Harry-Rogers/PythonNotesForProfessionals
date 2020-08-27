# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 12:54:19 2020

@author: Harry
"""

import pandas as pd
d = {'a': (1, 101), 'b': (2, 202), 'c': (3, 303)}
df = pd.DataFrame.from_dict(d, orient="index")
df.to_csv("data.csv")

df = pd.read_csv("data.csv")
d = df.to_dict()
print(d)