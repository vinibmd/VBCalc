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
        placeholder="Altura em cm...", 
        min_value=0, 
        max_value=300, 
        label_visibility='collapsed',
        key='Altura'
    )
    st.subheader('Peso (kg)')
    peso = st.number_input(
        "Peso", 
        placeholder="Peso em Kg...", 
        min_value=0.0, 
        max_value=500.0, 
        label_visibility='collapsed', 
        step=0.1, 
        format="%.1f",
        key='Peso'
    )
    
    # Botões
    # Função de Callback para limpar os botões
    def limpar_inputs():
        st.session_state["Altura"] = 0
        st.session_state["Peso"] = 0.0
    
    if "Altura" not in st.session_state:
        st.session_state["Altura"] = 0
    if "Peso" not in st.session_state:
        st.session_state["Peso"] = 0.0

    col1, col2 = st.columns(2)  # Criar duas colunas para posicionar os botões
    calcular = col1.button("Calcular", type="primary", use_container_width=True, key='botao_imc')
    limpar = col2.button("Limpar", type="secondary", use_container_width=True, key='limpar_imc', on_click=limpar_inputs)

    # Lógica dos botões
    if calcular:
        if altura > 0 and peso > 0:
            altura_metros = altura / 100  # Converter altura para metros
            imc_valor = peso / (altura_metros ** 2)  # Calcular IMC
            st.subheader('IMC:')
            st.write(f'##### **{imc_valor:.2f}**')  # Mostrar IMC com 2 casas decimais
            if imc_valor < 25:
                st.write('##### :green[IMC normal]')
            elif imc_valor >= 25 and imc_valor < 30:
                st.write('##### :orange[Sobrepeso]')
            elif imc_valor >= 30 and imc_valor < 35:
                st.write('##### :red[Obesidade Grau I]')
            elif imc_valor >= 35 and imc_valor < 40:
                st.write('##### :red[Obesidade Grau II]')
            else:
                st.write('##### :red[Obesidade Grau III]')
        else:
            st.warning("Por favor, insira valores válidos para altura e peso.")

with ckd:
    # Inputs de idade, sexo e creatinina
    st.subheader('Idade:')
    idade = st.number_input(
        "Idade", 
        placeholder="Idade em anos...", 
        min_value=0, 
        max_value=100, 
        label_visibility='collapsed',
        key='Idade'
    )
    st.subheader('Creatinina (mg/dL):')
    creat = st.number_input(
        "Creatinina", 
        placeholder="Valor de creatinina...", 
        min_value=0.0, 
        max_value=10.0, 
        label_visibility='collapsed', 
        step=0.1, 
        format="%.1f",
        key='Creatinina'
    )
    
    sexo = st.radio('Sexo:', ['Masculino', 'Feminino'])

    def limpar_inputs2():
            st.session_state["Idade"] = 0
            st.session_state["Creatinina"] = 0.0
        
    if "Altura" not in st.session_state:
        st.session_state["Idade"] = 0
    if "Peso" not in st.session_state:
        st.session_state["Creatinina"] = 0.0

    # Botões
    col1, col2 = st.columns(2)  # Criar duas colunas para posicionar os botões
    calcular = col1.button("Calcular", type="primary", use_container_width=True)
    limpar = col2.button("Limpar", type="secondary", use_container_width=True, on_click=limpar_inputs2)

    
    if calcular:
        if idade > 0 and creat > 0 and sexo == 'Masculino':
            if creat <= 0.9:
                A = 0.9
                B = -0.302
            else:  # creat > 0.9
                A = 0.9
                B = -1.2
            ckd_epi = 142 * (creat/A) ** B * 0.9938 ** idade
            st.subheader('Clearence de Creatinina:')
            st.write(f'##### {ckd_epi:.1f} ml/min/1.73 m²')
        elif idade > 0 and creat > 0  and sexo == 'Feminino':
            if creat <= 0.7:
                A = 0.7
                B = -0.241
            else:  # creat > 0.7
                A = 0.7
                B = -1.2
            ckd_epi = (142 * (creat/A) ** B * 0.9938 ** idade) * 1.012
            st.subheader('Clearence de Creatinina:')
            st.write(f'##### {ckd_epi:.1f} ml/min/1.73 m²')
        else:
            st.warning('Insira um valor válido')