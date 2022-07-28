'''[Quiz] Xbox'''
def main():
    '''วาดรูปกล่องสี่เหลี่ยมจตุรัส โดยมีกากบาทอยู่ในสี่เหลี่ยม'''
    numb = int(input())
    for row in range(numb):
        for column in range(numb):
            if column == row:
                print("*", end=" ")
            elif column + row == numb - 1:
                print("*", end=" ")
            elif row == 0 or row == numb - 1:
                print("*", end=" ")
            elif column == 0 or column == numb - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
main()
