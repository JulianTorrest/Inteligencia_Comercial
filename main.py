import streamlit as st
import pandas as pd
import requests

def get_csv_from_github(token, repo_path):
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3.raw"
    }
    response = requests.get(f"https://api.github.com/repos/{repo_path}", headers=headers)
    if response.status_code == 200:
        return response.content
    else:
        st.error(f"Error al obtener el archivo: {response.text}")
        return None

def load_data():
    st.title("Inteligencia Comercial, sector Abonos. Exportación del año 2023.")

    # Usa una forma segura para almacenar y recuperar el token en lugar de codificarlo directamente.
    token = "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"

    file_options = {
        "CO-EX-ABONO-SALIDA.xlsx": "JulianTorrest/Inteligencia_Comercial/Abonos/CO-EX-ABONO-SALIDA.xlsx",
        "CO-EX-ABONO.xlsx": "JulianTorrest/Inteligencia_Comercial/contents/CO-EX-ABONO.xlsx",
        "CO-EX-ABONOS-DETALLE.xlsx": "JulianTorrest/Inteligencia_Comercial/Abonos/CO-EX-ABONOS-DETALLE.xlsx",
        "CO-EX-ABONOS-EMPRESAS.xlsx": "JulianTorrest/Inteligencia_Comercial/Abonos/CO-EX-ABONOS-EMPRESAS.xlsx",
        "CO-EX-ABONOS-MES.xlsx": "JulianTorrest/Inteligencia_Comercial/Abonos/CO-EX-ABONOS-MES.xlsx",
    }
    
    for file_name, repo_path in file_options.items():
        st.subheader(f"Datos de {file_name}")
        content = get_csv_from_github(token, repo_path)
        if content:
            data = pd.read_excel(content, engine='openpyxl')
            st.write(data)

if __name__ == "__main__":
    load_data()

