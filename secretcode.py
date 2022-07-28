"""Secret code"""
def main():
    """Print ข้อความ รหัสที่ถอดมาได้"""
    among = int(input())
    ant = str(int(among / 100000000) % 10)
    bird = str(int(among / 1000000) % 10)
    cat = str(int(among / 10000) % 10)
    dog = str(int(among / 100) % 10)
    egg = str(among % 10)
    print(ant + bird + cat + dog + egg)
main()
