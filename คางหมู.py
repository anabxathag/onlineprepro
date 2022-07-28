"""น้องน้องควรช่วยพี่ หาพื้นที่ของคางหมู"""
def main():
    """พื้นที่สี่เหลี่ยมคางหมูเป็นตัวเลขที่มีทศนิยม 2 ตำแหน่ง"""
    high, app, bana = float(input()), float(input()), float(input())
    area = 0.5 * high * (app + bana)
    print("Trapezoidal area = %.2f" %area)
main()
