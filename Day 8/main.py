from art import logo
from replit import clear
print(logo)

def add(num1, num2):
  return(num1 + num2) 

def subtract(num1, num2):
  return(num1 - num2) 

def multiply(num1, num2):
  return(num1 * num2) 

def divide(num1, num2):
  return(num1 / num2) 

operation = {
  "+" : add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  num1 = float(input("Enter first number:\n"))

  for symbols in operation:
    print(symbols)

  end_of_calc = True
  while end_of_calc:
    operator = input("Enter an operator for calculation:\n")
    num2 = float(input("Enter another number:\n"))

    calc = operation[operator]
    answer = calc(num1, num2)
    print(f"{num1} {operator} {num2} = {answer}") 
    another = input("Type 'y' to calculate again, or 'a' to start again, else 'n': \n")
    if another == "y":
      num1 = answer
    elif another == "a":
      calculator()
      clear()
    else:
      end_of_calc = False
calculator()