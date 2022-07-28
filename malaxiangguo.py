"""Mala xiang guo"""
def main():
    """ปริ้นระดับความเผ็ด"""
    menu = ['celery stalks', 'carrots', 'potatoes', 'mushrooms', 'tofu' \
    , 'lotus root', 'cabbage', 'instant noodles', 'glass noodle', 'wonton' \
    , 'beef', 'pork loin', 'chicken', 'fish balls', 'cheese ball' \
    , 'octopus', 'fish', 'shrimp', 'mussels', '1', '2', '3', '4']
    mala = []
    tmp = input().lower()
    ans = 0
    while tmp != "stop":
        mala.append(tmp)
        tmp = input().lower()
    if ("1" not in mala and "2" not in mala and "3" not in mala and "4" not in mala) \
        or not mala[-1].isdecimal():
        ans = 3
    if len(mala) == 0:
        ans = 2
    for iso in mala:
        if iso not in menu:
            ans = 1
            break
        elif iso.isdecimal() and mala.index(iso) != 0:
            temp = iso.replace("1", "Mild").replace("2", "Medium")\
            .replace("3", "Hot").replace("4", "Extra hot")
            break
        elif iso.isdecimal() and len(mala) == 1:
            ans = 2
            break
    if ans == 0:
        print("%s Mala xiang guo is here." %temp)
    elif ans == 1:
        print("Get out!")
    elif ans == 2:
        print("Huh? you didn't order anything!")
    elif ans == 3:
        print("Please choose a spicy level!")
main()
