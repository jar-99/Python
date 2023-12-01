
def hello():
    print("Call counter: ")

def main():
    n = int(input("Enter a number: "))
    hello_list = [hello] * n
    for hello_func in hello_list:
        hello_func()

main()