#ex03.py

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 2.0 * x * (1-x)
        print(x)
main()
#for the same value the results in ex02.py and ex03.py differ in huge amounts