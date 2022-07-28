"""Fast server"""
def main():
    """Print ค่าความเร็วของ Server A หรือ B"""
    fast_a = int(input())
    time_a = str(input())
    fast_b = int(input())
    time_b = str(input())
    # A
    if time_a == "Millisecond":
        sec_a = fast_a / (10 ** 3)
    elif time_a == "Microsecond":
        sec_a = fast_a / (10 ** 6)
    elif time_a == "Nanosecond":
        sec_a = fast_a / (10 ** 9)
    elif time_a == "Picosecond":
        sec_a = fast_a / (10 ** 12)
    # B
    if time_b == "Millisecond":
        sec_b = fast_b / (10 ** 3)
    elif time_b == "Microsecond":
        sec_b = fast_b / (10 ** 6)
    elif time_b == "Nanosecond":
        sec_b = fast_b / (10 ** 9)
    elif time_b == "Picosecond":
        sec_b = fast_b / (10 ** 12)
    # output
    if sec_a > sec_b:
        print("Server B, %.6f second" %sec_b)
        print("Faster than server A , %d times" %(sec_a // sec_b))
    elif sec_a < sec_b:
        print("Server A, %.6f second" %sec_a)
        print("Faster than server B , %d times" %(sec_b // sec_a))
    elif sec_a == sec_b:
        print("equal")
main()
