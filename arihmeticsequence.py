"""Arithmetic Sequence"""
def main():
    """ลำดับเลขคณิต"""
    mem1 = int(input())
    num = int(input())
    diff = int(input())
    for iso in range(num):
        print(mem1 + (iso * diff), end=" ")
main()
