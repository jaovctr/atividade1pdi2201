import matplotlib.pyplot as plt
from copy import deepcopy as copia

folha = plt.imread("folha.png")
print(folha)
plt.imshow(folha)
plt.show()

#adj4
folhaAdj4=copia(folha)
for y in range(255):
  for x in range(255):
    if folha[x][y][0]==1 and folha[x][y][1]==1 and folha[x][y][2]==1:
      if x>0 and y>0 and x<254 and y<255:
        esquerda = bool (folha[x-1][y][0]==1 and folha[x-1][y][1]==1 and folha[x-1][y][2]==1) 
        cima = bool (folha[x][y-1][0]==1 and folha[x][y-1][1]==1 and folha[x][y-1][2]==1)
        direita = bool (folha[x+1][y][0]==1 and folha[x+1][y][1]==1 and folha[x+1][y][2]==1)
        baixo = bool (folha[x][y+1][0]==1 and folha[x][y+1][1]==1 and folha[x][y+1][2]==1)
        if(esquerda and cima and direita and baixo):
            folhaAdj4[x][y][0]=0 
            folhaAdj4[x][y][1]=0
            folhaAdj4[x][y][2]=0
      
plt.imshow(folhaAdj4)
plt.show()

#adj8
folhaAdj8=copia(folha)
for y in range(255):
  for x in range(255):
    if folha[x][y][0]==1 and folha[x][y][1]==1 and folha[x][y][2]==1:
      if x>0 and y>0 and x<254 and y<254:
        esquerda = bool (folha[x-1][y][0]==1 and folha[x-1][y][1]==1 and folha[x-1][y][2]==1)   
        supEsquerda = bool (folha[x-1][y-1][0]==1 and folha[x-1][y-1][1]==1 and folha[x-1][y-1][2]==1)
        cima = bool (folha[x][y-1][0]==1 and folha[x][y-1][1]==1 and folha[x][y-1][2]==1)
        supDireita = bool (folha[x+1][y+1][0]==1 and folha[x+1][y+1][1]==1 and folha[x+1][y+1][2]==1)
        direita = bool (folha[x+1][y][0]==1 and folha[x+1][y][1]==1 and folha[x+1][y][2]==1)
        infEsquerda = bool (folha[x-1][y+1][0]==1 and folha[x-1][y+1][1]==1 and folha[x-1][y+1][2]==1)
        baixo = bool (folha[x][y+1][0]==1 and folha[x][y+1][1]==1 and folha[x][y+1][2]==1)
        infDireita = bool (folha[x+1][y+1][0]==1 and folha[x+1][y+1][1]==1 and folha[x+1][y+1][2]==1)
        if(esquerda and cima and direita and baixo and supEsquerda and supDireita and infEsquerda and infDireita):
            folhaAdj8[x][y][0]=0 
            folhaAdj8[x][y][1]=0
            folhaAdj8[x][y][2]=0
      
plt.imshow(folhaAdj8)
plt.show()
