def remove_nth_element(list1, n):

  if n < 0 or n >= len(list1):
    raise IndexError("Invalid index.")

  del list1[n]
  return list1


list1 = [int(x) for x in input("Enter a list of integers: ").split()]
n = int(input("Enter the index of the element to remove (1-based index): "))

list1 = remove_nth_element(list1, n)
print("List with the nth element removed:", list1)