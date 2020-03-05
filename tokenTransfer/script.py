import subprocess

f = open('redpocket.txt')

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
        #print("new:",count)
        curLine=line.strip().split("\t")
        data.append(curLine)
        #print(curLine)

    count = count + 1

#print(data)

for item in data:
    #print(item)
    amount = item[0]
    address = item[1]
    memo = ""
    if len(item) == 3:
        memo =  item[2]
    print(amount,address,memo)
    cmd = "blockstack-cli balance " +address
    subprocess.call(cmd, shell=True)
