import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pwd111= os.getcwd()
print(pwd111)
ls111 = os.listdir()
print(ls111)

dalys_data = pd.read_csv('dalys-rate-from-all-causes(1).csv')
first_5=dalys_data.head(5)
print(first_5)
dalys_data.info()
detail = dalys_data.describe()
print(detail)

dalys_data.iloc[4,2]
dalys_data.iloc[2,0:5]
dalys_data.iloc[0:2,:]
dalys_data.iloc[0:10:2,0:5]
dalys_data.iloc[0:3,[0,1,3]]
my_columns = [True,True,False,True]
dalys_data.iloc[0:3,my_columns]
dalys_data.loc[2:4,'Year']
dalys_data.loc[dalys_data['Entity']=='Afghanistan','DALYs']
china_data=dalys_data.loc[dalys_data['Entity']=='China',['Year','DALYs']]
type(dalys_data['Entity']=='China')
list(dalys_data['Entity']=='China')
pd.DataFrame(list(dalys_data['Entity']=='China'))# change list into Dataframe which is included in pandas
plt.plot(china_data.Year, china_data.DALYs, 'b+')#b+ means blue cross and r+ means red cross, bo mwans blue dot
plt.xticks(china_data.Year, rotation=-90)#ratate the number on x-axis
plt.show()
plt.clf()
