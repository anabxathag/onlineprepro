"""Composite Function"""
def main():
    """print คำตอบของ fog(x) หรือ gof(x)"""
    xmen = float(input())
    func = input().lower()
    if func == "gof":
        fox = (15 + xmen - (xmen **3)) / (((xmen **2) / 3) + 11)
        god = (fox ** 3) + (4 * fox) - 1
        print("%.2f" %god)
    elif func == "fog":
        god = (xmen ** 3) + (4 * xmen) - 1
        fox = (15 + god - (god **3)) / (((god **2) / 3) + 11)
        print("%.2f" %fox)
main()
