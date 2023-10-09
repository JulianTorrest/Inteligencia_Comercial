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
    st.title("Visualizador de Archivos de Excel desde GitHub")

    # Asumiendo que tienes un token fijo que se usará (es un riesgo de seguridad, no lo hagas en una aplicación real)
    token = "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"

    file_options = {
        "CO-EX-ABONO-SALIDA.xlsx": "JulianTorrest/Inteligencia_Comercial/contents/Abonos/CO-EX-ABONO-SALIDA.xlsx",
        "CO-EX-ABONO.xlsx": "JulianTorrest/Inteligencia_Comercial/blob/main/Abonos/CO-EX-ABONO.xlsx",
        "CO-EX-ABONOS-DETALLE.xlsx": "JulianTorrest/Inteligencia_Comercial/blob/main/Abonos/CO-EX-ABONOS-DETALLE.xlsx",
        "CO-EX-ABONOS-EMPRESAS.xlsx": "JulianTorrest/Inteligencia_Comercial/blob/main/Abonos/CO-EX-ABONOS-EMPRESAS.xlsx",
        "CO-EX-ABONOS-MES.xlsx": "JulianTorrest/Inteligencia_Comercial/blob/main/Abonos/CO-EX-ABONOS-MES.xlsx",
    }
    
    for file_name, repo_path in file_options.items():
        st.subheader(f"Datos de {file_name}")
        content = get_csv_from_github(token, repo_path)
        if content:
            data = pd.read_excel(content, engine='openpyxl')
            st.write(data)

if __name__ == "__main__":
    load_data()

