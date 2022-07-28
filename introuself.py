'''Introduce Yourself'''
def main():
    """Print name, nickname, ปีเกิด"""
    firstn = input()
    nickn = input()
    age = int(input())
    year = 2022 - age
    print("My name is "+ firstn +", My nickname is "+ nickn +", I'm I was born in "+ str(year))
main()
