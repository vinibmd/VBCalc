import streamlit as st

st.set_page_config(
    page_title="VB Calc - Home",
    page_icon=":house:"
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
    st.page_link("pages/nitratos.py", label="Nitratos")
    st.page_link("pages/ref.py", label="Referências")
    st.page_link("pages/tutorial.py", label="Tutorial")
    st.page_link("pages/termos.py", label="Termos de Uso")
st.sidebar.markdown("---")
st.sidebar.markdown("Desenvolvido por **[Dr. Vinícius Beleze](https://instagram.com/drviníciusbeleze)**")

st.title("Bem vindo(a)! :smile:")

st.header("É um prazer ter você por aqui!")

st.markdown("""É com muita alegria que apresento para vocês o **VB Calc.1.0**, um aplicação
multiplataforma (desktop, iOS e Android), desenvolvida por mim ([Dr. Vinícius Beleze](https://instagram.com/drviniciusbeleze))!

Fique a vontade para utilizar a plataforma na sua prática clínica diária!

Os conteúdos podem ser acessados na **barra lateral esquerda**.""")
st.markdown("Ao utilizar a plataforma, você **CONCORDA** e **ACEITA** os **Termos de Uso**.")

st.markdown("Segue um **Tutorial em Vídeo** sobre como utilizar a plataforma:")

st.video("https://www.youtube.com/watch?v=lKSZnZggcto&list=RDlKSZnZggcto&start_radio=1")
     
st.markdown("Se houver qualquer outra dúvida quanto a utilização da plataforma, você pode acessar a página de **Tutorial**.")

st.markdown("""
Agora, se você está gostando da plataforma, que tal ajudar a continuar e manter esse
projeto sempre ativo e grauito? [Apoie o VB Calc.](https://biolivre.com.br/vbcardiologia)

Qualquer dúvida, sugestão, reclamação ou proposta de colaboração me manda um email
no drbeleze@gmail.com.

Um ótimo dia!
""")



