import numpy as np
import cv2
print(cv2.__version__)
imagem = cv2.imread('imagens/imagens Angelo/a a folou a folou u.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
imagemIFollow = cv2.imread('imagens/imagens Angelo/letra_i_follow.png')
cv2.imshow("Original", imagem)
cv2.imshow("Cinza", imagemCinza)
cv2.imshow("A A FOLLOW, A FOLLOW U", imagemIFollow)
cv2.waitKey()
