import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
np.random.seed(123)
final_head = []

for x in range(10000):
    heads = 0
    for x in range(10):
        coin = np.random.randint(0,2)
        if coin == 1:
            heads +=1
        
    final_head.append(heads)

prob = []

print(final_head.count(0))

for i in range(11):
    prob.append(final_head.count(i)/len(final_head))
print(prob)


plt.hist(final_head, bins = 10, edgecolor = 'k', density = True, color = 'skyblue', alpha = 0.6)
plt.plot(prob, linestyle = '--', marker = 'o', color = 'k')
plt.axvline(np.mean(final_head), color = 'red', label = 'Mean')
plt.axvline(np.median(final_head), color = 'yellow', label = 'Median')
# plt.axvline(stats.mode(final_head)[0], color = 'blue', label = 'Mode')

plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.legend()
plt.xticks(range(11))
plt.show()




