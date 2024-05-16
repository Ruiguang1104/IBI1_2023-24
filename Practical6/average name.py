import matplotlib.pyplot as plt
import numpy as np
day_activity={"Sleeping": 8, "Classes": 6, "Studying": 3.5, "TV": 2, "Music": 1}
other_time=24-day_activity['Sleeping']-day_activity["Classes"]-day_activity['Studying']-day_activity['TV']-day_activity['Music']#calculate the dictionary
day_activity['other']=other_time#add the other time in the dictionary
day_activity_list = list(day_activity.values())
labels = day_activity.keys()
sizes = day_activity.values()
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('average day')#add a title
plt.show()#show the picture
