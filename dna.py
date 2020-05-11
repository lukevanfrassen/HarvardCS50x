import csv
from cs50 import get_string
from sys import argv

if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1)
print(f"hello, {argv[1]}")
file = open(argv[1])
reader = csv.reader(file)
data = list(reader)
file2 = open(argv[2], "r")
reader2 = file2.read()
count = 0
hicount = 0
print("data:"+ str(len(data)))
print("txt:"+ reader2)
for j in range(len(data[0])-1):

        hit = len(str(data[0][j+1]))
        for i in range(len(reader2)):
            if str(reader2)[i:i+hit] == data[0][j+1]:
                count = count +1;
                if str(reader2)[i:i+hit] != str(reader2)[i+hit:i+hit+hit]:
                    if count > hicount:
                        hicount = count
                    count = 0
        data[0][j+1] = hicount
        count =0
        hicount = 0
print("data:"+ str(data))
truers = 0
for k in range(len(data)-1):
    truers = 0
    for l in range(len(data[k+1])-1):
        if data[k+1][l+1] == str(data[0][l+1]):
            truers = truers + 1
    if truers == (len(data[0]) -1):
            print("Name:" + str(data[k+1][0]))
            exit(0)
    else:
        print("No name:" + str(truers))

print("No name:" + str(len(data[0]) -1))
exit(0)


