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
st.markdown("Herramienta interactiva basada rigurosamente en la **Hoja 3 de Topología (Aplicaciones y Continuidad)** y las relaciones de Cálculo.")

# Base de datos integrada con Hoja 3, identidades, discontinuidades y cálculo básico
@st.cache_data
def load_data():
    data = [
        # --- TOPOLOGÍA: HOJA 3 (APLICACIONES Y CONTINUIDAD) ---
        {
            "tema": "Topología - Hoja 3",
            "teorema": "Continuidad de la Aplicación Identidad según la Finura de las Topologías",
            "hipotesis_rota": "La identidad entre espacios con distinta topología no es necesariamente continua en ambos sentidos",
            "nombre_contraejemplo": "Identidad entre Recta Usual y Recta de Sorgenfrey",
            "definicion_formal": "id: (R, tau_u) -> (R, tau_S) frente a id: (R, tau_S) -> (R, tau_u)",
            "explicacion_detallada": "Basado en Hoja 3[cite: 97]:\n- **id: (R, tau_S) -> (R, tau_u)** es **continua globalmente** porque cualquier intervalo abierto usual (a,b) es abierto en Sorgenfrey al poder expresarse como unión de básicos [a + 1/n, b).\n- **id: (R, tau_u) -> (R, tau_S)** **no es continua en ningún punto**, ya que los abiertos básicos [a, b) de Sorgenfrey no contienen ningún entorno abierto usual simétrico (a - epsilon, a + epsilon) alrededor del extremo inferior a."
        },
        {
            "tema": "Topología - Hoja 3",
            "teorema": "Continuidad de la Identidad: Usual frente a Cofinita",
            "hipotesis_rota": "Comparación de continuidad según la densidad y finura de la topología cofinita",
            "nombre_contraejemplo": "id: (R, tau_u) -> (R, tau_cf) y su inversa",
            "definicion_formal": "id: (R, tau_u) -> (R, tau_cf) y id: (R, tau_cf) -> (R, tau_u)",
            "explicacion_detallada": "Basado en Hoja 3[cite: 97]:\n- **id: (R, tau_u) -> (R, tau_cf)** es **continua** porque la topología cofinita es más gruesa que la usual (todo abierto cofinito es abierto en la usual).\n- **id: (R, tau_cf) -> (R, tau_u)** **no es continua**, ya que un abierto usual (como (0,1)) no es abierto en la topología cofinita (su complementario no es finito)."
        },
        {
            "tema": "Topología - Hoja 3",
            "teorema": "Invarianza Topológica: La Continuidad NO Preserva la Acotación",
            "hipotesis_rota": "Una función continua definida en un conjunto acotado puede tener una imagen no acotada",
            "nombre_contraejemplo": "f(x) = 1/x sobre el conjunto acotado (0, 1]",
            "definicion_formal": "f: (0, 1] -> R dada por f(x) = 1/x con la topología usual",
            "explicacion_detallada": "Basado en propiedades generales de continuidad[cite: 97]: El dominio A = (0, 1] es un conjunto acotado en la recta real. La función f(x) = 1/x es continua en todo su dominio. Sin embargo, su imagen es f((0, 1]) = [1, +infty), que es un conjunto **no acotado**. Esto demuestra rigurosamente que la propiedad de acotación **no se conserva** bajo aplicaciones continuas."
        },
        {
            "tema": "Topología - Hoja 3",
            "teorema": "Caracterización de Continuidad en Topología Cofinita",
            "hipotesis_rota": "Una aplicación entre espacios cofinitos no es continua a menos que sus fibras cumplan una condición estricta",
            "nombre_contraejemplo": "Aplicación con Fibras Infinitas",
            "definicion_formal": "f: (X, tau_cf) -> (Y, tau_cf) donde existe y en Y con f^{-1}({y}) infinito",
            "explicacion_detallada": "Basado en Hoja 3 (Ejercicio 6)[cite: 98]: Una aplicación entre espacios con la topología cofinita es continua en x si y solo si la imagen inversa de cada punto exterior, f^{-1}({y}), es un conjunto **finito** para todo y != f(x). Globalmente, f es continua si y solo si es constante o todas sus fibras (excepto quizás una) son finitas[cite: 98]."
        },
        {
            "tema": "Topología - Hoja 3",
            "teorema": "Topología de Rayos a Izquierda (tau_<-)",
            "hipotesis_rota": "La continuidad de funciones monótonas y escalón en topologías no Hausdorff",
            "nombre_contraejemplo": "f(x) = x^2 y g(x) = floor(x) en (R, tau_<-)",
            "definicion_formal": "tau_<- = {emptyset, R} union {(-infty, a) | a en R}",
            "explicacion_detallada": "Basado en Hoja 3 (Ejercicio 7*)[cite: 98, 99]: En esta topología, los abiertos básicos son rayos hacia la izquierda. Toda aplicación continua u: R -> R con esta topología es obligatoriamente **no decreciente**[cite: 99]. Funciones como g(x) = floor(x) o h(x) = ceil(x) exhiben puntos de discontinuidad característicos debido a los saltos y la asimetría de los abiertos."
        },
        {
            "tema": "Topología - Hoja 3",
            "teorema": "Función Característica y Fronteras",
            "hipotesis_rota": "La función característica de un conjunto es continua si y solo si el conjunto es abierto y cerrado a la vez",
            "nombre_contraejemplo": "chi_Q (Función de Dirichlet en R)",
            "definicion_formal": "chi_Q(x) = 1 si x en Q, y 0 si x no en Q",
            "explicacion_detallada": "Basado en Hoja 3 (Ejercicio 4)[cite: 98]: Con la topología discreta en {0,1}, los puntos de discontinuidad de la función característica chi_A coinciden exactamente con la **frontera del conjunto A** (Fr(A)). Para A = Q en la recta usual, Fr(Q) = R, por lo que chi_Q es discontinua en todos los puntos de la recta."
        },

        # --- CÁLCULO: RELACIONES 1, 2 Y 3 ---
        {
            "tema": "Cálculo - Sucesiones",
            "teorema": "Convergencia del Valor Absoluto vs Sucesión Original",
            "hipotesis_rota": "El recíproco no es cierto: La convergencia de {|a_n|} no implica la convergencia de {a_n}",
            "nombre_contraejemplo": "Sucesión Alternada a_n = (-1)^n",
            "definicion_formal": "a_n = (-1)^n",
            "explicacion_detallada": "Basado en Relación 2 de Sucesiones[cite: 92]: El valor absoluto |a_n| = 1 es constante y converge a 1. Sin embargo, la sucesión original a_n oscila perpetuamente entre -1 y 1, por lo que **diverge**[cite: 92]."
        },
        {
            "tema": "Cálculo - Sucesiones",
            "teorema": "Convergencia en Media (Cesàro) y Término General",
            "hipotesis_rota": "Si las sumas medias S_n/n convergen a l, el término general a_n no necesita converger",
            "nombre_contraejemplo": "Sucesión de Medias con a_n = (-1)^n",
            "definicion_formal": "a_n = (-1)^n y S_n = a_1 + ... + a_n",
            "explicacion_detallada": "Basado en Relación 2 de Sucesiones[cite: 93]: Aunque a_n diverge[cite: 92], las sumas parciales S_n oscilan acotadamente, haciendo que el límite en media S_n/n tienda a 0[cite: 93]."
        },
        {
            "tema": "Cálculo - Números Reales",
            "hipotesis_rota": "Simplificación algebraica prohibida por división entre cero",
            "nombre_contraejemplo": "Falacia de x = y que demuestra 2 = 1",
            "definicion_formal": "x = y => x^2 - y^2 = xy - y^2 => (x-y)(x+y) = y(x-y) => x+y = y",
            "explicacion_detallada": "Basado en Relación 1[cite: 89]: El error radica en cancelar el factor (x-y) en ambos lados. Como se partía de x = y, entonces x - y = 0, lo que constituye una **división ilegal entre cero**[cite: 89]."
        },
        {
            "tema": "Cálculo - Series Numéricas",
            "hipotesis_rota": "Condición necesaria de convergencia: que a_n tienda a 0 no garantiza que la serie converja",
            "nombre_contraejemplo": "Serie Armónica",
            "definicion_formal": "sum_{n=1}^infty (1/n)",
            "explicacion_detallada": "Basado en Relación 3[cite: 95]: El término general 1/n tiende a 0 cuando n -> infinity. No obstante, las sumas parciales crecen de forma logarítmica y divergen al infinito."
        }
    ]
    return pd.DataFrame(data)

df = load_data()

if df is not None and not df.empty:
    # --- BARRA LATERAL: NAVEGACIÓN Y FILTROS ---
    st.sidebar.header("🧭 Navegación Académica")
    
    temas_disponibles = ['Todos los Bloques'] + list(df['tema'].unique())
    tema_seleccionado = st.sidebar.selectbox("📂 Selecciona el Bloque (Materia):", temas_disponibles)

    if tema_seleccionado != 'Todos los Bloques':
        df_filtrado = df[df['tema'] == tema_seleccionado]
    else:
        df_filtrado = df

    st.sidebar.markdown("---")
    
    busqueda = st.sidebar.text_input("🔍 Buscar Teorema o Contraejemplo:", placeholder="Ej. Hoja 3, Sorgenfrey, Identidad...")
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
                st.markdown(f"**Nivel:** Universitario (UPM)[cite: 97]")
            
            st.markdown("---")
            st.markdown(f"**💡 Demostración y Explicación Detallada:**\n\n{row['explicacion_detallada']}")
