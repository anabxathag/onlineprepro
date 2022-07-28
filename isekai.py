"""ฺIsekai to 2 Dimensional Space"""
def main():
    """หาพิกัดตำแหน่งทางกลับโลกเดิม"""
    import math
    xa1, ya1 = float(input()), float(input())
    disi, ogsa = float(input()), float(input())
    xa2 = (disi * math.cos(math.radians(ogsa))) + xa1
    ya2 = (disi * math.sin(math.radians(ogsa))) + ya1
    print("%.2f" %xa2)
    print("%.2f" %ya2)
main()
