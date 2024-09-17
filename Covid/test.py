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
    'Testados': 'sum',
    'Primeira dose por 100 mil habitantes': 'mean',
    'Segunda dose por 100 mil habitantes': 'mean',
    'Terceira dose por 100 mil habitantes': 'mean'
}).reset_index()
df_total['state'] = 'TOTAL'

# Concatenando o DataFrame total com o DataFrame original
df_combined = pd.concat([df, df_total], ignore_index=True)

# Navegação entre guias
page = st.sidebar.selectbox("Escolha uma página", ["Página Inicial", "Resumo Total", "Vacinação", "Outros Dados"])

if page == "Outros Dados":
    st.title('Outros Dados')

    # Mapeamento das siglas dos estados brasileiros
    estados_siglas = {
        'Acre': 'AC', 'Alagoas': 'AL', 'Amapá': 'AP', 'Amazonas': 'AM',
        'Bahia': 'BA', 'Ceará': 'CE', 'Distrito Federal': 'DF', 'Espírito Santo': 'ES',
        'Goiás': 'GO', 'Maranhão': 'MA', 'Mato Grosso': 'MT', 'Mato Grosso do Sul': 'MS',
        'Minas Gerais': 'MG', 'Pará': 'PA', 'Paraíba': 'PB', 'Paraná': 'PR',
        'Pernambuco': 'PE', 'Piauí': 'PI', 'Rio de Janeiro': 'RJ', 'Rio Grande do Norte': 'RN',
        'Rio Grande do Sul': 'RS', 'Rondônia': 'RO', 'Roraima': 'RR', 'Santa Catarina': 'SC',
        'São Paulo': 'SP', 'Sergipe': 'SE', 'Tocantins': 'TO', 'TOTAL': 'TOTAL'
    }

    # Adicionar coluna com siglas dos estados
    df_combined['state_sigla'] = df_combined['state'].map(estados_siglas)
    
    # Filtragem para obter o total de mortes por estado ao longo do tempo
    df_mortes = df_combined[['date', 'state_sigla', 'Novos óbitos']]
    
    # Filtros para seleção de estados
    estados = list(df_combined['state'].unique())
    estados_sem_total = [estado for estado in estados if estado != 'TOTAL']
    selected_states = st.sidebar.multiselect(
        'Selecione os estados:',
        options=estados_sem_total,
        default=estados_sem_total  # Selecionar todos por padrão
    )
    
    if 'TOTAL' in selected_states:
        selected_states.remove('TOTAL')

    if len(selected_states) > 0:
        df_mortes_filtered = df_mortes[df_mortes['state_sigla'].isin([estados_siglas[estado] for estado in selected_states])]
    else:
        df_mortes_filtered = df_mortes[df_mortes['state_sigla'] == estados_siglas['TOTAL']]
    
    # Criando o gráfico de mapa
    fig = px.choropleth(
        df_mortes_filtered,
        locations='state_sigla',
        locationmode='ISO-3',  # Usando siglas dos estados brasileiros
        color='Novos óbitos',
        hover_name='state_sigla',
        animation_frame='date',  # Atualiza com base na data
        color_continuous_scale=px.colors.sequential.Plasma,
        labels={'Novos óbitos': 'Total de Mortes'},
        title='Total de Mortes por Estado ao Longo do Tempo'
    )

    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)
