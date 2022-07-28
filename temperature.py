"""Temperature"""
def main():
    """print อุณหภูมิที่ถูกแปลง"""
    mugen = float(input())
    infi = input().upper()
    if infi == "C→F" or infi == "F→C":
        cffc(mugen, infi)
    elif infi == "C→K" or infi == "K→C":
        ckkc(mugen, infi)
    elif infi == "C→R" or infi == "R→C":
        crrc(mugen, infi)
    elif infi == "F→K" or infi == "K→F":
        fkkf(mugen, infi)
    elif infi == "F→R" or infi == "R→F":
        frrf(mugen, infi)
    elif infi == "K→R" or infi == "R→K":
        krrk(mugen, infi)
    elif infi == "C→C" or infi == "F→F" or infi == "K→K" or infi == "R→R":
        cfkr(mugen, infi)
def cffc(mugen, infi):
    """C->F or F->C"""
    if infi == "C→F":
        print("Fahrenheit = %.2f" %((mugen * (9 / 5)) + 32))
    elif infi == "F→C":
        print("Celsius = %.2f" %((mugen - 32) * (5 / 9)))
def ckkc(mugen, infi):
    """C->K or K->C"""
    if infi == "C→K":
        print("Kelvin = %.2f" %(mugen + 273.15))
    elif infi == "K→C":
        print("Celsius = %.2f" %(mugen - 273.15))
def crrc(mugen, infi):
    """C->R or R->C"""
    if infi == "C→R":
        print("Rankine = %.2f" %((mugen + 273.15) * (9 / 5)))
    elif infi == "R→C":
        print("Celsius = %.2f" %((mugen - 491.67) * (5 / 9)))
def fkkf(mugen, infi):
    """F->K or K->F"""
    if infi == "F→K":
        print("Kelvin = %.2f" %((mugen + 459.67) * (5 / 9)))
    elif infi == "K→F":
        print("Fahrenheit = %.2f" %((mugen * (9 / 5)) - 459.67))
def frrf(mugen, infi):
    """F->R or R->F"""
    if infi == "F→R":
        print("Rankine = %.2f" %(mugen + 459.67))
    elif infi == "R→F":
        print("Fahrenheit = %.2f" %(mugen - 459.67))
def krrk(mugen, infi):
    """K->R or R->K"""
    if infi == "K→R":
        print("Rankine = %.2f" %(mugen * (9 / 5)))
    elif infi == "R→K":
        print("Kelvin = %.2f" %(mugen * (5 / 9)))
def cfkr(mugen, infi):
    """C->C or F->F or K->K or R->R"""
    if infi == "C→C":
        print("Celsius = %.2f" %mugen)
    elif infi == "F→F":
        print("Fahrenheit = %.2f" %mugen)
    elif infi == "K→K":
        print("Kelvin = %.2f" %mugen)
    elif infi == "R→R":
        print("Rankine = %.2f" %mugen)
main()
