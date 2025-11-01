import requests   
import json     
import time
import RPi.GPIO as GPIO

KEY_1   ="......"             #put your signal key here  
VALUE_1 = 0                  #this is a variable
TOKEN_1  ="................................................." #the token is found under account in circusofthings.com

data_1={'Key':'0','Value':0,'Token':'0'}     

redLED = 12
         
GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BOARD)		#set pin numbering system
GPIO.setup(redLED,GPIO.OUT)
pi_pwm = GPIO.PWM(redLED,1000)		#create PWM instance with frequency
pi_pwm.start(0)				#start PWM of required Duty Cycle 

while True:
    data_1['Key'] = KEY_1 
    data_1['Value']=VALUE_1
    data_1['Token']=TOKEN_1

    payload = data_1
    response=requests.get('https://circusofthings.com/ReadValue',params=payload)

    datahandling=json.loads(response.content)  
    i = datahandling["Value"]
    print(i)
    pi_pwm.ChangeDutyCycle(i)

    time.sleep(2)
