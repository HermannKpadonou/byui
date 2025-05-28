# this is a comment because it has
# hash symbols at the beginning
# variable
length = 5
time = 7.2
in_flight = True
first_name = "Cho"
# string
greeting = "hello"
text = "23"
# boolean
found = True
# int
x = 14
# float
sample = 7.51
# list
colors = ["yellow","red","green","yellow","blue"]
samples = [6.5, 7.2, 7.0, 8.1, 7.2, 6.8, 6.8]
#Dictionnary
students = {
    "42-039-4736": "Clint Huish",
    "61-315-0160": "Amelia Davis",
    "10-450-1203": "Ana Soares",
    "75-421-2310": "Abdul Ali",
    "07-103-5621": "Amelia Davis"
}

text = input("Please Enter your name : ")
color = input("What is your favorite color? ")

print(f"Hello {text}, your favorite color is {color}.")

rate = input("Enter your heart rate: ")
print(f'Heart rate: {rate}')


# Example 1
# Create variables of different data types and then
# print the variable names, data types, and values.
a = "Her name is "  # string
b = "Isabella"      # string
c = a + b           # string plus string makes string
print(f"a: {type(a)} {a}")
print(f"b: {type(b)} {b}")
print(f"c: {type(c)} {c}")
print()
d = False  # boolean
e = True   # boolean
print(f"d: {type(d)} {d}")
print(f"e: {type(e)} {e}")
print()
f = 15     # int
g = 7.62   # float
h = f + g  # int plus float makes float
print(f"f: {type(f)} {f}")
print(f"g: {type(g)} {g}")
print(f"h: {type(h)} {h}")
print()
i = "True"   # string because of the surrounding quotes
j = "2.718"  # string because of the surrounding quotes
print(f"i: {type(i)} {i}")
print(f"j: {type(j)} {j}")

# Example 2
# The input function always returns a string.
k = input("Please enter a number: ")        # string
m = input("Please enter another number: ")  # string
n = k + m          # string plus string makes string
print(f"k: {type(k)} {k}")
print(f"m: {type(m)} {m}")
print(f"n: {type(n)} {n}")
print()
# The int and float functions convert a string to a number.
p = int(input("Please enter a number: "))          # int
q = float(input("Please enter another number: "))  # float
r = p + q                     # int plus float makes float
print(f"p: {type(p)} {p}")
print(f"q: {type(q)} {q}")
print(f"r: {type(r)} {r}")

x= 5
y= 3
z = int(x**y)  # int to int makes int
print(f"x: {type(x)} {x}")
print(f"y: {type(y)} {y}")
print(f"z: {type(z)} {z}")

print()

print(f"21 % 5 == {21 % 5}")
print(f"45 % 5 == {45 % 5}")
print(f"5 % 1 == {5 % 1}")
print(f"3 % 8 == {3 % 8}")
print(f"-3 % 8 == {-3 % 8}")
print(f"3 % -8 == {3 % -8}")
print(f"-3 % -8 == {-3 % -8}")
