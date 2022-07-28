"""Walking average distance"""
import math as m
def main():
    """ผลต่างของจำนวนก้าวในวันที่ n กับค่าเฉลี่ยของจำนวนก้าวทั้งหมดในช่วงที่กำหนดให้"""
    num = int(input())
    total = 0
    tol_list = []
    for _ in range(num):
        memb = int(input())
        total += memb
        tol_list.append(memb)
    avg = total / num
    for olo in tol_list:
        print(m.ceil(abs(olo - avg)))
main()
