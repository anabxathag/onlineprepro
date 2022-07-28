"""สมการตัวน้อย"""
def main():
    """Print คำตอบของสมการ"""
    act = float(input())
    big = float(input())
    cat = float(input())
    dog = float(input())
    xia = float(input())
    yoyo = float(input())
    print("%.2f" %float((((big / (act ** 2 / dog)) + ((xia * big) / act)) * yoyo) / (yoyo * cat)))
main()
