# -*- coding: utf-8 -*-
"""codigoBase_upd.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bLgLWjGzwZsk0dERCmEOc5T71xG61rHC
"""

import pandas as pd
import plotly.express as px
import streamlit as st

# Carregando o dataset
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

# Renomeando colunas de interesse
df = df.rename(columns={
    'newDeaths': 'Novos óbitos',
    'newCases': 'Novos casos',
    'deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes',
    'totalCases_per_100k_inhabitants': 'Casos por 100 mil habitantes',
    'recovered': 'Recuperados',
    'suspects': 'Suspeitos',
    'tests': 'Testados',
    'vaccinated_single_per_100_inhabitants': 'Primeira dose por 100 mil habitantes',
    'vaccinated_second_per_100_inhabitants': 'Segunda dose por 100 mil habitantes',
    'vaccinated_third_per_100_inhabitants': 'Terceira dose por 100 mil habitantes'
})

# Adicionando uma linha com o total geral
df_total = df.groupby('date').agg({
    'Novos óbitos': 'sum',
    'Novos casos': 'sum',
    'Óbitos por 100 mil habitantes': 'mean',
    'Casos por 100 mil habitantes': 'mean',
    'Recuperados': 'sum',
    'Suspeitos': 'sum',
    'Testados': 'sum'
}).reset_index()
df_total['state'] = 'TOTAL'

# Concatenando o DataFrame total com o DataFrame original
df_combined = pd.concat([df, df_total], ignore_index=True)

# Navegação entre guias
page = st.sidebar.selectbox("Escolha uma página", ["Página Inicial", "Resumo Total", "Vacinação", "Outros Dados"])

if page == "Página Inicial":
    st.title('DADOS COVID - BRASIL')
    
    # Selecionando os estados disponíveis
    estados = list(df_combined['state'].unique())
    
    # Garantir que "TOTAL" esteja na lista de opções
    estados_sem_total = [estado for estado in estados if estado != 'TOTAL']
    
    # Permitir seleção de múltiplos estados
    selected_states = st.sidebar.multiselect(
        'Selecione os estados:',
        options=estados_sem_total,
        default=[]
    )

    # Se "TOTAL" estiver na seleção, adiciona-o à lista de seleção
    if len(selected_states) == 0:
        selected_states = ['TOTAL']
    elif 'TOTAL' in selected_states and len(selected_states) > 1:
        selected_states.remove('TOTAL')
    
    # Selecionando colunas de interesse
    colunas = ['Novos óbitos', 'Novos casos', 'Óbitos por 100 mil habitantes', 'Casos por 100 mil habitantes']
    column = st.sidebar.selectbox('Qual tipo de informação?', colunas)

    # Filtrando os dados para os estados selecionados
    df_filtered = df_combined[df_combined['state'].isin(selected_states)]

    # Verificar se apenas "TOTAL" está selecionado
    if len(selected_states) == 1 and 'TOTAL' in selected_states:
        # Agregar dados se apenas "TOTAL" estiver selecionado
        df_filtered = df_filtered[['date', column]].groupby('date').sum().reset_index()
        fig = px.line(df_filtered, x="date", y=column, title=f'{column} - TOTAL')
    else:
        # Criar gráfico para múltiplos estados
        fig = px.line(df_filtered, x="date", y=column, color='state', title=f'{column} por Estado')

    fig.update_layout(
        xaxis_title='Data', 
        yaxis_title=column.upper(), 
        title={'x':0.5}
    )

    # Exibindo o gráfico
    st.plotly_chart(fig, use_container_width=True)
    st.caption('Os dados foram obtidos a partir do site: https://github.com/wcota/covid19br')

elif page == "Resumo Total":
    st.title('Resumo Total dos Dados')
    
    # Filtros adicionais
    estados = list(df_combined['state'].unique())
    
    # Garantir que "TOTAL" esteja na lista de opções
    estados_sem_total = [estado for estado in estados if estado != 'TOTAL']
    
    # Permitir seleção de múltiplos estados
    selected_states = st.sidebar.multiselect(
        'Selecione os estados:',
        options=estados_sem_total,
        default=[]
    )

    # Se "TOTAL" estiver na seleção, adiciona-o à lista de seleção
    if len(selected_states) == 0:
        selected_states = ['TOTAL']
    elif 'TOTAL' in selected_states and len(selected_states) > 1:
        selected_states.remove('TOTAL')

    # Novo filtro
    filtro = st.sidebar.selectbox(
        'Selecione o tipo de dado:',
        ['Recuperados', 'Suspeitos', 'Testados']
    )

    # Filtrando os dados para os estados selecionados e o filtro
    coluna_filtro = filtro
    if coluna_filtro in df.columns:
        df_filtered = df_combined[df_combined['state'].isin(selected_states)]

        # Verificar se é necessário agregar dados para o estado "TOTAL"
        if 'TOTAL' in selected_states:
            # Se 'TOTAL' estiver incluído, agregue os dados e renomeie 'state' para 'TOTAL'
            df_filtered = df_filtered[['date', 'state', coluna_filtro]].groupby(['date']).sum().reset_index()
            df_filtered['state'] = 'TOTAL'

        # Criando o gráfico
        fig = px.line(df_filtered, x="date", y=coluna_filtro, color='state', title=f'{filtro} por Estado')
        fig.update_layout(
            xaxis_title='Data',
            yaxis_title=coluna_filtro,
            title={'x':0.5}
        )

        # Exibindo o gráfico
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error(f"A coluna '{coluna_filtro}' não existe no DataFrame.")

elif page == "Vacinação":
    st.title('DADOS COVID - VACINAÇÃO')
    
    # Filtros adicionais
    estados = list(df_combined['state'].unique())
    
    # Garantir que "TOTAL" esteja na lista de opções
    estados_sem_total = [estado for estado in estados if estado != 'TOTAL']
    
    # Permitir seleção de múltiplos estados
    selected_states = st.sidebar.multiselect(
        'Selecione os estados:',
        options=estados_sem_total,
        default=[]
    )

    # Se "TOTAL" estiver na seleção, adiciona-o à lista de seleção
    if len(selected_states) == 0:
        selected_states = ['TOTAL']
    elif 'TOTAL' in selected_states and len(selected_states) > 1:
        selected_states.remove('TOTAL')

    # Novo filtro
    filtro = st.sidebar.selectbox(
        'Selecione o tipo de dado:',
        ['Primeira dose por 100 mil habitantes', 'Segunda dose por 100 mil habitantes', 'Terceira dose por 100 mil habitantes']
    )

    # Filtrando os dados para os estados selecionados e o filtro
    coluna_filtro = filtro
    if coluna_filtro in df.columns:
        df_filtered = df_combined[df_combined['state'].isin(selected_states)]

        # Verificar se é necessário agregar dados para o estado "TOTAL"
        if 'TOTAL' in selected_states:
            # Se 'TOTAL' estiver incluído, agregue os dados e renomeie 'state' para 'TOTAL'
            df_filtered = df_filtered[['date', 'state', coluna_filtro]].groupby(['date']).sum().reset_index()
            df_filtered['state'] = 'TOTAL'

        # Criando o gráfico
        fig = px.line(df_filtered, x="date", y=coluna_filtro, color='state', title=f'{filtro} por Estado')
        fig.update_layout(
            xaxis_title='Data',
            yaxis_title=coluna_filtro,
            title={'x':0.5}
        )

        # Exibindo o gráfico
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error(f"A coluna '{coluna_filtro}' não existe no DataFrame.")

elif page == "Outros Dados":
    st.title('Outros Dados')
    
    # Adicione aqui qualquer outra visualização ou dados que você deseja exibir em uma guia separada.
    st.write("Aqui você pode exibir outros tipos de dados ou visualizações.")

