"""Geometic Sequence"""
def main():
    """ลำดับเรขาคณิต ทศนิยม2ตำแหน่ง"""
    mem1 = float(input())
    num = int(input())
    ratio = float(input())
    for iso in range(num):
        print("%.2f" %(mem1 * (ratio ** iso)), end=" ")
main()
