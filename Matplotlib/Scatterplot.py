import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9]
y = [2,4,6,8,10,12,14,16,18]

plt.scatter(x,y, label='Skitscat', color='k')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot')
plt.legend()
plt.show()