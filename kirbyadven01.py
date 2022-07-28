"""[Extra] KIRBY Adventure - 01 [HELP!]"""
def role(agent):
    "เลือกอาชีพ"
    if agent == "sword":
        return 4
    elif agent == "magic":
        return 2
    elif agent == "sleep":
        return 0
    elif agent == "master":
        return 9
def enlife(enemy):
    """เลือดศัตรู"""
    if enemy == "waddle dee":
        return 2
    if enemy == "waddle doo":
        return 5
    if enemy == "laser ball":
        return 3
    else:
        return 0
def enatk(enemy):
    """พลังโจมตีศัตรู"""
    if enemy == "waddle dee":
        return 1
    if enemy == "waddle doo":
        return 3
    if enemy == "laser ball":
        return 2
    else:
        return 0
def main():
    """เหลือHpเท่าไหร่ killศัตรูเท่าไหร่"""
    hp_ag = int(input())
    num_kill = 0
    hp_en = 0
    atac_en = 0
    while hp_ag > 0:
        agent = input().lower()
        atac_ag = role(agent)
        enemy = input().lower()
        hp_en = enlife(enemy)
        atac_en = enatk(enemy)
        print("------------")
        if enemy == "none":
            print("%d HP left" %hp_ag)
            print("Kirby won!")
            print("You had defeated %d enemies" %num_kill)
            print("------------")
            break
        elif enemy == "heal":
            hp_ag += 2
        else:
            hp_ag -= atac_en
            hp_en -= atac_ag
            if hp_en <= 0 and hp_ag > 0:
                print("- %s had defeated -" %enemy)
                num_kill += 1
            elif hp_ag <= 0:
                print("%d HP left" %hp_ag)
                print("GameOver!")
                print("You had defeated %d enemies" %num_kill)
                print("------------")
                break
        print("%d HP left" %hp_ag)
        print("------------")
main()
