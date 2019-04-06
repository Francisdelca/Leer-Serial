from serial import Serial
arduino = Serial('/dev/ttyACM0',9600, timeout = 1)

while True:
    try:
        a = arduino.readline() #se lee lo que llega por el serial
        #v = '' +str(int(a))
        file = open('sensor.txt','w') # cracion del archivo que guarda el valor
        file.write(a)
        file.close()
        print(a)
    except keyboardInterrupt:
        break
arduino.close()
