"""นี่คือสูตรความเร็ว พี่ปวดเอวเจ็บหัวใจ"""
def main():
    """print อัตราเร็ว"""
    length, time = float(input())*1852, int(input())/1000
    velocity = length / time
    print("อัตราเร็วเท่ากับ : %.3f เมตรต่อวินาที " %velocity)
main()
