# -*- coding: utf-8 -*-

# ������ ������ ���������
import math
import numpy
import matplotlib.pyplot as mpp

# ���� ������ ������� ��������������
if __name__=='__main__':
    # ��������� arguments ������, ��������� ����� �� 0 �� 200 � ����� 0.1
    arguments = numpy.r_[0:200:0.1]
    # �������� ������ �� �����:
    mpp.plot(
        # �������� ������ �����
        arguments,
        # �� �������� - ������ �������� ������� sin(x)/sin(x/20) ��� ������ ����� �� ������ arguments
        [math.sin(a) * math.sin(a/20.0) for a in arguments]
    )
    # ������ ��� ���������� �������
    mpp.show()