"""Append"""
def main():
    """เพิ่มสมาชิกในlist"""
    num = int(input())
    iso = 0
    long_list = []
    outp = "["
    while iso < num:
        iso += 1
        long_list.append(input())
    for yoy in long_list:
        outp += '"%s", ' %yoy
    print(outp.rstrip(", "), end="")
    print("]", end="")
main()
