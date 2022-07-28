"""Machine"""
def main():
    """เอาเลขคี่และผลรวม"""
    beg, eno = int(input()), int(input())
    iso = 0 #enoใส่เลขคู่ตลอด
    total = 0
    if beg < eno:
        print("Integer Pass :", end="")
        for iso in range(beg, eno + 1):
            if iso % 2 != 0:
                print(" " + str(iso), end="")
                total += iso
        print("\nSum Answer : " + str(total))
    elif beg > eno:
        print("Integer Pass :", end="")
        for iso in range(beg, eno, -1):
            if iso % 2 != 0:
                print(" " + str(iso), end="")
                total += iso
        print("\nSum Answer : " + str(total))
main()
