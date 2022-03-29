import m5stick as stick

while True:
  dist = stick.read_sonar_distance()
  msg = "Distance = {}\"".format(dist)
  stick.display_message(msg)
  wait_ms(100)
