# simple version

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = (weight)/(height**2)
print(int(BMI))


# upgraded version
bmi = int(weight/height**2)

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you're underweight")
elif bmi < 25 & bmi >= 18.5:
  print(f"Your BMI is {bmi}, you have a normal weight")
elif bmi < 30 & bmi >= 25:
  print(f"Your BMI is {bmi}, you're obese")
else: 
  print(f"Your BMI is {bmi}, you're clinically obese")
  





