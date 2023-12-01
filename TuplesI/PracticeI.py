def remove_elements(tuple1, tuple2):
    result = ()

    for i in tuple1:
        if i not in tuple2:
            result += (i,)

    return result

tuple1 = ("apple", "banana","cherry")
tuple2 = ("dewberry","eggplant")

result = remove_elements(tuple1, tuple2)
combined = tuple1 + tuple2
combined_result = combined
print(combined_result)