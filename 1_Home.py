import streamlit as st

def main():
    st.set_page_config(
        page_title="Isadora Meneghetti - Engenheira de Software" ,
        layout="wide"
    )
    
    # Header
    st.title("Isadora de Morais Meneghetti")
    st.subheader("Estudante de Engenharia de Software | Desenvolvedora Full Stack")
    st.write("📍 Vila Prudente, São Paulo - SP | 📞 (11) 99219-3528")
    st.write("📧 isadorammeneghetti@gmail.com")
    st.write("[LinkedIn](https://linkedin.com/in/isadora-meneghetti) | [GitHub](https://github.com/isadorameneghetti)")
    
    # Sobre mim
    st.header("👋 Sobre Mim")
    st.write("""
    Sou estudante de Engenharia de Software na FIAP com sólida base em programação e forte desejo de aprender e crescer 
    na área de desenvolvimento. Tenho experiência em projetos acadêmicos desafiadores e estou pronta para aplicar e 
    aprimorar minhas habilidades em codificação, resolução de problemas e desenvolvimento de software de qualidade.
    """)
    
    # Objetivo profissional
    st.header("🎯 Objetivo Profissional")
    st.write("""
    Busco minha primeira oportunidade na área de Engenharia de Software, onde possa contribuir com meus conhecimentos 
    em desenvolvimento full stack e aprender com profissionais experientes. Tenho interesse em trabalhar com tecnologias 
    modernas como Java, Python, React e cloud computing.
    """)
    
    # Destaques
    st.header("⭐ Destaques")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Linguagens", "10+")
    with col2:
        st.metric("Projetos Acadêmicos", "2+")
    with col3:
        st.metric("Certificações", "10+")



if __name__ == "__main__":
    main()