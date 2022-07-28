'''[Quiz] Squid game 2'''
def main():
    '''หาหมายเลขสุดท้ายที่ยังมีชีวิตรอด'''
    people = int(input())
    kiler = 1
    killed = kiler + 1
    if 1 < people <= 1000:
        for iso in range(1, people + 1):
            print("Round %d : Person %d killed person %d" %(iso, kiler, killed))
            kiler += 2
            killed = kiler + 1
            if killed > people:
                killed -= people
            elif kiler > people:
                kiler -= people
        print("Person %d is the winner" %kiler)
    else:
        print("Person 1 is the winner")
main()
