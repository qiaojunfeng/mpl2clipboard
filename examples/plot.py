import mpl2clipboard
import matplotlib.pyplot as plt

plt.plot([0, 1], [0, 1.0], label='Label 1')
plt.plot([0, 1], [0, 1.1], label='Label 2')
plt.plot([0, 1], [0, 1.2], label='Label 3')
plt.plot([0, 1], [0, 1.3], label='Label 4')
plt.plot([0, 1], [0, 1.4], label='Label 5')

# Change the number of columns here
plt.legend(ncol=2)

plt.show()
