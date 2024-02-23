import matplotlib.pyplot as plt

population_ages = [22,55,62,45,21,22,34,42,42,102,122,130,34,87,65,49]
bins =  [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

plt.hist(population_ages,bins, histtype='bar', rwidth=0.8)
plt.xlabel('X')
plt.ylabel('Y')

plt.title('Histogram plot')

plt.legend()
plt.show()