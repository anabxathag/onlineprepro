"""ร้านขายเสื้อของจอมเวทย์"""
def main():
    """Print ราคาที่ต้องจ่าย"""
    career = input()
    if career == "Magician":
        guild = input()
        num = int(input())
        if guild == "Fairy Tail":
            print("Total %d Jewel" %((12800 * num) * 0.8))
        elif guild == "Sabertooth" and num > 5:
            print("Total %d Jewel" %((12800 * num) * 0.85))
        elif guild == "Lamia Scale" and num >= 3:
            print("Total %d Jewel" %((12800 * num) * 0.9))
        elif guild == "Blue Pegasus" and num > 10:
            print("Total %d Jewel" %((12800 * num) * 0.95))
        else:
            print("Total %d Jewel" %(12800 * num))
    elif career != "Magician":
        num = int(input())
        print("Total %d Jewel" %(12800 * num))
main()
