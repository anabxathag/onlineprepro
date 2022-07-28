"""[Quiz] โรงเรียนเวทย์มนต์เปิดรับสมัครแล้ว"""
def main():
    """คัดคนเข้าเรียน"""
    name = input()
    age = int(input())
    sex = input().capitalize()
    high = float(input())
    if sex == "Male":
        print("Mr. " + name + " Age: " + str(age) + " Height: %.2f" %high)
        if 13 <= age <= 15 and high >= 160:
            print("You can study in junior high school.")
        elif 16 <= age <= 18 and high >= 170:
            print("You can study in senior high school.")
        else:
            print("You can not join this school.")
    elif sex == "Female":
        print("Miss " + name + " Age: " + str(age) + " Height: %.2f" %high)
        if 13 <= age <= 15 and high >= 155:
            print("You can study in junior high school.")
        elif 16 <= age <= 18 and high >= 165:
            print("You can study in senior high school.")
        else:
            print("You can not join this school.")
main()
