from __future__ import division
import time
import Adafruit_PCA9685
#-*- coding:utf-8 -*-
import serial
ser=serial.Serial('/dev/ttyUSB0',115200)
import math
pwm = Adafruit_PCA9685.PCA9685()
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //=100    # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# 设置频率为60Hz，这是一个比较好的值
pwm.set_pwm_freq(100)

#代码42c  socket02c.py
#!/usr/bin/env python3
#coding:utf -8
import socket
import time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.2.99',8088))
print('I am connecting the server!')


x='1'
todos=open('data.txt','w')
while 1:
    s.send(x.encode('utf -8'))
   
   
    str1=s.recv(1024)
    str2=str(str1,encoding='utf - 8')
    if int(str2)==3 :
        '''
        pwm.set_pwm(15,0,500)
        pwm.set_pwm(0,0,200)
        '''
      ##电机复位
        continue
    else:
        print('transfer start...')
    for n in range(90):
        a=int(900-n*4.4)
        print(a)
        #print(n,file=todos)
        pwm.set_pwm(15,0,a)
        time.sleep(0.1)
        pwm.set_pwm(15,0,0)
        
        if n%2!=0:
            for i in range(180):
                b=int(200+i*4.4)
                #print(b)
                pwm.set_pwm(0,0,b)
                time.sleep(0.01)
                pwm.set_pwm(0,0,0)
                #time.sleep(0.01)
                #count=ser.inWaiting()
                
                if  ser.inWaiting():
                    count=ser.inWaiting()
                    if count!='  ':
                        
                        recv=ser.read(count)
                        recv=str(recv,encoding='utf-8')
                        recv=str.strip(recv)
                        print(n,'    ',i,'   ',recv,file=todos)
                    #time.sleep(0.01)
               
        if n%2==0:
            for i1 in range(180):
                c=int(1000-i1*4.4)
                #print(c)
                pwm.set_pwm(0,0,c)
                time.sleep(0.01)
                pwm.set_pwm(0,0,0)
                #time.sleep(0.01)
                count=ser.inWaiting()
                if ser.inWaiting():
                    recv=ser.read(count)
                    recv=str(recv,encoding='utf-8')
                    recv=str.strip(recv)
                    print(n,'   ',i1,'   ',recv,file=todos) 
    break
todos.close()
ser.close()

#500-900  
f=open('data.txt','r')
for line in f:
   

   line=line.strip()
   if s.recv(1024):
      s.send(line.encode('utf -8'))
f.close()
s.close()  
