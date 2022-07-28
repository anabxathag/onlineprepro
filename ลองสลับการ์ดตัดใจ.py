"""ลองสลับการ์ด แล้วตัดขาดจากใจเธออีกครั้ง"""
def main():
    """ระบุตำแหน่งของการ์ดที่สลับ"""
    num = int(input())
    card1, card2, card3 = "A", "B", "C"
    for iso in range(num):
        iso = iso
        switch = int(input())
        if switch == 12 or switch == 21:
            (card2, card1) = (card1, card2)
        elif switch == 32 or switch == 23:
            (card2, card3) = (card3, card2)
        elif switch == 13 or switch == 31:
            (card1, card3) = (card3, card1)
    print(card1)
    print(card2)
    print(card3)
main()
