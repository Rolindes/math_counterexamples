import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Explorador de Contraejemplos Matemáticos", page_icon="📐", layout="wide")

st.title("📐 Explorador de Contraejemplos Universitarios")
st.markdown("Busca y comprende por qué fallan los teoremas en Análisis y Topología.")

# Cargar el archivo CSV directamente desde el repositorio de GitHub
@st.cache_data
def load_data():
    try:
        # Al estar en la misma carpeta del repositorio, lee directamente el CSV
        return pd.read_csv("contraejemplos.csv")
    except Exception as e:
        st.error(f"Error al cargar el archivo contraejemplos.csv: {e}")
        return None

df = load_data()

if df is not None and not df.empty:
    # --- FILTRO 1: Por Bloque / Tema (Sidebar) ---
    st.sidebar.header("🔍 Filtrar Contenido")
    temas_disponibles = ['Todos'] + list(df['tema'].unique())
    tema_seleccionado = st.sidebar.selectbox("Selecciona un Bloque (Tema):", temas_disponibles)

    if tema_seleccionado != 'Todos':
        df_filtrado = df[df['tema'] == tema_seleccionado]
    else:
        df_filtrado = df

    # --- FILTRO 2: Buscador por Nombre o Teorema ---
    busqueda = st.sidebar.text_input("Buscar por Teorema o Contraejemplo:")
    if busqueda:
        df_filtrado = df_filtrado[
            df_filtrado['teorema'].str.contains(busqueda, case=False, na=False) |
            df_filtrado['nombre_contraejemplo'].str.contains(busqueda, case=False, na=False)
        ]

    # --- MOSTRAR RESULTADOS ---
    st.subheader(f"Resultados encontrados ({len(df_filtrado)})")
    
    for index, row in df_filtrado.iterrows():
        with st.expander(f"📌 **{row['teorema']}** — *Contraejemplo: {row['nombre_contraejemplo']}*"):
            st.markdown(f"**Bloque / Tema:** {row['tema']}")
            st.markdown(f"**Hipótesis que se rompe:** ⚠️ _{row['hipotesis_rota']}_")
            st.markdown(f"**Definición Formal:** `{row['definicion_formal']}`")
            st.markdown("---")
            st.markdown(f"**Explicación Detallada:**\n{row['explicacion_detallada']}")
else:
    st.warning("No se pudieron cargar los datos. Asegúrate de haber subido el archivo 'contraejemplos.csv' al mismo repositorio de GitHub.")
