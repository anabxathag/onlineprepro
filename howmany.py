"""ฺHow many"""
def main():
    """จำนวนครั้งที่นับคำหรือตัวอักษรนั้นๆได้"""
    mess = input().lower()
    wocha = input().lower()
    if len(wocha) == 1:
        if mess.count(wocha) != 0:
            print("Character : %d" %(mess.count(wocha)))
        elif mess.count(wocha) == 0:
            print("No word and character.")
    elif len(wocha) > 1:
        if mess.count(wocha) != 0:
            print("Word : %d" %(mess.count(wocha)))
        elif mess.count(wocha) == 0:
            print("No word and character.")
main()
