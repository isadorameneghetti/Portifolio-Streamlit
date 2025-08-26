import streamlit as st

def main():
    st.title("🛠️ Skills e Conhecimentos")
    
    # Habilidades técnicas
    st.header("💻 Habilidades Técnicas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Linguagens de Programação")
        st.markdown("""
        - **JavaScript** ⭐⭐⭐⭐
        - **TypeScript** ⭐⭐⭐
        - **Python** ⭐⭐⭐⭐
        - **Java** ⭐⭐⭐
        - **C/C++** ⭐⭐⭐
        - **C#** ⭐⭐
        - **Lua** ⭐⭐
        - **PHP** ⭐⭐⭐
        - **MySQL** ⭐⭐⭐
        """)
    
    with col2:
        st.subheader("Desenvolvimento Web")
        st.markdown("""
        - **HTML5** ⭐⭐⭐⭐
        - **CSS3** ⭐⭐⭐⭐
        - **SASS** ⭐⭐⭐
        - **React** ⭐⭐⭐
        - **Bootstrap** ⭐⭐⭐⭐
        - **Tailwind CSS** ⭐⭐⭐
        - **UX/UI Design** ⭐⭐⭐
        """)
    
    # Ferramentas e tecnologias
    st.header("🔧 Ferramentas e Tecnologias")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Versionamento")
        st.markdown("""
        - Git
        - GitHub
        """)
    
    with col2:
        st.subheader("Design e Prototipagem")
        st.markdown("""
        - Figma
        - Canva
        """)
    
    with col3:
        st.subheader("Produtividade")
        st.markdown("""
        - Notion
        - Google Workspace
        - Microsoft Office
        """)
    
    # Habilidades de inovação
    st.header("🚀 Habilidades de Inovação")
    
    inovacao = [
        "Design Thinking",
        "Criatividade Empreendedora", 
        "Storytelling",
        "Gestão Ágil de Projetos",
        "Trabalho em Equipe Multidisciplinar"
    ]
    
    for skill in inovacao:
        st.write(f"✨ {skill}")
    
    # Projetos
    st.header("📂 Projetos Acadêmicos")
    
    with st.expander("BLUE FUTURE - Inovação Azul (Maio 2024 - Jun 2024)"):
        st.markdown("""
        **Parcerias:** UNESCO, OCEANS20, AWS, SOFTTEK
        
        **Tecnologias:** Python, Arduino, HTML, CSS, JavaScript
        
        **Contribuições:**
        - Desenvolvimento de software em Python e Arduino para soluções ambientais
        - Criação de landing page responsiva com foco em UX
        - Realização de pitchs e aplicação de gestão ágil
        """)
    
    with st.expander("FÓRMULA E (Abril 2024 - Set 2024)"):
        st.markdown("""
        **Parcerias:** TechMahindra, FIA
        
        **Tecnologias:** HTML, CSS, JavaScript
        
        **Contribuições:**
        - Desenvolvimento web para promover a Fórmula E
        - Aplicação de storytelling em apresentações
        - Trabalho em equipe multidisciplinar
        """)

if __name__ == "__main__":
    main()