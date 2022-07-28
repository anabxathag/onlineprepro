"""Derivative"""
def main():
    """วิธีเบส"""
    num = input().split(",")
    listnum = list(map(int, num))
    j = 0
    for i in listnum:
        listnum[j] = i*j
        j += 1
    del listnum[0]
    lenght = len(listnum)
    listnum.insert(lenght+1, 0)
    print(listnum)
main()
