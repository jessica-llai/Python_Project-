

def add(a1, a2):
  return a1 + a2
def subtract(a1, a2):
  return a1 - a2
def multiply(a1, a2):
  return a1 * a2
def devide(a1, a2):
  return a1 / a2
def exponential(a1, a2):
  return a1 ** a2

calc={
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": devide,
  "**": exponential
}
def calculation():
  num1 = float(input("what's your first number?"))
  for symbol in calc:
      print(symbol)
      
  stop = False
  while not stop:
      
    op_symbol = input("pick one symbol")
    num2 = float(input("what's your next number?"))
    
    
    result = calc[op_symbol](num1, num2)
    print(f" {num1} {op_symbol} {num2} = {result}")
  
    if input("type y to continue the calculation, type n to exit") == "n":
        stop = True
        calculation()
        
    else: num1 = result
    

calculation()
  
  
  
  
