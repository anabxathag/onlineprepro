"""อันดับสองรองสุดท้าย"""
def main():
    """หาอันดับสองของตัวที่น้อยสุด"""
    inum = 0
    min1 = 0
    min2 = 0
    dis = 0
    while inum < 10:
        inum += 1
        num = int(input())
        if num < min1:
            temp = min1
            min1 = num
            min2 = temp
            dis = min2 - min1
        elif min1 == 0:
            min1 = num
            min2 = num
            dis = num
        elif num > min1:
            if num-min1 <= dis:
                min2 = num
                dis = min2 - min1
    print("Almost the min :", min2)
main()
