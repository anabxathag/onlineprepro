"""Increase"""
def main():
    """Print ผมรวมของเลขที่รับเข้ามา"""
    num = 0
    summa = 0
    while num >= 0:
        num = int(input())
        if num < 0:
            break
        summa += num
    print(summa)
main()
