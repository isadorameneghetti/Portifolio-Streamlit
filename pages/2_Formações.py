import streamlit as st

def main():
    st.title("🎓 Formação e Experiência")
    
    # Formação acadêmica
    st.header("Formação Acadêmica")
    
    with st.expander("FIAP - Faculdade de Informática e Administração Paulista (Fev. 2024 - Dez. 2027)"):
        st.write("""
        **Bacharelado em Engenharia de Software**
        - Cursando o primeiro ano
        - Foco em desenvolvimento full stack, arquitetura de software e engenharia de requisitos
        - Participação em projetos interdisciplinares
        """)
    
    # Idiomas
    st.header("🌎 Idiomas")
    
    with st.expander("Wizard (Jan. 2012 - Cursando)"):
        st.write("""
        **Inglês** - Nível Avançado (C1)
        - Leitura, escrita e conversação avançadas
        - Capacidade de acompanhar documentação técnica e conteúdos em inglês
        """)
    
    # Certificações
    st.header("📜 Certificações Principais")
    
    certificacoes = [
        "Funções com Excel: operações matemáticas e filtros - 2025",
        "Java: aplicando a Orientação a Objetos - 2025",
        "Formação Social e Sustentabilidade - 2024",
        "C: conhecendo a Linguagem das Linguagens - 2024",
        "PHP: criando sua aplicação - 2024",
        "Lógica de Programação: mergulhe em programação com JavaScript - 2022",
        "Python: avançando na linguagem - 2022"
    ]
    
    for cert in certificacoes:
        st.write(f"✅ {cert}")

if __name__ == "__main__":
    main()