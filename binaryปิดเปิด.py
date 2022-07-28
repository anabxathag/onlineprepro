"""ฺBinaryปิด/เปิด"""
def main():
    """นำเลขฐาน10ที่รับเข้ามา แปลงเป็น binary เเล้วทำให้เป็น String close/open"""
    bina10 = int(input())# รับเลขฐาน10
    bina2 = bin(bina10)# กลายเป็นเลขฐาน2
    ant = bina2[2:]# ข้าม2ตัวแรกไปเลย , rstripใช้ลบข้อความทางขวาสุด
    print(ant.replace("1", "open, ").replace("0", "close, ").rstrip(", "))
main()
