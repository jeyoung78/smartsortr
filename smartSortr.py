import requests

url = "https://mantis-object-detection.p.rapidapi.com/rest/v1/public/detectObjects/base64/json"

import base64
from io import BytesIO
from PIL import Image

import RPi.GPIO as GPIO
import time

import cv2 as cv
import RPi.GPIO as GPIO
import numpy as np

cam = cv.VideoCapture(0)
font = cv.FONT_HERSHEY_SIMPLEX

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14, GPIO.OUT)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

ret, frame = cam.read()
    
numpy_array = frame
cv.imwrite('output.jpg', numpy_array)

image_path = "/home/jeyoung7/raspberry-camera-object-recognition/output1.jpg"

image = Image.open(image_path)

buffered = BytesIO()
image.save(buffered, format="JPEG")
img_str = base64.b64encode(buffered.getvalue())

headers = {
    "content-type": "text/plain",
    "X-RapidAPI-Key": "",
    "X-RapidAPI-Host": "mantis-object-detection.p.rapidapi.com"
}

image = Image.open('/home/jeyoung7/raspberry-camera-object-recognition/output1.jpg')
image.show()

response = requests.post(url, data=img_str, headers=headers)
print(response.json())

recycle = {'bottle', 'glass bottle', 'plastic bottle', 'can', 'cup', 'plastic cup','utensil', 'paper',  'newspaper', 'shredded paper', 'paper bags', 'box'}
label = response['detected-objects'][0]['label']

if label in recycle:
    GPIO.output(18, True)
else:
    GPIO.output(23, False)



