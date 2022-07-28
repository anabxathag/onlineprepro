"""เรียงข้อความ ยามเธออ่านไม่ตอบ"""
def main():
    """เรียงจากความยาวน้อยไปมาก"""
    messa1, messa2, messa3 = input().capitalize(), input().capitalize(), input().capitalize()
    if len(messa1) < len(messa2) < len(messa3):
        print(messa1)
        print(messa2)
        print(messa3)
    elif len(messa1) < len(messa3) < len(messa2):
        print(messa1)
        print(messa3)
        print(messa2)
    elif len(messa2) < len(messa1) < len(messa3):
        print(messa2)
        print(messa1)
        print(messa3)
    elif len(messa2) < len(messa3) < len(messa1):
        print(messa2)
        print(messa3)
        print(messa1)
    elif len(messa3) < len(messa2) < len(messa1):
        print(messa3)
        print(messa2)
        print(messa1)
    elif len(messa3) < len(messa1) < len(messa2):
        print(messa3)
        print(messa1)
        print(messa2)
main()
