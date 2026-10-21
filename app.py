import streamlit as st
import pandas as pd
import json
import os

# Configuración de la página
st.set_page_config(
    page_title="MathCounterexamples - Nivel Universitario", 
    page_icon="📐", 
    layout="wide"
)

# Estilo visual moderno
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

# Archivo local donde se guardarán los contraejemplos dinámicos
DB_FILE = "database_contraejemplos.json"

# Datos iniciales por defecto si el archivo no existe
DATOS_INICIALES = [
    {
        "tema": "Topología - Separabilidad y Metrizabilidad",
        "teorema": "Todo espacio metrizable separable es 2AN",
        "hipotesis_rota": "La existencia de un subconjunto denso numerable garantiza base numerable en espacios métricos",
        "nombre_contraejemplo": "Espacio métrico separable (X, τ_d) con A = {a_n} denso numerable",
        "definicion_formal": "ℬ = {B_d(a_n; 1/m) | n, m ∈ ℕ} es base numerable de la topología",
        "explicacion_detallada": "Si (X, τ_d) es metrizable y posee un subconjunto denso numerable A, la familia de bolas con radios racionales centradas en A forma una base numerable de la topología, demostrando que todo espacio métrico separable es 2AN[cite: 114]."
    },
    {
        "tema": "Topología - Axiomas de Separación (T_i)",
        "teorema": "Axioma T1 frente a Hausdorff (T2)",
        "hipotesis_rota": "Un espacio T1 no es necesariamente Hausdorff (T2) ni metrizable",
        "nombre_contraejemplo": "Topología Cofinita en un conjunto infinito (ℝ, τ_{cf})",
        "definicion_formal": "τ_{cf} = {U ⊂ ℝ | ℝ \\ U es finito} ∪ {∅}",
        "explicacion_detallada": "Los cerrados propios son los conjuntos finitos[cite: 7]. Dados x ≠ y, se pueden aislar de forma unilateral mediante complementarios finitos (cumple T1). No obstante, dos abiertos no vacíos cualesquiera tienen complementarios finitos, por lo que su intersección nunca puede ser vacía[cite: 31, 34, 47, 113]."
    }
]

# Función para cargar datos desde el archivo JSON local
def load_data():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            try:
                return pd.DataFrame(json.load(f))
            except json.JSONDecodeError:
                return pd.DataFrame(DATOS_INICIALES)
    else:
        # Si no existe, creamos el archivo con los datos iniciales
        df = pd.DataFrame(DATOS_INICIALES)
        save_data(df)
        return df

# Función para guardar el DataFrame en el archivo JSON
def save_data(df):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(df.to_dict(orient="records"), f, ensure_ascii=False, indent=4)

# Cargar base de datos actual
df = load_data()

st.title("📐 Explorador Dinámico: Cálculo y Topología UPM")
st.markdown("Busca teoremas, filtra por bloques o añade tus propios contraejemplos a la base de datos local.")

# --- BARRA LATERAL: NAVEGACIÓN, BÚSQUEDA Y AÑADIR ---
st.sidebar.header("🧭 Navegación y Filtros")

temas_disponibles = ['Todos los Bloques'] + list(df['tema'].unique())
tema_seleccionado = st.sidebar.selectbox("📂 Selecciona el Bloque:", temas_disponibles)

if tema_seleccionado != 'Todos los Bloques':
    df_filtrado = df[df['tema'] == tema_seleccionado]
else:
    df_filtrado = df

busqueda = st.sidebar.text_input("🔍 Buscar Teorema / Contraejemplo:", placeholder="Ej. T1, Sorgenfrey, Adherencia...")
if busqueda:
    df_filtrado = df_filtrado[
        df_filtrado['teorema'].str.contains(busqueda, case=False, na=False) |
        df_filtrado['nombre_contraejemplo'].str.contains(busqueda, case=False, na=False) |
        df_filtrado['explicacion_detallada'].str.contains(busqueda, case=False, na=False)
    ]

st.sidebar.markdown("---")
st.sidebar.metric(label="Elementos en la base de datos", value=len(df_filtrado))

# --- FORMULARIO EN LA BARRA LATERAL PARA AÑADIR NUEVOS CONTRAEJEMPLOS ---
with st.sidebar.expander("➕ Añadir Nuevo Contraejemplo"):
    with st.form("form_nuevo_contraejemplo"):
        nuevo_tema = st.text_input("Bloque / Materia", placeholder="Ej. Topología - Hoja 3")
        nuevo_teorema = st.text_input("Teorema / Concepto", placeholder="Ej. Teorema de la Función Abierta")
        nueva_hipotesis = st.text_input("Hipótesis que se rompe", placeholder="Ej. Aplicación continua biyectiva")
        nuevo_contra = st.text_input("Nombre del Contraejemplo", placeholder="Ej. Proyección canónica")
        nueva_formal = st.text_area("Definición / Ejemplo Formal", placeholder="Ej. f: X → Y ...")
        nueva_explicacion = st.text_area("Explicación Detallada", placeholder="Explica por qué falla...")
        
        submit_button = st.form_submit_button(label="Guardar en la Base de Datos")
        
        if submit_button:
            if nuevo_teorema and nuevo_contra:
                nuevo_registro = {
                    "tema": nuevo_tema if nuevo_tema else "General",
                    "teorema": nuevo_teorema,
                    "hipotesis_rota": nueva_hipotesis,
                    "nombre_contraejemplo": nuevo_contra,
                    "definicion_formal": nueva_formal,
                    "explicacion_detallada": nueva_explicacion
                }
                # Añadir al DataFrame y guardar en el archivo JSON
                df = pd.concat([df, pd.DataFrame([nuevo_registro])], ignore_index=True)
                save_data(df)
                st.sidebar.success("¡Contraejemplo añadido con éxito!")
                st.rerun()
            else:
                    st.sidebar.error("Por favor, completa al menos el Teorema y el Contraejemplo.")

# --- PANTALLA PRINCIPAL ---
st.subheader(f"Resultados en: {tema_seleccionado} ({len(df_filtrado)} elementos encontrados)")

for index, row in df_filtrado.iterrows():
    with st.expander(f"📌 **{row['teorema']}** — *{row['nombre_contraejemplo']}*"):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown(f"**Materia / Bloque:** `{row['tema']}`")
            st.markdown(f"**Concepto / Hipótesis:** ⚠️ _{row['hipotesis_rota']}_")
            st.markdown(f"**Definición / Ejemplo Formal:**")
            st.code(row['definicion_formal'], language="text")
        with col2:
            st.markdown(f"**Nivel:** Universitario (UPM)")
        
        st.markdown("---")
        st.markdown(f"**💡 Explicación y Demostración Detallada:**\n\n{row['explicacion_detallada']}")
