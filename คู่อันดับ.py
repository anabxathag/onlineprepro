"""คู่อันดับแบบตามใจฉัน"""
def main():
    """คู่อันดับแบบตามใจฉัน"""
    numb = int(input())
    for row in range(1, (2 * numb) + 2):
        for col in range(1, (2 * numb) + 2):
            print("(%02d, %02d)" %(abs(row - numb - 1), abs(col - numb - 1)), end=" ")
        print()
main()
