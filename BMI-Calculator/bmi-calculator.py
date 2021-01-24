def bmi_calculator(height, weight):
    bmi = round(weight / ((height / 100) ** 2), 2)
    print('Your BMI(Body Mass Index) is:', bmi)

height = float(input('Enter your height in cm: '))
weight = float(input('Enter your weight in kg: '))
bmi_calculator(height, weight)