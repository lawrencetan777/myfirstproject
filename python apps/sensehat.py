from sense_emu import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()


def orientation():
    orientation = sense.get_orientation()
    pitch = round(orientation["pitch"], 1)
    roll = round(orientation["roll"], 1)
    yaw = round(orientation["yaw"], 1)
    sense.show_message("Pitch {0}, Roll {1}, Yaw {2}".format(pitch, roll, yaw))


def temperature():
    temp = round(sense.get_temperature(), 1)
    sense.show_message("Temperature: %s degrees Celsius" % temp)


def humidity():
    humidity = round(sense.get_humidity(), 1)
    sense.show_message("Humidity: %s percent" % humidity)


def pressure():
    pressure = round(sense.get_pressure(), 1)
    sense.show_message("Pressure: %s millibars" % pressure)


def compass():
    for i in range(1, 10):
        north = round(sense.get_compass(), 1)
    sense.show_message("North: %s degrees" % north)


sense.stick.direction_up = orientation
sense.stick.direction_right = temperature
sense.stick.direction_down = compass
sense.stick.direction_left = humidity
sense.stick.direction_middle = pressure
while True:
    pass
