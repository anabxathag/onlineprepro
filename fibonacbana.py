"""Fibonacci ดูEasyเหมือนปลอกBanana"""
def fibo(num):
    """ใส่ลำดับ Fibonacci ที่ต้องการหา แล้วPrint ค่าของลำดับที่ใส่เข้าไป """
    if num < 0:
        pass
    elif num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fibo(num - 1) + fibo(num - 2)
print(fibo(int(input())))
