import m5stick as stick
import time
import socket_client as client


WIFI_NAME = 'LOCAL_NETGEAR'
WIFI_PASSWORD = 'woodbury'
IP_ADDRESS = '192.168.1.2'
PORT = 8080


def main():
    stick.connect_to_wifi(WIFI_NAME, WIFI_PASSWORD)
    client.connect(IP_ADDRESS, PORT, stick)
    buffer = stick.SampleBuffer(3)
    while True:
        dist = stick.read_sonar_distance()
        buffer.add(dist)
        client.send("dist={}".format(buffer.mean()))


main()

