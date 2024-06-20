import numpy as np
import cv2
import time

def transformarImagem(imagem):
    classificador =  cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    #imagem = cv2.imread('imagens/imagens Angelo/Pessoas-Angelo/vencedores-trabalho-tales.jpg')
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    facesDetectadas = classificador.detectMultiScale(imagemCinza)

    cv2.imshow("Imagem Analisada", imagem)
    cv2.waitKey()

    print("Na foto, o sistema encontrou " + str(len(facesDetectadas)) + " faces")

#Ocorreram alguns problemas com algumas imagens, provavelmente pelas imagens de treinamento serem mais focadas e profissionais, o problema foi solucionado cortando os arredores da imagem e focando mais no rosto

transformarImagem(cv2.imread('imagens/imagens Angelo/Pessoas-Angelo/vencedores-trabalho-tales.jpg'))
transformarImagem(cv2.imread('imagens/imagens Angelo/Pessoas-Angelo/Homossexuais-e-Angelo.jpg'))
transformarImagem(cv2.imread('imagens/imagens Angelo/Pessoas-Angelo/primos-Angelo.jpg'))