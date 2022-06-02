import pandas as pd
import numpy as np

df=pd.read_csv("savings_data.csv")
quantList=df["quant_saved"]
q75,q25=np.percentile(quantList,[75,25])
iqr=q75-q25
print("Interquartile range of quantity saved: "+str(iqr))