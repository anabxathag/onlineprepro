"""Countdown"""
def main():
    """แสดงการนับถอยหลัง บรรทัดสุดท้ายเป็นคำว่า Prepro 65 !!"""
    countdown = int(input())
    while countdown > 0:
        print(countdown)
        countdown -= 1
    print("Prepro 65 !!")
main()
