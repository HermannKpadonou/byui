def main():
  # Create and print a list named fruit.
  fruit_list = ["pear", "banana", "apple", "mango"]
  print(f"original: {fruit_list}")

  #revserse the list
  fruit_list.reverse()
  print(f"reversed: {fruit_list}")

  #add a new fruit to the list
  fruit_list.append("orange")
  print(f"append orange: {fruit_list}")

    
  #insert a new fruit before apple
  fruit_list.insert(2, "cherry")
  print(f"insert cherry: {fruit_list}")

  #remove banana from the list
  fruit_list.remove("banana")
  print(f"remove banana: {fruit_list}")

  # extract the last fruit from the list
  last_fruit = fruit_list.pop()
  print(f"pop last fruit: {last_fruit}")
  # print the final list
  print(f"final list: {fruit_list}")

  # sort the list
  fruit_list.sort()   
  print(f"sorted list: {fruit_list}")

  #clear the list
  fruit_list.clear()
  print(f"cleared list: {fruit_list}")

if __name__ == "__main__":
  main()