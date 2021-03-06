#Pico alarm clock

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep
import framebuf
import random
from urtc import DS1307
import utime

i2c = I2C(1,scl = Pin(3),sda = Pin(2),freq = 400000)
rtc = DS1307(i2c)
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

oled.text("Powering On", 0, 0)
oled.show()
sleep(0.5)
oled.fill(0)

btu = Pin(15, Pin.IN)
btd = Pin(14, Pin.IN)
sel = Pin(13, Pin.IN)
beep = Pin(16,Pin.OUT)

def rngnumdisp(num):
    if random.randint(1,10) == 1:
        oled.fill(0)
        
    ranint = random.randint(0,1)
    if ranint == 1:
        vertical = random.randint(17,57)
    else:
        vertical = random.randint(0,9)
    
    horizontal = random.randint(0,75)
        
    oled.text(str(num), horizontal, vertical)
    oled.show()
    sleep(0.01)

def alarm():
    while True:
        if sel.value():
            break
        beep.value(1)
        sleep(0.2)
        beep.value(0)
        sleep(0.1)
        beep.value(1)
        sleep(0.2)
        beep.value(0)
        sleep(0.5)

val = 1
def checkval(val,mx):
    if val < 1:
        val = mx
    if mx < val:
        val = 1
    return val

def iodval(val,mx):
    if btu.value():
        val-=1
        sleep(0.3)
    if btd.value() and val < mx+1:
        val+=1
        sleep(0.3)
    return val

def time24to12(time24):
    hours, minutes = time24.split(':')
    hours = int(hours) 
    hours = 24 if not hours else hours
    if hours > 12:
        hours -= 12
        td = 'PM'
    else:
        td = 'AM'
    return str(hours)+':'+str(minutes)+' '+td

def showtime():
    time = list(rtc.datetime())
    if len(str(time[5])) == 1:
        t24 = str(time[4])+':0'+str(time[5])
    if len(str(time[5])) == 2:
        t24 = str(time[4])+':'+str(time[5])
    return time24to12(t24)

def checkalarm():
    lines = []
    f = open('alarms.txt', 'r')
    lines = f.readlines()
    f.close()
    
    if len(lines) > 1:
        f = open('alarms.txt', 'w')
        for number, line in enumerate(lines):
            if number not in [0]:
                f.write(line)
        f.close()

def checktime():
    hour = rtc.datetime()[4]
    minute = rtc.datetime()[5]
    f = open('alarms.txt', 'r')
    atime = f.readlines()[0]
    
    if str(atime) == str(hour)+':'+str(minute)+'\n':
        alarm()

hour = 0
minute = 0
out = False

oled.fill(0)
oled.show()

while True:
    rngnumdisp(str(showtime()))
    
    if sel.value():
        oled.fill(0)
        oled.text("Loading...", 0, 0)
        oled.show()
        sleep(0.5)
        while True:
            out = False
            val = checkval(val, 3)
            oled.text('Menu',48,0)
            
            if val == 1:
                oled.text(' 1: Alarm',0,18)
                oled.text('2: Time',0,27)
                oled.text('3: Back', 0, 36)
            if val == 2:
                oled.text('1: Alarm',0,18)
                oled.text(' 2: Time',0,27)
                oled.text('3: Back',0,36)
            if val == 3:
                oled.text('1: Alarm',0,18)
                oled.text('2: Time',0,27)
                oled.text(' 3: Back',0,36)
                
            oled.show()
            oled.fill(0)
            
            val = iodval(val,3)
            
            if sel.value() and val == 1:
                oled.fill(0)
                oled.text("Loading...", 0, 0)
                oled.show()
                sleep(0.5)
                val = 1
                while True:
                    out = False
                    checkalarm()
                    val = checkval(val,2)
                    oled.text('Alarms',48,0)
                    oled.show()
                    oled.fill(0)
                    
                    if val == 1:
                        oled.text(' 1: Set Alarm',0,18)
                        oled.text('2: Back',0,27)
                    if val == 2:
                        oled.text('1: Set Alarm',0,18)
                        oled.text(' 2: Back',0,27)
                        
                    val = iodval(val,2)
                    
                    if sel.value() and val == 2:
                        break
                               
                    if sel.value() and val == 1:
                        oled.fill(0)
                        oled.text("Loading...", 0, 0)
                        oled.show()
                        sleep(0.5)
                        while out == False:
                            if hour > 24:
                                hour = 0
                            if hour < 0:
                                hour = 24
                            
                            oled.text('Set Alarm',32,0)
                            oled.text('Hour: '+time24to12(str(hour)+':00'),0,9)
                            oled.show()
                            
                            if btu.value():
                                hour += 1
                                sleep(0.1)
                            if btd.value():
                                hour -= 1
                                sleep(0.1)
                            
                            if sel.value():
                                oled.fill(0)
                                oled.text("Loading...", 0, 0)
                                oled.show()
                                sleep(0.5)
                                while out == False:
                                    if minute > 59:
                                        minute = 0
                                    if minute < 0:
                                        minute = 59
                                    
                                    oled.text('Alarms',32,0)
                                    oled.text('Minute: '+str(minute),0,9)
                                    oled.show()
                                    
                                    if btu.value():
                                        minute += 1
                                        sleep(0.1)
                                    if btd.value():
                                        minute -= 1
                                        sleep(0.1)
                                    
                                    oled.fill(0)
                                    
                                    if sel.value():
                                        f = open("alarms.txt", "a")
                                        if minute < 10:
                                            minute ='0'+str(minute)
                                        f.write(str(hour)+':'+str(minute)+'\n')
                                        f.close
                                        out = True
                                        sleep(0.5)
                                        checkalarm()
                                    
                            oled.fill(0)
                
                
            if sel.value() and val == 2:
                oled.fill(0)
                oled.text("Loading...", 0, 0)
                oled.show()
                sleep(0.5)
                while out == False:
                    if hour > 24:
                        hour = 0
                    if hour < 0:
                        hour = 24
                    
                    oled.text('Set Time',32,0)
                    oled.text('Hour: '+time24to12(str(hour)+':00'),0,9)
                    oled.show()
                    
                    if btu.value():
                        hour += 1
                        sleep(0.1)
                    if btd.value():
                        hour -= 1
                        sleep(0.1)
                    
                    if sel.value():
                        oled.fill(0)
                        oled.text("Loading...", 0, 0)
                        oled.show()
                        sleep(0.5)
                        while out == False:
                            #input minute
                            if minute > 59:
                                minute = 0
                            if minute < 0:
                                minute = 59
                            
                            oled.text('Set Time',32,0)
                            oled.text('Minute: '+str(minute),0,9)
                            oled.show()
                            
                            if btu.value():
                                minute += 1
                                sleep(0.1)
                            if btd.value():
                                minute -= 1
                                sleep(0.1)
                            
                            oled.fill(0)
                            
                            if sel.value():
                                #set the time
                                tlis = rtc.datetime()
                                now = (tlis[0],tlis[1],tlis[2],tlis[3],hour,minute,tlis[6],0)
                                rtc.datetime(now)   
                                
                                out = True
                                sleep(0.5)
                    
                    oled.fill(0)     
            if sel.value() and val == 4:
                sleep(1)
                break
            
            oled.fill(0)

print('how did you get here?')
