print("Welcome to the Heart Rate Calculator!")

name = input("Pease,enter your name:")
age=int(input("Please enter your age: "))
max_rate = 220 - age
slowest = max_rate * 0.65
fastest = max_rate * 0.85
print(f"Hello {name}, when you exercise to strengthen your heart, you should")
print(f"keep your heart rate between {slowest:.0f} and {fastest:.0f} beats per minute.")