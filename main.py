import streamlit as st
import pandas as pd
from sklearn.datasets import load_wine
from scipy.spatial.distance import euclidean
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
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
    2: "Região Sul Americana",
    3: "Região Asiática",
    4: "Região Oceania",
    5: "Região Africana",
    6: "Região Centro Americana"
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
if "acuracia" not in st.session_state:
    st.session_state.acuracia = None

st.image("Vinho_garrafa (Custom).png") # st.title("Sistema RBC - Vinho Similar")

# Sidebar: entrada de dados
st.sidebar.title("🎯 IA RBC - Identificação da região do Vinho.")
st.sidebar.header("🧪 Insira os atributos das análises do vinho.")
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
if col1.button("**Buscar vinhos similares**"):
    st.session_state.entrada = entrada

    # Calcular distâncias
    df['distancia'] = df[dados.feature_names].apply(lambda x: euclidean(x, entrada), axis=1)
    similares = df.sort_values('distancia').head(3)
    mais_similar = similares.head(1)
    target_valor = int(mais_similar['target'].values[0])
    st.session_state.regiao_sugerida = regioes.get(target_valor, "Região desconhecida")
    st.session_state.similares = similares
    st.session_state.mais_similar = mais_similar

    # Calcular acurácia com KNN
    X = df[dados.feature_names]
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    st.session_state.acuracia = round(accuracy_score(y_test, y_pred) * 100, 2)

    st.session_state.pagina = "resultado"

if col2.button("**Registrar novo vinho**"):
    st.session_state.entrada = entrada
    st.session_state.pagina = "registrar"

# Página: resultado da busca
if st.session_state.pagina == "resultado":
    st.title("Resultado da busca por vinhos similares")

    colunas_exibicao = dados.feature_names + ['target', 'distancia']
    colunas_renomeadas = {nome: descricao_atributos.get(nome, nome) for nome in dados.feature_names}
    colunas_renomeadas['target'] = 'Região'
    colunas_renomeadas['distancia'] = 'Distância Euclidiana'

    mais_similar_exibicao = st.session_state.mais_similar[colunas_exibicao].rename(columns=colunas_renomeadas)
    mais_similar_exibicao.index = [f"Vinho n°{i}" for i in st.session_state.mais_similar.index]

    similares_exibicao = st.session_state.similares[colunas_exibicao].rename(columns=colunas_renomeadas)
    similares_exibicao.index = [f"Vinho n°{i}" for i in st.session_state.similares.index]

    st.subheader(f"🍇 Vinho mais similar: {f'🎯 Vinho n° {st.session_state.mais_similar.index[0]}' if not st.session_state.mais_similar.empty else '⚠️ Desconhecido'}")
    st.write(mais_similar_exibicao)
    st.success(f"**Resultado:** O vinho mais similar pertence à ***{st.session_state.regiao_sugerida}***.")

    st.subheader("📊 Top 3 vinhos similares:")
    st.write(similares_exibicao)

    st.subheader("📈 Acurácia da análise:")
    st.info(f"A acurácia do modelo é de **{st.session_state.acuracia}%**.")

# Página: registrar novo vinho
elif st.session_state.pagina == "registrar":
    st.title("Registrar novo vinho")
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

        try:
            df_atualizado = pd.concat([df_existente, novo_vinho], ignore_index=True)
            df_atualizado.to_csv(caminho_csv, index=False)
            st.success("✅ Novo vinho registrado com sucesso!")
        except PermissionError:
            st.error("❌ Não foi possível salvar o arquivo. Verifique se ele está aberto ou se você tem permissão de escrita.")

        st.session_state.pagina = "buscar"