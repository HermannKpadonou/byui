def my_function(*fname):
    print(fname[1] + " Hello my dear " + fname[0])
    
my_function("Kynew225" , "well's")
my_function("Kpadonou" , "Hermann")


def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)