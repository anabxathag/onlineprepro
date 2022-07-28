'''[Quiz] Pager'''
def main():
    '''หาความยาวของข้อความ, ค่าบริการในการส่ง'''
    messa = input()
    cost = 0
    cost += ((len(messa) // 20) * 18.5)
    cost += (((len(messa) % 20) // 8) * 6.5)
    cost += ((((len(messa) % 20) % 8) // 3) * 3)
    cost += (((((len(messa) % 20) % 8) % 3) // 1) * 1.5)
    print("Text's length is : \"%d\"" %len(messa))
    print("Total price is   : %.2f Baht\\.-" %cost)
main()
