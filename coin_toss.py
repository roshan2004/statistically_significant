import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
plt.style.use('ggplot')
np.random.seed(112)

# Initializing an empty list to store the number of heads in ten tosses in each experiment 
final_head = []

# Simulating the ten tosses of a coin 10000 times
for x in range(10000):
    heads = 0
    # Tossing of a coin 10 times
    for x in range(10):
        coin = np.random.randint(0,2)
        if coin == 1:
            heads +=1
        
    final_head.append(heads)

#Initializing a probability list
prob = []

# Storing the probability of the number of heads
for i in range(11):
    prob.append(final_head.count(i)/len(final_head))


# Plotting histrogram
plt.hist(final_head, bins = 10, edgecolor = 'k', density = True, color = 'skyblue', alpha = 0.6)

# Plotting a line plot of probabilities of each number of heads
plt.plot(prob, linestyle = '--', marker = 'o', color = 'k')

# A vertical line to show mean
plt.axvline(np.mean(final_head), color = 'red', label = 'Mean', alpha = 0.4, linestyle = '--')

# A vertical line to show median
plt.axvline(np.median(final_head), color = 'yellow', label = 'Median', alpha = 1.0, linestyle = 'dotted')

# A vertical line to show mode
plt.axvline(stats.mode(final_head)[0], color = 'blue', label = 'Mode', alpha = 0.4)

plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title('Probability Distribution')
plt.legend()

# Adding texts (probabilities) 
for i in range(11):
	plt.text(i, prob[i], round(prob[i], 3))

plt.xticks(range(11))
plt.show()




