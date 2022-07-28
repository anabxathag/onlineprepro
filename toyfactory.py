"""Toy Factory"""
def toy(parts):
    """รับค่าชิ้นส่วน"""
    if parts == 1:
        return " ^----^"
    elif parts == 2:
        return "( 0--0 )"
    elif parts == 3:
        return "<------>"
    elif parts == 4:
        return "(------)"
    elif parts == 5:
        return " u----u"
def main():
    """นำชิ้นส่วนของเล่นมาต่อกัน"""
    head = toy(int(input()))
    neck = toy(int(input()))
    hand = toy(int(input()))
    body = toy(int(input()))
    leg = toy(int(input()))
    print(head)
    print(neck)
    print(hand)
    print(body)
    print(leg)
main()
