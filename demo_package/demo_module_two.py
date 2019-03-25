from demo_module_one import Calculator

def ask_for_input():
    a = input("Enter a number: ")
    b = input("Enter a number: ")

    return a, b


if __name__ == '__main__':
    n1, n2 = ask_for_input()
    calc = Calculator(n1, n2)
    sum = calc.add()

    print("Sum of two given number is :",sum)