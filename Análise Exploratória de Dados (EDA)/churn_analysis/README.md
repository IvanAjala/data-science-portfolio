# Análise Exploratória de Dados (EDA) - Análise de Churn

## Descrição do Projeto
Churn, ou rotatividade de clientes, refere-se à perda de clientes em uma empresa. A análise de churn é usada para entender os fatores que contribuem para a saída de clientes e para desenvolver estratégias para retê-los.

Este projeto realiza uma análise exploratória de dados (EDA) para investigar e entender em um conjunto de dados, os padrões e fatores que influenciam a rotatividade dos clientes.

O notebook **churn_analysis.ipynb** está disponível em [Google Colab](https://github.com/IvanAjala/data-science-portfolio/tree/main/An%C3%A1lise%20Explorat%C3%B3ria%20de%20Dados%20(EDA)/churn_analysis/notebooks).

## Objetivo

O objetivo é fornecer uma visão geral prática de como realizar tarefas de análise de dados, desde a importação e exploração dos dados até a visualização gráfica, de modo que obtenha os insights iniciais com base no dataframe carregado no Python

## Conteúdo do Notebook

Este notebook conduz uma análise exploratória de dados (EDA) com foco em churn, abordando desde a limpeza e inspeção inicial dos dados até a análise detalhada e visualizações que ajudam a entender os padrões de churn. Seguir este fluxo ajuda a obter uma visão clara dos dados e a desenvolver estratégias para melhorar a retenção de clientes.

1. **Importação de Bibliotecas e Carregamento de Dados**
   - Carregamento e visualização inicial dos dados.

2. **Limpeza e Preparação dos Dados**
   - Tratamento de valores ausentes e ajuste de dados.

3. **Análise Descritiva**
   - Estatísticas descritivas e visualizações para entender a distribuição dos dados.

4. **Análise de Correlações**
   - Avaliação das correlações entre diferentes variáveis e o churn.

5. **Visualização de Dados**
   - Criação de gráficos para visualizar a relação entre variáveis e churn.

## Insights Principais

- **Distribuição de Salário e Churn**
  - Clientes com salários mais altos tendem a ter uma menor taxa de churn.
  
- **Idade e Churn**
  - A idade não parece ter uma correlação significativa com a probabilidade de churn.

- **Cartão de Crédito e Churn**
  - A presença de um cartão de crédito não afeta significativamente a probabilidade de churn.

## Como Rodar o Código

Para rodar o código localmente, siga os seguintes passos:

1. **Clone o Repositório**
   ```bash
   git clone https://github.com/IvanAjala/data-science-portfolio.git
   cd data-science-portfolio/Análise Exploratória de Dados (EDA)/churn_analysis/notebooks

2. **Instale as Dependências**

**Usando pip:**

Certifique-se de ter o [Python 3.x]() instalado no seu sistema.

- É recomendável criar um ambiente virtual para gerenciar as dependências. Você pode criar e ativar um ambiente virtual com:
  ```bash
  python -m venv venv
  source venv/bin/activate  # No Windows use: venv\Scripts\activate
  ```

- Instale as dependências necessárias com:
  ```bash
  pip install pandas 
  pip install numpy
  pip install matplotlib
  pip install seaborn
  pip install scikit-learn

  ```
**Usando um arquivo `requirements.txt`**:
- Você também pode instalar todas as dependências listadas em um arquivo requirements.txt se ele estiver disponível no repositório. Para isso, crie um arquivo requirements.txt com o seguinte conteúdo:
    ```bash
  pandas
  numpy
  matplotlib
  seaborn
  scikit-learn
  ```
- E instale as dependências com:

```bash
pip install -r requirements.txt
```
3. **Execute o Notebook**

Abra o notebook no [Jupyter]() ou no [Google Colab]() e execute as células.

## Licença

Este projeto é licenciado sob a **Licença MIT** - veja o arquivo [LICENSE](https://github.com/IvanAjala/data-science-portfolio/blob/main/LICENSE) para mais detalhes.

## Referências

[Google Colab]()

[Documentação do Pandas]()

[Documentação do Seaborn]()
