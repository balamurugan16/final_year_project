from smbus2 import SMBus
from mlx90614 import MLX90614 as mlx

def tempTest():
     bus = SMBus(1)
     sensor = mlx(bus,address=0x5A)
     obj_temp,amb_temp = round(sensor.get_object_1(),2), round(sensor.get_ambient(),2)
     bus.close()
     return obj_temp







