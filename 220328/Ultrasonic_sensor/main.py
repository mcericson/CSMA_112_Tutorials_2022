import m5stick as stick

while True:
  dist = stick.read_sonar_distance()
  stick.display_message(dist)
  wait_ms(100)