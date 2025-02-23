import streamlit as st
from main import barra_lateral

st.set_page_config(
    page_title="VB Calc - Drogas Vasoativas",
    page_icon=":syringe:"
)

barra_lateral()

st.sidebar.markdown("---")
st.sidebar.markdown("Desenvolvido por **[Dr. Vinícius Beleze](https://instagram.com/drviníciusbeleze)**")

st.title("Drogas Vasoativas:")

# Variáveis para calculo e conversão:
var_peso = range(60, 121)
var_vazao = range(1, 101)

# Dicionário de concentrações e doses habituais:
medicamentos = {
    "Dobutamina 2 mg/mL": {"concentracao": 2 * 1000, "dose_hab": "2,5 a 20", "limites": (2.5, 20)},
    "Dobutamina 4 mg/mL": {"concentracao": 4 * 1000, "dose_hab": "2,5 a 20", "limites": (2.5, 20)},
    "Dopamina 1 mg/mL": {"concentracao": 1 * 1000, "dose_hab": "2 a 20", "limites": (2, 20)},
    "Dopamina 2 mg/mL": {"concentracao": 2 * 1000, "dose_hab": "2 a 20", "limites": (2, 20)},
    "Esmolol 10 mg/mL": {"concentracao": 10 * 1000, "dose_hab": "50 a 300", "limites": (50, 300)},
    "Nitroprussiato 0,2 mg/mL": {"concentracao": 0.2 * 1000, "dose_hab": "0,25 a 10", "limites": (0.25, 10)},
    "Noradrenalina 0,08 mg/mL": {"concentracao": 0.08 * 1000, "dose_hab": "0,1 a 0,5", "limites": (0.1, 0.5)},
    "Noradrenalina 0,16 mg/mL": {"concentracao": 0.16 * 1000, "dose_hab": "0,1 a 0,5", "limites": (0.1, 0.5)},
    "Noradrenalina 0,32 mg/mL": {"concentracao": 0.32 * 1000, "dose_hab": "0,1 a 0,5", "limites": (0.1, 0.5)},
    "Noradrenalina 0,64 mg/mL": {"concentracao": 0.64 * 1000, "dose_hab": "0,1 a 0,5", "limites": (0.1, 0.5)},
}

def calcular_dose(vazao, concentracao, peso):
    return (vazao * concentracao) / (peso * 60)

def exibir_resultado(res_final, limites, dose_hab):
    if res_final < limites[0] or res_final > limites[1]:
        st.markdown(f"Medicação selecionada: **{diluicao}**")
        st.subheader(f"**A dose infundida é:** :red[{res_final:.2f}] mcg/Kg/min.")
    else:
        st.markdown(f"Medicação selecionada: **{diluicao}**")
        st.subheader(f"**A dose infundida é:** :green[{res_final:.2f}] mcg/Kg/min.")
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
        res_final = calcular_dose(vazao, medicamento_selecionado["concentracao"], peso)
        exibir_resultado(res_final, medicamento_selecionado["limites"], medicamento_selecionado["dose_hab"])
    else:
        st.subheader("Escolha uma medicação!")

    st.divider()
