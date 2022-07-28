"""คณิตศาสตร์เข้าใจยากแต่รักเธอมากเข้าใจไหม"""
def main():
    """กลายเป็นเศษส่วนของตัวต่อไปเรื่อยๆ"""
    num = input().strip("[").rstrip("]").split(",")
    listnum = list(map(int, num))
    listnum1 = []
    for i in range(len(listnum)):
        num = listnum[i]
        for j in range(i-1, -1, -1):
            num = listnum[j] + (1/num)
        if str(num).find('.') <= 0:
            listnum1.append(num)
        else:
            num = "%.6f"%num
            listnum1.append(float(num))
    print(listnum1)
main()
