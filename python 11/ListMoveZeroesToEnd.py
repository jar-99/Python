def move_zeros_to_end(list1):

  non_zero_list = []
  for element in list1:
    if element != 0:
      non_zero_list.append(element)


  for i in range(len(list1) - len(non_zero_list)):
    non_zero_list.append(0)

  return non_zero_list



list1 = [int(x) for x in input("Enter a list of integers: ").split()]
list1 = move_zeros_to_end(list1)


print("List with zeroes moved to the end:", list1)