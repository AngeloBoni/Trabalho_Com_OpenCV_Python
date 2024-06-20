import numpy as np
import cv2

def colocarQuadrados(imagem):
    classificador = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    #imagem = cv2.imread('imagens\imagens Angelo\\Pessoas-Angelo\\primos-Angelo.jpg')
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    facesDetectadas = classificador.detectMultiScale(imagemCinza)
    print(len(facesDetectadas))
    print((facesDetectadas))

    for (x, y, l, a) in facesDetectadas:
        print(x, y, l, a)
        cv2.rectangle(imagem, (x,y), (x + l, y + a), (0, 0, 255), 2)
    cv2.imshow("Faces Encontradas", imagem)
    cv2.waitKey()

imagemPrimos = cv2.imread('imagens\\imagens Angelo\\Pessoas-Angelo\\primos-Angelo.jpg') 
imagemVencedores = cv2.imread('imagens\\imagens Angelo\\Pessoas-Angelo\\vencedores-trabalho-tales.jpg')
imagemAmigos = cv2.imread('imagens\\imagens Angelo\\Pessoas-Angelo\\Homossexuais-e-Angelo.jpg')

colocarQuadrados(imagemPrimos)
colocarQuadrados(imagemVencedores)
colocarQuadrados(imagemAmigos)
 