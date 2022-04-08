import m5stick as stick
import socket_client as client
import fusion
#import mockm5stick as stick
#import mocksocketclient as client


WIFI_NAME = ""
WIFI_PASSWORD = ""
IP_ADDRESS = "192.168.1.69"
PORT = 8080

def main():
    stick.connect_to_wifi(WIFI_NAME, WIFI_PASSWORD)
    client.connect(IP_ADDRESS, PORT, stick)
    filter = fusion.MahonyFilter()

    while True:

        
        stick.print_to_screen("pitch", 0, 10)
        stick.print_to_screen("roll", 0, 140)
        stick.print_to_screen("dist =", 0 , 100)

        dist_val = stick.read_sonar_distance()
        accel = stick.read_accelerometer()
        gyro = stick.read_gyroscope()
        filter.update(accel,gyro)
        pitch = round(filter.pitch)
        roll  = round(filter.roll)

        stick.print_to_screen(pitch, 0, 40)
        stick.print_to_screen(roll, 0, 165)
        stick.print_to_screen(dist_val, 80, 100)

  
        msg_1 = build_message("dist", dist_val)
        msg_2 = build_message("pitch", pitch)
        msg_3 = build_message("roll", roll)
        client.send(msg_1)
        client.send(msg_2)
        client.send(msg_3)
        lcd.clear()

def build_message(key, value):
    return "{}={}".format(key, value)




main()