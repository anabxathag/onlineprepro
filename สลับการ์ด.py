"""ลองสลับการ์ด แล้วตัดขาดจากใจเธอ"""
def main():
    """Print การ์ดตำแหน่งที่2"""
    switch = int(input())
    if switch == 12 or switch == 21:
        print("A")
    elif switch == 32 or switch == 23:
        print("C")
    else:
        print("B")
main()
