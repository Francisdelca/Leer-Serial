from serial import Serial
arduino = Serial('/dev/ttyACM0',9600, timeout = 1)

while True:
    try:
        a = arduino.readline()
        print(a)
    except keyboardInterrupt:
        break
arduino.close()