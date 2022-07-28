"""เต่าบิน"""
def main():
    """Print เงินทอน"""
    budget = float(input())
    cost = float(input())
    change = budget - cost
    print(int(change / 0.25))    # จน.เหรียญที่มากที่สุดที่จะทอน
    print(int((change // 10) + ((change % 10) // 5) + ((change % 5) // 2) + ((change % 2) // 1) +\
          ((change % 1) // 0.5) + ((change % 0.5) // 0.25)))     # จน.เหรียญที่น้อยที่สุดที่จะทอน
    print("%.1f" % change)     # เงินทอนเท่าไหร่
main()
