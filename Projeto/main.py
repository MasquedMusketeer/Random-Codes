import matplotlib.pyplot as plt

x = [i for i in range(10)]
y = [2*i for i in range(10)]

plt.plot(x, y)
plt.show()

lista = [1, 2, 3, 4]

quadrado = [i*i for i in lista]
print(quadrado)