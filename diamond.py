"""Diamond"""
def main():
    """Diamond"""
    hig = int(input())
    for iso in range(0, hig):
        if iso <= (hig // 2):
            print(" " * ((hig // 2) - iso), end="")
            print("*" * ((2 * iso) + 1))
        else:
            print(" " * (iso - (hig // 2)), end="")
            print("*" * (hig - ((2 * iso) - hig) - 1))
main()
