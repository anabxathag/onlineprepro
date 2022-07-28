"""Carpark"""
def main():
    """เช็คกรณี"""
    dayin = int(input())
    hourin = int(input())
    dayout = int(input())
    hourout = int(input())
    case1 = dayin <= 0 or dayout <= 0
    case2 = dayin > 365 or dayout > 365
    case3 = hourin >= 24 or hourout >= 24
    case4 = hourin < 0 or hourout < 0
    case5 = (dayin == dayout) and (hourin > hourout)
    case6 = ((dayout - dayin) < 0)
    if case1 or case2 or case3 or case4 or case5 or case6:
        print("error")
    else:
        cost(dayin, dayout, hourin, hourout)
def cost(din, dout, hin, hout):
    """คำนวณค่าจอดรถ"""
    day = dout - din
    hour = hout - hin
    if hour < 0:
        hour = hour + 24
        day = day - 1
    if  hour <= 2:
        money = 0
    elif hour <= 12:
        money = 15 * (hour)
    elif  hour < 24:
        money = 200
    if day == 0:
        print("%d day %d hour\n%d baht" %(day, hour, money))
    elif 1 <= day <= 6:
        print("%d day %d hour\n%d baht" %(day, hour, (money + (200 * day))))
    elif day >= 7 and day <= 365:
        if day // 7 > 0:
            money = money + ((200 * day) - (300 * (day // 7)))
            if day >= 28:
                money = money - 500
            print("%d day %d hour\n%d baht" %(day, hour, money))
main()
