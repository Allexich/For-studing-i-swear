# -*- coding: utf-8 -*-

# импорт нужных библиотек
import math
import numpy
import matplotlib.pyplot as mpp

# если модуль запущен самостоятельно
if __name__=='__main__':
    # присвоить arguments список, одержащий числа от 0 до 200 с шагом 0.1
    arguments = numpy.r_[0:200:0.1]
    # помещаем график на холст:
    mpp.plot(
        # абсциссы нужных точек
        arguments,
        # их ординаты - список значений функции sin(x)/sin(x/20) для каждой точки из списка arguments
        [math.sin(a) * math.sin(a/20.0) for a in arguments]
    )
    # рисуем все помещенные графики
    mpp.show()