"""4 Addict"""
def main():
    """Print ข้อความตามจำนวนครั้งที่หารได้ คำตอบเป็นทศนิยม4ตำแหน่ง """
    ant = float(input())
    big = str(input())
    num = ((((ant + 4)**0.25 + (ant / 4)) / (4 * ant - 4)) * 44)
    pig = int(ant // 44)
    print(big * pig)
    print("%.4f" %num)
main()
