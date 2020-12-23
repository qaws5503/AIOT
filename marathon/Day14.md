# Day14 使用程式控制 GPIO 接腳

## Raspberry PI 接腳圖

![image1](https://github.com/qaws5503/AIOT/blob/master/pictures/RaspberryPI_pin.png)

圖片取自 Cupoy 課程

## 作業一

問題：實際安裝 gpiozero，先安裝 RPi.GPIO，再安裝 pigpio，觀察安裝過程系統顯示的訊息。比較直接啟動 raspi-config 的 interfacing 選項，透過啟動 Remote GPIO，直接安裝GPIOZero。

Raspberry PI 的系統都已經內建 RPi.GPIO, pigpio, gpiozero

依然可以再用指令檢查更新

```linux
$ sudo apt update
$ sudo apt install python3-rpi.gpio
$ sudo apt install pigpio python-pigpio python3-pigpio
$ sudo apt install python3-pip
$ sudo pip3 install gpiozero
```

## 作業二

問題：實際練習 GPIOZero 控制 LED，確定單獨的 GPIO 控制 LED 亮跟暗交替閃爍完成，並且 PWM 控制 LED 明亮的完成後，嘗試依序改變led.value的值，分別設定 0.1, 0.3, 0.5, 0.7 觀察差異。

```python3
# LED明亮控制1

from gpiozero import LED
from time import sleep

led = PWMLED(17)

while True:
	led.on()
	sleep(1)
	led.off()
	sleep(1)
```

```python3
# LED明亮控制2

from gpiozero import LED
from signal import pause

led = PWMLED(17)

led.blink()

pause()
```

```python3
# LED控制PWM

from gpiozero import PWMLED
from time import sleep

led = PWMLED(17)

while True:
	led.value = 0
	sleep(1)
	led.value = 0.1
	sleep(1)
	led.value = 0.3
	sleep(1)
	led.value = 0.5
	sleep(1)
	led.value = 0.7
	sleep(1)

```

```python3
# LED呼吸燈

from gpiozero import PWMLED
from signal import pause

led = PWMLED(17)

led.pulse()

pause()
```

## 作業三

問題：實際練習 GPIOZero 透過 Button 控制 LED，在按鈕的過程中，觀察實際按下按鈕的次數，LED 點亮的次數，是否一致。練習修改程式，讓按鈕按下是全亮，按鈕放開後是 30% 的亮度。

```python3
# GPIO Button click number

from gpiozero import Button

button_click_number = 0
button = Button(2)

while True:
	if button.is_pressed:
		button_click_number += 1
		print(button_click_number)
```

使用 button.is_pressed

```python3
# GPIO button example 1

from gpiozero import Button
from gpiozero import PWMLED

led = LED(17)
button = Button(2)

while True:
	if button.is_pressed:
		led.value = 1
	else:
		led.value = 0.3
```

透過 button 的 when_pressed 和 when_released 函式來達成

```python3
# GPIO button example 2

from gpiozero import Button
from gpiozero import PWMLED

def led_fullbrightness():
	led.value = 1

def led_lowbrightness():
	led.value = 0.3

led = LED(17)
button = Button(2)

button.when_pressed = led_fullbrightness
button.when_released = led_lowbrightness

pause()
```