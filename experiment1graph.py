import matplotlib.pyplot as plt

xaxis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #number of prompts
y1 = [50.2, 46, 41.4, 34.4, 34.6, 32.4, 31.8, 30.4, 29.8, 33.4, 30] #opt 2.7 logit results
y2 = [81, 80, 82] #gpt logit results
y3 = [62.2, 41, 41.8] #opt 6.7 logit results

plt.plot(xaxis, y1, label = "opt-2.7 logit")
plt.plot(xaxis[:3], y2, label = "gpt-3 logit")
plt.plot(xaxis[:3], y3, label = "opt-6.7 logit")
plt.xlabel("Number of examples used in prompt (k)")
plt.ylabel("Accuracy (%)")
plt.legend()
plt.show()