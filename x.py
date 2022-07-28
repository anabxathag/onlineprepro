"""X"""
def main():
    """X"""
    numb = int(input())
    for row in range(numb):
        for column in range(numb):
            if column == row:
                print("*", end=" ")
            elif column + row == numb - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
main()
