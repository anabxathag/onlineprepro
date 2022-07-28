"""ค่าไฟแพงเกินปุยมุ้ย!!"""
def main():
    """คำนวณค่าพลังงานไฟฟ้า(Unit) ของแต่ละเครื่องในเดือนมิถุนายน"""
    tevis = int(input())
    miwave = int(input())
    hairdry = int(input())
    ligbulb = int(input())
    fridge = int(input())
    print("TV %d Watt 1 ea for 3 hours" %tevis)
    print("%.2f unit." %((tevis * (3 * 30)) / 1000))
    print("Microwave %d Watt 1 ea for 1 hours" %miwave)
    print("%.2f unit." %((miwave * (1 * 30)) / 1000))
    print("Hair dryer %d Watt 1 ea for 0.5 hours" %hairdry)
    print("%.2f unit." %((hairdry * (0.5 * 30)) / 1000))
    print("light bulb %d Watt 4 ea for 5 hours" %ligbulb)
    print("%.2f unit." %(((ligbulb * 4) * (5 * 30)) / 1000))
    print("Refrigerator %d Watt 1 ea for 24 hours" %fridge)
    print("%.2f unit." %((fridge * (24 * 30)) / 1000))
main()
