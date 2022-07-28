"""เค้กช็อกโกแลต"""
def main():
    """Print จำนวนเค้กที่ซื้อได้,เงินทอน"""
    budget = int(input())
    cost = int(input())     # ราคาเค้กต่อ1ชิ้น
    change = budget - cost
    if change >= 0:
        getcake = budget // cost
        print("Chocolate Cake: %d" %(getcake))
        print("Money left: "+ str(budget - (getcake * cost)))
    elif change < 0:
        print("Not enough money;(")
        print("Money left: "+ str(budget))
main()
