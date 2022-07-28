"""Basic Index"""
def main():
    """เพิ่มสมาชิกในlist"""
    my_list = []
    memb = input()
    if memb.upper() != "END":
        while memb.upper() != "END":
            my_list.append(memb)
            memb = input()
    num = int(input())
    if num > len(my_list) - 1:
        print("Index Not Found")
    elif my_list[num] in my_list:
        print('List[%d] = "%s"' %(num, my_list[num]))
main()
