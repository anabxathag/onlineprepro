''''''
def main():
    ''''''
    i = 0
    j = 0
    listfood = []
    text1 = ""
    while True:
        text = input().lower()
        if text == "stop":
            break
        else:
            listfood.append(text)
    for text in listfood:
        ingredient = text == "celery stalks" or text == "carrots" \
        or text == "potatoes" or text == "mushrooms" or text == "tofu" \
        or text == "lotus root" or text == "cabbage" \
        or text == "instant noodles" or text == "glass noodle" \
        or text == "wonton" or text == "beef" or text == "pork loin" \
        or text == "chicken" or text == "fish balls" or text == "cheese ball" \
        or text == "octopus" or text == "fish" or text == "shrimp" \
        or text == "mussels"
        if not ingredient and not text == "1" and not text == "2" \
           and not text == "3" and not text == "4":
            i = 1
        if text.isdecimal() == True and j != 0:
            text1 = "Mild"*(text == "1") + "Medium"*(text == "2") \
                    +"Hot"*(text == "3") + "Extra hot"*(text == "4")
        j += 1
    if i == 1:
        print("Get out!")
    elif listfood == []:
        print("Huh? you didn't order anything!")
    elif listfood[0].isdecimal() == True and len(listfood) == 1:
        print("Huh? you didn't order anything!")
    elif text1 == "":
        print("Please choose a spicy level!")
    else:
        print("%s Mala xiang guo is here."%text1)
main()
