"""cabadcduadtadtadhadaadtadwadoadradd"""
def main():
    """ถอดรหัส ตัดคำที่ไม่ต้องการทิ้งไป"""
    messa = input()
    while True:
        wordde = input()
        if messa.count(wordde) > 0:
            while messa.count(wordde) > 0:
                messa = messa.replace(wordde, "")
        else:
            break
    print(messa)
main()
