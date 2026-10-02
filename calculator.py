import os
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
operations_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator_function():
 num1=int(input("enter the first number:"))
 for symbol in operations_dict:
     print(symbol)

 continue_flag=True
 while continue_flag:
   op_symbol=input("pick an operation:")
   num2=int(input("enter the second number:"))
   calculator=operations_dict[op_symbol]
   output=calculator(num1,num2)
   print(f"{num1} {op_symbol} {num2} = {output}")
   should_continue=input(f"enter 'y' to continue calculation with {output} or 'n' to start a new calculation or 'x' to exit").lower()
   if should_continue=='y':
    num1=output
   elif should_continue=='n':
    continue_flag=False
    os.system('cls')
    calculator_function()
   else:
      continue_flag=False
      print("bye")
calculator_function()