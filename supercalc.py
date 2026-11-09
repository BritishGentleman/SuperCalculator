#-Coded on Linux python3-#

#-Variables-#
Name = "SuperCalculator"
vers = "0.25"
enter1 = "Enter first number: "
enter2 = "Enter second number: "
leavemes = "Press enter to exit "
Plus = "1"
Minus = "2"
Star = "3"
Slash = "4"
TwoStar = "5"
idk = "6"
SlashSlash = "7"

#-Start-#
print(f"Welcome to {Name}!")
print(f"Version number: {vers}")
print("")
print("Select a Mathematical operator")
print("1 = +")
print("2 = -")
print("3 = *")
print("4 = /")
#print("5 = **")
#print("6 = %")
#print("7 = //")

mathchoice = input("Type: ")

if mathchoice == 0:
    print("ga")
elif mathchoice == "1":
    plus1 = float(input(enter1))
    plus2 = float(input(enter2))
    plusans = plus1 + plus2
    print(plusans)
    input(leavemes)
elif mathchoice == "2":
    minus1 = float(input(enter1))
    minus2 = float(input(enter2))
    minusans = minus1 - minus2
    print(minusans)
    input(leavemes)
elif mathchoice == "3":
    star1 = float(input(enter1))
    star2 = float(input(enter2))
    starans = star1 * star2
    print(starans)
    input(leavemes)
elif mathchoice == "4":
    slash1 = float(input(enter1))
    slash2 = float(input(enter2))
    slashans = slash1 / slash2
    print(slashans)
    input(leavemes)
