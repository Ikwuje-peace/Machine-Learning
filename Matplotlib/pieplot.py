import matplotlib.pyplot as plt

slices = [7,2,2,13]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'b']

plt.pie(slices, 
        labels=activities, 
        colors=cols, 
        startangle=90,  
        shadow=True,  
        explode=(0,0.1,0,0),  
        autopct='%1.1f%%' )

plt.title('Pie Plot')

partitions = [45, 30, 15, 10]
names_of_section = ['Prayer', 'Reading', 'Coding', "Sleeping"]
colrs = ['k', 'c', 'r', 'b']

plt.pie(partitions, explode=(0,3,0,6.2), labels=names_of_section, colors=colrs, pctdistance=0.6, shadow=True, radius=20, )

plt.subplot(211)
plt.plot()

plt.subplot(212)
plt.plot()

plt.show()
