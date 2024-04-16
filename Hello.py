import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuração inicial da página
st.set_page_config(page_title="Calculadora de Opções Avançada", layout="wide", page_icon="📈")

# Estilos personalizados
st.markdown("""
<style>
    .big-font {
        font-size:25px !important;
        font-weight: bold;
    }
    .reportview-container .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .sidebar .sidebar-content {
        padding: 10px 10px 10px 10px;
    }
    h1 {
        color: #0e1117;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title('Calculadora de Opções Avançada', anchor=None)

# Sidebar - Parâmetros de Entrada
with st.sidebar:
    st.markdown("## Parâmetros de Entrada")
    mercado = st.selectbox("Escolha o Mercado:", ["Ações", "Moedas", "ETFs", "Offshore"])
    simbolo = st.text_input("Símbolo do Ativo:", placeholder="Ex: AAPL ou EURUSD")
    S = st.number_input("Preço do Ativo (S):", min_value=0.0, value=100.0, format="%.2f")
    K = st.number_input("Preço de Exercício (K):", min_value=0.0, value=100.0, format="%.2f")
    T = st.number_input("Tempo até a Expiração (T) em anos:", min_value=0.0, value=1.0, step=0.1, format="%.2f")
    r = st.number_input("Taxa de Juros Sem Risco (r):", min_value=0.0, value=0.05, step=0.01, format="%.2f")
    sigma = st.number_input("Volatilidade (σ):", min_value=0.0, value=0.20, step=0.01, format="%.2f")
    opcao_tipo = st.selectbox("Tipo de Opção:", ["Europeia", "Americana", "Asiática"])

# Main Area - Displaying Results and Graphs
col1, col2 = st.columns(2)

with col1:
    if st.button('Calcular Preço da Opção'):
        with st.spinner('Calculando...'):
            # Placeholder for calculation logic
            preco_opcao = S * np.exp(-r * T)  # Example calculation
            st.success(f"Preço da Opção Calculado: ${preco_opcao:.2f}")

with col2:
    st.write("### Gráfico de Simulação do Preço do Ativo")
    fig, ax = plt.subplots()
    ax.plot(np.random.normal(S, sigma, 100), marker='', color='skyblue', linewidth=2)
    ax.set_title("Simulação de Preço do Ativo ao Longo do Tempo")
    ax.grid(True)
    st.pyplot(fig)



def delta(S, K, T, r, sigma, option_type='call'):
    """Calcula o Delta, que mede a sensibilidade ao preço do ativo subjacente."""
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    if option_type == 'call':
        return stats.norm.cdf(d1)
    else:
        return stats.norm.cdf(d1) - 1

def gamma(S, K, T, r, sigma):
    """Calcula o Gamma, que mede a taxa de mudança do Delta em relação ao preço do ativo."""
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    return stats.norm.pdf(d1) / (S * sigma * np.sqrt(T))

def vega(S, K, T, r, sigma):
    """Calcula o Vega, que mede a sensibilidade ao preço em relação à volatilidade do ativo."""
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    return S * stats.norm.pdf(d1) * np.sqrt(T)


import plotly.graph_objects as go

def plot_interactive_price_simulation(S, sigma, T):
    prices = S * np.exp(np.cumsum(np.random.normal(0, sigma, int(T*365)))*np.sqrt(1/365))
    fig = go.Figure(data=[go.Line(x=list(range(int(T*365))), y=prices)])
    fig.update_layout(title='Simulação de Preço do Ativo', xaxis_title='Dias', yaxis_title='Preço do Ativo')
    st.plotly_chart(fig)



tab1, tab2, tab3 = st.tabs(["Cálculo de Opção", "Greeks", "Simulação de Preço"])

with tab1:
    st.header("Calculadora de Opção")
    # Adicionar campos para entrada de dados e botão para calcular

with tab2:
    st.header("Análise de Sensibilidade - Greeks")
    # Campos para entrada de dados e visualização de Greeks

with tab3:
    st.header("Simulação de Preço do Ativo")
    # Inserir gráfico interativo de simulação de preço

