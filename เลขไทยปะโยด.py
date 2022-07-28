"""เลขไทยมีประโยชน์"""
def main():
    """Print ค่าบัตรเข้าน้ำตก กรณีฟรี,เด็ก"""
    nation_t = input()
    # เช็คว่าเป็นคนไทยรึเปล่า?
    if nation_t == "N":
        nation_w = input()
    else:
        nation_w = ""   # เป็นstrอะไรก็ได้ เพราะไม่ตรงเงื่อนไขข้างล่างแน่นอน
    age = int(input())
    coupon_h = input()
    # เช็คว่ามีคูปองรึเปล่า?
    if coupon_h == "Y":
        coupon_m = int(input())
    else:
        coupon_m = 0    # ไม่มีส่วนลด
    # เช็คราคาตั๋ว
    if 0 <= age <= 10 or age > 60:
        print("%.2f" %0)
    elif 10 < age <= 20 and nation_t == "Y" and coupon_h == "N":
        print("%.2f" %(20))
    elif 10 < age <= 20 and nation_t == "Y" and coupon_h == "Y":
        print("%.2f" %(20 * (1 - (coupon_m / 100))))
    elif 10 < age <= 20 and nation_t == "N" and (nation_w == "Vietnam" \
        or nation_w == "Singapore" or nation_w == "India") and coupon_h == "N":
        print("%.2f" %(20 * 5 * 0.5))
    elif 10 < age <= 20 and nation_t == "N" and coupon_h == "N":
        print("%.2f" %(20 * 5))
    elif 10 < age <= 20 and nation_t == "N" and (nation_w == "Vietnam" \
        or nation_w == "Singapore" or nation_w == "India") and coupon_h == "Y":
        print("%.2f" %(20 * 5 * 0.5 *(1 - (coupon_m / 100))))
    elif 10 < age <= 20 and nation_t == "N" and coupon_h == "Y":
        print("%.2f" %(20 * 5 * (1 - (coupon_m / 100))))
    else:
        tuo(age, nation_t, nation_w, coupon_h, coupon_m)
def tuo(age, nation_t, nation_w, coupon_h, coupon_m):
    """Print ค่าบัตรเข้าน้ำตก กรณีผู้ใหญ่"""
    if 20 < age <= 60  and nation_t == "Y" and coupon_h == "N":
        print("%.2f" %(40))
    elif 20 < age <= 60  and nation_t == "Y" and coupon_h == "Y":
        print("%.2f" %(40 * (1 - (coupon_m / 100))))
    elif 20 < age <= 60  and nation_t == "N" and (nation_w == "Vietnam" \
        or nation_w == "Singapore" or nation_w == "India") and  coupon_h == "N":
        print("%.2f" %(40 * 5 *0.5))
    elif 20 < age <= 60  and nation_t == "N" and coupon_h == "N":
        print("%.2f" %(40 * 5))
    elif 20 < age <= 60  and nation_t == "N" and (nation_w == "Vietnam" \
        or nation_w == "Singapore" or nation_w == "India") and  coupon_h == "Y":
        print("%.2f" %(40 * 5 * 0.5 * (1 - (coupon_m / 100))))
    elif 20 < age <= 60  and nation_t == "N" and coupon_h == "Y":
        print("%.2f" %(40 * 5 * (1 - (coupon_m / 100))))
main()
