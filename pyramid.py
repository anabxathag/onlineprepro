"""Pyramid"""
def main():
    """make Pyramid"""
    king = 0
    number = int(input())
    for row in range(1, number + 1):
        for column in range(1, (number - row) + 1):
            column = column
            print(end="  ")
        while king != (2 * row) - 1:
            print("* ", end="")
            king += 1
        king = 0
        print()
main()
