"""
Autor : Douglas Nascimento (Shrek18.5)
Obs: Execício baseado no curso de ADS da UNINTER modulo EAD de 2022


"""
import cv2
import numpy as np

img = cv2.imread('OpenCV_Logo.png', cv2.IMREAD_COLOR)

cv2.namedWindow('Hello World')
cv2.imshow('Hello World', img )
cv2.waitKey()