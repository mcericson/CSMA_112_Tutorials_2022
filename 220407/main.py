import m5stick as stick
#import mockm5stick as stick
import socket_client as client
#import mocksocketclient as client


WIFI_NAME = "LOCAL_NETGEAR"
WIFI_PASSWORD = "woodbury"
IP_ADDRESS = "10.20.11.55"
PORT = 8080


def main():
    stick.connect_to_wifi(WIFI_NAME, WIFI_PASSWORD)
    client.connect(IP_ADDRESS, PORT, stick)
    while True:
        dist_val = stick.read_sonar_distance()
        msg = build_message("dist", dist_val)
        client.send(msg)


def build_message(key, value):
    return "{}={}".format(key, value)    


main()