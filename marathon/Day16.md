# Day16 使用 Python 控制 DHT22 感測器與繼電器

## 作業一

問題：練習將 DHT22 接於 GPIO 27 接腳，並且更改軟體的接腳設定值，重新執行範例程式，驗證在不同的接腳上安裝 DHT22，程式一樣可以正確地讀出數值。

```
$ sudo apt install python3-pip
$ sudo pip3 install Adafuit_DHT
```

```python3
#!/usr/bin/env python3

import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 27
while True:
	humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR,
	DHT_PIN)
	if humidity is not None and temperature is not None:
		print("Temp={0:0.1f}*C Humidity={1:0.1f}%".format(temperature, humidity)
	else:
		print("Failed to retrieve data from humidity sensor")

```

## 作業二

問題：觀察 RPi.GPIO 的程式碼，與 GPIOZero 程式碼對於繼電器控制上寫法的不同，如果我們要設定 GPIO 26, 19, 13, 6 四個接腳控制一個四路繼電器，練習實作一個 GPIOZero 四路繼電器的控制程式。

RPi.GPIO:

```python3
#!/usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep

relay_pin1 = 26
relay_pin2 = 19
relay_pin3 = 13
relay_pin4 = 6
pin_list = [relay_pin1, relay_pin2, relay_pin3, relay_pin4)

GPIO.setmode(GPIO.BCM)
for now_pin in pin_list:
	GPIO.setup(now_pin, GPIO.OUT)
	GPIO.output(now_pin, 1)

relay_list = [relay1, relay2, relay3, relay4]

try:
	while True:
		for now_relay in relay_list:
			GPIO.output(now_relay, 0)
			sleep(1)
		for now_relay in relay_list:
			GPIO.output(now_relay, 1)
			sleep(1)
except KeyboardInterrupt:
	pass
	GPIO.cleanup()
```

GPIOZero:

```python3
#! /usr/bin/env python3

import sys
import time
import gpiozero

relay_pin1 = 26
relay_pin2 = 19
relay_pin3 = 13
relay_pin4 = 6

relay1 = gpio.zero.OutputDevice(relay_pin1,active_high=False, initial_value=False)
relay2 = gpio.zero.OutputDevice(relay_pin2,active_high=False, initial_value=False)
relay3 = gpio.zero.OutputDevice(relay_pin3,active_high=False, initial_value=False)
relay4 = gpio.zero.OutputDevice(relay_pin4,active_high=False, initial_value=False)

relay_list = [relay1, relay2, relay3, relay4]

try:
	while True:
		for now_relay in relay_list:
			now_relay.off()
			sleep(1)
		for now_relay in relay_list:
			now_relay.on()
			sleep(1)
	
except KeyboardInterrupt:
	set_relay1.off()
	set_relay2.off()
	set_relay3.off()
	set_relay4.off()
	sys.exit(0)
```

## 作業三

問題：將作業 1 與作業 2 結合，設定程式在溫度 10 度以下，打開 GPIO26，溫度 10 度以上到 20 度之間，控制 GPIO19，溫度 20 度到 30 度之間，控制 GPIO13，溫度在 30 度以上，控制 GPIO6，達成在不同的溫度區間時，控制不同的繼電器的需求。

```python3
#! /usr/bin/env python3

import Adafruit_DHT
import time
import sys
import gpiozero

relay_pin1 = 26
relay_pin2 = 19
relay_pin3 = 13
relay_pin4 = 6

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

relay1 = gpio.zero.OutputDevice(eval(relay_pin1),active_high=False, initial_value=False)
relay2 = gpio.zero.OutputDevice(eval(relay_pin2),active_high=False, initial_value=False)
relay3 = gpio.zero.OutputDevice(eval(relay_pin3),active_high=False, initial_value=False)
relay4 = gpio.zero.OutputDevice(eval(relay_pin4),active_high=False, initial_value=False)

relay_list = [relay1, relay2, relay3, relay4]

def set_only_one_relay_on(on_relay):
	for now_relay in relay_list:
		if now_relay == on_relay
			now_relay.on()
		else:
			now_relay.off()

case = 0
while True:
	humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
	if humidity is not None and temperature is not None:
		print("Temp={0:0.1f}*C Humidity={1:0.1f}".format(temperature, humidity))

	if temperature < 10:
		if case != 1 :
			case = 1
			set_only_one_relay_on(relay1)
	elif temperature > 20:
		if case != 2:
			case = 2
			set_only_one_relay_on(relay2)
	elif temperature > 30:
		if case != 3:
			case = 3
			set_only_one_relay_on(relay3)
	else:
		if case != 4:
			case = 4
			set_only_one_relay_on(relay4)
      
	# this is the time between taking readings and acting on them you can reduce it but not below 5 seconds
	time.sleep(30)
```
