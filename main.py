import streamlit as st
import pandas as pd
import requests
from io import StringIO

# Función para obtener datos CSV de GitHub
def get_csv_from_url(token, url):
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return pd.read_csv(StringIO(response.text))
    else:
        st.error(f"Error obteniendo el archivo desde {url}. Código de error: {response.status_code}")
        return None

# Función para cargar todos los datos
def load_data(token):
    urls = [
        "https://raw.githubusercontent.com/JulianTorrest/Inteligencia_Comercial/main/Abonos/CO-EX-ABONO-SALIDA.csv",
        "https://raw.githubusercontent.com/JulianTorrest/Inteligencia_Comercial/main/Abonos/CO-EX-ABONO.csv",
        "https://raw.githubusercontent.com/JulianTorrest/Inteligencia_Comercial/main/Abonos/CO-EX-ABONOS-DETALLE.csv",
        "https://raw.githubusercontent.com/JulianTorrest/Inteligencia_Comercial/main/Abonos/CO-EX-ABONOS-EMPRESAS.csv",
        "https://raw.githubusercontent.com/JulianTorrest/Inteligencia_Comercial/main/Abonos/CO-EX-ABONOS-MES.csv"
    ]

    data = {}
    for url in urls:
        filename = url.split("/")[-1]
        data[filename] = get_csv_from_url(token, url)
    return data

# Aplicación principal de Streamlit
def main():
    # Título y subtítulos
    st.title("Inteligencia Comercial")
    st.subheader("Abono")
    st.subheader("Exportaciones - Colombia")

    # Cargar datos
    token = "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"
    datasets = load_data(token)
    
    # Desplegar datos
    for name, df in datasets.items():
        st.write(f"### {name}")
        st.write(df)

if __name__ == "__main__":
    main()
