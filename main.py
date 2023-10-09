import streamlit as st
import pandas as pd
import requests
from io import StringIO

# Función para obtener datos CSV de GitHub
def get_csv_from_github(token, repo_path):
    headers = {"Authorization": f"token {token}"}
    url = f"https://raw.githubusercontent.com/{repo_path}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return pd.read_csv(StringIO(response.text))
    else:
        st.error(f"Error obteniendo el archivo {repo_path}. Código de error: {response.status_code}")
        return None

# Función para cargar todos los datos
def load_data(token):
    base_path = "JulianTorrest/Inteligencia_Comercial/main/Abonos"
    files = [
        "CO-EX-ABONO-SALIDA.csv",
        "CO-EX-ABONO.csv",
        "CO-EX-ABONOS-DETALLE.csv",
        "CO-EX-ABONOS-EMPRESAS.csv",
        "CO-EX-ABONOS-MES.csv"
    ]

    data = {}
    for file in files:
        data[file] = get_csv_from_github(token, f"{base_path}/{file}")
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
