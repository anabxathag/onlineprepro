"""[Extra] ถอดรหัสเปลี่ยนโลก"""
def main():
    """recap"""
    char_1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = input().upper()#ข้อความ
    set_code = [input().upper(), input().upper(), input().upper()]#เอาไว้เก็บตัวเลื่อน
    number_decode = [0, 0, 0]#เอาไว้เลื่อนกี่ตัว
    for iso in range(0, 3):
        indo = 0
        for kon in set_code[iso]:
            indo += char_1.index(kon)
        number_decode[iso] = (indo % 26)
    indo = 0
    ans = ''
    for sop in text:
        if sop == " ":
            ans += " "
            continue
        if indo <= 2:#1-3
            inse = (char_1.index(sop) - number_decode[0]) % 26
            ans += char_1[inse]
            indo += 1
        elif indo >= 3 and indo <= 5:#4-6
            inse = (char_1.index(sop) - number_decode[1]) % 26
            ans += char_1[inse]
            indo += 1
        elif indo >= 6 and indo <= 8:#7-9
            inse = (char_1.index(sop) - number_decode[2]) % 26
            ans += char_1[inse]
            indo += 1
        if indo == 9:
            indo = 0
    print(ans.capitalize())
main()
