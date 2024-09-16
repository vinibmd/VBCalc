import streamlit as st
from main import barra_lateral

st.set_page_config(
    page_title="VB Calc - Tutorial",
    page_icon=":question:"
)

barra_lateral()

st.sidebar.markdown("---")
st.sidebar.markdown("Desenvolvido por **[Dr. Vinícius Beleze](https://instagram.com/drviníciusbeleze)**")


"""
# Tutorial de Uso do App VB Calc 1.0

19 de agosto de 2024 

---

## **1. Início: Selecionando a Página de Cálculo**

---

Ao abrir o aplicativo, você verá uma barra lateral à esquerda com opções de páginas que você pode acessar. Cada página é dedicada a um grupo específico de medicações:

- **Analgesia e Sedação:** Acesse essa página para calcular doses de sedativos.
- **Bloqueadores Neuromusculares:** Acesse essa página para calcular doses de sedativos.
- **Drogas Vasoativas**: Selecione essa página para calcular doses de medicações vasoativas.
- **Nitratos**: Use essa página para calcular doses de nitratos.
- **Referências:** Nesta página você pode encontrar as referências bibliográficas utilizadas para formulação das doses habituais.
- **Tutorial:** Aqui você encontra uma breve explicação de como utilizar o App.

Simplesmente clique no nome da página desejada na barra lateral para começar.

---

## **2. Escolhendo o Medicamento**

Dentro da página que você selecionou:

- **Medicamento**: Logo no topo, você verá um menu suspenso onde pode escolher o medicamento que deseja calcular. Clique na seta para baixo e selecione a medicação que deseja administrar.

---

## **3. Definindo o Peso do Paciente**

Após selecionar o medicamento:

- **Peso do Paciente (Kg)**: Use o controle deslizante para definir o peso do paciente em quilogramas (Kg). O peso será usado no cálculo da dose da medicação.
    - Deslize para a esquerda ou para a direita para ajustar o peso.
    - O valor padrão é de 75 Kg, mas você pode ajustá-lo de acordo com o peso real do paciente.

---

## **4. Configurando a Vazão da Bomba Infusora**

Depois de definir o peso do paciente:

- **Vazão (mL/h)**: Use o segundo controle deslizante para ajustar a vazão da bomba infusora em mililitros por hora (mL/h).
    - A vazão determina a velocidade com que a medicação será administrada ao paciente.
    - Ajuste para a vazão desejada para o tratamento.

---

## **5. Visualizando o Resultado**

Após configurar o medicamento, peso, e vazão:

- O aplicativo calculará automaticamente a dose da medicação em **mcg/Kg/min** ou **mcg/Kg/hora**, dependendo da medicação selecionada.
    - **Dose fora do intervalo habitual**: Se a dose calculada estiver fora do intervalo habitual, o resultado aparecerá em vermelho como um alerta.
    - **Dose dentro do intervalo habitual**: Se a dose calculada estiver dentro do intervalo habitual, o resultado aparecerá em verde.

---

## **6. Referência da Dose Habitual**

Abaixo do resultado do cálculo:

- **Dose Habitual**: O aplicativo exibe o intervalo de dose habitual da medicação, ajudando a comparar a dose calculada com as práticas clínicas comuns.

---

## **7. Considerações Finais**

- **Verifique as configurações**: Sempre revise as configurações antes de iniciar a infusão para garantir que o cálculo esteja correto.
- **Uso Clínico**: Este aplicativo é uma ferramenta de suporte e não substitui o julgamento clínico. Sempre siga os protocolos e diretrizes do hospital.

---

## **Exemplo Prático**

**Suponha que você queira administrar Dobutamina a um paciente de 70 Kg com uma vazão de 20 mL/h:**

1. Selecione a página "Drogas Vasoativas".
2. No menu suspenso, escolha "Dobutamina 2 mg/mL".
3. Ajuste o peso do paciente para 70 Kg.
4. Defina a vazão para 20 mL/h.
5. Veja o resultado calculado em mcg/Kg/min, com a cor correspondente ao intervalo habitual.

Pronto! Agora você pode seguir com a administração da medicação conforme o cálculo realizado.
"""