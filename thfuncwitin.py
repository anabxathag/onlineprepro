"""TheFunctionWithin"""
def main():
    """หาคำตอบจากฟังก์ชันทั้ง4"""
    ant, bird, cat, dog = float(input()), float(input()), float(input()), float(input())
    print(fox(fox(ant)))
    print(gon(fox(ant - bird)))
    print(hot(fox(ant + bird), fox(ant + cat), gon(fox(dog ** 2))))
    print(iso(hot(fox(ant + bird), fox(ant - cat), gon(fox(dog ** 2))),
              gon(fox(ant - bird)), fox(fox(fox(fox(fox(cat))))), dog ** 8))
def fox(xan):
    """คิดค่าฟังก์ชันf"""
    return 2 * xan
def gon(xan):
    """คิดค่าฟังก์ชันg"""
    return (3 * (xan ** 4)) - (xan ** 3) + (2 * (xan ** 2)) + 10
def hot(xan, yun, zoy):
    """คิดค่าฟังก์ชันh"""
    return ((zoy + xan) ** 2) - (xan * yun) + (yun ** 2)
def iso(ant, bird, cat, dog):
    """คิดค่าฟังก์ชันi"""
    return ((ant ** 2) + (bird ** 2) - (cat ** 2)) / ((dog ** 2) - (2 * (ant * dog)) + (2 * ant))
main()
