"""
Autor : Douglas Nascimento (Shrek18.5)
https://www.youtube.com/watch?v=r8Qg3NfdiHc


"""
import cv2

webcam = cv2.VideoCapture(0)

if webcam.isOpened():
    print('Conectou')
    validacao, frame = webcam.read()
    while validacao:
        validacao, frame = webcam.read()
        cv2.imshow('Video da Webcam', frame)
        key = cv2.waitKey(10)
        if key == 27: #ESC
            break
    cv2.imwrite('FotoDouglas.png', frame)

webcam.release()

cv2.destroyAllWindows()