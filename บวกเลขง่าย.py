"""บวกเลขง่ายๆ"""
def main():
    """หาผลรวมทั้งหมดของจำนวนเต็ม 10 จำนวน"""
    total = 0
    for iso in range(10):
        iso = iso
        num = int(input())
        if num < 0:
            total -= 5
        elif num >= 0:
            total += num
    if total < 0:
        print(-5)
    elif total >= 0:
        print(total)
main()
