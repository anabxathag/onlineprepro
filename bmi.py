"""กินมากพุงคงอยู่ จงมาดูอ้วนแล้วไง"""
def main():
    """Print name,high,weight,bmi"""
    name, weight, high = input(), int(input()), int(input())/100    # W/(H**2)
    bmi = weight / (high ** 2)
    print("Name: "+ name)
    print("Weight: %d kg." %weight)
    print("Height: %.2f m." %high)
    print("BMI: %.2f" %bmi)
main()
