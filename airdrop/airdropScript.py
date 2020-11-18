import subprocess
import time

f = open('./data/STX_address_201118.txt')
f2 = open('201118-1.txt', 'w')

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


print(data, count)



for i in range(0, 27):
    #print(item)
    amount = data[i][1]
    address = data[i][0]
    memo = ""
    print(amount, address, memo)

    cmd = "blockstack-cli-Gavin send_tokens " + address +" STACKS " #+ "$prikey $prikey"
    amountf = float(amount)
    amountf = int(amountf * 1000000)
    print(amountf,type(amountf))
    cmd = cmd + str(amountf) + " \"$prikey\" \"$prikey\" " 

    if len(data[i]) == 3:
        memo =  data[i][2]
        cmd = cmd + memo

    cmd = cmd + " -F 6"

    print("commond is:" ,cmd)
    
    t =  subprocess.call(cmd, shell=True)
    f2.write(str(i)+":"+str(cmd)+":"+str(t)+"\n")
    time.sleep(20)
    if i % 20 == 0:
        time.sleep(1800)

#t = subprocess.call("blockstack-cli balance 1234",shell=True)
#print("t is:",t)
#subprocess.call("echo $GTY",shell=True)

f.close()
f2.close()
