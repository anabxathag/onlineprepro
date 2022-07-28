"""ฺอักษรที่หายไป"""


def main():
    """แปลงตัวเลขเป็นข้อความ"""
    messa = input()
    if messa.count('"') != 0:
        inter = messa[messa.find('"') + 1: messa.rfind('"')]  # เอาแต่ตัวเลข
        doubin = messa[messa.find('"'): messa.rfind('"') + 1]  # เอา".ตัวเลข"
        gon = chr(int(inter))  # แปลงตัวเลขเป็นข้อความ
        print(messa.replace(doubin, gon))
    else:
        print("No error")


main()
