from cs50 import get_int
card = input("Enter your card #?:\n")
length = len(str(card))
oddsum = 0
evensum = ""
j = 0
for i in card[::-1]:
    if j%2 == 1:
        evensum += str(int(i)* 2)

    else:
        oddsum += int(i)
    j+=1

for i in evensum:
    oddsum += int(i)

if oddsum % 10 == 0:
    if length == 15 and ( str(card)[0:2] == "34" or str(card)[0:2] == "37"):
        print("American Express")
    elif length == 13 and str(card)[0:1] == "4":
        print("VISA")
    elif length == 16 and str(card)[0:1] == "4":
        print("VISA")
    elif length == 16 and str(card)[0:1] == "5" and 1<= int(str(card)[1:2]) <= 5:
        print("Mastercard")
    else:
        print("Valid #, invalid card")
else:
    print("sum:" + str(card)[0:2])