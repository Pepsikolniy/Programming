def bmi(weight: float, height: float) -> float:
    return weight / (height*height)
def print_bmi(bmi: float) -> float:
    if bmi < 18.0:
        print("Underweight")
    elif bmi >= 18.0 and bmi < 25.0:
        print("Normal")
    elif bmi >= 25.0 and bmi < 30.0:
         print("Overweight")
    elif bmi > 30:
        print("Obesity")

weight, height = map(int, input().split())
height /= 100
print_bmi(bmi(weight, height))
