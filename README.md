# **Projeto_IA_RBC_Wine_Dataset**
**Atividade Avaliativa 1 - Componente curricular Inteligencia Artificial - UNOESC - 2025**



## Tecnologias utilizadas
- Python 3.11+
- VS Code
- Pandas
- Numpy
- Streamlit
- Scikit-learn
- Scipy
- Os

## Como executar o projeto

### 1→ No Promt do VS Code, vá até o diretório designado ao projeto, crie e ative o ambiente virtual:
 
* ### Criar: 
    *(Obs.: Caso já exista a variável, não há necessidade de executar novamente.)*
```bash
python -m venv .venv
```    

* ### Ativar:

#### **Windows:**  
```bash
.venv\Scripts\activate
```
   
#### **Linux ou MacOS:**   
```bash
source .venv/bin/activate
```

### 2→ Instale os pacotes necessários no ambiente virtual:

```bash
pip install -r requirements.txt
``` 

### 3→ Execute o comando abaixo no terminal para gerar o Dashboard Streamlit:

```bash
streamlit run main.py
```


## Problemas
- Dificuldades para fazer a comparação de características físico-químicas dos vinhos analisados, para identificar a possível região de produção.

## Requisitos do negócio
- Criar um Dashboard para auxiliar os cientístas a identificar a região de fabricação do vinho conforme suas características e verificar os vinhos mais similares.

- Disponibilizar o dasboard online para interação do cliente (*usuário*).