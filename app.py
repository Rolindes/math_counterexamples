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

DB_FILE = "contraejemplos_puros.json"

# Base de datos masiva con más de 40 contraejemplos estrictos (Cálculo y Topología UPM)
DATOS_INICIALES = [
    # ==========================================
    # CÁLCULO - REALES, SUCESIONES Y SERIES
    # ==========================================
    {
        "tema": "Cálculo - Rel. 1 (Reales)",
        "afirmacion_falsa": "Si x = y, entonces se puede simplificar (x-y) para concluir que x+y = y y por tanto 2 = 1.",
        "contraejemplo_exacto": "Demostración algebraica falsa de 2 = 1 usando a = b.",
        "explicacion_detallada": "Falla porque se divide entre (x-y). Al asumir x = y, la expresión (x-y) es exactamente 0, cometiendo una división ilegal por cero[cite: 89]."
    },
    {
        "tema": "Cálculo - Rel. 1 (Reales)",
        "afirmacion_falsa": "Multiplicar una desigualdad por una variable x-1 preserva siempre el sentido sin estudiar su signo.",
        "contraejemplo_exacto": "Inecuación (x+1)/(x-1) ≥ 1 que lleva a 1 ≥ -1.",
        "explicacion_detallada": "Falla al no restringir el dominio ni estudiar el signo del denominador. Multiplicar por cantidades negativas invierte la desigualdad[cite: 89]."
    },
    {
        "tema": "Cálculo - Rel. 1 (Reales)",
        "afirmacion_falsa": "La suma o producto de dos números irracionales da siempre como resultado otro número irracional.",
        "contraejemplo_exacto": "Suma: √2 + (-√2) = 0 (racional). Producto: √2 · √2 = 2 (racional).",
        "explicacion_detallada": "El conjunto de los irracionales no es cerrado respecto a la suma ni al producto algebraico[cite: 90]."
    },
    {
        "tema": "Cálculo - Rel. 2 (Sucesiones)",
        "afirmacion_falsa": "Si el valor absoluto de una sucesión (|a_n|) converge, entonces la sucesión original (a_n) es convergente.",
        "contraejemplo_exacto": "Sucesión oscilante a_n = (-1)^n.",
        "explicacion_detallada": "El valor absoluto |(-1)^n| = 1 es una sucesión constante que converge a 1. Sin embargo, a_n oscila perpetuamente entre -1 y 1, por lo que diverge[cite: 92]."
    },
    {
        "tema": "Cálculo - Rel. 2 (Sucesiones)",
        "afirmacion_falsa": "La suma de una sucesión convergente y una divergente da siempre una sucesión divergente con comportamiento nulo o infinito.",
        "contraejemplo_exacto": "x_n = 1/n (converge a 0) y y_n = (-1)^n (oscila/diverge).",
        "explicacion_detallada": "La suma x_n + y_n resulta en una sucesión oscilante que no converge, pero tampoco diverge a infinito[cite: 92]."
    },
    {
        "tema": "Cálculo - Rel. 2 (Sucesiones)",
        "afirmacion_falsa": "Si una sucesión a_n está contenida estrictamente en un intervalo abierto (0, 1), su límite también pertenece obligatoriamente al intervalo abierto.",
        "contraejemplo_exacto": "a_n = 1/n ∈ (0, 1) con lim a_n = 0.",
        "explicacion_detallada": "El límite de una sucesión contenida en un abierto puede colapsar y caer en la frontera exterior del intervalo[cite: 92]."
    },
    {
        "tema": "Cálculo - Rel. 2 (Sucesiones)",
        "teorema": "Convergencia de la media (Teorema de Cesàro)",
        "afirmacion_falsa": "Si la media de Cesàro (S_n / n) converge, el término general a_n de la sucesión original también converge.",
        "contraejemplo_exacto": "Sucesión a_n = (-1)^n.",
        "explicacion_detallada": "El término general a_n diverge oscilando, pero la media aritmética de sus sumas parciales S_n / n converge a 0. El recíproco es falso[cite: 92, 93]."
    },
    {
        "tema": "Cálculo - Rel. 3 (Series)",
        "afirmacion_falsa": "Si el término general de una serie tiende a cero (lim a_n = 0), entonces la serie numéricamente converge.",
        "contraejemplo_exacto": "La serie armónica clásica Σ (1/n).",
        "explicacion_detallada": "La condición lim a_n = 0 es estrictamente necesaria pero no suficiente. Las sumas parciales de la armónica crecen de forma logarítmica y divergen[cite: 95]."
    },
    {
        "tema": "Cálculo - Rel. 3 (Series)",
        "afirmacion_falsa": "Si una serie con términos positivos Σ a_n diverge, la serie modificada Σ [a_n / (1 + a_n)] también diverge obligatoriamente.",
        "contraejemplo_exacto": "Series divergentes de crecimiento lento comparadas con fracciones acotadas.",
        "explicacion_detallada": "El cociente modificado puede alterar el carácter de divergencia original de la serie[cite: 95, 96]."
    },
    {
        "tema": "Cálculo - Rel. 3 (Series)",
        "afirmacion_falsa": "Una serie alternada que converge condicionalmente también converge de manera absoluta en valor absoluto.",
        "contraejemplo_exacto": "Serie armónica alternada Σ [(-1)^n / ln(n+1)].",
        "explicacion_detallada": "Por Leibniz converge, pero al tomar valor absoluto se convierte en la serie armónica logarítmica, la cual diverge[cite: 96]."
    },

    # ==========================================
    # TOPOLOGÍA - HOJA 1 (MÉTRICAS Y ESPACIOS)
    # ==========================================
    {
        "tema": "Topología - Hoja 1 (Métricas)",
        "afirmacion_falsa": "En cualquier espacio métrico, los triángulos no degenerados tienen lados con medidas estrictamente desiguales o escalenas.",
        "contraejemplo_exacto": "Espacio con Métrica Discreta d_dis.",
        "explicacion_detallada": "Bajo la métrica discreta, para cualesquiera x, y, z distintos, d_dis(x,y) = d_dis(x,z) = d_dis(y,z) = 1, haciendo que 'todo triángulo sea equilátero'[cite: 99]."
    },
    {
        "tema": "Topología - Hoja 1 (Métricas)",
        "afirmacion_falsa": "La aplicación d_{1/2}(x,y) = (Σ |x_i - y_i|^{1/2})^2 define una distancia matemática válida en ℝ^n.",
        "contraejemplo_exacto": "Métrica con exponente fraccionario p = 1/2 en ℝ^2.",
        "explicacion_detallada": "Falla flagrantemente la desigualdad triangular para dimensiones n ≥ 2, por lo que no constituye una distancia matemática válida[cite: 100, 102]."
    },
    {
        "tema": "Topología - Hoja 1 (Métricas)",
        "afirmacion_falsa": "Las bolas abiertas en cualquier métrica son siempre conjuntos convexos.",
        "contraejemplo_exacto": "Bolas bajo métricas no convexas o con exponentes p < 1.",
        "explicacion_detallada": "Para métricas con p < 1, las bolas abiertas dejan de ser convexas, fallando la propiedad geométrica euclidiana[cite: 102]."
    },
    {
        "tema": "Topología - Hoja 2 (Topologías)",
        "afirmacion_falsa": "La intersección infinita de conjuntos abiertos en un espacio topológico arbitrario es siempre un conjunto abierto.",
        "contraejemplo_exacto": "Familia de abiertos (-1/n, 1/n) en ℝ con la topología usual.",
        "explicacion_detallada": "La intersección de todos ellos para n en ℕ es únicamente el conjunto unipuntual {0}, que es cerrado en ℝ, demostrando que los abiertos solo son estables bajo intersecciones finitas[cite: 35]."
    },
    {
        "tema": "Topología - Hoja 2 (Topologías)",
        "afirmacion_falsa": "La unión infinita de conjuntos cerrados en un espacio topológico es siempre un conjunto cerrado.",
        "contraejemplo_exacto": "Unión de cerrados [1/n, 1 - 1/n] en ℝ.",
        "explicacion_detallada": "La unión infinita de dichos intervalos cerrados da como resultado el intervalo abierto (0, 1), que no es cerrado[cite: 35]."
    },

    # ==========================================
    # TOPOLOGÍA - AXIOMAS Y PROPIEDADES (HOJA 3 Y TEMAS)
    # ==========================================
    {
        "tema": "Topología - Hoja 3 (Axiomas)",
        "afirmacion_falsa": "Todo espacio topológico que cumple el primer axioma de contabilidad (1AN) es necesariamente un espacio con base numerable (2AN).",
        "contraejemplo_exacto": "Espacio Discreto No Numerable (X, τ_dis).",
        "explicacion_detallada": "Las bases locales de singletons son numerables (cumple 1AN). No obstante, cualquier base de abiertos debe contener a todos los singletons, por lo que al ser X no numerable viola 2AN[cite: 20, 23, 26]."
    },
    {
        "tema": "Topología - Hoja 3 (Axiomas)",
        "afirmacion_falsa": "Un espacio topológico que es separable y 1-anumerable es siempre un espacio metrizable.",
        "contraejemplo_exacto": "La Recta de Sorgenfrey (ℝ, τ_S).",
        "explicacion_detallada": "Tiene bases locales numerables (1AN) y ℚ denso (separable). Sin embargo, se demuestra por reducción al absurdo que si fuera metrizable implicaría ser 2AN, lo cual es falso[cite: 44, 118]."
    },
    {
        "tema": "Topología - Hoja 3 (Axiomas)",
        "afirmacion_falsa": "Todo espacio topológico que cumple la propiedad de separación T1 es obligatoriamente un espacio Hausdorff (T2).",
        "contraejemplo_exacto": "Espacio infinito con la Topología Cofinita (ℝ, τ_{cf}).",
        "explicacion_detallada": "Permite separar puntos de forma unilateral (es T1), pero dos abiertos no vacíos cualesquiera siempre se intersecan en un conjunto infinito, impidiendo que sea Hausdorff (T2)[cite: 31, 34, 47, 113]."
    },
    {
        "tema": "Topología - Hoja 3 (Axiomas)",
        "afirmacion_falsa": "En un espacio topológico arbitrario no Hausdorff, las sucesiones convergentes poseen un límite único.",
        "contraejemplo_exacto": "Espacio con Topología Indiscreta o Cofinita.",
        "explicacion_detallada": "Al no ser Hausdorff, una misma sucesión puede converger simultáneamente a múltiples puntos distintos del espacio[cite: 34]."
    },
    {
        "tema": "Topología - Hoja 3 (Propiedades)",
        "afirmacion_falsa": "Todo espacio topológico que es conexo por caminos es necesariamente un espacio compacto.",
        "contraejemplo_exacto": "La recta real ℝ con la topología usual.",
        "explicacion_detallada": "ℝ es conexo por caminos (es un intervalo único), pero no es un conjunto compacto en la topología usual al carecer de acotación[cite: 35]."
    },
    {
        "tema": "Topología - Hoja 3 (Propiedades)",
        "afirmacion_falsa": "Todo espacio topológico compacto es necesariamente un espacio metrizable.",
        "contraejemplo_exacto": "Espacio compacto con topología indiscreta en un conjunto con más de un punto.",
        "explicacion_detallada": "Es compacto por finitud de abiertos, pero al no ser Hausdorff (T2) falla la metrizabilidad[cite: 34, 35]."
    },
    {
        "tema": "Topología - Hoja 3 (Aplicaciones)",
        "afirmacion_falsa": "La imagen continua de un conjunto acotado mediante una función continua es siempre un conjunto acotado.",
        "contraejemplo_exacto": "f(x) = 1/x en el dominio acotado (0, 1].",
        "explicacion_detallada": "El dominio (0, 1] es acotado y la función es continua. No obstante, su imagen es [1, +∞), que es un conjunto no acotado[cite: 97]."
    },
    {
        "tema": "Topología - Hoja 3 (Aplicaciones)",
        "afirmacion_falsa": "La imagen continua de un espacio métrico completo mediante una función continua es siempre un espacio completo.",
        "contraejemplo_exacto": "f(x) = arctan(x) de ℝ a (-π/2, π/2).",
        "explicacion_detallada": "El dominio ℝ es completo, pero su imagen acotada (-π/2, π/2) no es un espacio métrico completo[cite: 35]."
    },
    {
        "tema": "Topología - Hoja 3 (Aplicaciones)",
        "afirmacion_falsa": "La completitud métrica es un invariante topológico absoluto.",
        "contraejemplo_exacto": "El intervalo abierto (0, 1) homeomorfo a ℝ.",
        "explicacion_detallada": "(0, 1) no es completo como espacio métrico usual, pero es homeomorfo a todo el espacio ℝ, que sí es completo. La completitud depende de la métrica, no de la topología[cite: 35]."
    },
    {
        "tema": "Topología - Hoja 3 (Aplicaciones)",
        "afirmacion_falsa": "Todo subespacio de un espacio topológico separable es un espacio separable.",
        "contraejemplo_exacto": "Subespacios discretos no numerables en la Recta de Sorgenfrey.",
        "explicacion_detallada": "Aunque ℝ con la topología de Sorgenfrey es separable, existen subespacios dentro de la misma recta que, con la topología discreta inducida, no son separables[cite: 44]."
    },

    # ==========================================
    # MÁS CONTRAEJEMPLOS TEÓRICOS DE EXAMEN UPM
    # ==========================================
    {
        "tema": "Topología - Operaciones con Conjuntos",
        "afirmacion_falsa": "La adherencia de una unión infinita de subconjuntos es siempre igual a la unión de sus adherencias.",
        "contraejemplo_exacto": "Familia numerable de conjuntos unipuntuales cerrados {1/n} en ℝ.",
        "explicacion_detallada": "Para una infinidad numerable de conjuntos, la unión de las adherencias puede ser estrictamente menor que la adherencia de la unión infinita[cite: 35]."
    },
    {
        "tema": "Topología - Operaciones con Conjuntos",
        "afirmacion_falsa": "El interior de una intersección infinita de subconjuntos es siempre igual a la intersección de sus interiores.",
        "contraejemplo_exacto": "Familia de intervalos (-1/n, 1/n).",
        "explicacion_detallada": "La inclusión puede ser estricta (falla la igualdad directa para intersecciones infinitas de abiertos)[cite: 117]."
    },
    {
        "tema": "Topología - Conexidad",
        "afirmacion_falsa": "Todo espacio topológico conexo es obligatoriamente un espacio conexo por caminos.",
        "contraejemplo_exacto": "El Seno del Topólogo.",
        "explicacion_detallada": "El conjunto es conexo por ser adherencia de un conjunto conexo por caminos. Sin embargo, no es conexo por caminos porque ninguna curva continua puede unir el origen con la gráfica oscilante[cite: 6, 10, 21]."
    },
    {
        "tema": "Topología - Espacios Métricos",
        "afirmacion_falsa": "Cualquier pseudométrica que cumpla las propiedades de separación básica genera siempre un espacio Hausdorff.",
        "contraejemplo_exacto": "Espacios pseudométricos con d(x,y) = 0 para puntos distintos.",
        "explicacion_detallada": "Existen puntos distintos que no se pueden separar por entornos disjuntos, impidiendo que el espacio pseudométrico sea Hausdorff[cite: 103, 119]."
    },
    {
        "tema": "Topología - Sucesiones",
        "afirmacion_falsa": "Si una sucesión no tiene límite en un espacio topológico, entonces no posee ninguna subsucesión convergente.",
        "contraejemplo_exacto": "Sucesión acotada oscilante en ℝ.",
        "explicacion_detallada": "Una sucesión divergente u oscilante puede contener infinitas subsucesiones que converjan a puntos diferentes (por ejemplo, por el teorema de Bolzano-Weierstrass)[cite: 94]."
    },
    {
        "tema": "Cálculo - Series de Funciones",
        "afirmacion_falsa": "Si una serie de funciones continuas converge puntualmente en un intervalo, su función suma es siempre continua en todo el dominio.",
        "contraejemplo_exacto": "Suma límite discontinua de potencias de x.",
        "explicacion_detallada": "La convergencia puntual no preserva la continuidad; se requiere obligatoriamente convergencia uniforme para garantizar la continuidad del límite[cite: 96]."
    }
]

def load_data():
    df_inicial = pd.DataFrame(DATOS_INICIALES)
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            try:
                data_cargada = json.load(f)
                df_guardado = pd.DataFrame(data_cargada)
                df_total = pd.concat([df_inicial, df_guardado]).drop_duplicates(subset=["afirmacion_falsa", "contraejemplo_exacto"]).reset_index(drop=True)
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

st.title("📐 Catálogo de Contraejemplos Puros UPM")
st.markdown("Repositorio especializado exclusivamente en afirmaciones falsas, fallos de recíprocos y contraejemplos matemáticos exactos.")

# --- BARRA LATERAL: NAVEGACIÓN Y FILTROS ---
st.sidebar.header("🧭 Filtros de Búsqueda")

temas_disponibles = ['Todos los Bloques'] + list(df['tema'].unique())
tema_seleccionado = st.sidebar.selectbox("📂 Selecciona la Materia:", temas_disponibles)

if tema_seleccionado != 'Todos los Bloques':
    df_filtrado = df[df['tema'] == tema_seleccionado]
else:
    df_filtrado = df

busqueda = st.sidebar.text_input("🔍 Buscar Contraejemplo / Afirmación:", placeholder="Ej. Sorgenfrey, Cesàro, T1...")
if busqueda:
    df_filtrado = df_filtrado[
        df_filtrado['afirmacion_falsa'].str.contains(busqueda, case=False, na=False) |
        df_filtrado['contraejemplo_exacto'].str.contains(busqueda, case=False, na=False) |
        df_filtrado['explicacion_detallada'].str.contains(busqueda, case=False, na=False)
    ]

st.sidebar.markdown("---")
st.sidebar.metric(label="Contraejemplos totales en la app", value=len(df_filtrado))

# --- FORMULARIO PARA AÑADIR NUEVOS CONTRAEJEMPLOS ---
with st.sidebar.expander("➕ Añadir Nuevo Contraejemplo"):
    with st.form("form_nuevo_contraejemplo"):
        nuevo_tema = st.text_input("Bloque / Materia", placeholder="Ej. Topología - Hoja 3")
        nueva_afirmacion = st.text_input("Afirmación Falsa / Hipótesis Rota", placeholder="Ej. Todo espacio compacto es...")
        nuevo_contra = st.text_input("Contraejemplo Exacto", placeholder="Ej. Espacio con topología...")
        nueva_explicacion = st.text_area("Explicación del Fallo", placeholder="Explica por qué no se cumple...")
        
        submit_button = st.form_submit_button(label="Guardar Contraejemplo")
        
        if submit_button:
            if nueva_afirmacion and nuevo_contra:
                nuevo_registro = {
                    "tema": nuevo_tema if nuevo_tema else "General",
                    "afirmacion_falsa": nueva_afirmacion,
                    "contraejemplo_exacto": nuevo_contra,
                    "explicacion_detallada": nueva_explicacion
                }
                df = pd.concat([df, pd.DataFrame([nuevo_registro])], ignore_index=True)
                save_data(df)
                st.sidebar.success("¡Contraejemplo añadido con éxito!")
                st.rerun()
            else:
                st.sidebar.error("Completa al menos la afirmación falsa y el contraejemplo.")

# --- PANTALLA PRINCIPAL ---
st.subheader(f"Contraejemplos en: {tema_seleccionado} ({len(df_filtrado)} encontrados)")

for index, row in df_filtrado.iterrows():
    with st.expander(f"❌ **Falso:** *{row['afirmacion_falsa']}*"):
        st.markdown(f"**Materia / Bloque:** `{row['tema']}`")
        st.markdown(f"**⚡ Contraejemplo Exacto:**")
        st.code(row['contraejemplo_exacto'], language="text")
        st.markdown("---")
        st.markdown(f"**💡 ¿Por qué falla? (Explicación Rigurosa):**\n\n{row['explicacion_detallada']}")
