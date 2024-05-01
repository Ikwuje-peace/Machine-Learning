import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [3,6,9,12,15]

x2 = [7,9,16,35,40]
y2 = [3,7,10,15,21]
plt.plot(x, y, scalex=True, scaley= True, color='k', label='First Graph')
plt.plot(x2, y2, label='Second graph', color='green', scalex=True, scaley=True)
plt.xlabel('Minumum Score')
plt.ylabel('Correspomding Mark')
plt.title('A Prctice Graph')
plt.legend()
plt.show()