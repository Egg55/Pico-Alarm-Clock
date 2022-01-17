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
beep = Pin(20,Pin.OUT)

#immages

#heart
#TH = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00?\xe0\x07\xfc\x00\x00\x00\x00\xff\xfc?\xff\x00\x00\x00\x01\xff\xfe\x7f\xff\x80\x00\x00\x03\xff\xff\xff\xff\xc0\x00\x00\x07\xff\xff\xff\xff\xe0\x00\x00\x07\xff\xff\xff\xff\xe0\x00\x00\x07\xff\xff\xff\xff\xe0\x00\x00\x07\xff\xff\xff\xff\xe0\x00\x00\x07\xff\xff\xff\xff\xe0\x00\x00\x03\xff\xff\xff\xff\xc0\x00\x00\x03\xff\xff\xff\xff\xc0\x00\x00\x01\xff\xff\xff\xff\x80\x00\x00\x00\xff\xff\xff\xff\x00\x00\x00\x00\x7f\xff\xff\xfe\x00\x00\x00\x00?\xff\xff\xfc\x00\x00\x00\x00\x1f\xff\xff\xf8\x00\x00\x00\x00\x0f\xff\xff\xf0\x00\x00\x00\x00\x07\xff\xff\xe0\x00\x00\x00\x00\x03\xff\xff\xc0\x00\x00\x00\x00\x01\xff\xff\x80\x00\x00\x00\x00\x00\xff\xff\x00\x00\x00\x00\x00\x00\x7f\xfe\x00\x00\x00\x00\x00\x00?\xfc\x00\x00\x00\x00\x00\x00\x1f\xf8\x00\x00\x00\x00\x00\x00\x0f\xf0\x00\x00\x00\x00\x00\x00\x07\xe0\x00\x00\x00\x00\x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x01\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

#ily
#TH = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x00\x00\x00\x00\x00\x07\x80\x1f\x81\xe0<<?\x87\x80?\xc1\xe0<?\xff\x87\x80\x7f\xe1\xf0<?\xff\x87\x80\x7f\xe1\xf0\xfc?\xff\x07\x80\x7f\xf1\xf8\xfc\x0f\xf8\x07\xc0y\xf0\xfd\xf8\x01\xf0\x07\xc0\xf9\xfc\xff\xf0\x01\xf0\x07\xc0\xf8\xfc\x7f\xe0\x01\xf0\x03\xc0\xf8\xfc\x7f\xc0\x0f\xfe\x03\xc0\xf8|?\x80\x0f\xfe\x03\xe0\xfc<\x1f\x00\x0f\xfe\x03\xfe\xfe\xfc\x1f\x00\x0f\xfc\x03\xfe\x7f\xfc\x1e\x00\x00\x00\x01\xfe?\xf8\x1c\x00\x00\x00\x01\xfc\x1f\xf0\x00\x00\x00\x00\x00\x00\x0f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x80\xf0\x00\x00\x00\x00\x00\x07\x81\xf0\x00\x00\x00\x00\x00\x07\xc1\xf0\x00\x00\x00\x00\x00\x07\xc1\xf8\x00\x00\x00\x00\x00\x07\xc1\xf8\x00\x00\x00\x00\x00\x03\xe1\xf8\x00\x00\x00\x00\x00\x03\xe0\xf8\x00\x00\x00\x00\x00\x03\xe0x\x00\x00\x00\x00\x00\x01\xe0x\x00\x00\x00\x00\x00\x01\xf0\xf8\x00\x00\x00\x00\x00\x01\xf1\xf8\x00\x00\x00\x00\x00\x01\xf3\xf0\x00\x00\x00\x00\x00\x00\xff\xf0\x00\x00\x00\x00\x00\x00\xff\xe0\x00\x00\x00\x00\x00\x00\xff\x80\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

def byteimg(TH):
    fb = framebuf.FrameBuffer(TH,64,64, framebuf.MONO_HLSB)

    for x in range(192):
        oled.fill(0)
        oled.blit(fb,x-64,0)
        oled.show()

#funky mode
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

def checkval(val,mn,mx):
    if val < 1:
        val = 5
    if 5 < val:
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
    #split hours and minutes
    hours, minutes = time24.split(':')
    # change hours into integer
    hours = int(hours) 
    # if hours is 00 make it 24 
    hours = 24 if not hours else hours
    #then do the math over noon time
    if hours > 12:
        hours -= 12
        td = 'PM'
    # or leave it alone if it's AM
    else:
        td = 'AM'
    #then put it all together and return it
    return str(hours)+':'+str(minutes)+' '+td



def showtime():
    time = list(rtc.datetime())
    if len(str(time[5])) == 1:
        t24 = str(time[4])+':0'+str(time[5])
    if len(str(time[5])) == 2:
        t24 = str(time[4])+':'+str(time[5])
    return time24to12(t24)

hour = 0
minute = 0
out = False

oled.fill(0)
oled.show()

while True:
   
    
    #oled.text(str(showtime()), 0, 0)
    rngnumdisp(str(showtime()))
    oled.show()
    
    if sel.value():
        oled.text("Loading...", 0, 0)
        oled.show()
        sleep(0.5)
        while True:
            
            #check if value is out of range and correct it
            val = checkval(val,1,5)
            
            #display menu depending on value inputed
            oled.text('Menu',48,0)
            
            if val == 1:
                oled.text(' 1: Alarm',0,18)
                oled.text('2: Time',0,27)
                oled.text('3: Display',0,36)
                oled.text('4: General',0,45)
                oled.text('5: Back', 0, 54)
            if val == 2:
                oled.text('1: Alarm',0,18)
                oled.text(' 2: Time',0,27)
                oled.text('3: Display',0,36)
                oled.text('4: General',0,45)
                oled.text('5: Back', 0, 54)
            if val == 3:
                oled.text('1: Alarm',0,18)
                oled.text('2: Time',0,27)
                oled.text(' 3: Display',0,36)
                oled.text('4: General',0,45)
                oled.text('5: Back', 0, 54)
            if val == 4:
                oled.text('1: Alarm',0,18)
                oled.text('2: Time',0,27)
                oled.text('3: Display',0,36)
                oled.text(' 4: General',0,45)
                oled.text('5: Back', 0, 54)
            if val == 5:
                oled.text('1: Alarm',0,18)
                oled.text('2: Time',0,27)
                oled.text('3: Display',0,36)
                oled.text('4: General',0,45)
                oled.text(' 5: Back', 0, 54)
            oled.show()
            oled.fill(0)
            
            #incramit or decramit menu value 
            val = iodval(val,5)
                
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
                                settime = (''+str(hour)+':'+str(minute))
                                out = True
                    
                    oled.fill(0)
                    
            if sel.value() and val == 5:
                print('breaking')
                sleep(1)
                break
            
            #reset display
            oled.fill(0)

oled.fill(0)
oled.show()

print('done!')