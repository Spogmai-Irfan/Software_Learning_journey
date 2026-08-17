#Example 2
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
temperature = [25, 27, 26, 30, 32]

plt.plot(days, temperature)

plt.title("Temperature During the Week")
plt.xlabel("Day")
plt.ylabel("Temperature")

plt.show()
#Example 3
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y,
    linestyle="--",
    marker="o"
)

plt.title("Sales")
plt.xlabel("Day")
plt.ylabel("Sales")

plt.show()

#Example 4
months = [1, 2, 3, 4, 5]

sales_2025 = [100, 120, 150, 170, 200]
sales_2026 = [110, 130, 160, 190, 230]

plt.plot(months, sales_2025, label="2025")
plt.plot(months, sales_2026, label="2026")

plt.title("Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.legend()

plt.show()

#Example 5
import matplotlib.pyplot as plt

subjects = ["Math", "Python", "Pandas", "NumPy"]
marks = [80, 90, 85, 95]

plt.bar(subjects, marks)

plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()