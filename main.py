# main.py
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

    token = st.text_input("Introduce tu token de GitHub:", type="password")
    if not token:
        st.warning("Por favor, introduce tu token de GitHub.")
        return

    file_options = {
        "CO-EX-ABONO-SALIDA.xlsx": "JulianTorrest/Inteligencia_Comercial/contents/Abonos/CO-EX-ABONO-SALIDA.xlsx",
        # ... otros archivos
    }
    
    selected_file = st.selectbox("Selecciona el archivo que deseas visualizar", list(file_options.keys()))

    if st.button("Cargar archivo"):
        content = get_csv_from_github(token, file_options[selected_file])
        if content:
            data = pd.read_excel(content, engine='openpyxl')
            st.write(data)

if __name__ == "__main__":
    load_data()
