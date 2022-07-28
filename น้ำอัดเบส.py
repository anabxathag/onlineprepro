''''' '''
def main():
    ''' '''
    cost = 0
    listtext = []
    text = ""
    count_soda = 0
    count_error = 0
    count_cup = 0
    while True:
        text = input().lower()
        if text == "end":
            break
        listtext.append(text)
        if text != "":
            cost += 5*(text == "cup")+5*(text == "ice")+17*(text == "orange") \
            +13*(text == "banana")+10*(text == "strawberry") \
            +15*(text == "cherrie")+12*(text == "watermelon") \
            +19*(text == "lemon")+21*(text == "mango")+11*(text == "grape") \
            +15*(text == "coke" or text == "pepsi" or text == "sprite" \
                 or text == "fanta")
    lenght = len(listtext)
    for text in listtext:
        order = text == "cup" or text == "ice" or text == "orange" \
            or text == "banana" or text == "strawberry" \
            or text == "cherrie" or text == "watermelon" \
            or text == "lemon" or text == "mango" or text == "grape" \
            or text == "coke" or text == "pepsi" or text == "sprite" \
            or text == "fanta"
        if text == "coke" or text == "pepsi" or text == "sprite" \
           or text == "fanta":
            count_soda += 1
        if text == "cup":
            count_cup += 1
        if not order or listtext[0] != "cup" \
           or listtext[lenght-1] != "ice" or lenght < 3:
            count_error += 1
    if count_error == 0 and listtext != [] and count_cup == 1:
        if count_soda >= 1:
            print("""Here's your soft drink!""")
            print("Cost %d baht."%cost)
        else:
            print("""Here's your juice!""")
            print("Cost %d baht."%cost)
    else:
        print("Invalid order!")
main()