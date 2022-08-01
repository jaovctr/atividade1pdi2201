import matplotlib.pyplot as plt
from copy import deepcopy as copia
from PIL import Image
import math
import numpy as np

lena = plt.imread("lena_gray.bmp")

#Histograma simples 
def histograma(foto):
    intensidade=[0]*256
    dimensoes=foto.shape          
    for x in range (dimensoes[0]):
        for y in range(dimensoes[1]):
            valor=foto[x][y]
            intensidade[valor]=intensidade[valor]+1
    return intensidade

eixox=[]
for i in range(256):
    eixox.append(i)

plt.bar(eixox, histograma(lena))
plt.title("histograma")
plt.xlabel("nivel")
plt.ylabel("quantidade")
plt.show()


#histograma fdp
def histogramaFdp(foto):
    histSimples=histograma(foto)
    dimensoes=foto.shape
    totalPixels=dimensoes[0]*dimensoes[1]
    histFdp=[0]*256
    for i in range(256):
        fdp=histSimples[i]/totalPixels
        histFdp[i]=fdp
    return histFdp

histFdp=histogramaFdp(lena)
plt.bar(eixox, histFdp)
plt.title("histograma fdp")
plt.xlabel("nivel")
plt.ylabel("quantidade")
plt.show()


#histograma acumulado
def histogramaAcum(foto):
    histFdp=histogramaFdp(foto)
    histAcum=[]
    acum=histFdp[0]
    for x in histFdp:
        histAcum.append(acum)
        acum=acum+x
    return histAcum

histAcum=histogramaAcum(lena)    
plt.bar(eixox, histAcum)
plt.title("histograma acumulado")
plt.xlabel("nivel")
plt.ylabel("quantidade")
plt.show()


#função de equalização
def equalizar(foto):
    histAcum=histogramaAcum(foto)
    transformado=[0]*256
    for x in range(256):
        valort=histAcum[x]*256
        transformado[x]=round(valort,0)
    imagemEq=copia(foto)
    dimensoes=foto.shape
    for x in range (dimensoes[0]):
        for y in range (dimensoes[1]):          
            valorAntigo=foto[x][y]        
            imagemEq[x][y]=transformado[valorAntigo]
    return imagemEq


lenaEq=equalizar(lena)
plt.imshow(lenaEq,cmap="gray")
plt.show()

lenaEq2x=equalizar(lenaEq)
plt.imshow(lenaEq2x,cmap="gray")
plt.show()

img1Original=Image.open("image1.png")
imggray=img1Original.convert('L')
imggray.save("image1.bmp")
image1=plt.imread("image1.bmp")

image1Eq=equalizar(image1)
plt.imshow(image1,cmap="gray")
plt.show()

image1Eq2x=equalizar(image1Eq)
plt.imshow(image1Eq2x,cmap="gray")
plt.show()


#questao4 letra a
def transfIntensidade(foto,c,b):
    hist=histogramaAcum(foto)
    transformado=[0]*256
    for x in range(256):
        valort=((c*hist[x])+b)*256
        transformado[x]=round(valort,0)
    imagemEq=copia(foto)
    dimensoes=foto.shape
    for x in range (dimensoes[0]):
        for y in range (dimensoes[1]):            
            valorAntigo=foto[x][y]                    
            imagemEq[x][y]=transformado[valorAntigo]
    return imagemEq

fatorC=float(input("digite o valor C:"))
fatorB=float(input("digite o fator B:"))
lenaIn=transfIntensidade(lena, fatorC, fatorB)
plt.imshow(lenaIn,cmap="gray")
plt.show()       

#4 letra b
def transfLog(foto,c):
    imagemEq=copia(foto)
    hist=histogramaAcum(foto)
    transformado=[0]*256
    for x in range(256):
        valort=(c*math.log2(hist[x]+1))*256
        transformado[x]=round(valort,0)
    dimensoes=foto.shape
    for x in range (dimensoes[0]):
        for y in range (dimensoes[1]):            
            valorAntigo=foto[x][y]                    
            imagemEq[x][y]=transformado[valorAntigo]
    return imagemEq

fatorC=float(input("digite o valor C:"))
lenaLog=transfLog(lena, fatorC)
plt.imshow(lenaEq,cmap="gray")
plt.show() 

#q4 letra c
#c × (f + 1)^gama
def transfGama(foto,c,gama):
    imagemEq=copia(foto)
    hist=histogramaAcum(foto)
    transformado=[0]*256
    for x in range(256):
        valort=(c*(hist[x]+1)**gama)*256
        transformado[x]=round(valort,0)
    dimensoes=foto.shape
    for x in range (dimensoes[0]):
        for y in range (dimensoes[1]):            
            valorAntigo=foto[x][y]                    
            imagemEq[x][y]=transformado[valorAntigo]
    return imagemEq



fatorC=float(input("digite o valor C:"))
gama=float(input("digite o valor gama:"))
lenaGama=transfGama(lena, fatorC, gama)
plt.imshow(lenaGama,cmap="gray")
plt.show()

#5a 
def especificaHistograma(foto, histEntrada):
    acumFoto=histogramaAcum(foto)
    transfEntrada=[0]*256
    transEspec=[0]*256
    for x in range(256):
        valort=acumFoto[x]*255
        transfEntrada[x]=valort
        valortEspec=histEntrada[x]*255
        transEspec[x]=valortEspec    
    histSaida=[0]*256    
    nptransEspec = np.asarray(transEspec)
    for i in range(256):
        maisprox = nptransEspec[(np.abs(nptransEspec - transfEntrada[i])).argmin()]
        histSaida[i]=round(maisprox,0)    
    imagemSaida=copia(foto)
    dimensoes=foto.shape
    for x in range(dimensoes[0]):
        for y in range(dimensoes[1]):
            valorAntigo=foto[x][y]
            imagemSaida[x][y]=histSaida[valorAntigo]
    return imagemSaida


img1=plt.imread("image1.bmp")
img1Saida=especificaHistograma(img1, histogramaAcum(lena))
plt.imshow(img1Saida,cmap="gray")
plt.show()
