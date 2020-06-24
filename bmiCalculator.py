
name = input("Enter a name:\n")
weight = int(input("Enter a weight in KGs:\n"))
height = int(input("Enter a height in CMs:\n"))

def bmi(name, weight, height):
    height = height / 100
    bmi = weight / (height * height)
    print ("BMI is ", int(bmi))
    if bmi > 30:
        return name + " is Obese"
    elif 29.9 > bmi >25:
        return name + " is overweight"
    elif 24.9 > bmi > 18.5:
        return name + " has normal weight"
    else:
        return name + " is Underweight"

print(bmi(name, weight, height))