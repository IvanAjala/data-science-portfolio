import streamlit as st
import folium
from io import BytesIO
import pandas as pd

# Dados com as iniciais dos estados e suas coordenadas (latitude e longitude)
data = {
    'Estado': ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO'],
    'Latitude': [-8.7742, -9.5714, -1.3833, -3.1000, -12.9714, -3.7172, -15.7801, -20.3155, -15.7801, -2.5489, -19.8157, -20.4413, -12.6416, -1.4558, -7.1150, -8.0476, -5.0892, -25.4284, -22.9068, -5.7945, -11.4396,  -1.9390, -27.5954, -27.5954, -10.2646, -9.4136],
    'Longitude': [-70.5551, -36.7820, -51.0682, -60.0250, -38.5014, -38.5433, -47.9292, -40.3128, -49.2650, -44.2828, -43.3547, -54.6212, -55.4280, -51.9783, -34.8774, -34.8774, -42.8034, -49.2718, -43.1729, -35.2110, -63.4939, -61.5240, -51.2177, -48.5480, -37.7333, -51.1745]
}

# Crie um DataFrame a partir dos dados
df = pd.DataFrame(data)

# Função para criar o mapa
def create_map(dataframe):
    # Crie um mapa base
    m = folium.Map(location=[-15, -55], zoom_start=4)
    
    # Adicione marcadores para cada estado
    for index, row in dataframe.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=row['Estado'],
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(m)
    
    return m

# Streamlit para exibir o mapa
st.title('Mapa dos Estados com Iniciais')

# Crie o mapa
m = create_map(df)

# Converta o mapa para um objeto que o Streamlit possa exibir
map_html = BytesIO()
m.save(map_html, close_file=False)

st.markdown(f'<iframe srcdoc="{map_html.getvalue().decode()}" width="700" height="500"></iframe>', unsafe_allow_html=True)
