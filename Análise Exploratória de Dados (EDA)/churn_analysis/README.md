# Análise Exploratória de Dados (EDA) - Análise de Churn

## Descrição do Projeto

Este projeto realiza uma análise exploratória de dados (EDA) para investigar padrões de churn em um conjunto de dados de clientes. O objetivo é identificar fatores que podem influenciar a decisão dos clientes de deixar o serviço.

O notebook está disponível em [Google Colab](https://colab.research.google.com/github/IvanAjala/data-science-portfolio/blob/main/An%C3%A1lise%20Explorat%C3%B3ria%20de%20Dados%20(EDA)/churn_analysis/notebooks/churn_analysis.ipynb).

## Objetivo

O objetivo desta análise é entender os padrões de churn entre os clientes, explorando as seguintes questões:
- Quais características estão associadas ao churn?
- Existem padrões visíveis nas variáveis como Salário, Idade e outros atributos?

## Conteúdo do Notebook

O notebook realiza as seguintes etapas de análise:

1. **Importação de Dados**
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
  Certifique-se de ter o [Python 3.x]() e os seguintes pacotes instalados:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```
3. **Execute o Notebook**

Abra o notebook no [Jupyter]() ou no [Google Colab]() e execute as células.

## Dependências

  - **Python 3.x**
  - **pandas:** `pip install pandas`
  - **numpy:** `pip install numpy`
  - **matplotlib:** `pip install matplotlib`  
  - **seaborn:** `pip install seaborn`
  - **scikit-learn:** `pip install scikit-learn`

## Licença

Este projeto é licenciado sob a `Licença MIT` - veja o arquivo [LICENSE]() para mais detalhes.

## Referências

[Google Colab]()

[Documentação do Pandas]()

[Documentação do Seaborn]()
