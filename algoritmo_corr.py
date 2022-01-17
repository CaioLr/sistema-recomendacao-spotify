import pandas as pd
import numpy as np

df = pd.read_csv('datamusic')

musicmat = df.pivot_table(columns='nomes')

thislove_numbers = musicmat['This Love']
similar_to_thislove = musicmat.corrwith(thislove_numbers)
corr_thislove = pd.DataFrame(similar_to_thislove,columns=['Correlation'])

print(corr_thislove.nlargest(20, 'Correlation'))

