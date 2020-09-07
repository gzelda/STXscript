import subprocess
import time

f0 = open('log69-500.txt')
f1 = open('log318-count.txt')
f2 = open('./data/STX_address_2.txt', 'w')

count = 0
data = []
def isSpecial(i):
    if i=="\n" or i=="\t" or i==" ":
        return True
    else:
        return False

while True:
    line = f0.readline()
    if not line:
        break
    else:
        #print("new:",count)
        curLine=line.strip().split(" ")
        data.append(curLine)
        #print(curLine)
    count = count + 1

while True:
    line = f1.readline()
    if not line:
        break
    else:
        #print("new:",count)
        curLine=line.strip().split(" ")
        data.append(curLine)
        #print(curLine)
    count = count + 1

#print(data)

for item in data:
    print(item)
    number = item[0].split(":")[0]
    address = item[2]
    amount = str(int(item[4])/1000000)
    status = item[9]
    if status == "6:1":
        cmd = "blockstack-cli convert_address " + address
        t =  subprocess.call(cmd, shell=True)
        print(t)
        if t == 0:
            f2.write(address + " " + amount + "\n")
        #f2.write(number + " " + address + " " + amount + "\n")

f0.close()
f1.close()
f2.close()   
