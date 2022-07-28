"""เลือกคนคุยให้หน่อย"""
def main():
    """Print ชื่อคนคุยตามลักษณะนิสัย"""
    behav1, behav2 = input(), input()
    charac = behav1 + " " + behav2
    if charac == "Calm Empathetic" or charac == "Empathetic Calm":
        print("Ice")
    elif charac == "Reliable Courageous" or charac == "Courageous Reliable":
        print("Fern")
    elif charac == "Optimistic Cheerful" or charac == "Cheerful Optimistic":
        print("Bam")
    elif charac == "Attractive Creative" or charac == "Creative Attractive":
        print("Tangmo")
    elif charac == "Cheerful Creative" or charac == "Creative Cheerful":
        print("Mild")
    elif charac == "Reliable Optimistic" or charac == "Optimistic Reliable":
        print("Prae")
    elif charac == "Courageous Calm" or charac == "Calm Courageous":
        print("Dream")
    elif charac == "Empathetic Attractive" or charac == "Attractive Empathetic":
        print("Aom")
    else:
        pass
main()
