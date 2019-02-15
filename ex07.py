#ex07.py

def main():
    print("The program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter a number between 0 and 2: "))
    for i in range(10):
        x = 3.9 * x * (1-x)
        y = 3.9 * x * (1-x)
        print(x,y)
main()