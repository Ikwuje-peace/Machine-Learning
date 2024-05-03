import matplotlib.pyplot as plt

scores = [71, 75, 89, 68, 79, 80, 90, 95, 76, 78, 77, 67, 55, 54, 79]
bins = [0, 10, 20, 30, 40 , 50, 60, 70, 75, 80, 90, 100]

plt.hist(scores, bins, histtype='bar', rwidth=0.9, label="Scores of students")
plt.xlabel('X')
plt.ylabel('Y')

plt.title('Histogram plot')

plt.legend()
plt.show()