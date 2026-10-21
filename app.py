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
st.markdown("Herramienta interactiva avanzada basada en Topología General y Análisis Real (UPM).")

# Base de datos interna con demostraciones detalladas extraídas de la teoría
@st.cache_data
def load_data():
    data = [
        {
            "tema": "Topología General",
            "teorema": "Metrizabilidad y Axiomas de Numerabilidad",
            "hipotesis_rota": "Un espacio separable y 1-anumerable no es necesariamente metrizable ni 2-anumerable",
            "nombre_contraejemplo": "Recta de Sorgenfrey (R, tau_Sor)",
            "definicion_formal": "R dotada de la base de abiertos B_Sor = {[a, b) | a < b}",
            "explicacion_detallada": "Demostración detallada: La familia de entornos básicos B(x) = {[x, x + 1/n) | n en N} es numerable y demuestra que el espacio cumple el primer axioma de numerabilidad (1AN)[cite: 26, 40]. Asimismo, Q es denso, por lo que es separable. Sin embargo, no es 2-anumerable (2AN) porque cualquier base de abiertos debe contener para cada real a un abierto básico cuyo ínfimo sea a, lo que impide que sea numerable[cite: 44]. Dado que todo espacio métrico separable debe ser 2-anumerable (Proposición 2.8.5), se concluye rigurosamente por reducción al absurdo que la recta de Sorgenfrey **no es metrizable**[cite: 34, 44]."
        },
        {
            "tema": "Topología General",
            "teorema": "Axiomas de Separación (Hausdorff vs T1)",
            "hipotesis_rota": "Un espacio T1 no es necesariamente Hausdorff (T2) ni metrizable",
            "nombre_contraejemplo": "Topología Cofinita en un conjunto infinito (R, tau_cf)",
            "definicion_formal": "tau_cf = {U subset R | R \\ U es finito} unida con el vacío",
            "explicacion_detallada": "Demostración detallada: Los cerrados propios de esta topología son exactamente los conjuntos finitos[cite: 7]. Dados dos puntos distintos x != y, podemos encontrar abiertos cuyos complementarios sean finitos que aíslan cada punto de manera unilateral (por lo que el espacio es T1). No obstante, dados dos abiertos no vacíos U y V, sus complementarios son finitos, lo que implica que su intersección R \\ (R\\U union R\\V) no puede ser vacía (se intersecan siempre en un conjunto infinito). Por tanto, es imposible separarlos mediante entornos abiertos disjuntos, demostrando que **no es Hausdorff (T2)**[cite: 31, 47]. Al ser Hausdorff una condición necesaria de metrizabilidad, la topología cofinita no es metrizable[cite: 34, 47]."
        },
        {
            "tema": "Topología General",
            "teorema": "Conexidad y Conexidad por Caminos",
            "hipotesis_rota": "Todo espacio conexo por caminos es conexo, pero el recíproco falla",
            "nombre_contraejemplo": "El Seno del Topólogo",
            "definicion_formal": "A = {(x, sin(1/x)) | x en (0, 1]} unida con el segmento vertical {(0, y) | y en [-1, 1]}",
            "explicacion_detallada": "Demostración detallada: El conjunto A es conexo por ser la adherencia en R^2 de la gráfica de una función continua (que es conexa por caminos). Sin embargo, **no es conexo por caminos** porque ninguna función continua gamma: [0, 1] -> R^2 puede unir el origen (0,0) con un punto de la curva oscilante sin que las oscilaciones infinitas rompan la continuidad en la trayectoria límite."
        },
        {
            "tema": "Topología General",
            "teorema": "Axioma de Separación Hausdorff (T2)",
            "hipotesis_rota": "Espacios con bases locales simétricas que fallan en separar puntos globales",
            "nombre_contraejemplo": "La Recta de Dos Orígenes",
            "definicion_formal": "X = Rsqcup{*}, con base que duplica el punto 0 añadiendo entornos abiertos con dos orígenes",
            "explicacion_detallada": "Demostración detallada: Consideremos los dos orígenes 0 y *. Cualquier entorno abierto básico de 0 contiene un intervalo abierto estándar de la forma (-epsilon, epsilon) sin el punto, el cual comparte exactamente los mismos puntos que el entorno correspondiente de *. Por consiguiente, es imposible encontrar entornos abiertos disjuntos que separen 0 de *. El espacio **no es Hausdorff**, y por tanto **no es metrizable**[cite: 34, 42, 45]."
        },
        {
            "tema": "Topología General",
            "teorema": "Axiomas de Numerabilidad (1AN vs 2AN)",
            "hipotesis_rota": "Todo espacio 1-anumerable (1AN) no es necesariamente 2-anumerable (2AN)",
            "nombre_contraejemplo": "Espacio Discreto No Numerable (X, tau_dis)",
            "definicion_formal": "X es un conjunto infinito no numerable dotado de tau_dis = P(X)",
            "explicacion_detallada": "Demostración detallada: Para cada punto x en X, la familia de singletons B(x) es una base de entornos numerable trivial, por lo que cumple 1AN[cite: 20, 26]. No obstante, cualquier base de abiertos B de la topología discreta debe contener obligatoriamente a todos los subconjuntos unipuntuales {{x} | x en X}. Al ser X un conjunto no numerable, la base B es necesariamente no numerable, violando el segundo axioma de numerabilidad (2AN)[cite: 23, 24]."
        },
        {
            "tema": "Topología General",
            "teorema": "Invariantes Topológicos y Métricas",
            "hipotesis_rota": "Las propiedades métricas (como la acotación) se conservan bajo homeomorfismos",
            "nombre_contraejemplo": "Métrica Euclidiana vs Métrica Acotada Asociada en R^n",
            "definicion_formal": "d_2(x,y) y su contraparte acotada d_bar(x,y) = min(1, d_2(x,y))",
            "explicacion_detallada": "Demostración detallada: Mediante la caracterización de equivalencia topológica, ambas métricas inducen exactamente la misma topología en R^n (tau_d2 = tau_d_bar)[cite: 34, 35]. Sin embargo, todo el espacio R^n con d_bar es un espacio métrico acotado (con diámetro menor o igual a 1), mientras que con d_2 es claramente no acotado[cite: 34, 35]. Esto demuestra rigurosamente que **la acotación NO es una propiedad topológica**[cite: 34, 35]."
        },
        {
            "tema": "Topología General",
            "teorema": "Continuidad de la Aplicación Identidad entre Topologías",
            "hipotesis_rota": "La identidad es continua independientemente de la finura relativa de las topologías",
            "nombre_contraejemplo": "id: (R, tau_Sor) -> (R, tau_u) frente a id': (R, tau_u) -> (R, tau_Sor)",
            "definicion_formal": "Aplicación identidad evaluada entre la recta de Sorgenfrey y la recta usual",
            "explicacion_detallada": "Demostración detallada: La aplicación id: (R, tau_Sor) -> (R, tau_u) es **continua** porque cualquier intervalo abierto usual (a, b) es abierto en Sorgenfrey al poder expresarse como unión numerable de abiertos básicos [a + 1/n, b)[cite: 25, 28]. En dirección opuesta, id': (R, tau_u) -> (R, tau_Sor) **no es continua en ningún punto**, ya que los abiertos básicos [a, b) de Sorgenfrey no contienen ningún entorno abierto usual simétrico (a - epsilon, a + epsilon) alrededor del extremo inferior a[cite: 25, 28]."
        },
        {
            "tema": "Análisis Real",
            "teorema": "Teorema del Valor Intermedio (Bolzano)",
            "hipotesis_rota": "La función debe ser continua en todo el intervalo cerrado [a, b]",
            "nombre_contraejemplo": "Función Escalón (Parte Entera)",
            "definicion_formal": "f(x) = floor(x) en el intervalo [0, 2]",
            "explicacion_detallada": "Demostración detallada: El teorema exige continuidad completa en [a, b]. En este contraejemplo, la función presenta un salto brusco de 0 a 1 en x = 1. Debido a esta discontinuidad de salto, la función jamás toma valores decimales intermedios como 0.5, invalidando la conclusión del teorema."
        },
        {
            "tema": "Análisis Real",
            "teorema": "Diferenciabilidad Implica Continuidad",
            "hipotesis_rota": "El recíproco no es cierto: la continuidad no garantiza la existencia de derivada",
            "nombre_contraejemplo": "Función Valor Absoluto en el Origen",
            "definicion_formal": "f(x) = |x| evaluada en x = 0",
            "explicacion_detallada": "Demostración detallada: La función es continua en todo su dominio real, incluido x = 0. No obstante, al calcular los límites laterales de la tasa de variación media en el origen, obtenemos -1 por la izquierda y +1 por la derecha. Como los límites laterales no coinciden, la derivada no existe debido al punto anguloso."
        },
        {
            "tema": "Álgebra Abstracta",
            "teorema": "Teorema de Lagrange en Grupos",
            "hipotesis_rota": "El suborden debe dividir al orden del grupo y cumplirse condiciones estructurales",
            "nombre_contraejemplo": "Grupo Simétrico S3 y su subgrupo de orden 2",
            "definicion_formal": "S3 de orden 6 con un subgrupo H de orden 2",
            "explicacion_detallada": "Demostración detallada: El teorema de Lagrange establece que el orden de cualquier subgrupo divide al orden del grupo principal (2 divide a 6). Sin embargo, este contraejemplo estructural ilustra que el recíproco no es general: no todo divisor del orden del grupo garantiza la existencia de un subgrupo normal de dicho orden, fallando en estructuras no abelianas."
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
    
    busqueda = st.sidebar.text_input("🔍 Buscar Teorema o Contraejemplo:", placeholder="Ej. Sorgenfrey, Hausdorff, Bolzano...")
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
                st.markdown(f"**Nivel:** Universitario (UPM)")
            
            st.markdown("---")
            st.markdown(f"**💡 Demostración y Explicación Detallada:**\n\n{row['explicacion_detallada']}")
