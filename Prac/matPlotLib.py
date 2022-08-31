import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from sklearn.metrics import r2_score

xp = np.random.uniform(0.0, 5.0, 100000)
xp = np.random.normal(50.1, 10, 10000) #normal data distribution
yp = np.random.normal(30.2, 5, 10000)

slope, intercept, r, p, stat_err = stats.linregress(xp, yp)
print(r, 'r')

def myfunc(x):
    return slope * x + intercept

# xp = np.array([0, 10])
# yp = np.array([0, 250])

mymod = list(map(myfunc, xp))

plt.scatter(xp, yp)

#linear regression
plt.plot(xp, mymod)

# plt.hist(xp, 100)
# print(matplotlib.__version__)

#polynomial regression
mymodel = np.poly1d(np.polyfit(xp, yp, 3))
myline = np.linspace(0, 100, 1000)
plt.plot(myline, mymodel(myline))
print(r2_score(yp, mymodel(xp)))
plt.show()