
# import streamlit as st
# import pandas as pd
# from sklearn.datasets import load_wine
# from scipy.spatial.distance import euclidean
# import os


# # ✅ Expandir largura da página
# st.set_page_config(page_title="Sistema RBC - Vinho Similar", layout="wide")

# # 🔧 Estilo adicional (opcional)
# st.markdown("""
#     <style>
#         table {
#             width: 100% !important;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # 📁 Caminho do dataset externo
# caminho_csv = r"D:\Ciencia de Dados e Inteligencia Artificial\4 Semestre\Inteligencia Artificial\Semana 1 e 2\AA1\Projeto_IA_RBC_Wine_Dataset\load_wine.csv"

# # 🌍 Mapeamento de regiões
# regioes = {
#     0: "Região Européia",
#     1: "Região Norte Americana",
#     2: "Região Sul Americana"
# }

# # 🧪 Mapeamento de descrições dos atributos
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

# # 📊 Carregamento do dataset
# if os.path.exists(caminho_csv):
#     df = pd.read_csv(caminho_csv)
#     dados = load_wine()  # Para manter os nomes dos atributos e target
#     if 'target' not in df.columns:
#         df['target'] = -1
# else:
#     dados = load_wine()
#     df = pd.DataFrame(dados.data, columns=dados.feature_names)
#     df['target'] = dados.target

# # 🏷️ Interface principal
# st.title("🔍 Sistema RBC")
# st.title("Identificar a Região de Produção o Vinho")
# st.write("Este sistema encontra os vinhos mais similares com base nos atributos químicos informados.")

# # 📥 Sidebar para entrada de dados
# st.sidebar.header("🧪 Atributos do vinho")
# entrada = []
# for atributo in dados.feature_names:
#     descricao = descricao_atributos.get(atributo, atributo)
#     valor = st.sidebar.number_input(f"{descricao}", value=float(df[atributo].mean()))
#     entrada.append(valor)

# # 🔘 Botão de busca
# if st.sidebar.button("Buscar similares"):
#     df['distancia'] = df[dados.feature_names].apply(lambda x: euclidean(x, entrada), axis=1)
#     similares = df.sort_values('distancia').head(3)
#     mais_similar = similares.head(1)

#     # 🎯 Identificar a região do vinho mais similar
#     target_valor = int(mais_similar['target'].values[0])
#     regiao_predita = regioes.get(target_valor, "Região desconhecida")

#     # 🏷️ Renomear colunas para exibição
#     colunas_exibicao = dados.feature_names + ['target', 'distancia']
#     colunas_renomeadas = {nome: descricao_atributos.get(nome, nome) for nome in dados.feature_names}
#     colunas_renomeadas['target'] = 'Região'
#     colunas_renomeadas['distancia'] = 'Distância Euclidiana'

#     # 🧾 Aplicar renomeação e personalizar índice
#     mais_similar_exibicao = mais_similar[colunas_exibicao].rename(columns=colunas_renomeadas)
#     mais_similar_exibicao.index = [f"Vinho n°{i}" for i in mais_similar.index]

#     similares_exibicao = similares[colunas_exibicao].rename(columns=colunas_renomeadas)
#     similares_exibicao.index = [f"Vinho n°{i}" for i in similares.index]

#     # 📤 Exibir resultados
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

# Configuração da página
st.set_page_config(page_title="Sistema RBC - Vinho Similar", layout="wide")

# Estilo para tabelas
st.markdown("""
    <style>
        table {
            width: 100% !important;
        }
    </style>
""", unsafe_allow_html=True)

# Caminho do dataset externo
caminho_csv = r"D:\Ciencia de Dados e Inteligencia Artificial\4 Semestre\Inteligencia Artificial\Semana 1 e 2\AA1\Projeto_IA_RBC_Wine_Dataset\load_wine.csv"

# Mapeamento de regiões
regioes = {
    0: "Região Européia",
    1: "Região Norte Americana",
    2: "Região Sul Americana"
}
regioes_invertido = {v: k for k, v in regioes.items()}

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

# Carregamento do dataset
if os.path.exists(caminho_csv):
    df = pd.read_csv(caminho_csv)
    dados = load_wine()
    if 'target' not in df.columns:
        df['target'] = -1
else:
    dados = load_wine()
    df = pd.DataFrame(dados.data, columns=dados.feature_names)
    df['target'] = dados.target

# Inicializar estado da sessão
if "pagina" not in st.session_state:
    st.session_state.pagina = "buscar"
if "entrada" not in st.session_state:
    st.session_state.entrada = []
if "regiao_sugerida" not in st.session_state:
    st.session_state.regiao_sugerida = None

# Sidebar: entrada de dados com vírgula e 2 casas decimais
st.sidebar.header("🧪 Atributos do vinho")
entrada = []
for atributo in dados.feature_names:
    descricao = descricao_atributos.get(atributo, atributo)
    valor_str = st.sidebar.text_input(
        f"{descricao}",
        value=f"{df[atributo].mean():.2f}".replace(".", ","),
        key=atributo
    )
    try:
        valor = round(float(valor_str.replace(",", ".")), 2)
    except ValueError:
        valor = round(float(df[atributo].mean()), 2)
    entrada.append(valor)

# Botões na sidebar
col1, col2 = st.sidebar.columns(2)
if col1.button("Buscar similares"):
    st.session_state.entrada = entrada
    df['distancia'] = df[dados.feature_names].apply(lambda x: euclidean(x, entrada), axis=1)
    similares = df.sort_values('distancia').head(3)
    mais_similar = similares.head(1)
    target_valor = int(mais_similar['target'].values[0])
    st.session_state.regiao_sugerida = regioes.get(target_valor, "Região desconhecida")
    st.session_state.similares = similares
    st.session_state.mais_similar = mais_similar
    st.session_state.pagina = "resultado"

if col2.button("Registrar novo vinho"):
    st.session_state.entrada = entrada
    st.session_state.pagina = "registrar"

# Página: resultado da busca
if st.session_state.pagina == "resultado":
    st.title("🔍 Resultado da busca por vinhos similares")

    colunas_exibicao = dados.feature_names + ['target', 'distancia']
    colunas_renomeadas = {nome: descricao_atributos.get(nome, nome) for nome in dados.feature_names}
    colunas_renomeadas['target'] = 'Região'
    colunas_renomeadas['distancia'] = 'Distância Euclidiana'

    mais_similar_exibicao = st.session_state.mais_similar[colunas_exibicao].rename(columns=colunas_renomeadas)
    mais_similar_exibicao.index = [f"Vinho n°{i}" for i in st.session_state.mais_similar.index]

    similares_exibicao = st.session_state.similares[colunas_exibicao].rename(columns=colunas_renomeadas)
    similares_exibicao.index = [f"Vinho n°{i}" for i in st.session_state.similares.index]

    st.subheader("🍇 Vinho mais similar:")
    st.write(mais_similar_exibicao)
    st.success(f"O vinho mais similar pertence à **{st.session_state.regiao_sugerida}**.")

    st.subheader("📊 Top 3 similares:")
    st.write(similares_exibicao)

# Página: registrar novo vinho
elif st.session_state.pagina == "registrar":
    st.title("📝 Registrar novo vinho")
    st.write("Confirme os dados e selecione a região para salvar no banco de dados.")

    dados_inseridos = pd.DataFrame(
        [st.session_state.entrada],
        columns=[descricao_atributos.get(a, a) for a in dados.feature_names]
    )
    dados_inseridos.index = ["Novo vinho"]
    st.write("🔍 Dados informados:")
    st.write(dados_inseridos)

    regiao_escolhida = st.selectbox(
        "Selecione a região do vinho:",
        list(regioes.values()),
        index=list(regioes.values()).index(st.session_state.regiao_sugerida)
        if st.session_state.regiao_sugerida in regioes.values() else 0
    )

    if st.button("Registrar"):
        novo_vinho = pd.DataFrame([st.session_state.entrada], columns=dados.feature_names)
        novo_vinho['target'] = regioes_invertido[regiao_escolhida]
        novo_vinho['distancia'] = 0.0

        try:
            df_existente = pd.read_csv(caminho_csv)
        except FileNotFoundError:
            dados_base = load_wine()
            df_existente = pd.DataFrame(dados_base.data, columns=dados_base.feature_names)
            df_existente['target'] = dados_base.target
            df_existente['distancia'] = 0.0

        df_atualizado = pd.concat([df_existente, novo_vinho], ignore_index=True)
        df_atualizado.to_csv(caminho_csv, index=False)

        st.success("✅ Novo vinho registrado com sucesso!")
        st.session_state.pagina = "buscar"