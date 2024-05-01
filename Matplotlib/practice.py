import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [3,6,9,12,15]

plt.plot(x, y, scalex=True, scaley= True)
plt.xlabel('Minumum Score')
plt.ylabel('Correspomding Mark')
plt.show()