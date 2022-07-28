"""ทำให้ดูง่าย"""
def main():
    """เรียงอาชีพ แล้วเรียงชื่อต่อ"""
    num = int(input())
    goop = []
    for iso in range(num):
        pepo = input().split()
        goop.append(pepo)
        goop[iso][2], goop[iso][0] = goop[iso][0], goop[iso][2]
        iso += 1
    goop.sort()
    job = []
    for kuy in goop:
        if kuy[0] not in job:
            job.append(kuy[0])
    for lol in job:
        print("OCCUPATION : " + lol.upper())
        noi = 1
        for pig in goop:
            if pig[0] == lol:
                print("%d. %s, %s" %(noi, pig[1], pig[2]))
                noi += 1
main()
