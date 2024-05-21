import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dalys_data = pd.read_csv(r"C:\Users\86138\OneDrive - International Campus, Zhejiang University\桌面\ibi ica\IBI1_2023-24\Practical7\dalys-rate-from-all-causes(1).csv")#read the csv file

# just a try about what we have learned in IBI1
# first_5=dalys_data.head(5)
# print(first_5)
# dalys_data.info()
# detail = dalys_data.describe()
# print(detail)
# dalys_data.iloc[4,2]
# dalys_data.iloc[2,0:5]
# dalys_data.iloc[0:2,:]
# dalys_data.iloc[0:10:2,0:5]
# dalys_data.iloc[0:3,[0,1,3]]
# my_columns = [True,True,False,True]

specific_value = dalys_data.iloc[0:100:10,3]# Show the forth column from every 10th row, starting from the first row for the first 100 rows
print(specific_value)
dalys_data.loc[dalys_data['Entity']=='Afghanistan','DALYs']
china_data=dalys_data.loc[dalys_data['Entity']=='China',['Year','DALYs']]
type(dalys_data['Entity']=='China')
list(dalys_data['Entity']=='China')
mean_value = np.mean(china_data)
print('The mean DALYS value of China is',mean_value)
pd.DataFrame(list(dalys_data['Entity']=='China'))# change list into Dataframe which is included in pandas
plt.plot(china_data.Year, china_data.DALYs, 'b+')#b+ means blue cross and r+ means red cross, bo mwans blue dot
plt.xticks(china_data.Year, rotation=-90)#ratate the number on x-axis
plt.figure()

#for the question solution
dalys_data = pd.read_csv(r"C:\Users\86138\OneDrive - International Campus, Zhejiang University\桌面\ibi ica\IBI1_2023-24\Practical7\dalys-rate-from-all-causes(1).csv")#read the "dalys-rate-from-all-causes"
canada_data = dalys_data[dalys_data["Entity"] == "Canada"]#look for the canada data from the "dalys-rate-from-all-causes"
uk_data =dalys_data[dalys_data["Entity"] == "France"]
mean_dalys_canada = canada_data["DALYs"].mean() #create a variable to store the data of the mean of canada
plt.plot(canada_data["Year"], canada_data["DALYs"], 'b+', label='Canada')
plt.plot(uk_data["Year"], uk_data["DALYs"], 'ro-', label='France')
plt.xlabel('Year') 
plt.ylabel('DALYs')  
plt.title('DALYs Over Time for Canada and France')
plt.legend()
plt.xticks(rotation=-90)
plt.show()#draw the picture about the data of Canada
