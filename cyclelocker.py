'''[Quiz] Cycle Locker'''
def main():
    '''หาจำนวนครั้งที่น้อยที่สุดในการหมุนหารหัส'''
    real = int(input())
    fake = int(input())
    re_1000, re_100 = real // 1000, (real % 1000) // 100
    re_10, re_1 = ((real % 1000) % 100) // 10, ((real % 1000) % 100) % 10
    fa_1000, fa_100 = fake // 1000, (fake % 1000) // 100
    fa_10, fa_1 = ((fake % 1000) % 100) // 10, ((fake % 1000) % 100) % 10
    diff_1000 = abs(re_1000 - fa_1000)
    diff_100 = abs(re_100 - fa_100)
    diff_10 = abs(re_10 - fa_10)
    diff_1 = abs(re_1 - fa_1)
    if diff_1000 >= 5:
        diff_1000 = 9 - diff_1000
    if diff_100 >= 5:
        diff_100 = 9 - diff_100
    if diff_10 >= 5:
        diff_10 = 9 - diff_10
    if diff_1 >= 5:
        diff_1 = 9 - diff_1
    tol_min = diff_1000 + diff_100 + diff_10 + diff_1
    print(tol_min)
main()
