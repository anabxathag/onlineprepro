"""Restaurant"""
def main():
    """Print จำนวนเงินทอน"""
    pay = float(input())
    cost = float(input())
    change = pay - cost
    if pay > cost:
        print("เเบงค์ 100 บาท : %d" %(change // 100))
        change %= 100
        print("เเบงค์ 50 บาท : %d" %(change // 50))
        change %= 50
        print("เเบงค์ 20 บาท : %d" %(change // 20))
        change %= 20
        print("เหรียญ 12 บาท : %d" %(change // 12))
        change %= 12
        print("เหรียญ 10 บาท : %d" %(change // 10))
        change %= 10
        print("เหรียญ 5 บาท : %d" %(change // 5))
        change %= 5
        print("เหรียญ 2 บาท : %d" %(change // 2))
        change %= 2
        print("เหรียญ 1 บาท : %d" %(change // 1))
        change %= 1
        print("เหรียญ 50 สตางค์ : %d" %(change // 0.5))
        change %= 0.5
        print("เหรียญ 25 สตางค์ : %d"%(change // 0.25))
    elif pay < cost:
        print("จำนวนเงินไม่พอ")
    elif pay == cost:
        print("จ่ายมาพอดี")
main()
