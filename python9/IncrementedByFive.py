def incrementByFive(num):
    for i in range(0, num + 1, 5):
        print(i)

num = int(input("Enter a number: "))
incrementByFive(num)