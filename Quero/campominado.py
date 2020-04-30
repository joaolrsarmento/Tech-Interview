import random

class Cell:
  def __init__(self):
    self.value = ' '
    self.isFlag = False
    self.unknown = True
    
class Minesweeper:
  
  def __init__(self, largura, altura, nBombas):
    self.h = altura
    self.l = largura
    self.n = nBombas
    
    print('Criando tabuleiro...')
    self.table = self.criaTabuleiro(self.l, self.h, self.n)
    
    self.printaTabuleiro()
  
  def flag(self, x, y):
    if x >= self.h or x < 0 or y >= self.l or y < 0:
      return False
    
    if not self.table[x][y].unknown:
      print('Já clicado.')
      return False
      
    if self.table[x][y].unknown: self.table[x][y].isFlag = True
    elif self.table[x][y].isFlag: self.table[x][y].isFlag = False
    
  def play(self, x, y):

    if x >= self.h or x < 0 or y >= self.l or y < 0:
      print('Jogada invalida.')
      return False
    
    
    if self.table[x][y].value == '#':
      print("Fim de jogo.")
      return False
      
    jogadaValida = True if self.table[x][y].unknown and self.table[x][y].value != 'F' else False
    
    if not jogadaValida:
      print('Jogada invalida.')
      return False
      
    
    self.expande(x, y)
    
    return jogadaValida
    
  def expande(self, x, y):
    
    if x >= self.h or x < 0 or y >= self.l or y < 0:
      return False
    
    if self.table[x][y].value == '#':
      return False
      
    for i in [-1,0,1]:
      for j in [-1,0,1]:
        if (i,j) != (0,0):
          if 0 <= x + i < self.h and 0 <= y + j < self.l:
            valor = self.table[x+i][y+j].value
            if valor == '#':
              return False
            
    if self.table[x][y].unknown and self.table[x][y].value == ' ':
      self.table[x][y].unknown = False
      
      for i in [-1,0,1]:
        for j in [-1,0,1]:
          if (i,j) != (0,0):
            if 0 <= x + i < self.h and 0 <= y + j < self.l:
              if self.table[x+i][y+j].unknown:
                self.expande(x+i, y+j)
            

      
    
  def criaTabuleiro(self, largura, altura, nbombas):
    
    table = [[Cell() for i in range(largura)] for j in range(altura)]
    
    indices = [random.randint(0, largura*altura - 1) for i in range(nbombas)]
  
    for ind in indices:
      
      indx = int(ind // altura)
      indy = int(ind % altura)
      
      table[indy][indx].value = '#'
      
    return table
      
  def printaJogoDoTabuleiro(self):
    tabuleiro = self.table
    for i in range(len(tabuleiro)):
      for j in range(len(tabuleiro[i])):
        print(tabuleiro[i][j].value if not tabuleiro[i][j].unknown else '.' if not tabuleiro[i][j].isFlag else 'F', end = ' ')
      print()
  
  def printaTabuleiro(self):
    tabuleiro = self.table
    for i in range(len(tabuleiro)):
      for j in range(len(tabuleiro[i])):
        print(tabuleiro[i][j].value, end = ' ')
      print()
  
  def stillPlaying(self):
    tabuleiro = self.table
    
    stillPlaying = False 
    
    for i in range(len(tabuleiro)):
      for j in range(len(tabuleiro[i])):
        if tabuleiro[i][j].unknown and tabuleiro[i][j].value != '#':
          stillPlaying = True
          print('Still playing...')
          return True
    
    print('End of game.')
    return False
  
largura = 5
altura = 10

jogo = Minesweeper(largura = 5, altura = 10, nBombas = 1)

while jogo.stillPlaying():
  input()
  jogo.printaJogoDoTabuleiro()
  x,y = random.randint(0, altura-1), random.randint(0, largura-1)
  if jogo.table[x][y].value == '#':
    print('Fim de jogo.')
    break
  print('Playing at', x, y)
  jogo.play(x,y)
