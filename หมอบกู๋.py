"""หมอบกู๋"""
def main():
    """หาราคาที่จ่ายและร้านที่ไปซื้อข้าวกะเพราหมูกรอบไช่ดาว"""
    budget = float(input())
    iso = 0
    restau = 1
    lowcost = 0
    lowrest = 1
    while iso < 50:
        cost = float(input())
        if iso == 5 or iso == 10 or iso == 15 or iso == 20 or iso == 25 or \
iso == 30 or iso == 35 or iso == 40 or iso == 45:
            restau = restau + 1
        iso += 1
        if lowcost == 0:
            lowcost = cost
            lowrest = restau
        if cost <= lowcost:
            if cost == lowcost:
                pass
            else:
                lowcost = cost
                lowrest = restau
        if budget >= cost:
            print("%.2F\n%d" %(cost, restau))
            break
        if iso == 50:
            print("%.2F\n%d" %(lowcost, lowrest))
            break
main()
