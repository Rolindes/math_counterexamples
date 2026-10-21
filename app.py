import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="MathCounterexamples - Nivel Universitario", 
    page_icon="📐", 
    layout="wide"
)

# Estilo visual moderno y limpio
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stExpander {
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        background-color: white;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📐 Explorador de Contraejemplos Matemáticos Universitarios")
st.markdown("La herramienta definitiva para entender por qué las hipótesis de los teoremas no se pueden relajar.")

# Cargar el archivo CSV de contraejemplos
@st.cache_data
def load_data():
    try:
        return pd.read_csv("contraejemplos.csv")
    except Exception as e:
        st.error(f"Error al cargar el archivo contraejemplos.csv: {e}")
        return None

df = load_data()

if df is not None and not df.empty:
    # --- BARRA LATERAL: SEPARACIÓN POR BLOQUES Y FILTROS ---
    st.sidebar.header("🧭 Navegación Académica")
    
    # Selector principal de Bloques (Temas)
    temas_disponibles = ['Todos los Bloques'] + list(df['tema'].unique())
    tema_seleccionado = st.sidebar.selectbox("📂 Selecciona el Bloque (Materia):", temas_disponibles)

    # Filtrar por tema seleccionado
    if tema_seleccionado != 'Todos los Bloques':
        df_filtrado = df[df['tema'] == tema_seleccionado]
    else:
        df_filtrado = df

    st.sidebar.markdown("---")
    
    # Buscador avanzado por texto
    busqueda = st.sidebar.text_input("🔍 Buscar Teorema o Contraejemplo:", placeholder="Ej. Bolzano, compacidad, métrica...")
    if busqueda:
        df_filtrado = df_filtrado[
            df_filtrado['teorema'].str.contains(busqueda, case=False, na=False) |
            df_filtrado['nombre_contraejemplo'].str.contains(busqueda, case=False, na=False) |
            df_filtrado['explicacion_detallada'].str.contains(busqueda, case=False, na=False)
        ]

    # Métrica rápida en la barra lateral
    st.sidebar.markdown("---")
    st.sidebar.metric(label="Contraejemplos disponibles", value=len(df_filtrado))

    # --- PANTALLA PRINCIPAL ---
    st.subheader(f"Resultados en: {tema_seleccionado} ({len(df_filtrado)} contraejemplos)")
    
    for index, row in df_filtrado.iterrows():
        with st.expander(f"📌 **{row['teorema']}** — *{row['nombre_contraejemplo']}*"):
            col1, col2 = st.columns([2, 1])
            with col1:
                st.markdown(f"**Materia / Bloque:** `{row['tema']}`")
                st.markdown(f"**Hipótesis que se rompe:** ⚠️ _{row['hipotesis_rota']}_")
                st.markdown(f"**Definición / Ejemplo Formal:**")
                st.code(row['definicion_formal'], language="text")
            with col2:
                st.markdown(f"**Grado de Dificultad:** Universitaria")
            
            st.markdown("---")
            st.markdown(f"**💡 Explicación Detallada y Demostración:**\n\n{row['explicacion_detallada']}")
else:
    st.warning("⚠️ No se pudieron cargar los datos. Asegúrate de que el archivo 'contraejemplos.csv' está correctamente subido al repositorio.")
