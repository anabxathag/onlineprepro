"""News Doll"""
def main():
    """บอกที่เริ่มและทิศที่จะไป"""
    place = int(input())
    drive = input().capitalize()
    move(place, drive)
def move(place, drive):
    """เก็บค่าตำแหน่งที่อยู่"""
    if drive == "Stop":
        print(place)
    elif place == 1 and (drive == "East" or drive == "South"):
        move(((2 * (drive == "East")) + (3 * (drive == "South"))), input().capitalize())
    elif place == 2 and (drive == "West" or drive == "South"):
        move(((1 * (drive == "West")) + (4 * (drive == "South"))), input().capitalize())
    elif place == 3 and (drive == "East" or drive == "North"):
        move(((4 * (drive == "East")) + (1 * (drive == "North"))), input().capitalize())
    elif place == 4 and (drive == "West" or drive == "North"):
        move(((3 * (drive == "West")) + (2 * (drive == "North"))), input().capitalize())
    else:
        move(place, input().capitalize())
main()
