#Matplotlib Basics Code Different Concepts
##Example 1
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]
plt.plot(x, y)
plt.title("Sales")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

#Example 2
x=[1,2,3,4,5]
y=[10,20,30,40,50]
plt.figure(figsize=(10,5))
plt.plot(x,y)
plt.title("Graph Design")
plt.show()

#Example 3
x=[2,3,4,5,7]
y=[11,22,33,5,6]
plt.plot(x,y)
plt.title("Save the graph")
plt.savefig("Save the graph.png")
plt.show()

#Example 4
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,10,0.1)
y=x**2
plt.plot(x,y)
plt.title("y = x²")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

#Example 5
import numpy as np 
import matplotlib.pyplot as plt
x= np.linspace(-10,10,100)
y1=x**2
y2=x**3
plt.plot(x,y1,label="x^2")
plt.plot(x,y2,label="x^3")
plt.title("Mathematical Functions")
plt.xlabel("x")
plt.ylabel("y")

plt.legend()
plt.grid(True)

plt.show()

#Example 6
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
y = np.sin(x)
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, y)
ax.set_title("Sine Wave")
ax.set_xlabel("X")
ax.set_ylabel("sin(X)")

ax.grid(True)

plt.show()

#Example 7
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(1, 11)
sales = np.array([10, 20, 25, 30, 35, 40, 45, 50, 55, 60])
profit = np.array([2, 5, 7, 9, 12, 15, 18, 20, 23, 25])
fig, ax1 = plt.subplots()
ax1.plot(x, sales)
ax1.set_xlabel("Month")
ax1.set_ylabel("Sales")
ax2 = ax1.twinx()
ax2.plot(x, profit)
ax2.set_ylabel("Profit")

plt.title("Sales and Profit")

plt.show()

#Example 9
import numpy as np
import matplotlib.pyplot as plt
data = np.array([
    [10,23,23,45,23],
    [23,54,76,98,24],
    [21,32,54,76,89]
])
plt.imshow(data)
plt.colorbar()
plt.title("Heatmap")
plt.show()

#Example 10
import matplotlib.pyplot as plt
epochs=[11,2,3,5,67,8,7,5,9,8]
loss=[
    0.99,
    0.95,
    0.88,
    0.77,
    0.66,
    0.55,
    0.44,
    0.33,
    0.32,
    0.22
]
plt.plot(epochs,loss,marker="o")
plt.title("Spogmai")
plt.xlabel("Huda")
plt.ylabel("Talhoooo")
plt.grid(True)
plt.show()

#Example 11
import matplotlib.pyplot as plt
epochs=[1,2,3,4,5,6,7,8,9]
accuracy=[11,22,333,44,55,66,77,88,99]
plt.plot(epochs,accuracy,marker="o")
plt.title("accauracy Management ")
plt.xlabel("epochs")
plt.ylabel("accuracy(%)")
plt.grid(True)
plt.show()

#Example 12
import matplotlib.pyplot as plt

epochs = range(1, 11)

loss = [0.9, 0.75, 0.62, 0.5, 0.42,
        0.35, 0.30, 0.25, 0.22, 0.20]

accuracy = [50, 55, 60, 65, 70,
            74, 78, 82, 85, 88]

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

ax[0].plot(epochs, loss, marker="o")
ax[0].set_title("Training Loss")
ax[0].set_xlabel("Epoch")
ax[0].set_ylabel("Loss")

ax[1].plot(epochs, accuracy, marker="o")
ax[1].set_title("Training Accuracy")
ax[1].set_xlabel("Epoch")
ax[1].set_ylabel("Accuracy (%)")

plt.tight_layout()

plt.show()

#Example 13
import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [100, 150, 130, 180, 220]
}

df = pd.DataFrame(data)

plt.plot(df["Month"], df["Sales"], marker="o")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()