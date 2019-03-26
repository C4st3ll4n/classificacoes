import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier as Dtc
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.externals.six import StringIO
from sklearn import tree
import pydotplus as pdp


dt_treino = pd.read_csv('Dados/treino_mamifero', index_col=0)
dt_validacao = pd.read_csv('Dados/validacao_mamifero', index_col=0)
dt_teste    = pd.read_csv('Dados/teste_mamifero', index_col=0)
# print(dt_treino)

x_treino = np.array(dt_treino[['Sangue', 'Da a luz', 'Pode voar', 'Mora na agua']])
y_treino = np.array(dt_treino['Mamifero'])

x_validacao = np.array(dt_validacao[['Sangue', 'Da a luz', 'Pode voar', 'Mora na agua']])
y_validacao = np.array(dt_validacao['Mamifero'])

# print(x_treino)
# print("\n", y_treino)

x_teste = np.array(dt_teste[['Sangue', 'Da a luz', 'Pode voar', 'Mora na agua']])
y_teste = []

modeloAD = Dtc()

modeloAD.fit(x_treino, y_treino)

y_predicao = modeloAD.predict(x_validacao)

for item in x_teste:
    resultado = modeloAD.predict(item.reshape(1, -1))
    print("Resultado do conjunto{} -> {}".format(item, resultado))
    print("Não é mamifero" if resultado == 2 else "É mamifero")
    y_teste.append(resultado)

    idFolha = modeloAD.apply(item.reshape(1, -1))
    print('\nID do nó folha da classificacao {}:    {}'.format(item, idFolha))

    path = modeloAD.decision_path(item.reshape(1, -1))
    print('\nCaminho da classificacao de {}:\n{}'.format(item, path))
    print("\n"+5*"################")

y_predicao_validacao = modeloAD.predict(x_validacao)
y_predicao_treino = modeloAD.predict(x_treino)
y_predicao_teste = modeloAD.predict(x_teste)

acuracia_treino = accuracy_score(y_treino, y_predicao_treino, normalize=False)
acuracia_validacao = accuracy_score(y_validacao, y_predicao_validacao, normalize=False)
acuracia_teste = accuracy_score(y_teste, y_predicao_teste, normalize=False)

print("\n")
print("Acurancy do treino -> {}".format(acuracia_treino))
print("Acurancy da validação -> {}".format(acuracia_validacao))
print("Acurancy do teste -> {}".format(acuracia_teste))
print("\n")
print("Matriz de confusão do treinamento :\n {}".format(confusion_matrix(y_treino, y_predicao_treino)))
print("Matriz de confusão da validação :\n {}".format(confusion_matrix(y_validacao, y_predicao_validacao)))
print("Matriz de confusão da teste :\n {}".format(confusion_matrix(y_teste, y_predicao_teste)))

# Não estou conseguindo gerar um *.png
arquivo_dot = StringIO()

tree.export_graphviz(modeloAD, out_file=arquivo_dot,
                     node_ids=True, feature_names=['Sangue', 'Da a luz', 'Pode voar', 'Mora na agua'],
                     class_names=['SIM', 'NAO'], filled=True)

arvore = pdp.graph_from_dot_data(arquivo_dot.getvalue())

lista_edge = []
for edge in arvore.get_edge_list():
    lista_edge.append(edge.get_source())

nodes = arvore.get_node_list()
for node in nodes:
    if node.get_name() == '0':
        node.set_fillcolor('#F19C99')
    elif node.get_name() not in lista_edge:
        node.set_fillcolor('#E1D5E7')
    else:
        node.set_fillcolor('#D5E8D4')

arvore.write_png("arvore_mamifero.png")

qtd_nos = modeloAD.tree_.node_count
print("\nQuantidade de nos -> {}".format(qtd_nos))

filhosEsq = modeloAD.tree_.children_left
print("Filhos a esquerda:\n{}".format(filhosEsq))

filhosDir = modeloAD.tree_.children_right
print("Filhos a direita:\n{}".format(filhosDir))

feat = modeloAD.tree_.feature
print("IDs das features para cada no:\n{}".format(feat))

vLimite = modeloAD.tree_.threshold
print("IDs dos valores limite para cada no:\n{}".format(vLimite))
