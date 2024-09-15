import streamlit as st

st.set_page_config(
    page_title="VB Calc - Termos de Uso",
    page_icon=":open_file_folder:"
)


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
st.sidebar.markdown("---")
st.sidebar.markdown("Desenvolvido por **[Dr. Vinícius Beleze](https://instagram.com/drviníciusbeleze)**")


"""
# Termos de Uso:

**Última atualização: 19 de agosto de 2024** 

---

## **1. Aceitação dos Termos**

Ao acessar e utilizar o aplicativo VB Calc 1.0 ("App"), você concorda em cumprir este Termo de Uso. Caso não concorde com qualquer parte dos termos, você não deve usar o App.

---

## **2. Licença de Uso**

O App é disponibilizado gratuitamente para uso pessoal e profissional em ambiente clínico. Este uso é limitado à utilização das funcionalidades do App conforme descrito no tutorial. Não há cobrança pelo uso do App neste momento, mas o desenvolvedor se reserva o direito de implementar modelos de monetização ou cobrança no futuro.

---

## **3. Direitos Autorais**

O código-fonte do App, bem como todos os elementos visuais, gráficos, e conteúdos associados, são protegidos por direitos autorais e outras leis de propriedade intelectual. O desenvolvedor do App detém todos os direitos, títulos e interesses relativos ao código-fonte e ao App como um todo.

**Você não tem permissão para:**

- Reproduzir, distribuir ou modificar o código-fonte do App, total ou parcialmente.
- Utilizar qualquer parte do código-fonte em outros projetos, sejam eles comerciais ou não comerciais.
- Engajar-se em qualquer atividade que implique na redistribuição do App, modificado ou não, sem autorização prévia e por escrito do desenvolvedor.

---

## **4. Limitação de Responsabilidade**

O App foi desenvolvido como uma ferramenta de suporte e não substitui o julgamento clínico. O desenvolvedor não será responsável por quaisquer danos diretos, indiretos, incidentais, especiais ou consequenciais resultantes do uso ou da incapacidade de uso do App.

---

## **5. Alterações nos Termos**

O desenvolvedor se reserva o direito de modificar este Termo de Uso a qualquer momento. As alterações serão publicadas no App, e o uso contínuo do App após a publicação das alterações constituirá sua aceitação dos novos termos.

---

## **6. Contato**

Para dúvidas ou solicitações de autorização, entre em contato pelo e-mail: drbeleze@gmail.com

---

**Ao utilizar este App, você reconhece que leu, compreendeu e concorda com os termos acima.**

"""