"""Deep In Abyss"""
def main():
    """Print ความลึกที่ทำการสำรวจ คำสาปที่ติดตัวมา"""
    pepo1, deep1, deci1 = input(), int(input()), input().upper()
    pepo2, deep2, deci2 = input(), int(input()), input().upper()
    pepo3, deep3, deci3 = input(), int(input()), input().upper()
    print("Name : " + pepo1)
    howdeep(deep1, deci1)
    print("---")
    print("Name : " + pepo2)
    howdeep(deep2, deci2)
    print("---")
    print("Name : " + pepo3)
    howdeep(deep3, deci3)
def howdeep(pod, ced):
    """หาความลึก"""
    if 0 <= pod <= 1350:
        print("1st Layer : Edge of the Abyss")
        curse1(ced)
    elif 1351 <= pod <= 2600:
        print("2nd Layer : Forest of Temptation")
        curse2(ced)
    elif 2601 <= pod <= 7000:
        print("3rd Layer : Great Fault")
        curse3(ced)
    elif 7001 <= pod <= 12000:
        print("4th Layer : The Goblets of Giants")
        curse4(ced)
    elif 12001 <= pod <= 13000:
        print("5th Layer : Sea of Corpses")
        curse5(ced)
    elif 13001 <= pod <= 15500:
        print("6th Layer : The Capital of the Unreturned")
        curse6(ced)
    elif pod >= 15501:
        print("7th Layer : The Final Maelstrom")
        curse7(ced)
def curse1(dert):
    """คำสาปชั้นที่1"""
    if dert == "UP":
        print("Curse : Light dizziness and nausea.")
    else:
        print("Curse : -")
def curse2(dert):
    """คำสาปชั้นที่2"""
    if dert == "UP":
        print("Curse : Intense nausea, headaches, and numbness of limbs.")
    else:
        print("Curse : -")
def curse3(dert):
    """คำสาปชั้นที่3"""
    if dert == "UP":
        print("Curse : Vertigo combined with visual and auditory hallucinations.")
    else:
        print("Curse : -")
def curse4(dert):
    """คำสาปชั้นที่4"""
    if dert == "UP":
        print("Curse : Intense pain throughout the body and bleeding from every orifice.")
    else:
        print("Curse : -")
def curse5(dert):
    """คำสาปชั้นที่5"""
    if dert == "UP":
        print("Curse : Complete sensory deprivation, confusion and self-harming behavior.")
    else:
        print("Curse : -")
def curse6(dert):
    """คำสาปชั้นที่6"""
    if dert == "UP":
        print("Curse : Loss of humanity or death, or under specific conditions, the Blessing.")
    else:
        print("Curse : -")
def curse7(dert):
    """คำสาปชั้นที่7"""
    if dert == "UP":
        print("Curse : Certain death.")
    else:
        print("Curse : -")
main()
