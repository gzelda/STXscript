import subprocess

f = open('redpocket.txt')

'''
line = f.readline()
for i in line:
    if i=="\n":
        print("n")
    elif i=="\t":
        print("t")
    elif i==" ":
        print("space")
'''
count = 0
data = []
def isSpecial(i):
    if i=="\n" or i=="\t" or i==" ":
        return True
    else:
        return False

while True:
    line = f.readline()
    if not line:
        break
    else:
        print("new:",count)
        curLine=line.strip().split("\t")
        data.append(curLine)
        print(curLine)

    count = count + 1

print(data)
