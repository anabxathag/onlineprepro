"""Ratatype"""
def main():
    """Print จำนวนครั้งที่ใช้นิ้วชี้ขวา"""
    messa = input()
    total = 0
    for iso in "67YUHJNM":
        total += messa.count(iso)
    print(total)
main()
