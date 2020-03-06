import subprocess
import time

f = open('data3-6screen3.txt')
f2 = open('logdata3-6screen3.txt', 'w')

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
    #print(amount,address,memo)
    #cmd = "blockstack-cli balance " +address
    cmd = "blockstack-cli send_tokens " + address +" STACKS " #+ "$prikey $prikey"
    amountf = float(amount)
    amountf = int(amountf * 1000000)
    #print(amountf,type(amountf))
    cmd = cmd + str(amountf) + " \"$prikey\" \"$prikey\" "
    if len(item) == 3:
        memo =  item[2]
        cmd = cmd + memo
    print("commond is:" ,cmd)
    t =  subprocess.call(cmd, shell=True)
    time.sleep(3)
    #if t == 1 :
    #    print(count,item)
    f2.write(str(count)+":"+str(cmd)+":"+str(t)+":"+str(item)+"\n")
    count = count + 1
    if count % 24 == 0:
        time.sleep(1200)
    #print("t is:",t)

#t = subprocess.call("blockstack-cli balance 1234",shell=True)
#print("t is:",t)
#subprocess.call("echo $GTY",shell=True)
f.close()
f2.close()
