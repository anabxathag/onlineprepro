"""Prepro"""
def role(atk):
    "Job role"
    if atk == "sword":
        return 4
    elif atk == "magic":
        return 2
    elif atk == "sleep":
        return 0
    elif atk == "master":
        return 9
def opoatk1(atk):
    "Opponent attack"
    if atk == "waddle dee":
        return 1
    if atk == "waddle doo":
        return 3
    if atk == "laser ball":
        return 2
    else:
        return 0
def opolife1(life):
    "Opponent life"
    if life == "waddle dee":
        return 2
    if life == "waddle doo":
        return 5
    if life == "laser ball":
        return 3
    else:
        return 0
def main():
    """77KIRBY Adventure"""
    life = int(input())
    num = 0
    opoatk = 0
    opolife = 0
    while life > 0:
        job = input().lower()
        attack = role(job)
        opo = input().lower()
        opoatk = opoatk1(opo)
        opolife = opolife1(opo)
        print("------------")
        if opo == "none":
            print("%s HP left" %life)
            print('''Kirby won!\nYou had defeated %d enemies''' %num)
            print("------------")
            break
        elif opo == "heal":
            life += 2
        else:
            life -= opoatk
            opolife -= attack
            if life <= 0:
                print('''%d HP left\nGameOver!\nYou had defeated %d enemies''' %(life, num))
                print("------------")
                break
            elif opolife <= 0:
                print("- %s had defeated -" %opo)
                num += 1
        print("%s HP left" %life)
        print("------------")
main()
