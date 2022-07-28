"""Restaurant"""
def main():
    """Print ค่าอาหารทั้งหมด """
    age = int(input())
    num = int(input())
    if age >= 60:
        if num == 1:
            print("Free")
        elif num > 1:
            print("Pay %d bath" %((num*100)*0.5))
    elif 0 <= age < 60:
        print("Pay %d bath" %(num*100))
main()
