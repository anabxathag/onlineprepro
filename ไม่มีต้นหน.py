"""ไม่มีต้นหนก็ลำบากหน่อยนะ"""
def main():
    """print จำนวนปลา"""
    fish = input()
    numfish = fish.count("<^))))><")
    numcrew = int(input())
    if numfish == numcrew:
        print("We have enough fish for everyone.")
    elif numfish > numcrew:
        print("We have many fish ahoyy!!!")
    elif numfish < numcrew and numfish != 0:
        if (2*numfish) % numcrew == 0:
            print("We can share the fish together Yahoooo!!!")
        else:
            print("No one will eat them  because we cannot be divided the fish.")
    elif numfish == 0:
        print("No one will eat them  because we cannot be divided the fish.")
main()
