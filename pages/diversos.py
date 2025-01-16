import streamlit as st
from main import barra_lateral

st.set_page_config(
    page_title="Diversos",
    page_icon=":smile:"
)


barra_lateral()

st.sidebar.markdown("---")
st.sidebar.markdown("Desenvolvido por **[Dr. Vinícius Beleze](https://instagram.com/drviníciusbeleze)**")

st.title("Calculadoras Diversas:")

imc_tab, ckd_tab = st.tabs(['Calculadora IMC', 'Clearence de Creatinina'])

with imc_tab:
    st.subheader('Altura (cm):')
    altura = st.number_input(
    "Altura", 
    value=None, 
    placeholder="Altura em cm...", 
    min_value=100,
    max_value=200, 
    label_visibility='collapsed'
    )
    st.subheader('Peso (kg)')
    peso = st.number_input(
    "Peso", 
    value=None, 
    placeholder="Peso em Kg..", 
    max_value=500.0, 
    label_visibility='collapsed',
    step=0.1,
    format="%0.1f"
    )
    st.subheader('IMC:')
    if altura and peso:
        altura_metros = altura / 100
        imc_valor = peso / (altura_metros ** 2)
        st.write(f'{imc_valor:.2f}')
    else:
        st.write('Por favor, insira um valor válido.')