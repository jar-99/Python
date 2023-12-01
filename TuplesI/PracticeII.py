def remove_elements(tuple1, tuple2):
    result = ()

    for i in tuple1:
        if i not in tuple2:
            result += (i,)

    return result

tuple1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
tuple2 = ("orange", "kiwi", "banana")

result = remove_elements(tuple1, tuple2)
print(result)