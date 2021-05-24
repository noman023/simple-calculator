def calculator():
    num1 = float(input("Enter The First Number: "))
    relation = input("Give An Operator(+,-,*,/,%): ")
    num2 = float(input("Enter The Second Number: "))
    if relation == "+":
        print("The Result Is:", (num1 + num2)) 
    elif relation == "-":
        print("The Result Is:", (num1 - num2))
    elif relation == "*":
        print("The Result Is:" , (num1 * num2)) 
    elif relation == "/":
        print("The Result Is:", (num1 / num2))
    elif relation == "%":
      print("The Result Is:", (num1 % num2))
calculator()
