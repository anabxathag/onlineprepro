"""[Quiz] เรื่องวุ่นๆกับวัยรุ่นจำนวนเฉพาะ"""
def main():
    """Prime Number หรือ Not Prime Number"""
    num = int(input())
    ans = ""
    if num > 5:
        for i in range(2, num//2):
            if (num % i) == 0:
                ans = "Not Prime Number"
                break
            else:
                ans = "Prime Number"
        print(ans)
    elif num == 2 or num == 3 or num == 5:
        print("Prime Number")
    else:
        print("Not Prime Number")
main()
