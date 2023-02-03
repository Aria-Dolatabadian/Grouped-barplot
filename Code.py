import numpy as np
import matplotlib.pyplot as plt
# set width of bar
barWidth = 0.25
# set height of bar
bars1 = [12, 30, 1, 8, 22]
bars2 = [28, 6, 16, 5, 10]
bars3 = [29, 3, 24, 25, 17]
# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
# Make the plot
plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='black', label='50kg')
plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='black', label='100kg')
plt.bar(r3, bars3, color='#2d7f5e', width=barWidth, edgecolor='black', label='150kg')
# Add xticks on the middle of the group bars
plt.xlabel('Crops', fontweight='bold', color='red', fontsize='10', horizontalalignment='center')
plt.ylabel('Yield', fontweight='normal', color='green', fontsize='12', horizontalalignment='center')
plt.xticks([r + barWidth for r in range(len(bars1))], ['Wheat', 'Barley', 'Canola', 'Corn', 'Bean'])
# Create legend & Show graphic
plt.legend()
plt.show()
