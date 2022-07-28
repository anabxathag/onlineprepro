"""PeterPanframe"""
def main():
    """บรรทัด1"""
    messa = input()
    num_1 = 0
    print(".", end="")
    for iso in messa:
        iso = iso
        num_1 += 1
        if num_1 % 3 == 0:
            print(".◊..", end="")
        else:
            print(".♦..", end="")
    peter2(messa)
    peter3(messa)
    peter4(messa)
    peter5(messa)
def peter2(messa):
    """บรรทัด2"""
    num_2 = 0
    print()
    print(".", end="")
    for iso in messa:
        iso = iso
        num_2 += 1
        if num_2 % 3 == 0:
            print("◊.◊.", end="")
        else:
            print("♦.♦.", end="")
def peter3(messa):
    """บรรทัด3"""
    num_3 = 0
    print()
    print("♦", end="")
    for iso in messa:
        iso = iso
        num_3 += 1
        if num_3 % 3 == 1:
            print("."+ iso +".♦", end="")
        else:
            print("."+ iso +".◊", end="")
def peter4(messa):
    """บรรทัด4"""
    num_4 = 0
    print()
    print(".", end="")
    for iso in messa:
        iso = iso
        num_4 += 1
        if num_4 % 3 == 0:
            print("◊.◊.", end="")
        else:
            print("♦.♦.", end="")
def peter5(messa):
    """บรรทัด5"""
    num_5 = 0
    print()
    print(".", end="")
    for iso in messa:
        iso = iso
        num_5 += 1
        if num_5 % 3 == 0:
            print(".◊..", end="")
        else:
            print(".♦..", end="")
main()
