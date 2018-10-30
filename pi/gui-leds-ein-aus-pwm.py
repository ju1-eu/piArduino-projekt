#!/usr/bin/python3
from tkinter import *
import RPi.GPIO as gpio, signal
gpio.setmode(gpio.BOARD)#Pins 1-40
gpio.setwarnings(False)  

ledPin1 = 35
ledPin2 = 33
ledPWMPin = 37
motAntrieb_vorPin = 12
motAntrieb_backPin = 16
motLenkung_leftPin = 18
motLenkung_rightPin = 22

gpio.setup(ledPin1, gpio.OUT) 
gpio.setup(ledPin2, gpio.OUT) 
gpio.setup(ledPWMPin, gpio.OUT) 
gpio.setup(motAntrieb_vorPin, gpio.OUT) 
gpio.setup(motAntrieb_backPin, gpio.OUT) 
gpio.setup(motLenkung_leftPin, gpio.OUT) 
gpio.setup(motLenkung_rightPin, gpio.OUT) 

gpio.output(ledPin1, gpio.LOW)
gpio.output(ledPin2, gpio.LOW)
gpio.output(ledPWMPin, gpio.LOW)
gpio.output(motAntrieb_vorPin, gpio.LOW)
gpio.output(motAntrieb_backPin, gpio.LOW)
gpio.output(motLenkung_leftPin, gpio.LOW)
gpio.output(motLenkung_rightPin, gpio.LOW)

# pwm
pwm1 = gpio.PWM(ledPWMPin, 1000)          # Frequenz: 1000 Hertz
pwm1.start(0)                             # Duty:     anfangs 0%
pwm2 = gpio.PWM(motAntrieb_vorPin, 1000)# Frequenz: 1000 Hertz
pwm2.start(0)                             # Duty:     anfangs 0%
pwm3 = gpio.PWM(motAntrieb_backPin, 1000)# Frequenz: 1000 Hertz
pwm3.start(0)                             # Duty:     anfangs 0%
pwm4 = gpio.PWM(motLenkung_leftPin, 1000) # Frequenz: 1000 Hertz
pwm4.start(0)                             # Duty:     anfangs 0%
pwm5 = gpio.PWM(motLenkung_rightPin, 1000)# Frequenz: 1000 Hertz
pwm5.start(0)                             # Duty:     anfangs 0%

# Reaktion auf Mausklick im Fenster
def pwmChange1(value):
  pwm1.ChangeDutyCycle(float(value))
def pwmChange2(value):
  pwm2.ChangeDutyCycle(float(value))
def pwmChange3(value):
  pwm3.ChangeDutyCycle(float(value))
def pwmChange4(value):
  pwm4.ChangeDutyCycle(float(value))
def pwmChange5(value):
  pwm5.ChangeDutyCycle(float(value))
  

# ein/aus
# Reaktion auf Mausklick im Fenster
def pinChange1():
  if pinStatus1.get():
    gpio.output(ledPin1, gpio.HIGH)  
    lb1.configure(text='high')
  else:
    gpio.output(ledPin1, gpio.LOW)  
    lb1.configure(text='low')
def pinChange2():
  if pinStatus2.get():
    gpio.output(ledPin2, gpio.HIGH)  
    lb2.configure(text='high = 3,3 V')
  else:
    gpio.output(ledPin2, gpio.LOW)  
    lb2.configure(text='low = 0 V')
  
  
# Programmende durch Windows-Close-Button
def win_close():
  gpio.cleanup()
  root.quit()

# Programmende durch Strg+C im Terminal
def strg_c(signal, frame):
  win_close()

# regelmäßiger Aufruf, damit Strg+C funktioniert
def do_nothing():
  root.after(200, do_nothing)

# Benutzeroberfläche
root = Tk()         # Fenster
root.wm_title('LED - Motor')# Titel

# ein/aus
pinStatus1 = IntVar()
pinStatus2 = IntVar()

# label - ein/aus
lb1 = Label(root, text='LED - low')
lb2 = Label(root, text='LED - low')
btn1 = Checkbutton(root, text='LED ein/aus', indicatoron=0, variable=pinStatus1,command=pinChange1, padx=10, pady=10)
btn2 = Checkbutton(root, text='LED ein/aus', indicatoron=0, variable=pinStatus2,command=pinChange2, padx=10, pady=10)

# label - pwm
lb3 = Label(root, text='LED-PWM steuern')
lb4 = Label(root, text='Antrieb-vor-PWM steuern')
lb5 = Label(root, text='Antrieb-back-PWM steuern')
lb6 = Label(root, text='Lenkung-links-PWM steuern')
lb7 = Label(root, text='Lenkung-rechts-PWM steuern')

# scale - pwm
pinscale1 = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=pwmChange1)
pinscale2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=pwmChange2)
pinscale3 = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=pwmChange3)
pinscale4 = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=pwmChange4)
pinscale5 = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=pwmChange5)
pinscale1.set(0)# Duty:     anfangs 0%
pinscale2.set(0)
pinscale3.set(0)
pinscale4.set(0)
pinscale5.set(0)

# grid - ein/aus
# label - 1. Zeile u. 1., 2. Spalte
lb1.grid(row=0, column=0, padx=5, pady=5)
lb2.grid(row=0, column=1, padx=5, pady=5)
# button - 2. Zeile u. 1., 2. Spalte 
btn1.grid(row=1, column=0, padx=5, pady=5)
btn2.grid(row=1, column=1, padx=5, pady=5)

# grid - pwm
# label - 3. Zeile u. 1. Spalte
lb3.grid(row=2, column=0, padx=5, pady=5)
# scale - 4. Zeile u. 14 Spalte
pinscale1.grid(row=3, column=0, padx=5, pady=5)

# label - 5. Zeile u. 1., 2., 3., 4. Spalte
lb4.grid(row=4, column=0, padx=5, pady=5)
lb5.grid(row=4, column=1, padx=5, pady=5)
lb6.grid(row=4, column=2, padx=5, pady=5)
lb7.grid(row=4, column=3, padx=5, pady=5)
# scale - 6. Zeile u. 1., 2., 3., 4. Spalte
pinscale2.grid(row=5, column=0, padx=5, pady=5)
pinscale3.grid(row=5, column=1, padx=5, pady=5)
pinscale4.grid(row=5, column=2, padx=5, pady=5)
pinscale5.grid(row=5, column=3, padx=5, pady=5)

# Ereignisse
root.protocol("WM_DELETE_WINDOW", win_close) # ordentliches Programmende, wenn Fenster geschlossen wird
signal.signal(signal.SIGINT, strg_c) # auf Strg+C in Terminal reagieren
root.after(200, do_nothing)          # damit Strg+C funktioniert

root.mainloop()

