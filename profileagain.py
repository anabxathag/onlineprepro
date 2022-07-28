"""ProfileAgain"""
def main():
    """print ข้อมูลลูกค้า"""
    sex = input()
    sex = sex.casefold()    # ทำให้เป็นตัวเล็กทั้งหมด
    sex = sex.replace("female", "Mrs.")
    sex = sex.replace("male", "Mr.")
    idnum = input()
    firstname = input().capitalize()    # พิมพ์ใหญ่ตัวแรก พิมพ์เล็กตัวที่เหลือ
    lastname = input().capitalize()
    age = input()
    career = input().upper()    # ทำให้เป็นตัวใหญ่ทั้งหมด
    print("======")
    print("ID : " + idnum[:6])  # เอาแค่6ตัว
    print("Name : " + sex, firstname, lastname)
    print("Age : " + age + " years old")
    print("Occupation : " + career)
    print("======")
main()
