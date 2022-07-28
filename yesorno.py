"""yes or no"""
def main():
    """print yes or no"""
    messa = input()
    if messa.isalnum() == True: # ตัวเลขและข้อความ
        print("Yes, it is.")
    else:
        print("No, it's not.")
main()
