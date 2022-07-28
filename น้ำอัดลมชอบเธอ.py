"""น้ำอัดลมทำให้ผมชอบเรอ น่ารักแบบเธอทำให้ผมชอบใจ"""
def cost_1(iso):
    """คิดเงิน"""
    if iso == 'cup':
        return 5
    elif iso == 'ice':
        return 5
    elif iso == 'orange':
        return 17
    elif iso == 'banana':
        return 13
    elif iso == 'strawberry':
        return 10
    elif iso == 'cherrie':
        return 15
    else:
        return 0
def cost_2(iso):
    """คิดเงิน"""
    if iso == 'watermelon':
        return 12
    elif iso == 'lemon':
        return 19
    elif iso == 'mango':
        return 21
    elif iso == 'grape':
        return 11
    else:
        return 0
def conclu(ans, total):
    """output"""
    if ans == 1:
        print("Invalid order!")
    elif ans == 0:
        print("Here's your juice!")
        print("Cost %d baht." %total)
    elif ans == 2:
        print("Here's your soft drink!")
        print("Cost %d baht." %total)
def main():
    """ตัวหลักในการคิดทุกอย่าง"""
    jusodr = ['cup', 'ice', 'orange', 'banana', 'strawberry', 'cherrie', 'watermelon', \
    'lemon', 'mango', 'grape', 'coke', 'pepsi', 'sprite', 'fanta']
    drinking = []
    ans = 0
    order = input().lower()
    while order != "end":
        drinking.append(order)
        order = input().lower()
    total = 0
    for iso in drinking:
        if iso not in jusodr:
            ans = 1
            break
        elif iso == 'coke' or iso == 'pepsi' or iso == 'sprite' or iso == 'fanta':
            ans = 2
            total += 15
        total += cost_1(iso)
        total += cost_2(iso)
    if drinking[0] != 'cup':
        ans = 1
    elif drinking.count('cup') != 1:
        ans = 1
    elif drinking[-1] != 'ice':
        ans = 1
    elif drinking.count('ice') == 0:
        ans = 1
    elif drinking.count('ice') > 1 and drinking[-1] == 'ice':
        if drinking[-2] != 'ice' and drinking[-3] == 'ice':
            ans = 1
    elif len(drinking) < 3:
        ans = 1
    conclu(ans, total)
main()
