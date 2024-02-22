import matplotlib.pyplot as plt
from matplotlib import  style

style.use("ggplot")
#Plotting our canvas
x = [5,8,9]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]

plt.plot(x,y,'g',label='line one', linewidth=5)
plt.plot(x2,y2,'c',label='line two', linewidth=5)
#
# #Showing what we plotted
plt.title("Demo graph")
plt.xlabel("Minumum Temperature")
plt.ylabel("Maximum Temperature")

plt.legend() #to add legend information to the top of your graph
plt.grid(True, color='k') #to  add grid line
plt.show()

#to add style to the graph
