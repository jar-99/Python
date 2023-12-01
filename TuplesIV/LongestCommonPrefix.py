def longestCommonPrefix(arr):
    if len(arr) == 0:
        return ""

    shortest = min(arr, key=len)

    for i, char in enumerate(shortest):
        for word in arr:
            if word[i] != char:
                return shortest[:i]

    return shortest

def main():
    arr = input("Enter the strings separated by enter: ")
    print("Longest common prefix is: ", longestCommonPrefix(arr))


main()