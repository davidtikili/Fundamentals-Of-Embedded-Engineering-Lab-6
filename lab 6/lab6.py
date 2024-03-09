import RPi.GPIO as GPIO
import time

SDI = 11
RCLK = 12
SRCLK = 13
SDI2 = 26
RCLK2 = 15
SRCLK2 = 16

segCode = [0x7f,0x7f,0x0b,0x6f,0x7f,0x0d,0x23,0x63,0x7f,0x21,0x6f,0x21,0x7f,0x10,0x23,0x23,0x21,0x7f,0x71,0x23,0x03,0x7f]
segCode2 = [0x7f,0x0b,0x6f,0x7f,0x0d,0x23,0x63,0x7f,0x21,0x6f,0x21,0x7f,0x10,0x23,0x23,0x21,0x7f,0x71,0x23,0x03,0x7f,0x7f]

def print_msg():
    print ("Program is running...")
    print("please press ctrl + c to end the program...")

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SDI, GPIO.OUT)
    GPIO.setup(RCLK, GPIO.OUT)
    GPIO.setup(SRCLK, GPIO.OUT)
    GPIO.output(SDI, GPIO.HIGH)
    GPIO.output(RCLK, GPIO.HIGH)
    GPIO.output(SRCLK, GPIO.HIGH)
    GPIO.setup(SDI2, GPIO.OUT)
    GPIO.setup(RCLK2, GPIO.OUT)
    GPIO.setup(SRCLK2, GPIO.OUT)
    GPIO.output(SDI2, GPIO.HIGH)
    GPIO.output(RCLK2, GPIO.HIGH)
    GPIO.output(SRCLK2, GPIO.HIGH)
    

def hc595_shift(dat):
    for bit in range(0,8):
        GPIO.output(SDI, 0x80 & (dat << bit))
        GPIO.output(SRCLK, GPIO.LOW)
        time.sleep(0.001)
        GPIO.output(SRCLK, GPIO.HIGH)
    GPIO.output(RCLK, GPIO.LOW)
    time.sleep(0.001)
    GPIO.output(RCLK, GPIO.HIGH)

def hc595_shift2(dat):
    for bit in range(0,8):
        GPIO.output(SDI2, 0x80 & (dat << bit))
        GPIO.output(SRCLK2, GPIO.LOW)
        time.sleep(0.001)
        GPIO.output(SRCLK2, GPIO.HIGH)
    GPIO.output(RCLK2, GPIO.LOW)
    time.sleep(0.001)
    GPIO.output(RCLK2, GPIO.HIGH)

def loop():
    
    while True:
        for i in range(22):
            hc595_shift2(segCode[i])
            hc595_shift(segCode2[i])
            time.sleep(0.5)
       
def destroy():
    GPIO.cleanup()

print_msg()
setup()
try:
    loop()
except KeyboardInterrupt:
    destroy()
