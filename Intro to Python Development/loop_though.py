name = [ 'Hermann','Benedicte']   
print(name)
index = 0
while index < len(name):
    print(name[index])
    # change the condition
    index = index + 1

items = ["crayon", "scissors", "paper", "glitter glue", "markers", "pens"]

for item in items:
    print(f"The item is: {item}")

for number in range (10):
    print(number)
# This loop will start with 100, and go up to, but not including 200
for i in range(100, 200):
    print(i)

# This loop will do the same thing, but this time, it will count by 10's
for i in range(100, 200, 10):
    print(i)
for i in range(5):
    print(i)
    for j in range(10, 13):
        print(f"--{j}")