class Vertice:

  def __init__(self, rotulo, distancia_objetivo):
    self.rotulo = rotulo
    self.visitado = False
    self.distancia_objetivo = distancia_objetivo
    self.adjacentes = []

  def adiciona_adjacente(self, adjacente):
    self.adjacentes.append(adjacente)

  def mostra_adjacentes(self):
    for i in self.adjacentes:
      print(i.vertice.rotulo, i.custo)

class Adjacente:
  def __init__(self, vertice, custo):
    self.vertice = vertice
    self.custo = custo

    # Novo atributo
    self.distancia_aestrela = vertice.distancia_objetivo + self.custo

class Grafo:
  porto_uniao = Vertice("Porto União", 203)
  paulo_frontin = Vertice("Paulo Frontin", 172)
  canoinhas = Vertice("Canoinhas", 141)
  tres_barras = Vertice("Três Barras", 131)
  sao_mateus = Vertice("São Mateus do Sul", 123)
  irati = Vertice("Irati", 139)
  curitiba = Vertice("Curitiba", 0)
  palmeira = Vertice("Palmeira", 59)
  mafra = Vertice("Mafra", 94)
  campo_largo = Vertice("Campo Largo", 27)
  balsa_nova = Vertice("Balsa Nova", 41)
  lapa = Vertice("Lapa", 74)
  tijucas_dosul = Vertice("Tijucas do Sul", 56)
  araucaria = Vertice("Araucária", 23)
  sjdospinhais = Vertice("São José dos Pinhais", 13)
  contenda = Vertice("Contenda", 39)

  porto_uniao.adiciona_adjacente(Adjacente(paulo_frontin, 46))
  porto_uniao.adiciona_adjacente(Adjacente(sao_mateus, 87))
  porto_uniao.adiciona_adjacente(Adjacente(canoinhas, 78))

  paulo_frontin.adiciona_adjacente(Adjacente(irati, 75))
  paulo_frontin.adiciona_adjacente(Adjacente(porto_uniao, 46))

  canoinhas.adiciona_adjacente(Adjacente(porto_uniao, 78))
  canoinhas.adiciona_adjacente(Adjacente(tres_barras, 12))
  canoinhas.adiciona_adjacente(Adjacente(mafra, 66))

  tres_barras.adiciona_adjacente(Adjacente(canoinhas, 66))
  tres_barras.adiciona_adjacente(Adjacente(sao_mateus, 43))

  sao_mateus.adiciona_adjacente(Adjacente(tres_barras, 43))
  sao_mateus.adiciona_adjacente(Adjacente(porto_uniao, 87))
  sao_mateus.adiciona_adjacente(Adjacente(irati, 57))
  sao_mateus.adiciona_adjacente(Adjacente(palmeira, 77))
  sao_mateus.adiciona_adjacente(Adjacente(lapa, 60))

  irati.adiciona_adjacente(Adjacente(sao_mateus, 57))
  irati.adiciona_adjacente(Adjacente(paulo_frontin, 75))
  irati.adiciona_adjacente(Adjacente(palmeira, 75))

  curitiba.adiciona_adjacente(Adjacente(campo_largo, 29))
  curitiba.adiciona_adjacente(Adjacente(balsa_nova, 51))
  curitiba.adiciona_adjacente(Adjacente(araucaria, 37))
  curitiba.adiciona_adjacente(Adjacente(sjdospinhais, 15))

  palmeira.adiciona_adjacente(Adjacente(irati, 75))
  palmeira.adiciona_adjacente(Adjacente(sao_mateus, 77))
  palmeira.adiciona_adjacente(Adjacente(campo_largo, 55))

  mafra.adiciona_adjacente(Adjacente(lapa, 57))
  mafra.adiciona_adjacente(Adjacente(tijucas_dosul, 99))
  mafra.adiciona_adjacente(Adjacente(canoinhas, 66))

  campo_largo.adiciona_adjacente(Adjacente(palmeira, 55))
  campo_largo.adiciona_adjacente(Adjacente(balsa_nova, 22))
  campo_largo.adiciona_adjacente(Adjacente(curitiba, 29))

  balsa_nova.adiciona_adjacente(Adjacente(campo_largo, 22))
  balsa_nova.adiciona_adjacente(Adjacente(contenda, 19))
  balsa_nova.adiciona_adjacente(Adjacente(curitiba, 51))

  lapa.adiciona_adjacente(Adjacente(sao_mateus, 60))
  lapa.adiciona_adjacente(Adjacente(contenda, 26))
  lapa.adiciona_adjacente(Adjacente(mafra, 57))

  tijucas_dosul.adiciona_adjacente(Adjacente(mafra, 99))
  tijucas_dosul.adiciona_adjacente(Adjacente(sjdospinhais, 49))

  araucaria.adiciona_adjacente(Adjacente(contenda, 18))
  araucaria.adiciona_adjacente(Adjacente(curitiba, 37))

  sjdospinhais.adiciona_adjacente(Adjacente(curitiba, 15))
  sjdospinhais.adiciona_adjacente(Adjacente(tijucas_dosul, 49))

  contenda.adiciona_adjacente(Adjacente(balsa_nova, 19))
  contenda.adiciona_adjacente(Adjacente(araucaria, 18))
  contenda.adiciona_adjacente(Adjacente(lapa, 26))

grafo = Grafo()

"""## Vetor ordenado (adjacente)"""

import numpy as np
class VetorOrdenado:
  
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    # Mudança no tipo de dados
    self.valores = np.empty(self.capacidade, dtype=object)

  # Referência para o vértice e comparação com a distância para o objetivo
  def insere(self, adjacente):
    if self.ultima_posicao == self.capacidade - 1:
      print('Capacidade máxima atingida')
      return
    posicao = 0
    for i in range(self.ultima_posicao + 1):
      posicao = i
      if self.valores[i].distancia_aestrela > adjacente.distancia_aestrela:
        break
      if i == self.ultima_posicao:
        posicao = i + 1
    x = self.ultima_posicao
    while x >= posicao:
      self.valores[x + 1] = self.valores[x]
      x -= 1
    self.valores[posicao] = adjacente
    self.ultima_posicao += 1

  def imprime(self):
    if self.ultima_posicao == -1:
      print('O vetor está vazio')
    else:
      for i in range(self.ultima_posicao + 1):
        print(i, ' - ', self.valores[i].vertice.rotulo, ' - ', 
              self.valores[i].custo, ' - ', 
              self.valores[i].vertice.distancia_objetivo, ' - ',
              self.valores[i].distancia_aestrela)

grafo.porto_uniao.adjacentes

grafo.porto_uniao.adjacentes[0].vertice.rotulo, grafo.porto_uniao.adjacentes[0].vertice.distancia_objetivo

grafo.porto_uniao.adjacentes[0].distancia_aestrela, grafo.porto_uniao.adjacentes[0].custo

vetor = VetorOrdenado(20)
vetor.insere(grafo.porto_uniao.adjacentes[0])
vetor.insere(grafo.porto_uniao.adjacentes[1])
vetor.insere(grafo.porto_uniao.adjacentes[2])

vetor.imprime()

"""## Busca AEstrela"""

class AEstrela:
  def __init__(self, objetivo):
    self.objetivo = objetivo
    self.encontrado = False

  def buscar(self, atual):
    print('------------------')
    print('Atual: {}'.format(atual.rotulo))
    atual.visitado = True

    if atual == self.objetivo:
      self.encontrado = True
    else:
      vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
      for adjacente in atual.adjacentes:
        if adjacente.vertice.visitado == False:
          adjacente.vertice.visitado = True
          vetor_ordenado.insere(adjacente)
      vetor_ordenado.imprime()

      if vetor_ordenado.valores[0] != None:
        self.buscar(vetor_ordenado.valores[0].vertice)

busca_aestrela = AEstrela(grafo.curitiba)
busca_aestrela.buscar(grafo.porto_uniao)