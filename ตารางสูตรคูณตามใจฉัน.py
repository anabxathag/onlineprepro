"""ตารางสูตรคูณแบบตามใจฉัน"""
def main():
    """สูตรคูณแบบตามใจฉัน"""
    print("-----")
    runo = int(input())
    cole = int(input())
    for row in range(2, runo + 1):
        for column in range(1, cole + 1):
            print(row, "x", column, "=", row * column)
        print("-----")
main()
