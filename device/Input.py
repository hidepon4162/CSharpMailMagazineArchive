import utime
from machine import ADC


class Potentiometer:

    def __init__(self, pin):
        self.pin = pin
        self.meter = ADC(self.pin)

    conversion_factor = 3.3 / (65535)

    interval = .03
    diffratio = .3
    ratio = 0
    diffcount = 5
    count = 0

    def get_ratio(self):
        voltage = self.meter.read_u16() * self.conversion_factor / 3.3 * 100

        return voltage

    def get_value(self):

        adjustRatio = self.get_ratio()

        print(adjustRatio)
        diff = self.ratio - adjustRatio

        if abs(diff) > self.diffratio:
            self.count = self.count + 1

            if self.count > self.diffcount:

                self.ratio = adjustRatio
                self.count = 0

        else:
            self.count = 0

        utime.sleep(self.interval)

        return self.ratio


class Soilsensor:

    def __init__(self, pin, highLebelVoltage, lowLebelVoltage):
        self.pin = pin
        self.sensor = ADC(self.pin)
        self.highLebelVoltage = highLebelVoltage
        self.lowLebelVoltage = lowLebelVoltage
        self.conversion_factor = 3.3 / (65535)

        self.needWater = True

    def get_value(self):
        voltage = self.sensor.read_u16() * self.conversion_factor
        return voltage

    def get_needWater(self):
        reading = self.get_value()
        
        print(reading)

        if self.needWater == False and reading > self.lowLebelVoltage:
            self.needWater = True

        if self.needWater == True and reading < self.highLebelVoltage:
            self.needWater = False

        return self.needWater
