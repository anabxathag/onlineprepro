"1 สัปดาห์น่ะมีอยู่ 7 วันในหนึ่งวัน 24 ชม. 1440 นาที 86400 วินาที คิดถึงเธอทุกที"
def main():
    """Print ผลลัพธ์เป็น วัน:ชั่วโมง:นาที:วินาที"""
    allsec = int(input())
    day = allsec // 86400
    allsec %= 86400
    hour = allsec // 3600
    allsec %= 3600
    minute = allsec // 60
    allsec %= 60
    sec = allsec
    print("%02d:%02d:%02d:%02d" %(day, hour, minute, sec))
main()
