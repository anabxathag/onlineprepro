'''[Onsite Day 2] โดนใยแมงมุม เหมือนโดนเธอกุมหัวใจ'''
def main():
    '''สร้างใยแมงมุม'''
    numb = int(input())
    web = (2 * numb) + 1
    for row in range(web):
        for column in range(web):
            if column == row:
                print("*", end=" ")
            elif column + row == web - 1:
                print("*", end=" ")
            elif row == 1 or row == web - 2:
                print("*", end=" ")
            elif column == 1 or column == web - 2:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
main()
