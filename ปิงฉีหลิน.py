"""ปิงฉีหลิน"""
def main():
    """ทำไอติมโคน"""
    size = int(input())
    flavor = input().lower()
    if flavor == "m" or flavor == "s" or flavor == "c" or flavor == "b" or flavor == "r":
        for iso in range(0, (2 * size) - 1):
            if iso <= (((2 * size) - 1) // 2):
                print(" " * ((((2 * size) - 2) // 2) - iso), end="")
                print(flavor * ((2 * iso) + 1))
            else:
                print(" " * (iso - (((2 * size) - 1) // 2)), end="")
                print("_" * (((2 * size) - 1) - ((2 * iso) - ((2 * size) - 1)) - 1))
    else:
        print("Hey!,buy another shop.")
main()
