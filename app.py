import requests
import streamlit as st

def buscar_letra(banda,musica):
    endpoint = f"https://api.lyrics.ovh/v1/{banda}/{musica}"
    response = requests.get(endpoint)
    letra= response.json()["lyrics"] if response.status_code == 200 else ""
    return letra


st.image("cat.jpg")
st.title("Karaoke")

banda = st.text_input("Digite o nome da banda/cantor(a): ", key="banda")
musica = st.text_input("Qual é a música maestro?: ", key="musica")
pesquisar = st.button("Pesquisar", key="pesquisar")

if pesquisar:
    letra = buscar_letra(banda,musica)
    if letra:
        st.success("Encontrei!!!")
        st.text(letra)
    else:
        st.error("infelizmente não foi posivel encontrar a letra dessa música")