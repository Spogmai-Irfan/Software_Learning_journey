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

#Example 6
subjects = ["Math", "Python", "Pandas", "NumPy"]
marks = [80, 90, 85, 95]

plt.barh(subjects, marks)

plt.title("Student Marks")

plt.show()

#Example 7
hours = [1, 2, 3, 4, 5, 6, 7]
marks = [40, 45, 50, 60, 65, 75, 85]

plt.scatter(hours, marks)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

#Example 8
marks = [45, 50, 55, 60, 62, 65, 67, 70,
         72, 75, 78, 80, 82, 85, 90, 95]

plt.hist(marks, bins=5)

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()

#Example 9
subjects = ["Python", "Math", "Pandas", "NumPy"]
hours = [10, 5, 8, 7]

plt.pie(
    hours,
    labels=subjects,
    autopct="%1.1f%%"
)
plt.title("Study Time")
plt.show()

#Example 10
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 15, 30, 25]
y2 = [5, 15, 25, 20, 35]
plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Line Graph")
plt.subplot(1, 2, 2)
plt.bar(x, y2)
plt.title("Bar Graph")
plt.show()

