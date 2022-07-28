"""Simple matrix"""
def main():
    """Matrixตามใจ"""
    row = int(input())
    column = int(input())
    for rol in range(row):
        for col in range(column):
            print((col + 1) * (rol + 1), end=" ")
        print()
main()
