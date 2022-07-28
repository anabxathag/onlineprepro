"""รวมเงิน"""
def main():
    """Print ชื่อคน2คน เงินรวม สาขา"""
    firstn = input()
    secondn = input()
    firmon = float(input())
    secmon = float(input())
    allmon = firmon + secmon
    team = input()
    separ = input()
    print(firstn, secondn + separ + str(allmon) + separ + team)
main()
