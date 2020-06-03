import serial
import time
import matplotlib.pyplot as plt
import numpy as np

# XBee setting
serdev = '/dev/ttyUSB0'
s = serial.Serial(serdev, 9600)

s.write("+++".encode())
char = s.read(2)
print("Enter AT mode.")
print(char.decode())

s.write("ATRE\r\n".encode())
char = s.read(3)
print("Reset the XBee.")
print(char.decode())

s.write("ATMY 0x327\r\n".encode())
char = s.read(3)
print("Set MY 0x327.")
print(char.decode())

s.write("ATDL 0x427\r\n".encode())
char = s.read(3)
print("Set DL 0x427.")
print(char.decode())

s.write("ATID 0x2\r\n".encode())
char = s.read(3)
print("Set PAN ID 0x2.")
print(char.decode())

s.write("ATWR\r\n".encode())
char = s.read(3)
print("Write config.")
print(char.decode())

s.write("ATMY\r\n".encode())
char = s.read(4)
print("MY :")
print(char.decode())

s.write("ATDL\r\n".encode())
char = s.read(4)
print("DL : ")
print(char.decode())

s.write("ATCN\r\n".encode())
char = s.read(3)
print("Exit AT mode.")
print(char.decode())

print("start sending RPC")
num = 0
number_log = []

while num != 4:
    s.write("/getAcc/run\r".encode())
    time.sleep(1)
    num += 1
c = s.read(1)
num = 0
while num != 200:
    line = s.readline().decode()
    #line = s.read(1)
    number_log.append(float(line))
    print(line)
    num += 1
number_log[0] = 2


s.close()