import streamlit as st
import pandas as pd
from sklearn.datasets import load_wine
from scipy.spatial.distance import euclidean

# Carregar dados
dados = load_wine()
df = pd.DataFrame(dados.data, columns=dados.feature_names)
df['target'] = dados.target

# Interface do usuário
st.title("Sistema RBC - Vinho Similar")
st.write("Insira os atributos do vinho para encontrar os mais similares:")

# Inputs dinâmicos
entrada = []
for atributo in dados.feature_names:
    valor = st.number_input(f"{atributo}", value=float(df[atributo].mean()))
    entrada.append(valor)

# Botão de busca
if st.button("Buscar similares"):
    # Calcular similaridade
    df['distancia'] = df[dados.feature_names].apply(lambda x: euclidean(x, entrada), axis=1)
    similares = df.sort_values('distancia').head(3)

    st.subheader("Casos mais similares:")
    st.write(similares[dados.feature_names + ['target', 'distancia']])