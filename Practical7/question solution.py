import os
import pandas as pd
import matplotlib.pyplot as plt
dalys_data = pd.read_csv('dalys-rate-from-all-causes(1).csv')#read the "dalys-rate-from-all-causes"
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
plt.clf()# done

