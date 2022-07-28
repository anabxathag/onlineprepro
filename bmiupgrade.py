"""BMI upgrade"""
def main():
    """Print ผลลัพธ์เป็นประเภทจำแนกของBMI"""
    weight, high, age = float(input()), float(input())/100, int(input())
    bmi = weight / (high ** 2)  # W/(H**2)
    if age >= 18:
        if bmi < 16:
            print("Severe Thinness")
        elif 16 <= bmi <= 16.99:
            print("Moderate Thinness")
        elif 17 <= bmi <= 18.49:
            print("Mild Thinness")
        elif 18.5 <= bmi <= 24.99:
            print("Normal")
        elif 25 <= bmi <= 29.99:
            print("Overweight")
        elif 30 <= bmi <= 34.99:
            print("Obese Class I")
        elif 35 <= bmi <= 39.99:
            print("Obese Class II")
        elif bmi >= 40:
            print("Obese Class III")
    else:
        print("Please use BMI for Children and Teens.")
main()
