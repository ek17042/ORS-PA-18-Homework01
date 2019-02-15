#ex06c.py
def main():
    print("This program illutrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(100):
        x = 3.9 * x - 3.9 * x * x
        print(x)
main()
