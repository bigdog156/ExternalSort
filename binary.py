import random
import struct


def readBinaFile(PATH,size):
    arrdata = []
    bina = open(PATH,"rb+")
    for i in range(size):
        data = bina.read(4)
        arrdata.append(struct.unpack("f",data)[0])
    print(arrdata)
    return arrdata

#Tạo và random số ghi nhị phân vào file
def binaryFile(PATH,size):
    bina = open(PATH,"wb+")
    for i in range(size):
        num = random.uniform(-100000000,100000000)
        ba = bytearray(struct.pack("f",num))
        bina.write(ba)
    bina.close()

# data = randomNumber(5)
# openBinaryFile("/Users/lethachlam/Desktop/UIT_HK7/CTRR_NC/bina.bin",data)
PATH = "/Users/lethachlam/Desktop/UIT_HK7/CTRR_NC/External_Sort/bina.dat"
binaryFile(PATH,4096000)
readBinaFile(PATH,4096000)
    