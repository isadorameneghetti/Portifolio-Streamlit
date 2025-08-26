## 📋 Streamlit

![Banner](imgs/banner.jpeg)


## Portfólio com Análise: Java & IA - Stack Overflow Analysis


Este é um portfólio interativo desenvolvido em **Streamlit** para apresentar as habilidades, experiências e projetos de **Isadora Meneghetti, Engenheira de Software**, akém de uma análise ligada a falta de profissionais de Java & IA.

## Link - Streamlit
https://isadorameneghetti.streamlit.app/

## Características

- **Design Responsivo**: Layout adaptável para diferentes dispositivos  
- **Navegação Intuitiva**: Menu lateral com acesso às diferentes seções  
- **Paleta de Cores Personalizada**: Esquema de cores em tons de azul  
- **Seções Organizadas**:  
  - **Home**: Apresentação e informações de contato  
  - **Formação e Experiência**: Histórico acadêmico e profissional  
  - **Skills**: Habilidades técnicas e ferramentas  
  - **Análise Java**: Análise específica de competências em Java  

## Análise Java

A seção de **Análise Java** inclui:  

- **Métricas de Proficiência**: Avaliação visual das habilidades em Java  
- **Framework Experience**: Análise comparativa de experiência com **Spring Boot, Hibernate, Maven e JUnit**  
- **Evolução Temporal**: Gráfico de progresso ao longo do tempo  
- **Projetos Java**: Listagem de projetos desenvolvidos com Java  
- **Certificações**: Certificações relacionadas a Java  

### Visualizações Incluídas

1. **Radar Chart**: Competências técnicas em Java (OOP, Collections, Multithreading, etc.)  
2. **Gráfico de Barras**: Experiência com frameworks Java  
3. **Gráfico de Linhas**: Evolução temporal das habilidades  
4. **Gráfico de Dispersão**: Relação entre complexidade de projetos e domínio de Java  

## Tecnologias Utilizadas

- **Streamlit**: Framework principal para criação da aplicação web  
- **Pandas**: Manipulação de dados  
- **NumPy**: Computação numérica  
- **Matplotlib**: Visualizações gráficas  
- **Seaborn**: Visualizações estatísticas  
- **Plotly**: Gráficos interativos  
- **SciPy**: Estatísticas e computação científica  
- **Scikit-learn**: Métricas de avaliação (R² score)  

## Estrutura do Projeto
    
```bash 
├── 1_Home.py 
├── pages/
│ ├── 2_Formações.py 
│ ├──3_Skills.py 
│ └── 4_Análise.py 
├── banner/
│ ├── banner.jpeg 
├── requirements.txt 
└── README.md 
```

## Como Executar

### 1. Clone o repositório:
```bash
git clone https://github.com/isadorameneghetti/Portifolio-Streamlit
cd portfolio-isadora
```

### 2. Instale as dependências:
```bash
pip install -r requirements.txt
```

### 3. Execute a aplicação:
```bash
streamlit run 1_Home.py
```

### 4. Acesse no navegador:
```bash
http://localhost:8501
```

## Requisitos
```bash
streamlit
pandas
numpy
matplotlib
seaborn
plotly
scipy
scikit-learn
```

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).
