from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Greenhouse(object):
    LEDS = {
        'red': [16, 11, 23],
        'white': [13, 9, 27],
        'green': [21, 12, 25],
        'blue': [20, 6, 22],
    }

    target_temperature_lower = 5
    target_temperature_upper = 30

    target_humidity_lower = 0.3
    target_humidity_upper = 0.6

    target_soil = 0.6

    target_light = 0.6

    @property
    def temperature(self):
        return 30.0

    @property
    def humidity(self):
        return 0.4

    @property
    def soil(self):
        return 0.6

    @property
    def light(self):
        return 0.8

    @property
    def temperature_status(self):
        lower = self.target_temperature_lower
        upper = self.target_temperature_upper
        return lower <= self.temperature <= upper

    @property
    def humidity_status(self):
        lower = self.target_humidity_lower
        upper = self.target_humidity_upper
        return lower <= self.humidity <= upper

    @property
    def soil_status(self):
        return self.soil >= self.target_soil

    @property
    def light_status(self):
        return self.light >= self.target_light

    def __init__(self):
        self._setup_gpio()

    def _setup_gpio(self):
        for colour in self.LEDS:
            for led in self.LEDS[colour]:
                GPIO.setup(led, GPIO.OUT)
                GPIO.output(led, False)

    def _turn_led_on_or_off(self, colour, index, on_or_off):
        led = self.LEDS[colour][index]
        GPIO.output(led, on_or_off)

    def _turn_colour_leds_on_or_off(self, colour, on_or_off):
        leds = self.LEDS[colour]
        for led in range(len(leds)):
            if on_or_off:
                self.turn_led_on(colour, led)
            else:
                self.turn_led_off(colour, led)

    def _turn_all_leds_on_or_off(self, on_or_off):
        for colour in self.LEDS:
            if on_or_off:
                self.turn_colour_leds_on(colour)
            else:
                self.turn_colour_leds_off(colour)

    def turn_led_on(self, colour, index):
        """
        Turn a single LED on, by colour and index

        e.g. turn_led_on('red', 0)
        """
        self._turn_led_on_or_off(colour, index, on_or_off=True)

    def turn_led_off(self, colour, index):
        """
        Turn a single LED off, by colour and index

        e.g. turn_led_off('red', 0)
        """
        self._turn_led_on_or_off(colour, index, on_or_off=False)

    def turn_colour_leds_on(self, colour):
        """
        Turn all LEDs of a particular colour on

        e.g. turn_colour_leds_on('red')
        """
        self._turn_colour_leds_on_or_off(colour, on_or_off=True)

    def turn_colour_leds_off(self, colour):
        """
        Turn all LEDs of a particular colour off

        e.g. turn_colour_leds_off('red')
        """
        self._turn_colour_leds_on_or_off(colour, on_or_off=False)

    def turn_all_leds_on(self):
        """
        Turn all LEDs on
        """
        self._turn_all_leds_on_or_off(on_or_off=True)

    def turn_all_leds_off(self):
        """
        Turn all LEDs off
        """
        self._turn_all_leds_on_or_off(on_or_off=False)

def main():
    greenhouse = Greenhouse()
    if greenhouse.temperature_status:
        print("Temperature ok")
    else:
        print("Temperature not ok")
    if greenhouse.humidity_status:
        print("Humidity ok")
    else:
        print("Humidity not ok")
    if greenhouse.soil_status:
        print("Soil ok")
    else:
        print("Soil not ok")
    if greenhouse.light_status:
        print("Light ok")
    else:
        print("Light not ok")

if __name__ == '__main__':
    main()
