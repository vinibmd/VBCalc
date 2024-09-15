import streamlit as st

st.set_page_config(
    page_title="Eletrocardiograma",
    page_icon=":zap:"
)


######################
logo_ext_color = "imagens/logo_extended_color.png"
logo_ext_bw = "imagens/logo_extended_bw.png"
logo_only_color = "imagens/logo_only_color.png"
logo_only_bw = "imagens/logo_only_bw.png"
logo_vbcalc = "imagens/VBCalc_logo.png"
logo_vbcalc2 = "imagens/VBCalc_logo_ext.png"

# st.sidebar.image(logo_vbcalc, use_column_width=True)
st.sidebar.image(logo_vbcalc2, use_column_width=True)
st.sidebar.link_button("Apoie o VB Calc.", "https://biolivre.com.br/vbcardiologia", type="primary", use_container_width=True)
with st.sidebar:
    st.page_link("main.py", label="Home")
    st.page_link("pages/sedacao.py", label="Analgesia e Sedação")
    st.page_link("pages/bloqueadores.py", label="Bloq. Neuromuscular")
    st.page_link("pages/dva.py", label="Drogas Vasoativas")
    st.page_link("pages/ecg.py", label="ECG")
    st.page_link("pages/nitratos.py", label="Nitratos")
    st.page_link("pages/ref.py", label="Referências")
    st.page_link("pages/tutorial.py", label="Tutorial")
    st.page_link("pages/termos.py", label="Termos de Uso")
    ###########################

st.sidebar.markdown("---")
st.sidebar.markdown("Desenvolvido por **[Dr. Vinícius Beleze](https://instagram.com/drviníciusbeleze)**")

st.title('Calculadoras para Eletrocardiograma:zap:')

qtc, loc_via = st.tabs(['Calculadora de QTc', 'Localização de V.A.'])

with qtc:
    st.header('Calculadora de QTc:')
    st.subheader('Escolha a Fórmula:')
    formula_selec = st.radio('Fórmula', ['Bazett', 'Hodges', 'Fridericia', 'Framingham'], label_visibility='collapsed', horizontal=True)
    
    # Colunas para entrada de dados
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('### Intervalo QT:')
        qti = st.number_input('Intervalo QT:', placeholder='Intervalo QT em ms', step=1, label_visibility='collapsed', min_value=300, max_value=600, value=440)
    with col2:
        st.markdown('### Frequência Cardíaca:')
        fc = st.number_input('Frequência Cardíaca (bpm):', placeholder='Frequência Cardíaca em bpm', step=1, label_visibility='collapsed', min_value=30, max_value=200, value=60)
    
    # Verificação de entradas válidas
    if qti and fc:
        # Calcular o intervalo RR em segundos
        intervalo_rr = 60 / fc
        
        # Dicionário de cálculos das fórmulas de QTc
        formula_calc = {
            'Bazett': qti / (intervalo_rr ** 0.5),
            'Hodges': qti + 1.75 * (fc - 60),
            'Fridericia': qti / (intervalo_rr ** (1/3)),
            'Framingham': qti + 0.154 * (60 - fc)
        }

        # Calcular o QTc usando a fórmula selecionada
        qtc_valor = formula_calc[formula_selec]
        
        # Exibir o resultado formatado
        st.markdown(f'### Resultado: :red[{qtc_valor:.0f}] ms.')
    else:
        st.markdown(f'### Resultado: __Insira valores válidos para QT e FC.__')

    st.markdown(
    """
    #### Valores de Referência:\n
    **Idade < 40 anos:** Homem: 430 ms | Mulher: 440 ms\n
    **Idade entre 40 a 69 anos:** Homem: 440 ms | Mulher: 450 ms\n
    **Idade maior ou igual a 70 anos:** Homem: 455 ms | Mulher: 460 ms
    """
    )

with loc_via:
    st.header('Calculadora de QTc:')
    st.subheader('Escolha a Fórmula:')
    # Definição dos selecionáveis.
    st.markdown("#### Polaridade:")
    polaridade_v1 = st.radio("**Polaridade em V1**",
    ["Isoelétrico ou Negativo", "Positivo"],
    horizontal=True,
    label_visibility="collapsed")

    # Selecionável para vias direitas:
    st.markdown("#### Transição ≤ V3:")
    if polaridade_v1 == "Isoelétrico ou Negativo":
        transicao = st.radio("**Transição**",
        ["Sim", "Não"],
        horizontal=True,
        label_visibility="collapsed")
    else:
        transicao = st.radio("**Transição**",
        ["Sim", "Não"],
        horizontal=True,
        label_visibility="collapsed", disabled=True)

    # Selecionável para vias esquerdas:
    st.markdown("#### Onda delta mais positiva em:")
    if polaridade_v1 == "Isoelétrico ou Negativo":
        if transicao == "Sim":
            positividade_delta = st.radio("**Delta**",
            ["II ou III", "aVL ou aVR"],
            horizontal=True,
            label_visibility="collapsed")
        else:
            positividade_delta = st.radio("**Delta**",
            ["II", "III", "aVL", "aVR"],
            horizontal=True,
            label_visibility="collapsed")
    else:
        positividade_delta = st.radio("**Delta**",
            ["aVL", "II ou aVR", "III"],
            horizontal=True,
            label_visibility="collapsed")
    st.markdown("#### Localização Provável:")
    
    # Função para cáculo da localização.
    def localiza_via (polaridade, delta):
        if polaridade == "Isoelétrico ou Negativo":
            if transicao == "Sim":
                if delta == "II ou III":
                    localizacao = "Anterosseptal"
                else:
                    localizacao = "Posterosseptal"
            else:
                if delta == "II":
                    localizacao = "Anterolateral"
                elif delta == "III":
                    localizacao = "Anterosseptal"
                elif delta == "aVR":
                    localizacao = "Posterosseptal"
                elif delta == "aVL":
                    localizacao = "Posterolateral"
        if polaridade == "Positivo":
            if delta == "aVL":
                localizacao = "Posterosseptal"
            elif delta == "II ou aVR":
                localizacao = "Posterolateral"
            else:
                localizacao = "Anterolateral"
        return localizacao
    
    st.markdown(f"##### :green[{localiza_via(polaridade_v1, positividade_delta)}]")
