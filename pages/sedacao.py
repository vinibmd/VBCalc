import streamlit as st
from main import barra_lateral

st.set_page_config(
    page_title="VB Calc - Analgesia e Sedação",
    page_icon=":pill:"
)

barra_lateral()
    
st.sidebar.markdown("---")
st.sidebar.markdown("Desenvolvido por **[Dr. Vinícius Beleze](https://instagram.com/drviníciusbeleze)**")

st.title("Sedação e Analgesia:")

# Variáveis para cálculo e conversão:
var_peso = range(60, 121)
var_vazao = range(1, 101)

# Dicionário de concentrações e doses habituais:
medicamentos = {
    "Cetamina 2 mg/mL": {"concentracao": 2 * 1000, "dose_hab": "0,04 a 2,5", "limites": (0.2, 1.5), "unidade": "mg/kg/hora"},
    "Dexmedetomidina 4 mcg/mL": {"concentracao": 4, "dose_hab": "0,25 a 1,5", "limites": (0.2, 1.5), "unidade": "hora"},
    "Fentanil 10 mcg/mL": {"concentracao": 10, "dose_hab": "0,7 a 10", "limites": (0.7, 10), "unidade": "hora"},
    "Fentanil 20 mcg/mL": {"concentracao": 20, "dose_hab": "0,7 a 10", "limites": (0.7, 10), "unidade": "hora"},
    "Fentanil 30 mcg/mL": {"concentracao": 30, "dose_hab": "0,7 a 10", "limites": (0.7, 10), "unidade": "hora"},
    "Propofol 10 mg/mL": {"concentracao": 10 * 1000, "dose_hab": "5 a 50", "limites": (5, 50), "unidade": "min"},
    #"Propofol 20 mg/mL": {"concentracao": 20 * 1000, "dose_hab": "5 a 50", "limites": (5, 50), "unidade": "min"},
    "Midazolam 1 mg/mL": {"concentracao": 1 * 1000, "dose_hab": "0,01 a 0,1", "limites": (0.01, 0.1), "unidade": "mg/kg/hora"},
    "Midazolam 2 mg/mL": {"concentracao": 2 * 1000, "dose_hab": "0,01 a 0,1", "limites": (0.01, 0.1), "unidade": "mg/kg/hora"},
}

def calcular_dose(vazao, concentracao, peso, unidade="min"):
    if unidade == "hora":
        return (vazao * concentracao) / peso  # Dose em mcg/Kg/hora ou mg/kg/hora
    elif unidade == "mg/kg/hora":
        return (vazao * concentracao) / peso / 1000  # Converte de mcg para mg
    else:
        return (vazao * concentracao) / (peso * 60)  # Dose em mcg/Kg/min

def exibir_resultado(res_final, limites, dose_hab, unidade="min"):
    # Verifica se a dose está fora dos limites e formata a cor adequadamente
    if res_final < limites[0] or res_final > limites[1]:
        cor = "red"
    else:
        cor = "green"

    # Exibe a dose infundida com a unidade correta
    if unidade == "hora":
        st.markdown(f"Medicação selecionada: **{diluicao}**")
        st.subheader(f"**A dose infundida é:** :{cor}[{res_final:.2f}] mcg/Kg/hora.")
        st.markdown(f"**Dose habitual:** {dose_hab} mcg/Kg/hora")
    elif unidade == "mg/kg/hora":
        st.markdown(f"Medicação selecionada: **{diluicao}**")
        st.subheader(f"**A dose infundida é:** :{cor}[{res_final:.2f}] mg/Kg/hora.")
        st.markdown(f"**Dose habitual:** {dose_hab} mg/Kg/hora")
    else:
        st.markdown(f"Medicação selecionada: **{diluicao}**")
        st.subheader(f"**A dose infundida é:** :{cor}[{res_final:.2f}] mcg/Kg/min.")
        st.markdown(f"**Dose habitual:** {dose_hab} mcg/Kg/min")

st.subheader("Medicamento:")
diluicao = st.selectbox(
    "**Escolha um medicamento**",
    list(medicamentos.keys()),
    index=None,
    placeholder="Selecione uma medicação...",
    label_visibility="collapsed"
)

with st.container(border=True):
    st.subheader("Peso do Paciente (Kg):")
    peso = st.slider(
        "**Peso do paciente (Kg):**",
        min_value=60,
        max_value=120,
        value=75
    )

    st.subheader("Vazão (mL/h):")
    vazao = st.slider(
        "**Vazão (mL/h):**",
        min_value=1,
        max_value=100,
        value=10
    )

    st.divider()

    if diluicao:
        medicamento_selecionado = medicamentos[diluicao]
        res_final = calcular_dose(vazao, medicamento_selecionado["concentracao"], peso, unidade=medicamento_selecionado["unidade"])
        exibir_resultado(res_final, medicamento_selecionado["limites"], medicamento_selecionado["dose_hab"], unidade=medicamento_selecionado["unidade"])
    else:
        st.subheader("Escolha uma medicação!")

    st.divider()
