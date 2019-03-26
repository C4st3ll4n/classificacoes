import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier as Dtc
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.externals.six import StringIO
from sklearn import tree
import pydotplus as pdp


dt_treino = pd.read_csv('dados/treino_titanic.csv', index_col=0)
dt_validacao = pd.read_csv('dados/validacao_titanic.csv', index_col=0)

x_treino = np.array(dt_treino[['sexo', 'idade', 'classe']])
y_treino = np.array(dt_treino['sobreviveu'])

x_validacao = np.array(dt_validacao[['sexo', 'idade', 'classe']])
y_validacao = np.array(dt_validacao['sobreviveu'])

modeloAD = Dtc()

modeloAD.fit(x_treino, y_treino)

y_predito = modeloAD.predict(x_validacao)

x_teste = np.array([[2, 2, 3], [2, 1, 1]])

resultado1 = modeloAD.predict(x_teste[0].reshape(1, -1))

resultado2 = modeloAD.predict(x_teste[1].reshape(1, -1))

y_predito_validacao = modeloAD.predict(x_validacao)
y_predito_treino = modeloAD.predict(x_treino)

acuracia_treino = accuracy_score(y_treino, y_predito_treino, normalize=False)
acuracia_validacao = accuracy_score(y_validacao, y_predito_validacao, normalize=False)

# print("Matriz de confusão [Treinamento]\n{}".format(confusion_matrix(y_treino, y_predito_treino)))
# print("Matriz de confusão [Validação]\n{}".format(confusion_matrix(y_validacao, y_predito_validacao)))

arquivo_dot = StringIO()

tree.export_graphviz(modeloAD, out_file=arquivo_dot, node_ids=True, feature_names=['Sexo', 'Idade', 'Classe'], class_names=['SIM', 'NAO'], filled=True)

arvore = pdp.graph_from_dot_data(arquivo_dot.getvalue())

#Recupera todos os nós que possuem arestas (edges)
lista_edge = []
for edge in arvore.get_edge_list():
    lista_edge.append(edge.get_source())

#Recupera todos os nós da Árvore de Decisão
nodes = arvore.get_node_list()
for node in nodes:
    #se é o nó raiz
    if node.get_name() == '0':
        node.set_fillcolor('#F19C99')
    #se o nó não possue arestas, então é um nó folha
    elif node.get_name() not in lista_edge:
        node.set_fillcolor('#E1D5E7')
    #se não é nó raiz nem folha é nó interno
    else:
        node.set_fillcolor('#D5E8D4')

#Salva a nova versão da árvore de decisão em um arquivo *.png
arvore.write_png("arvore_titanic_cores.png")

qtd_nos = modeloAD.tree_.node_count
print("Quantidade de nos -> {}".format(qtd_nos))
