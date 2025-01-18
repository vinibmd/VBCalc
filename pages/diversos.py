import streamlit as st
from main import barra_lateral

st.set_page_config(
    page_title="Diversos",
    page_icon=":smile:"
)


barra_lateral()

st.sidebar.markdown("---")
st.sidebar.markdown("Desenvolvido por **[Dr. Vinícius Beleze](https://instagram.com/drviníciusbeleze)**")

# Título
st.title("Calculadoras Diversas:")

# Aba de cálculo de IMC
imc_tab, ckd = st.tabs(['Calculadora IMC', 'Clearence de Creatinina'])

with imc_tab:
    # Inputs de altura e peso
    st.subheader('Altura (cm):')
    altura = st.number_input(
        "Altura", 
        value=0, 
        placeholder="Altura em cm...", 
        min_value=0, 
        max_value=300, 
        label_visibility='collapsed'
    )
    st.subheader('Peso (kg)')
    peso = st.number_input(
        "Peso", 
        value=0.0, 
        placeholder="Peso em Kg...", 
        min_value=0.0, 
        max_value=500.0, 
        label_visibility='collapsed', 
        step=0.1, 
        format="%.1f"
    )
    
    # Botões
    col1, col2 = st.columns(2)  # Criar duas colunas para posicionar os botões
    calcular = col1.button("Calcular")
    limpar = col2.button("Limpar")

    # Lógica dos botões
    if calcular:
        if altura > 0 and peso > 0:
            altura_metros = altura / 100  # Converter altura para metros
            imc_valor = peso / (altura_metros ** 2)  # Calcular IMC
            st.subheader('IMC:')
            st.write(f'**{imc_valor:.2f}**')  # Mostrar IMC com 2 casas decimais
        else:
            st.warning("Por favor, insira valores válidos para altura e peso.")

    if limpar:
        # Resetar os valores de altura e peso
        st.session_state["Altura"] = 0
        st.session_state["Peso"] = 0.0
        st.experimental_rerun()  # Recarrega a página para atualizar os inputs