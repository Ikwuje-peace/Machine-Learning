import matplotlib.pyplot as plt
partitions = [45, 30, 15, 10]
names_of_section = ['Prayer', 'Reading', 'Coding', "Sleeping"]
colrs = ['k', 'c', 'r', 'b']

plt.pie(partitions, explode=(0,0,0,0.2), labels=names_of_section, colors=colrs, shadow=True)
plt.show()
