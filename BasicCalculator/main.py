# define the functions needed, + - * /
# print options to the user
# ask for values
# call the functions
# while loop to continue the program until the user wants to exit


def add(a,b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer)+"\n")
    
def subtract(a,b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer)+"\n")
    
def multiply(a,b):
    answer = a* b
    print(str(a) + " * " + str(b) + " = " + str(answer)+"\n")
    
def divide(a,b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer)+"\n")

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E: Exit")

    a = int(input("input first number: "))
    b = int(input("input second number: "))
    choice = str(input("Input your choice: ")).lower()

    if choice == "a":
        print("Addition")
        add(a,b)
        
    elif choice == "b":
        print("Subtraction")
        subtract(a,b)
        
    elif choice == "c":
        print("Multiplication")
        multiply(a,b)
        
    elif choice == "d":
        print("Division")
        divide(a,b)

    elif choice == 'e':
        print("Program ended")
        break