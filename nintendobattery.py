"""[Quiz] Nintendo Battery"""
def main():
    """แสดงรูปแบตเตอรี่ และ เลขแบตเตอรี่เป็นเปอร์เซ็นต์"""
    import math
    batter = int(input())
    kwang = int(input())
    conbat = math.floor((batter / 100) * kwang)
    print("(" + (conbat * "O") + \
    ((kwang - conbat) * "_") + ")", \
    str(batter) + "%")
main()
