"""บันไดอักษรลง"""
def main():
    """A-Z"""
    import string
    # string.ascii_uppercase
    # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    word = input().upper()
    posi1 = string.ascii_uppercase.find(word)
    rang1 = string.ascii_uppercase[:posi1+1]
    for row in rang1:
        posi2 = string.ascii_uppercase.find(row)
        rang2 = string.ascii_uppercase[:posi2+1]
        for column in rang2:
            print(column, end=" ")
        print()
main()
