import streamlit as st

st.set_page_config(
    page_title="VB Calc 1.0",
    page_icon=":syringe:"
    )

st.title("Conversor de Doses BIC:")

# Variáveis para calculo e conversão:
var_peso = range(60, 121)
var_vazao = range(1,101)

# Dicionários:
conc = {"db4": 4} #Não sei se vale a pena usar dicionário para concentrações
dose_hab = {"dobutamina": "2,5 a 20", "dopamina": "2 a 20", "noradrenalina": "0,1 a 0,5"}


st.subheader("Medicamento:")
diluicao = st.selectbox(
    "**Escolha um medicamento**",
    (
        "Dobutamina 2 mg/mL",
        "Dobutamina 4 mg/mL", 
        "Dopamina 1 mg/mL",
        "Dopamina 2 mg/mL",
        "Noradrenalina 0,08 mg/mL",
        "Noradrenalina 0,16 mg/mL",
        "Noradrenalina 0,32 mg/mL",
        "Noradrenalina 0,64 mg/mL"     
    ),
    index=None,
    placeholder="Selecione uma medicação...",
    label_visibility="collapsed"
)

with st.container(border=True):

    st.subheader("Peso do Paciente (Kg):")

    peso = st.select_slider(
        "**Peso do paciente:**",
        options=var_peso,
        value=75,
        label_visibility="collapsed"
    )

    st.subheader("Vazão (mL/h):")

    vazao = st.select_slider(
        "**Vazão (mL/h)**",
        options=var_vazao,
        value=10,
        label_visibility="collapsed"
    )

    st.divider()
    ########## Dopamina ##########
    if diluicao == "Dopamina 1 mg/mL":
        conc_dobuta = 1 * 1000
        res_final = (vazao * conc_dobuta) / (peso * 60)
        if res_final < 2 or res_final > 20:
            st.subheader(f"**A dose infundida é**: :red[{res_final:.2f}] mcg/Kg/min.")
        else:
            st.subheader(f"**A dose infundida é**: :green[{res_final:.2f}] mcg/Kg/min.")
        st.markdown(f"**Dose habitual:** {dose_hab['dopamina']} mcg/Kg/min")
    
    if diluicao == "Dopamina 2 mg/mL":
        conc_dobuta = 2 * 1000
        res_final = (vazao * conc_dobuta) / (peso * 60)
        if res_final < 2 or res_final > 20:
            st.subheader(f"**A dose infundida é**: :red[{res_final:.2f}] mcg/Kg/min.")
        else:
            st.subheader(f"**A dose infundida é**: :green[{res_final:.2f}] mcg/Kg/min.")
        st.markdown(f"**Dose habitual:** {dose_hab['dopamina']} mcg/Kg/min")
    ########## Dobutamina ##########
    if diluicao == "Dobutamina 2 mg/mL":
        conc_dobuta = 2 * 1000
        res_final = (vazao * conc_dobuta) / (peso * 60)
        if res_final < 2.5 or res_final > 20:
            st.subheader(f"**A dose infundida é**: :red[{res_final:.2f}] mcg/Kg/min.")
        else:
            st.subheader(f"**A dose infundida é**: :green[{res_final:.2f}] mcg/Kg/min.")
        st.markdown(f"**Dose habitual:** {dose_hab['dobutamina']} mcg/Kg/min")

    if diluicao == "Dobutamina 4 mg/mL":
        conc_dobuta = 4 * 1000
        res_final = (vazao * conc_dobuta) / (peso * 60)
        if res_final < 2.5 or res_final > 20:
            st.subheader(f"**A dose infundida é**: :red[{res_final:.2f}] mcg/Kg/min.")
        else:
            st.subheader(f"**A dose infundida é**: :green[{res_final:.2f}] mcg/Kg/min.")
        st.markdown(f"**Dose habitual:** {dose_hab['dobutamina']} mcg/Kg/min")
        
    ########## Noradrenalina ##########
    if diluicao == "Noradrenalina 0,08 mg/mL":
        conc_nora = 0.08 * 1000
        res_final = (vazao * conc_nora) / (peso * 60)
        if res_final < 0.1 or res_final > 0.5:
            st.subheader(f"**A dose infundida é**: :red[{res_final:.2f}] mcg/Kg/min.")
        else:
            st.subheader(f"**A dose infundida é**: :green[{res_final:.2f}] mcg/Kg/min.")
        st.markdown(f"**Dose habitual:** {dose_hab['noradrenalina']} mcg/Kg/min")


    if diluicao == "Noradrenalina 0,16 mg/mL":
        conc_nora = 0.16 * 1000
        res_final = (vazao * conc_nora) / (peso * 60)
        if res_final < 0.1 or res_final > 0.5:
            st.subheader(f"**A dose infundida é**: :red[{res_final:.2f}] mcg/Kg/min.")
        else:
            st.subheader(f"**A dose infundida é**: :green[{res_final:.2f}] mcg/Kg/min.")
        st.markdown(f"**Dose habitual:** {dose_hab['noradrenalina']} mcg/Kg/min")

    if diluicao == "Noradrenalina 0,32 mg/mL":
        conc_nora = 0.32 * 1000
        res_final = (vazao * conc_nora) / (peso * 60)
        if res_final < 0.1 or res_final > 0.5:
            st.subheader(f"**A dose infundida é**: :red[{res_final:.2f}] mcg/Kg/min.")
        else:
            st.subheader(f"**A dose infundida é**: :green[{res_final:.2f}] mcg/Kg/min.")
        st.markdown(f"**Dose habitual:** {dose_hab['noradrenalina']} mcg/Kg/min")

    if diluicao == "Noradrenalina 0,64 mg/mL":
        conc_nora = 0.64 * 1000
        res_final = (vazao * conc_nora) / (peso * 60)
        if res_final < 0.1 or res_final > 0.5:
            st.subheader(f"**A dose infundida é**: :red[{res_final:.2f}] mcg/Kg/min.")
        else:
            st.subheader(f"**A dose infundida é**: :green[{res_final:.2f}] mcg/Kg/min.")
        st.markdown(f"**Dose habitual:** {dose_hab['noradrenalina']} mcg/Kg/min")

        
    if diluicao == None:
        st.subheader("Escolha uma medicação!")

    st.divider()
