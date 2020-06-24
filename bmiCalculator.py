
def bmi(name, weight, height):
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

print(bmi("omar", 70, 1.72))