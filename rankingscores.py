"""Ranking the scores"""
def main():
    """วิธีเบส"""
    listnum = list()
    listnum = input().split(",")
    intlist = list(map(int, listnum))
    lenght = len(intlist)
    listnum1 = sorted(intlist, reverse=True)
    j = 0
    for i in intlist:
        j += 1
        if j == lenght:
            print(listnum1.index(i)+1)
            break
        print(listnum1.index(i)+1, end=",")
main()
