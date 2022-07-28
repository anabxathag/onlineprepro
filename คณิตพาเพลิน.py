"""คณิตพาเพลิน"""
def main():
    """ใส่เลขในlist"""
    my_list = []
    numb = int(input())
    outp = "["
    for _ in range(numb):
        memb = int(input())
        my_list.append(memb)
    mul = float(input())
    for bmem in my_list:
        outp += "'%.2f', " %(bmem * mul)
    outp = outp.rstrip(", ")
    outp += "]"
    print(outp)
main()
