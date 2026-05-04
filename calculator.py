num1 = float(input("Enter first Number: "))
op = input("Enter operations (+,-,*,/,%,**): ").strip()
num2 = float(input("Enter second Number: "))

if op == "+":
   result = num1 + num2
elif op == "-":
   result = num1 - num2   
elif op == "*":
   result = num1 * num2   
elif op == "**":
   result = num1 ** num2   
elif op == "/":
    if num2 != 0:
     result = num1 / num2 
    else:
       print("Cannot divide by zero")
       exit()   
elif op == "%":
   if num2 != 0:
       result = num1 % num2
   else:
      print("Cannot take modulus withg zero")   
      exit()
else:
   print("Invalid operation")
   exit()

print("Result:", result)         
    



