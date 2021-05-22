from machine import I2C
i2c = I2C(0)
print(i2c.scan())

vl = VL53L0X(i2c)