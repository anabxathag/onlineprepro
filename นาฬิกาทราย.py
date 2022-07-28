"""นาฬิกาทราย"""
def main():
    """นาฬิกาทราย"""
    numb = int(input())
    print(("*" * numb * 2) + "*")
    for row in range(2*numb + 1):
        for column in range(2*numb +1):
            if column == row:
                print("*", end="")
            elif column + row == 2*numb:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    print(("*" * numb * 2) + "*")
main()
