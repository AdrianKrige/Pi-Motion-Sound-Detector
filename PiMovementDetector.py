import RPi.GPIO as GPIO
import time 
import os
from time import gmtime, strftime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
SOUND_PIN = 24
GPIO.setup(MOVEMENT_PIN, GPIO.IN)

while 1:
	GPIO.wait_for_edge(MOVEMENT_PIN, GPIO.RISING)
        time2 = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        print(time2)
        f = open("time.txt", 'a')
        f.write("Movement at " + str(time2))
        f.close()
        os.system("mail -s \"Intruder\" *YOUREMAIL@gmail.com < time.txt")
        time.sleep(10)

