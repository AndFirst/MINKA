import os
import network
import time
import json
import ufirebase as firebase
import ssd1306
from machine import Pin, SoftI2C
from random import randint
from hcsr04 import HCSR04


# oled initialisation
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


def get_data(path:str) -> tuple:
    '''
    Getting data from config json file.
    '''
    with open(path) as config:
        data = json.load(config)
    ssid = data['ssid']
    password = data['password']
    bin_id = data['id']
    return ssid, password, bin_id


def connect_to_wifi(ssid:str, password:str) -> None:
    '''
    Connect to given WiFi network.
    Print connecting process on OLED.
    '''
    wlan = network.WLAN(network.STA_IF)
    if not wlan.active() or not wlan.isconnected():
        wlan.active(True)
        wlan.connect(ssid, password)
        oled.text('Connecting', 0, 0)
        x = 0
        while not wlan.isconnected():
            oled.text('.', x, 10)
            x += 8
            time.sleep(0.5)
            oled.show()
        oled.fill(0)
        oled.text('Connected', 0, 0)
        oled.show()
        time.sleep(2)


class TrashBin:
    def __init__(self):
        self._distance_sensor = HCSR04(trigger_pin=5, echo_pin=18)
        self._opening_sensor = Pin(15, Pin.IN)
        self._distance = None
        self._opened = False
        self._full = False

    def distance_sensor(self):
        """
        Getter to distance sensor.
        """
        return self._distance_sensor

    def opening_sensor(self):
        """
        Getter to opening sensor.
        """
        return self._opening_sensor

    def distance(self):
        """
        Returns distance between sensor and rubbish.
        """
        return self._distance

    def opened(self):
        """
        Return true if trash bin opened.
        """
        return self._opened

    def full(self) -> bool:
        """
        Return bin fill state.
        """
        return self._full

    def make_full(self) -> None:
        """
        Set fill state to full.
        """
        self._full = True

    def make_empty(self) -> None:
        """
        Set bin state to empty.
        """
        self._full = False

    def check_distance(self):
        """
        Check distance between sensor and trash.
        """
        self._distance = self._distance_sensor.distance_cm()

    def check_open(self):
        """
        Check if trash bin is opened.
        Change bin opened status if opened
        """
        if self._opening_sensor.value():
            self._opened = True
        else:
            self._opened = False


def print_joke(joke: str) -> None:
    """
    Split joke to lines
    print lines in OLED.
    """
    x, y = 0, 20
    lines = joke.split('\n')
    for line in lines:
        oled.text(line, x, y)
        y += 10


def get_joke_from_database() -> None:
    """
    Draw joke id and get from firebase
    joke for this id.
    """
    joke_id = randint(0, 59)
    firebase.get(f'dad_jokes/{joke_id}', 'JOKE')


if __name__ == '__main__':
    # connect to WiFi
    ssid, password, bin_id = get_data('config.json')
    connect_to_wifi(ssid, password)

    # prepare to connect with database
    URL = ""
    firebase.setURL(URL)

    # create sensor
    trash_bin = TrashBin()

    # get first joke from database
    get_joke_from_database()

    # mainloop of program
    while True:
        trash_bin.check_distance()
        trash_bin.check_open()
        if trash_bin.opened():
            if trash_bin.distance() < 5:
                oled.fill(0)
                oled.text('BLAD ODCZYTU', 0, 0)
                oled.text('SPRAWDZ CZUJNIK', 0, 10)
            else:
                oled.fill(0)
                oled.text('SMIETNIK OTWARTY', 0, 0)
                oled.text('ZAMKNIJ POKRYWE', 0, 10)
            get_joke_from_database()
        else:
            if trash_bin.distance() < 5:
                trash_bin.make_full()
                oled.fill(0)
                oled.text('JESTEM PELNY', 0, 0)
                oled.text('WYRZUC SMIECI', 0, 20)
                oled.text('OPOWIEM CI ZART', 0, 40)
            else:
                trash_bin.make_empty()
                oled.fill(0)
                oled.text('CZEKAM NA', 0, 0)
                oled.text('TWOJE SMIECI', 0, 10)
                print_joke(firebase.JOKE)

        oled.show()
        firebase.patch(f"bins/{bin_id}", {'full': trash_bin.full()}, bg=0)
        time.sleep(1)

