import subprocess

f = open('redpocket.txt')
f2 = open('log.txt', 'w')
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
count = 0
for item in data:
    #print(item)
    amount = item[0]
    address = item[1]
    memo = ""
    if len(item) == 3:
        memo =  item[2]
    #print(amount,address,memo)
    cmd = "blockstack-cli balance " +address
    t =  subprocess.call(cmd, shell=True)
    if t == 1 :
        print(count,item)
    f2.write(str(count)+":"+str(item)+":"+str(t)+"\n")
    count = count + 1
    #print("t is:",t)

#t = subprocess.call("blockstack-cli balance 1234",shell=True)
#print("t is:",t)
f.close()
f2.close()
