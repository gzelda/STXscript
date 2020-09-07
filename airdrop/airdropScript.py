import subprocess
import time

f = open('./data/STX_address_2.txt')
f2 = open('l1-l128.txt', 'w')

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
        curLine=line.strip().split(" ")
        data.append(curLine)
        #print(curLine)
    count = count + 1


#print(data, count)



for i in range(126):
    #print(item)
    amount = data[i][1]
    address = data[i][0]
    print(amount, address)

    cmd = "blockstack-cli send_tokens " + address +" STACKS " #+ "$prikey $prikey"
    amountf = float(amount)
    amountf = int(amountf * 1000000)
    print(amountf,type(amountf))
    cmd = cmd + str(amountf) + " \"$prikey\" \"$prikey\" " + " -F 6"
    print("commond is:" ,cmd)
    
    t =  subprocess.call(cmd, shell=True)
    f2.write(str(i)+":"+str(cmd)+":"+str(t)+"\n")
    time.sleep(20)
    if i % 20 == 0:
        time.sleep(1200)

#t = subprocess.call("blockstack-cli balance 1234",shell=True)
#print("t is:",t)
#subprocess.call("echo $GTY",shell=True)

f.close()
f2.close()
