#-*- coding: utf-8 -*-
"""
# Binary Robust Independent Elementary Features(BRIEF)
    . SIFT는 512바이트, SURF는 256바이트의 메모리가 필요함
    . 실제 검출시 모두 필요하지 않음
    . SIFT나 SURF는 부동소수점을을 이용하여 처리를 하는데 이를 binary 문자열로 변환하여
      처리하면 고속 처리가 가능해짐
    . opencv_contrib 설치가 필요함 (OpenCV 3.0)
"""

import cv2
import numpy as np

