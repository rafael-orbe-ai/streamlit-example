# -*- coding: utf-8 -*-
"""K-NN_teste_deploy_streamlit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LVpFecowhKrcr3flCTGfOvIjjeGrsjEg
"""

import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# 03.FUNÇÃO PARA CARREGAR O DATASET (dados_de_credito_limpo.csv)
# obs: como este processo pode ser demorado e isso pode causar problemas,
# usamos o comando @st.cache para acelerar a execução da função carregar_dados()
@st.cache
def carregar_dados():
  return pd.read_csv('/content/dados_de_credito_limpo.csv')

# 04.FUNÇÃO PARA EXECUTAR/RODAR O MODELO.
def executar_modelo():
  # 04.a.Chamar a função carregar_dados() que nos retorna os dados
  #.     e em seguida usar estes dados para criar o DataFrame.
  df = carregar_dados()

  # 04.b.Separar dados entre atributos preditores e atributo alvo.
  X_atributos_preditores = df.iloc[:,1:4].values
  y_atributo_alvo = df.iloc[:,4].values

  # 04.c.Escalonar os atributos preditores.

  modelo_knn_classificacao = KNeighborsClassifier(n_neighbors=5,metric='minkowski', p=2)
  modelo_knn_classificacao.fit(X_atributos_preditores,y_atributo_alvo)
  return modelo_knn_classificacao

# MODELO DE CLASSIFICAÇÃO
# Executar o modelo
modelo = executar_modelo()
  
# SITE
# Título do site
st.title("Site para classificar empréstimo.")

# Subtítulo 
st.subheader("Insira seus dados.")

# Recebendo os dados do usuário.
salario = st.number_input("Salário", value=0)
idade = st.number_input("Idade", value=0)
valor_emprestimo = st.number_input("Valor empréstimo", value=0)

# Botão para realizar a avaliação de crédito.
botao_realizar_avaliacao = st.button("Realizar avaliação")

# SE o botão seja acionado.
# 01.Coletar todos os dados que o usuário informou.
# 02.Usar os dados para predizer o resultado. Crédito aprovado ou reprovado.
# 03.Mostrar o resultado da avaliação.
if botao_realizar_avaliacao:
    resultado = modelo.predict([[salario,idade,valor_emprestimo]])
    st.subheader("Resultado: ")
    if resultado == 0:
      resultado_avaliacao = "crédito aprovado"
    else:
      resultado_avaliacao = "crédito reprovado"
      
    st.write(resultado_avaliacao)