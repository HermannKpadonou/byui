"""# Example 3
import math
def main():
  radius = float(input("Enter the radius of a circle: "))
  area = circle_area()
  print(f"area: {area:.1f}")
def circle_area(radius):
  # Mistake! There is no variable named radius
  # defined inside this function, so the variable
  # radius cannot be used in this function.
  area = math.pi * radius * radius
  return area
main()  """

def func1():
  a=1
def func2():
  a=2
  func1()
  return a
a=0
print(func2())

def fullname(w1,w2):
  return w1 + ' ' + w2

f=fullname(w2='faith',w1='charity')
print(f)