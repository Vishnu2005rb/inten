
def add(x, y):
    return x + y

def subtract(x, y):
    
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice(1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            try:
                a = float(input("Enter a number: "))
                b = float(input("Enter b number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '1':
                print(f"sum  = {add(a,b)}")
            elif choice == '2':
                print(f"sum = {subtract(a,b)}")
            elif choice == '3':
                print(f"sum = {multiply(a,b)}")
            elif choice == '4':
                print(f"sum = {divide(a,b)}")
        else:
            print("Invalid Input")

        next_calculation = input("Do you want to perform another calculation? (y/n  ): ")
                                
        if next_calculation.lower() !='y':
            break

if __name__ == "__main__":
    calculator()





