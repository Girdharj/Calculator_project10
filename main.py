import os
import sys

def add(a,b):
  return a+b

def substract(a,b):
  return a-b

def multiply(a,b):
  return a*b

def divide(a,b):
  return a/b

def Calculator():
  print("NEW CALCULATiON")
  num1 = float(input("Enter the first number: "))
  
  symbols = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide
  }
  con = 'n'
  final = 0 
  while True:
    for key in symbols:
      print(key)
    sym = input("Please select a symbol from the given list: ")
    num2 = float(input("Enter the next number: "))
    cal = symbols[sym]
    if con == 'y':
      num1 = final
    final += cal(num1, num2) 
    print(f"you entered {num1} {sym} {num2} = {final}")
    con = input("Do you want to continue? y or n or ex: ").lower()
    if con == 'n':
      os.system('clear')
      Calculator()
    if con =='ex':
      os.system('clear')
      sys.exit()
  
  print(f"Your answer is {final}")

Calculator()