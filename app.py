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

DB_FILE = "database_contraejemplos.json"

# Base de datos completa, unificada y rigurosa basada en teoría y hojas UPM
DATOS_INICIALES = [
    # ==========================================
    # TOPOLOGÍA - SEPARABILIDAD Y METRIZABILIDAD
    # ==========================================
    {
        "tema": "Topología - Separabilidad y Metrizabilidad",
        "teorema": "Todo espacio metrizable separable es 2AN",
        "hipotesis_rota": "La existencia de un subconjunto denso numerable garantiza base numerable en espacios métricos",
        "nombre_contraejemplo": "Espacio métrico separable (X, τ_d) con A = {a_n} denso numerable",
        "definicion_formal": "ℬ = {B_d(a_n; 1/m) | n, m ∈ ℕ} es base numerable de la topología",
        "explicacion_detallada": "Si (X, τ_d) es metrizable y posee un subconjunto denso numerable A, la familia de bolas con radios racionales centradas en A forma una base numerable de la topología, demostrando que todo espacio métrico separable es 2AN[cite: 114]."
    },
    {
        "tema": "Topología - Separabilidad y Metrizabilidad",
        "teorema": "La Recta de Sorgenfrey NO es Metrizable ni 2AN",
        "hipotesis_rota": "Un espacio separable y 1-anumerable no es necesariamente metrizable",
        "nombre_contraejemplo": "Recta de Sorgenfrey (ℝ, τ_S)",
        "definicion_formal": "ℬ_S = {[a, b) | a < b} como base de abiertos",
        "explicacion_detallada": "Las bases locales ℬ(x) = {[x, x + 1/n)} son numerables (1AN) y ℚ es denso (separable)[cite: 21, 40, 44]. Sin embargo, se demuestra por reducción al absurdo que si fuera metrizable, implicaría que es 2AN, lo cual es falso[cite: 44, 118]."
    },
    # ==========================================
    # TOPOLOGÍA - AXIOMAS DE SEPARACIÓN (T_i)
    # ==========================================
    {
        "tema": "Topología - Axiomas de Separación (T_i)",
        "teorema": "Axioma T1 frente a Hausdorff (T2)",
        "hipotesis_rota": "Un espacio T1 no es necesariamente Hausdorff (T2) ni metrizable",
        "nombre_contraejemplo": "Topología Cofinita en un conjunto infinito (ℝ, τ_{cf})",
        "definicion_formal": "τ_{cf} = {U ⊂ ℝ | ℝ \\ U es finito} ∪ {∅}",
        "explicacion_detallada": "Los cerrados propios son los conjuntos finitos[cite: 7]. Dados x ≠ y, se pueden aislar de forma unilateral mediante complementarios finitos (cumple T1). No obstante, dos abiertos no vacíos cualesquiera se intersecan, por lo que no es Hausdorff (T2) ni metrizable[cite: 31, 34, 47, 113]."
    },
    {
        "tema": "Topología - Axiomas de Separación (T_i)",
        "teorema": "Espacios Normales y T4 en Métricas",
        "hipotesis_rota": "Todo espacio métrico es un espacio normal y cumple la propiedad de separación T4",
        "nombre_contraejemplo": "Espacios métricos (X, τ_d)",
        "definicion_formal": "Separación de cerrados disjuntos mediante entornos abiertos disjuntos",
        "explicacion_detallada": "Se demuestra formalmente utilizando la distancia a subconjuntos que todo espacio metrizable es un espacio T4, garantizando que cualesquiera dos cerrados disjuntos pueden encerrarse en abiertos disjuntos[cite: 113, 119]."
    },
    # ==========================================
    # TOPOLOGÍA - TEORÍA DE PUNTOS Y OPERACIONES
    # ==========================================
    {
        "tema": "Topología - Hoja 2 (Puntos y Operaciones)",
        "teorema": "Caracterización de Punto Interior y Negación",
        "hipotesis_rota": "Un punto no es interior si cualquier entorno básico intercepta al complementario",
        "nombre_contraejemplo": "Punto frontera o exterior respecto al interior de A",
        "definicion_formal": "x ∉ Int(A) ⟺ Para todo entorno U^x ∈ 𝒩(x), se tiene U^x ⊄ A",
        "explicacion_detallada": "No es necesario que los entornos sean abiertos para definir el interior; basta con que exista algún entorno completo contenido en A. Su negación implica que todo entorno de x se sale del conjunto A[cite: 106]."
    },
    {
        "tema": "Topología - Hoja 2 (Puntos y Operaciones)",
        "teorema": "Caracterización de Punto Adherente y Clausura",
        "hipotesis_rota": "Todo entorno de un punto adherente debe cortar de forma no vacía al conjunto",
        "nombre_contraejemplo": "Puntos en la adherencia Cl(A) frente a puntos exteriores",
        "definicion_formal": "x ∈ Cl(A) ⟺ Para todo entorno U^x ∈ 𝒩(x), se cumple U^x ∩ A ≠ ∅",
        "explicacion_detallada": "Un punto pertenece a la adherencia de A si ningún entorno suyo logra 'separarlo' de A sin tocarlo[cite: 106]. Su negación significa que existe un entorno disjunto de A (punto exterior)[cite: 106, 117]."
    },
    {
        "tema": "Topología - Hoja 2 (Puntos y Operaciones)",
        "teorema": "Puntos Aislados frente a Puntos de Acumulación",
        "hipotesis_rota": "Distinción entre aislamiento puntual e acumulación por entornos perforados",
        "nombre_contraejemplo": "Ais(A) frente a A' (Derivado)",
        "definicion_formal": "x ∈ Ais(A) ⟺ ∃U^x t.q. U^x ∩ A = {x}  //  x ∈ A' ⟺ ∀U^x, (U^x \\ {x}) ∩ A ≠ ∅",
        "explicacion_detallada": "Un punto aislado pertenece a A pero puede separarse solitario en un entorno. Un punto de acumulación exige que cualquier entorno perforado contenga puntos de A[cite: 106, 108]."
    },
    # ==========================================
    # CÁLCULO - REALES Y SUCESIONES
    # ==========================================
    {
        "tema": "Cálculo - Rel. 1 (Reales)",
        "teorema": "Falacia en Simplificación Algebraica",
        "hipotesis_rota": "Cancelar factores algebraicos nulos (división entre cero)",
        "nombre_contraejemplo": "Demostración falsa de 2 = 1",
        "definicion_formal": "Si x = y, entonces (x-y)(x+y) = y(x-y) ⇒ x+y = y ⇒ 2 = 1",
        "explicacion_detallada": "El error radica en dividir entre (x-y). Como se asumió x = y, entonces x - y = 0, lo cual constituye una división ilegal por cero[cite: 89]."
    },
    {
        "tema": "Cálculo - Rel. 2 (Sucesiones)",
        "teorema": "Convergencia del Valor Absoluto",
        "hipotesis_rota": "El recíproco no es cierto: |a_n| convergente no implica que a_n sea convergente",
        "nombre_contraejemplo": "Sucesión alternada a_n = (-1)^n",
        "definicion_formal": "a_n = (-1)^n",
        "explicacion_detallada": "El valor absoluto |(-1)^n| = 1 converge a 1. Sin embargo, la sucesión original oscila perpetuamente entre -1 y 1, por lo que diverge[cite: 92]."
    }
]

def load_data():
    df_inicial = pd.DataFrame(DATOS_INICIALES)
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            try:
                data_cargada = json.load(f)
                df_guardado = pd.DataFrame(data_cargada)
                # Unimos los iniciales con los que el usuario haya guardado para no perder nada
                df_total = pd.concat([df_inicial, df_guardado]).drop_duplicates(subset=["teorema", "nombre_contraejemplo"]).reset_index(drop=True)
                return df_total
            except json.JSONDecodeError:
                return df_inicial
    else:
        save_data(df_inicial)
        return df_inicial

def save_data(df):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(df.to_dict(orient="records"), f, ensure_ascii=False, indent=4)

df = load_data()

st.title("📐 Explorador Dinámico: Cálculo y Topología UPM")
st.markdown("Catálogo completo con teoría de puntos, separabilidad, axiomas T_i, metrizabilidad y formulario de adición.")

# --- BARRA LATERAL: NAVEGACIÓN Y FILTROS ---
st.sidebar.header("🧭 Navegación y Filtros")

temas_disponibles = ['Todos los Bloques'] + list(df['tema'].unique())
tema_seleccionado = st.sidebar.selectbox("📂 Selecciona el Bloque:", temas_disponibles)

if tema_seleccionado != 'Todos los Bloques':
    df_filtrado = df[df['tema'] == tema_seleccionado]
else:
    df_filtrado = df

busqueda = st.sidebar.text_input("🔍 Buscar Teorema / Contraejemplo:", placeholder="Ej. Separabilidad, T1, Interior...")
if busqueda:
    df_filtrado = df_filtrado[
        df_filtrado['teorema'].str.contains(busqueda, case=False, na=False) |
        df_filtrado['nombre_contraejemplo'].str.contains(busqueda, case=False, na=False) |
        df_filtrado['explicacion_detallada'].str.contains(busqueda, case=False, na=False)
    ]

st.sidebar.markdown("---")
st.sidebar.metric(label="Elementos totales en la app", value=len(df_filtrado))

# --- FORMULARIO PARA AÑADIR NUEVOS CONTRAEJEMPLOS ---
with st.sidebar.expander("➕ Añadir Nuevo Contraejemplo"):
    with st.form("form_nuevo_contraejemplo"):
        nuevo_tema = st.text_input("Bloque / Materia", placeholder="Ej. Topología - Hoja 3")
        nuevo_teorema = st.text_input("Teorema / Concepto", placeholder="Ej. Teorema de Baire")
        nueva_hipotesis = st.text_input("Hipótesis que se rompe", placeholder="Ej. Espacio métrico completo")
        nuevo_contra = st.text_input("Nombre del Contraejemplo", placeholder="Ej. Q en la métrica usual")
        nueva_formal = st.text_area("Definición / Ejemplo Formal", placeholder="Ej. Int(ℚ) = ∅...")
        nueva_explicacion = st.text_area("Explicación Detallada", placeholder="Explica la demostración...")
        
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
                df = pd.concat([df, pd.DataFrame([nuevo_registro])], ignore_index=True)
                save_data(df)
                st.sidebar.success("¡Contraejemplo añadido con éxito!")
                st.rerun()
            else:
                st.sidebar.error("Completa al menos el Teorema y el Contraejemplo.")

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
