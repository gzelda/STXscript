import subprocess
import time

f = open('./data/STX_address.txt')
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



count = 10
cmd = "npx stx-bulk-transfer "
for i in range(0, count):
    #print(item)
    amount = data[i][1]
    address = data[i][0]
    memo = ""
    print(amount, address, memo)
    #npx stx-bulk-transfer STADMRP577SC3MCNP7T3PRSTZBJ75FJ59JGABZTW,100 ST2WPFYAW85A0YK9ACJR8JGWPM19VWYF90J8P5ZTH,50 -k my_private_key -n testnet -b


t =  subprocess.call(cmd, shell=True)


f.close()
f2.close()
