#-Coded on Linux-#
#-Created by British Gentleman-#

#-MIT License
#
#Copyright (c) 2026 British Gentleman
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.-#

#-Variables-#
AppName = "SuperCalculator"
Version = "0.5"
License = "Copyright (c) 2026 British Gentleman"
enter1 = "Enter first number: "
enter2 = "Enter second number: "
leavemes = "Press enter to exit "
idk = "0"
Plus = "1"
Minus = "2"
Star = "3"
Slash = "4"
TwoStar = "5"
Percent = "6"
SlashSlash = "7"

#-Start-#
print(f"Welcome to {Name}!")
print(f"Version number: {Version}")
print(f"{License}")
print("")
print("Select a Mathematical operator")
print("1 = +")
print("2 = -")
print("3 = *")
print("4 = /")
print("5 = **")
print("6 = %")
print("7 = //")

mathchoice = input("Type: ")

if mathchoice == "0":
    print("01100110 01101001 01110010 01100101 00100000 01100101 01111000 01110100 01101001 01101110 01100111 01110101 01101001 01110011 01101000 01100101 01110010 00100000 01101001 01101110 00100000 01100011 01101000 01101001 01101110 01100101 01110011 01100101 00100000 01110100 01101111 00100000 01100101 01101110 01100111 01101100 01101001 01110011 01101000 00100000 01101001 01110011 00101100 00100000 01001000 01100001 01101110 01100100 00100000 01100111 01110010 01100101 01101110 01100001 01100100 01100101")
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

elif mathchoice == "5":
    starstar1 = float(input(enter1))
    starstar2 = float(input(enter2))
    starstarans = starstar1 ** starstar2
    print(starstarans)
    input(leavemes)

elif mathchoice == "6":
    percent1 = float(input(enter1))
    percent2 = float(input(enter2))
    percentans = percent1 ** percent2
    print(percentans)
    input(leavemes)

elif mathchoice == "7":
    slashslash1 = float(input(enter1))
    slashslash2 = float(input(enter2))
    slashslashans = slashslash1 ** slashslash2
    print(percentans)
    input(leavemes)
print("Cya")