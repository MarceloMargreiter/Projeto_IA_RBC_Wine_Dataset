
# import streamlit as st
# import pandas as pd
# from sklearn.datasets import load_wine
# from scipy.spatial.distance import euclidean
# import os

# # Caminho do dataset externo
# caminho_csv = r"D:\Ciencia de Dados e Inteligencia Artificial\4 Semestre\Inteligencia Artificial\Semana 1 e 2\AA1\Projeto_IA_RBC_Wine_Dataset\load_wine.csv"

# # Mapeamento de regiões
# regioes = {
#     0: "Região Européia",
#     1: "Região Norte Americana",
#     2: "Região Sul Americana"
# }

# # Mapeamento de descrições dos atributos
# descricao_atributos = {
#     "alcohol": "Teor alcoólico do vinho",
#     "malic_acid": "Quantidade de ácido málico",
#     "ash": "Conteúdo de cinzas",
#     "alcalinity_of_ash": "Alcalinidade das cinzas",
#     "magnesium": "Nível de magnésio",
#     "total_phenols": "Quantidade total de fenóis",
#     "flavanoids": "Subgrupo de fenóis com propriedades antioxidantes",
#     "nonflavanoid_phenols": "Fenóis que não são flavonoides",
#     "proanthocyanins": "Tipo de tanino presente no vinho",
#     "color_intensity": "Intensidade da cor do vinho",
#     "hue": "Tonalidade da cor",
#     "od280/od315_of_diluted_wines": "Absorbância do vinho diluído (280/315 nm)",
#     "proline": "Nível de prolina (aminoácido)"
# }

# # Verificar se o arquivo existe
# if os.path.exists(caminho_csv):
#     df = pd.read_csv(caminho_csv)
#     dados = load_wine()  # Para manter os nomes dos atributos e target
#     if 'target' not in df.columns:
#         df['target'] = -1
# else:
#     dados = load_wine()
#     df = pd.DataFrame(dados.data, columns=dados.feature_names)
#     df['target'] = dados.target

# # Interface do usuário
# st.title("🔍 Sistema RBC - Vinho Similar")
# st.write("Insira os atributos do vinho para encontrar os mais similares:")

# # Inputs dinâmicos com descrições
# entrada = []
# for atributo in dados.feature_names:
#     descricao = descricao_atributos.get(atributo, atributo)
#     valor = st.number_input(f"{descricao}", value=float(df[atributo].mean()))
#     entrada.append(valor)

# # Botão de busca
# if st.button("Buscar similares"):
#     # Calcular distâncias euclidianas
#     df['distancia'] = df[dados.feature_names].apply(lambda x: euclidean(x, entrada), axis=1)
#     similares = df.sort_values('distancia').head(3)
#     mais_similar = similares.head(1)

#     # Identificar a região do vinho mais similar
#     target_valor = int(mais_similar['target'].values[0])
#     regiao_predita = regioes.get(target_valor, "Região desconhecida")

#     # Renomear colunas para exibição
#     colunas_exibicao = dados.feature_names + ['target', 'distancia']
#     colunas_renomeadas = {nome: descricao_atributos.get(nome, nome) for nome in dados.feature_names}
#     colunas_renomeadas['target'] = 'Região'
#     colunas_renomeadas['distancia'] = 'Distância Euclidiana'

#     mais_similar_exibicao = mais_similar[colunas_exibicao].rename(columns=colunas_renomeadas)
#     similares_exibicao = similares[colunas_exibicao].rename(columns=colunas_renomeadas)

#     # Exibir resultados
#     st.subheader("🍇 Vinho mais similar:")
#     st.write(mais_similar_exibicao)
#     st.success(f"O vinho mais similar pertence à **{regiao_predita}**.")

#     st.subheader("📊 Top 3 similares:")
#     st.write(similares_exibicao)


import streamlit as st
import pandas as pd
from sklearn.datasets import load_wine
from scipy.spatial.distance import euclidean
import os

# Caminho do dataset externo
caminho_csv = r"D:\Ciencia de Dados e Inteligencia Artificial\4 Semestre\Inteligencia Artificial\Semana 1 e 2\AA1\Projeto_IA_RBC_Wine_Dataset\load_wine.csv"

# Mapeamento de regiões
regioes = {
    0: "Região Européia",
    1: "Região Norte Americana",
    2: "Região Sul Americana"
}

# Mapeamento de descrições dos atributos
descricao_atributos = {
    "alcohol": "Teor alcoólico do vinho",
    "malic_acid": "Quantidade de ácido málico",
    "ash": "Conteúdo de cinzas",
    "alcalinity_of_ash": "Alcalinidade das cinzas",
    "magnesium": "Nível de magnésio",
    "total_phenols": "Quantidade total de fenóis",
    "flavanoids": "Subgrupo de fenóis com propriedades antioxidantes",
    "nonflavanoid_phenols": "Fenóis que não são flavonoides",
    "proanthocyanins": "Tipo de tanino presente no vinho",
    "color_intensity": "Intensidade da cor do vinho",
    "hue": "Tonalidade da cor",
    "od280/od315_of_diluted_wines": "Absorbância do vinho diluído (280/315 nm)",
    "proline": "Nível de prolina (aminoácido)"
}

# Verificar se o arquivo existe
if os.path.exists(caminho_csv):
    df = pd.read_csv(caminho_csv)
    dados = load_wine()  # Para manter os nomes dos atributos e target
    if 'target' not in df.columns:
        df['target'] = -1
else:
    dados = load_wine()
    df = pd.DataFrame(dados.data, columns=dados.feature_names)
    df['target'] = dados.target

# Interface do usuário
st.title("🔍 Sistema RBC - Vinho Similar")
st.write("Insira os atributos do vinho para encontrar os mais similares:")

# Inputs dinâmicos com descrições
entrada = []
for atributo in dados.feature_names:
    descricao = descricao_atributos.get(atributo, atributo)
    valor = st.number_input(f"{descricao}", value=float(df[atributo].mean()))
    entrada.append(valor)

# Botão de busca
if st.button("Buscar similares"):
    # Calcular distâncias euclidianas
    df['distancia'] = df[dados.feature_names].apply(lambda x: euclidean(x, entrada), axis=1)
    similares = df.sort_values('distancia').head(3)
    mais_similar = similares.head(1)

    # Identificar a região do vinho mais similar
    target_valor = int(mais_similar['target'].values[0])
    regiao_predita = regioes.get(target_valor, "Região desconhecida")

    # Renomear colunas para exibição
    colunas_exibicao = dados.feature_names + ['target', 'distancia']
    colunas_renomeadas = {nome: descricao_atributos.get(nome, nome) for nome in dados.feature_names}
    colunas_renomeadas['target'] = 'Região'
    colunas_renomeadas['distancia'] = 'Distância Euclidiana'

    # Aplicar renomeação e personalizar índice
    mais_similar_exibicao = mais_similar[colunas_exibicao].rename(columns=colunas_renomeadas)
    mais_similar_exibicao.index = [f"Vinho n°{i}" for i in mais_similar.index]

    similares_exibicao = similares[colunas_exibicao].rename(columns=colunas_renomeadas)
    similares_exibicao.index = [f"Vinho n°{i}" for i in similares.index]

    # Exibir resultados
    st.subheader("🍇 Vinho mais similar:")
    st.write(mais_similar_exibicao)
    st.success(f"O vinho mais similar pertence à **{regiao_predita}**.")

    st.subheader("📊 Top 3 similares:")
    st.write(similares_exibicao)
