'''[Quiz] Cycle Locker'''
def main():
    '''หาจำนวนครั้งที่น้อยที่สุดในการหมุนหารหัส'''
    real = int(input())
    fake = int(input())
    re_1000, re_100 = real // 1000, (real % 1000) // 100
    re_10, re_1 = ((real % 1000) % 100) // 10, ((real % 1000) % 100) % 10
    fa_1000, fa_100 = fake // 1000, (fake % 1000) // 100
    fa_10, fa_1 = ((fake % 1000) % 100) // 10, ((fake % 1000) % 100) % 10
    tol_min = abs(re_1000 - fa_1000) +  abs(re_100 - fa_100) \
    + abs(re_10 - fa_10) +  abs(re_1 - fa_1)
    print(tol_min)
main()
