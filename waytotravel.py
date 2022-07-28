"""Way to travel"""
def main():
    """Print เดินทางไปด้วยอะไร,ไม่ไป,error"""
    weather = input()
    impo = input()
    dis = float(input())
    if weather == "sunny":
        if 0 <= dis < 1:
            print("Walk")
        elif 1 <= dis < 20:
            print("Motorcycle")
        elif 20 <= dis < 300:
            print("Car")
        elif 300 <= dis:
            print("Private jet")
    elif weather == "rainy" and impo == "important":
        if 0 <= dis < 1:
            print("Walk")
        elif 1 <= dis < 20:
            print("Motorcycle")
        elif 20 <= dis < 300:
            print("Car")
        elif 300 <= dis:
            print("Private jet")
    elif weather == "rainy" and impo == "not important":
        print("Not go")
    elif dis < 0:
        print("Error")
main()
