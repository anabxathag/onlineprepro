"""ฺChoose a book"""
from math import factorial
def main():
    """วิธีเลือกหนังสือ"""
    noa, rock = int(input()), int(input())
    print(int(factorial(noa) / (factorial(rock) * factorial(noa - rock))))
main()
