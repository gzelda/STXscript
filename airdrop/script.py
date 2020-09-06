import subprocess
import time

f = open('./data/STX_address.txt')
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


print(data, count)
count = 0

for i in range(100):
    #print(item)
    amount = data[i][1]
    address = data[i][0]
    print(amount, address)

    cmd = "blockstack-cli send_tokens " + address +" STACKS " #+ "$prikey $prikey"
    amountf = float(amount)
    amountf = int(amountf * 1000000)
    print(amountf,type(amountf))
    cmd = cmd + str(amountf) + " \"$prikey\" \"$prikey\" " + " -F 8"
    print("commond is:" ,cmd)
    
    t =  subprocess.call(cmd, shell=True)
    f2.write(str(count)+":"+str(cmd)+":"+str(t)+":"+"\n")
    time.sleep(20)
    if count % 30 == 0:
        time.sleep(1800)
    '''
    cmd = cmd + str(amountf) + " \"$prikey\" \"$prikey\" "
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
    '''
#t = subprocess.call("blockstack-cli balance 1234",shell=True)
#print("t is:",t)
#subprocess.call("echo $GTY",shell=True)

f.close()
f2.close()
