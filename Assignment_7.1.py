# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 20:20:38 2018

@author: vamshi
"""

import numpy as np
import pandas as pd
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})

# 1>
df['FlightNumber']=[10045+(10*i) for i in range(0, len(df))]

# 2>>
DF1 = pd.DataFrame(df.From_To)
DF1['From'] = DF1.From_To.str.split('_').str.get(0)
DF1['To'] = DF1.From_To.str.split('_').str.get(1)
DF1 = DF1.drop('From_To', 1)

# 3>>
DF1['From'] = DF1.From.str.title()
DF1['To'] = DF1.To.str.title()
# 4>>

df = df.drop('From_To', 1)
df = pd.concat([DF1,df], axis = 1)

# 5>>
tDelay = pd.DataFrame(df.RecentDelays)
tDelay = pd.DataFrame(df['RecentDelays'].values.tolist())
tDelay.columns = ['Delay_1', 'Delay_2', 'Delay_3']
df = df.drop('RecentDelays', 1)
df.insert(3, "Delay_1", tDelay['Delay_1'])
df.insert(4, "Delay_2", tDelay['Delay_2'])
df.insert(5, "Delay_3", tDelay['Delay_3'])
print(df)