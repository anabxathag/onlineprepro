"""TENET"""
def main():
    """Print ช้อความตามจำนวนบรรทัดที่กำหนด"""
    num = int(input())
    iso = 0
    for iso in range(num):
        iso = iso
        ton = input()
        if ton == ton[::-1]:
            print(ton)
main()
