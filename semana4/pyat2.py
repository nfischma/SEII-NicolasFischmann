import numpy as np
import matplotlib.pyplot as plt
a1 = np.array([4,6,8,2])
a2 = np.zeros(10)
a3 = np.ones(4)
a4 = np.random.random(10)
a5 = np.random.randn(10)
a6 = np.linspace(0, 10, 100)
a7 = np.arange(0, 10, 0.2)
print("array operations")
print(a1*2)
print(2*a1>10)
print(1/a4 + a4)
plt.plot(a6, a6**2)
plt.show()
plt.hist(a4)
plt.show()
def f(x):
    return x**2 * np.sin(x) / np.exp(-x)

plt.plot(a7, f(a7))

print()
print("Array indexing/slicing")
a1 = np.array([2,4,6,8,10])
print('a1[2]',a1[2])
print('a1[2:]',a1[2:])
print('a1[:-2]',a1[:-2])
print('a1[::2]',a1[::2])
print('a1>3',a1>3)
print('a1[a1>3]',a1[a1>3])
names = np.array(['Jim', 'Luke', 'Josh', 'Pete'])
first_letter_j = np.vectorize(lambda s: s[0])(names)=='J'
print(names[first_letter_j])
print('a1%4', a1%4)
print('a1%4==0',a1%4==0)
print('a1[a1%4==0]', a1[a1%4==0])

print()
print("Calculus/ statistical Functions")
a1 = 2*np.random.randn(10000) + 10
print('np.mean(a1)',np.mean(a1))
print('np.std(a1)',np.std(a1))
print('np.percentile(a1, 80)',np.percentile(a1, 80))
x = np.linspace(1, 10, 100)
y = 1/x**2 * np.sin(x)
dydx = np.gradient(y,x)
y_integral = np.cumsum(y) * (x[1]-x[0])
plt.plot(x,y)
plt.plot(x,dydx)
plt.plot(x,y_integral)
plt.show()