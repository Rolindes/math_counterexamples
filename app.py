import streamlit as st
import pandas as pd

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

st.title("📐 Explorador de Contraejemplos Matemáticos Universitarios")
st.markdown("La herramienta definitiva para entender por qué las hipótesis de los teoremas no se pueden relajar.")

# Base de datos interna integrada directamente en Python (sin archivos externos que den fallos)
@st.cache_data
def load_data():
    data = [
        {
            "tema": "Análisis Real",
            "teorema": "Teorema del Valor Intermedio (Bolzano)",
            "hipotesis_rota": "La función debe ser continua en todo el intervalo cerrado",
            "nombre_contraejemplo": "Función Escalón (Parte Entera)",
            "definicion_formal": "f(x) = floor(x) en [0, 2]",
            "explicacion_detallada": "El teorema afirma que si una función es continua en [a, b], toma todos los valores entre f(a) y f(b). En este contraejemplo, la función salta de 0 a 1 en x = 1, sin tomar valores intermedios como 0.5."
        },
        {
            "tema": "Topología General",
            "teorema": "Teorema de Heine-Borel (Compacidad)",
            "hipotesis_rota": "El conjunto debe ser cerrado en R^n",
            "nombre_contraejemplo": "Intervalo Abierto Acotado",
            "definicion_formal": "A = (0, 1) con la métrica usual",
            "explicacion_detallada": "Aunque está acotado, no es cerrado al faltarle sus puntos frontera (0 y 1), impidiendo extraer un subrecubrimiento finito de recubrimientos abiertos."
        },
        {
            "tema": "Análisis Real",
            "teorema": "Diferenciabilidad Implica Continuidad",
            "hipotesis_rota": "El recíproco no es cierto: Continuidad no garantiza derivabilidad",
            "nombre_contraejemplo": "Función Valor Absoluto en el Origen",
            "definicion_formal": "f(x) = |x| en x = 0",
            "explicacion_detallada": "Es continua en todo su dominio pero presenta un pico o esquina en x = 0, haciendo que los límites laterales de la derivada no coincidan y esta no exista."
        },
        {
            "tema": "Topología General",
            "teorema": "Conexidad y Funciones Continuas",
            "hipotesis_rota": "La imagen continua de un conjunto conexo es conexa",
            "nombre_contraejemplo": "Espacio Disconexo por Puntos Aislados",
            "definicion_formal": "X = [0, 1] u [2, 3] en R",
            "explicacion_detallada": "El espacio consta de dos componentes disjuntas cerradas. Ninguna función continua puede saltar de un componente a otro sin violar las propiedades topológicas del codominio."
        },
        {
            "tema": "Análisis Real",
            "teorema": "Teorema de Rolle",
            "hipotesis_rota": "La función debe ser derivable en el intervalo abierto (a, b)",
            "nombre_contraejemplo": "Función con Pico Anguloso",
            "definicion_formal": "f(x) = 1 - |x| en [-1, 1]",
            "explicacion_detallada": "Aunque f(-1) = f(1) = 0 y es continua, no existe ningún punto c en el intervalo abierto donde la derivada sea cero debido al pico anguloso en x = 0."
        },
        {
            "tema": "Topología General",
            "teorema": "Espacios Métricos Completos",
            "hipotesis_rota": "El espacio métrico debe ser completo para asegurar convergencia de Cauchy",
            "nombre_contraejemplo": "Los Números Racionales con la Métrica Usual",
            "definicion_formal": "Espacio Q con la sucesión que aproxima a raíz de 2",
            "explicacion_detallada": "La sucesión racional que aproxima a raíz de 2 es de Cauchy, pero no converge dentro de Q porque su límite es irracional, demostrando que Q no es completo."
        },
        {
            "tema": "Topología General",
            "teorema": "Teorema de Urysohn / Metrizabilidad",
            "hipotesis_rota": "El espacio debe ser regular y base numerable (2-anumerable)",
            "nombre_contraejemplo": "Espacio de Sorgenfrey (Recta de Sorgenfrey)",
            "definicion_formal": "R con la base de intervalos [a, b)",
            "explicacion_detallada": "Este espacio es separable y 1-anumerable, pero no es metrizable ni 2-anumerable, demostrando que las condiciones de contabilidad y separación son finas y distintas."
        },
        {
            "tema": "Topología General",
            "teorema": "Axiomas de Contabilidad",
            "hipotesis_rota": "Todo espacio 2-anumerable es 1-anumerable",
            "nombre_contraejemplo": "Espacio Discreto No Numerable",
            "definicion_formal": "Un conjunto no numerable X con la topología discreta",
            "explicacion_detallada": "Aunque es un espacio con base numerable en puntos individuales para la propiedad 1-anumerable, al ser no numerable no posee una base numerable global, fallando en ser 2-anumerable."
        },
        {
            "tema": "Topología General",
            "teorema": "Propiedad de Separabilidad",
            "hipotesis_rota": "Todo subespacio de un espacio separable es separable",
            "nombre_contraejemplo": "Espacio de Niemytzki (Plano de Moore)",
            "definicion_formal": "Subespacio del semiplano superior con la base de discos tangentes al eje x",
            "explicacion_detallada": "Demuestra que existen espacios perfectamente normales y separables que contienen subespacios no separables, rompiendo la herencia directa de la separabilidad."
        },
        {
            "tema": "Topología General",
            "teorema": "Invarianza Topológica por Homeomorfismos",
            "hipotesis_rota": "Toda propiedad métrica o algebraica se conserva por homeomorfismos arbitrarios",
            "nombre_contraejemplo": "Intervalo Abierto vs Recta Real",
            "definicion_formal": "El intervalo (0, 1) homeomorfo a R mediante f(x) = tan(pi*(x - 1/2))",
            "explicacion_detallada": "Aunque son homeomorfos como espacios topológicos (conservan abiertos y continuidad), (0, 1) es acotado métricamente y R no lo es, mostrando que la acotación no es un invariante topológico puro."
        },
        {
            "tema": "Topología General",
            "teorema": "Conexidad vs Conexidad por Caminos",
            "hipotesis_rota": "Todo espacio conexo por caminos es conexo, pero el recíproco falla",
            "nombre_contraejemplo": "El Seno del Topólogo",
            "definicion_formal": "Gráfica de sin(1/x) para x en (0, 1] unida con el segmento en el eje y",
            "explicacion_detallada": "El conjunto es conexo porque su cierre topológico no puede separarse en dos abiertos disjuntos, pero no es conexo por caminos ya que ninguna curva continua une el origen con la oscilación infinita."
        },
        {
            "tema": "Topología General",
            "teorema": "Compactitud en Espacios Métricos",
            "hipotesis_rota": "Un espacio métrico es compacto si y solo si es completo y totalmente acotado",
            "nombre_contraejemplo": "La Recta Real R con la Métrica Usual",
            "definicion_formal": "El espacio R completo pero no totalmente acotado",
            "explicacion_detallada": "R es un espacio métrico completo, pero no se puede recubrir por una cantidad finita de bolas de radio menor a 1, fallando la compacidad."
        },
        {
            "tema": "Análisis Real",
            "teorema": "Teorema de Bolzano-Weierstrass",
            "hipotesis_rota": "Todo conjunto acotado en R^n posee puntos de acumulación",
            "nombre_contraejemplo": "Espacio Métrico Discreto Infinito",
            "definicion_formal": "X = N con la métrica discreta d(x,y) = 1 si x!=y",
            "explicacion_detallada": "El conjunto de los números naturales está acotado en este espacio métrico (con diámetro 1), pero carece totalmente de puntos de acumulación porque cada punto está aislado."
        },
        {
            "tema": "Análisis Real",
            "teorema": "Teorema de Heine-Borel (Dimensión Infinita)",
            "hipotesis_rota": "La compacidad equivale a ser cerrado y acotado en espacios de dimensión infinita",
            "nombre_contraejemplo": "Espacio de Hilbert l2 o C[0, 1] con la norma infinito",
            "definicion_formal": "La bola unitaria cerrada B = {f en C[0,1] : ||f|| <= 1}",
            "explicacion_detallada": "En espacios normados de dimensión infinita, la bola unitaria cerrada es cerrada y acotada pero no es compacta, ya que existen sucesiones sin subsucesiones convergentes (falla el criterio de Riesz)."
        },
        {
            "tema": "Álgebra Abstracta",
            "teorema": "Teorema de Lagrange en Grupos",
            "hipotesis_rota": "El suborden debe dividir estrictamente al orden del grupo",
            "nombre_contraejemplo": "Subgrupo vs Grupo No Abeliano",
            "definicion_formal": "Grupo S3 y su subgrupo de orden 2",
            "explicacion_detallada": "El teorema asegura que el orden del subgrupo divide al grupo, pero se deben cumplir condiciones de normalidad para cocientes y estructuras directas."
        }
    ]
    return pd.DataFrame(data)

df = load_data()

if df is not None and not df.empty:
    # --- BARRA LATERAL: SEPARACIÓN POR BLOQUES Y FILTROS ---
    st.sidebar.header("🧭 Navegación Académica")
    
    temas_disponibles = ['Todos los Bloques'] + list(df['tema'].unique())
    tema_seleccionado = st.sidebar.selectbox("📂 Selecciona el Bloque (Materia):", temas_disponibles)

    if tema_seleccionado != 'Todos los Bloques':
        df_filtrado = df[df['tema'] == tema_seleccionado]
    else:
        df_filtrado = df

    st.sidebar.markdown("---")
    
    busqueda = st.sidebar.text_input("🔍 Buscar Teorema o Contraejemplo:", placeholder="Ej. Bolzano, compacidad, Sorgenfrey...")
    if busqueda:
        df_filtrado = df_filtrado[
            df_filtrado['teorema'].str.contains(busqueda, case=False, na=False) |
            df_filtrado['nombre_contraejemplo'].str.contains(busqueda, case=False, na=False) |
            df_filtrado['explicacion_detallada'].str.contains(busqueda, case=False, na=False)
        ]

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
            st.markdown("---")
            st.markdown(f"**💡 Explicación Detallada y Demostración:**\n\n{row['explicacion_detallada']}")
else:
    st.warning("⚠️ No se pudieron cargar los datos. Asegúrate de que el archivo 'contraejemplos.csv' está correctamente subido al repositorio.")
