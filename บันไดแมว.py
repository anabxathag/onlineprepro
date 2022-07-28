"""บันไดแมว"""
def main():
    """บันไดที่กลับหัว"""
    number = int(input())
    for row in range(number):
        for column in range(number):
            if column < row:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        print()
main()
