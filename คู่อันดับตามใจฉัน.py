"""คู่อันดับแบบตามใจฉัน"""
def main():
    """คู่อันดับแบบตามใจฉัน"""
    runo = int(input())
    cole = int(input())
    for row in range(1, runo + 1):
        for column in range(1, cole + 1):
            print((row, column), end=" ")
        print()
main()
