import matplotlib.pyplot as plt
import numpy as np
cities_of_countries={
    'UK':{
        "Edinburgh": 0.56,
        "Glasgow": 0.62,
        "Stirling": 0.04,
        "London": 9.7
    },
    'China':{
         "Haining": 0.58,
        "Hangzhou": 8.4,
        "Shanghai": 29.9,
        "Beijing": 22.2
    }
}
#make a dictionary about the cities of countries
uk_population=list(cities_of_countries['UK'].values())
China_population=list(cities_of_countries['China'].values())
uk_population.sort()
China_population.sort()
#classify the data
print(uk_population)
print(China_population)
#print the population of UK AND China----first part

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
#set a figure that includes two graphs
categories_uk = list(cities_of_countries['UK'].keys())
uk_population = list(cities_of_countries['UK'].values())
categories_china = list(cities_of_countries['China'].keys())
china_population = list(cities_of_countries['China'].values()) 
#define the bar chart and the corresponding population data

ax1.bar(categories_uk, uk_population, color='skyblue', edgecolor='purple', label='UK')
ax1.set_title('Population of UK Cities')
ax1.set_xlabel('Cities in UK')
ax1.set_ylabel('Population')
ax1.set_xticks(range(len(categories_uk)))
ax1.set_xticklabels(categories_uk, rotation=45, ha="right")
ax1.legend()
#draw the bar chart of UK

ax2.bar(categories_china, china_population, color='orange', edgecolor='purple', label='China')
ax2.set_title('Population of China Cities')
ax2.set_xlabel('Cities in China')
ax2.set_ylabel('Population')
ax2.set_xticks(range(len(categories_china)))
ax2.set_xticklabels(categories_china, rotation=45, ha="right")
ax2.legend()
#draw the bar chart of China

plt.tight_layout()
#Adjust the spacing of subgraphs

plt.show()
#final step! draw the figure!--second part