def lionelRichie():
    print("Hello, is it me you're looking for?")

def main():
    n = int(input("Enter a number: "))
    hello_list = [lionelRichie] * n
    for hello_func in hello_list:
        hello_func()

main()