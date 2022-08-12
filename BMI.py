H = float(input ("enter your height in cm : "))
W = float(input ("enter your weight in kg : "))

BMI = W / (H/100)**2
print("YOUR BMI IS")

if (BMI <= 18.5):
    print("you are underweight")
elif(BMI>=18.5 and BMI<=24.9):
    print("you are healthy")
elif BMI >=25.0 :
    print("you are overweight")
else :
    print ("Obesity class")
