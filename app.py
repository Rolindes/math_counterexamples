import streamlit as st
import pandas as pd
import json
import os

# Configuración de la página
st.set_page_config(
    page_title="MathCounterexamples - Topología UPM", 
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

DB_FILE = "contraejemplos_implicaciones_topologia.json"

# Base de datos masiva centrada en implicaciones falsas y contraejemplos topológicos UPM
DATOS_INICIALES = [
    # ==========================================
    # AXIOMAS DE SEPARACIÓN (T_i) - IMPLICACIONES FALSAS
    # ==========================================
    {
        "tema": "Topología - Separación (T_0 a T_4)",
        "afirmacion_falsa": "Todo espacio topológico que cumple el axioma T_0 es necesariamente un espacio T_1.",
        "contraejemplo_exacto": "El espacio de Sierpinski (\\{0, 1\\}, \\{\\emptyset, \\{0\\}, \\{0, 1\\}\\}) o la Topología del Punto Particular (X, \\tau_p).",
        "explicacion_detallada": "En el espacio de Sierpinski, dados los puntos 0 y 1, el abierto \\{0\\} contiene al 0 pero no al 1 (cumple T_0). Sin embargo, el punto 1 no posee ningún abierto que lo contenga excluyendo al 0, por lo que **no es T_1** (los singletons no son cerrados)."
    },
    {
        "tema": "Topología - Separación (T_0 a T_4)",
        "afirmacion_falsa": "Todo espacio topológico que cumple el axioma T_1 es obligatoriamente un espacio Hausdorff (T_2).",
        "contraejemplo_exacto": "Un conjunto infinito X dotado de la Topología Cofinita (X, \\tau_{cf}).",
        "explicacion_detallada": "Los cerrados propios de la topología cofinita son exactamente los conjuntos finitos[cite: 7]. Como todo singleton es finito, es un conjunto cerrado, lo que garantiza que el espacio es **T_1**. No obstante, dos abiertos no vacíos cualesquiera siempre se intersecan en un conjunto infinito, haciendo imposible encontrar entornos disjuntos que separen dos puntos; por tanto, **no es T_2 (Hausdorff)**."
    },
    {
        "tema": "Topología - Separación (T_0 a T_4)",
        "afirmacion_falsa": "Todo espacio Hausdorff (T_2) es necesariamente un espacio normal y cumple la propiedad T_4.",
        "contraejemplo_exacto": "La Recta de Sorgenfrey (ℝ, \\tau_S) o espacios métricos generales frente a topologías finas.",
        "explicacion_detallada": "Aunque la recta de Sorgenfrey es un espacio Hausdorff (T_2) y de hecho es normal (T_4), existen espacios topológicos Hausdorff que fallan en ser normales (T_4) al no poder separar ciertos cerrados disjuntos mediante abiertos disjuntos."
    },

    # ==========================================
    # SEPARABILIDAD Y METRIZABILIDAD
    # ==========================================
    {
        "tema": "Topología - Separabilidad y Metrizabilidad",
        "afirmacion_falsa": "Todo espacio topológico que es separable (posee un subconjunto denso numerable) es necesariamente un espacio metrizable.",
        "contraejemplo_exacto": "La Recta de Sorgenfrey (ℝ, \\tau_S) o la Topología Cofinita en un conjunto no numerable.",
        "explicacion_detallada": "El conjunto de los números racionales ℚ es denso en la recta de Sorgenfrey (es separable) y cumple el primer axioma de contabilidad (1AN)[cite: 21]. Sin embargo, se demuestra por reducción al absurdo que **no es metrizable**, ya que si lo fuera implicaría ser 2AN, condición que Sorgenfrey viola flagrantemente."
    },
    {
        "tema": "Topología - Separabilidad y Metrizabilidad",
        "afirmacion_falsa": "Todo espacio metrizable es obligatoriamente un espacio separable.",
        "contraejemplo_exacto": "Un conjunto no numerable X dotado de la Métrica Discreta (X, d_dis).",
        "explicacion_detallada": "El espacio métrico discreto sobre un conjunto no numerable (como ℝ con d_dis) es perfectamente metrizable. No obstante, como cada punto es abierto, el único subconjunto denso es el propio espacio X, impidiendo que contenga un subconjunto denso numerable; por tanto, **no es separable**."
    },
    {
        "tema": "Topología - Separabilidad y Metrizabilidad",
        "afirmacion_falsa": "Todo subespacio de un espacio separable es un espacio separable.",
        "contraejemplo_exacto": "Subespacios discretos no numerables construidos dentro de la Recta de Sorgenfrey o espacios métricos.",
        "explicacion_detallada": "Aunque el espacio total (como ℝ con Sorgenfrey) es separable gracias a ℚ, existen subespacios interiores dentro del mismo que, al inducir la topología discreta de manera no numerable, carecen por completo de subconjuntos densos numerables."
    },

    # ==========================================
    # 1AN vs 2AN (AXIOMAS DE CONTABILIDAD)
    # ==========================================
    {
        "tema": "Topología - Contabilidad (1AN y 2AN)",
        "afirmacion_falsa": "Todo espacio topológico que cumple el primer axioma de contabilidad (1AN) cumple también el segundo axioma de contabilidad (2AN).",
        "contraejemplo_exacto": "Espacio Discreto No Numerable (X, τ_dis) donde X es un conjunto infinito no numerable.",
        "explicacion_detallada": "Las bases locales de singletons ℬ(x) = \\{\\{x\\}\\} son numerables, por lo que cumple **1AN**[cite: 20]. Sin embargo, cualquier base de abiertos debe contener obligatoriamente a todos los singletons; al ser X no numerable, la base total es no numerable, violando estrictamente **2AN**[cite: 23]."
    },
    {
        "tema": "Topología - Contabilidad (1AN y 2AN)",
        "afirmacion_falsa": "Todo espacio topológico que cumple el segundo axioma de contabilidad (2AN) es necesariamente un espacio separable.",
        "contraejemplo_exacto": "Cualquier espacio 2AN (como ℝ con la topología usual).",
        "explicacion_detallada": "En este caso la implicación **sí es cierta** (todo 2AN es separable eligiendo un punto por cada abierto básico de la base numerable). El contraejemplo clásico se usa para demostrar que el **recíproco es falso**: existen espacios separables (como Sorgenfrey) que **no son 2AN**."
    },

    # ==========================================
    # COMPACIDAD Y CONEXIDAD
    # ==========================================
    {
        "tema": "Topología - Compacidad y Conexidad",
        "afirmacion_falsa": "Todo espacio topológico conexo por caminos es obligatoriamente un espacio compacto.",
        "contraejemplo_exacto": "La recta real (ℝ, \\tau_u) o el espacio euclidiano ℝ^n.",
        "explicacion_detallada": "ℝ es conexo por caminos porque cualquier par de puntos se une mediante un segmento lineal continuo. Sin embargo, **no es compacto** en la topología usual al carecer de acotación."
    },
    {
        "tema": "Topología - Compacidad y Conexidad",
        "afirmacion_falsa": "Todo espacio topológico compacto es necesariamente metrizable.",
        "contraejemplo_exacto": "Espacio compacto con topología indiscreta (X, \\tau_{indis}) con más de un punto.",
        "explicacion_detallada": "El espacio es compacto debido a la finitud de abiertos en la topología indiscreta. No obstante, al no ser Hausdorff (T_2), falla una condición necesaria fundamental de los espacios métricos, por lo que **no es metrizable**."
    },
    {
        "tema": "Topología - Compacidad y Conexidad",
        "afirmacion_falsa": "Todo espacio métrico compacto es separable y cumple el segundo axioma de contabilidad (2AN).",
        "contraejemplo_exacto": "Espacios métricos compactos generales (nota: en este caso la afirmación SÍ es cierta, todo métrico compacto es 2AN y separable; el fallo ocurre en espacios topológicos generales no métricos).",
        "explicacion_detallada": "Sirve para recordar que la compacidad en espacios métricos impone una estructura muy fuerte de contabilidad, a diferencia de los espacios topológicos arbitrarios."
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

st.title("📐 Contraejemplos de Implicaciones Topológicas UPM")
st.markdown("Catálogo especializado en propiedades que no se implican mutuamente (T_0 vs T_1, separable vs metrizable, 1AN vs 2AN).")

# --- BARRA LATERAL: NAVEGACIÓN Y FILTROS ---
st.sidebar.header("🧭 Filtros de Implicaciones")

temas_disponibles = ['Todos los Bloques'] + list(df['tema'].unique())
tema_seleccionado = st.sidebar.selectbox("📂 Selecciona la Categoría:", temas_disponibles)

if tema_seleccionado != 'Todos los Bloques':
    df_filtrado = df[df['tema'] == tema_seleccionado]
else:
    df_filtrado = df

busqueda = st.sidebar.text_input("🔍 Buscar Implicación:", placeholder="Ej. T0, T1, T2, separable, 1AN...")
if busqueda:
    df_filtrado = df_filtrado[
        df_filtrado['afirmacion_falsa'].str.contains(busqueda, case=False, na=False) |
        df_filtrado['contraejemplo_exacto'].str.contains(busqueda, case=False, na=False) |
        df_filtrado['explicacion_detallada'].str.contains(busqueda, case=False, na=False)
    ]

st.sidebar.markdown("---")
st.sidebar.metric(label="Contraejemplos en la app", value=len(df_filtrado))

# --- FORMULARIO PARA AÑADIR NUEVOS CONTRAEJEMPLOS ---
with st.sidebar.expander("➕ Añadir Nueva Implicación Falsa"):
    with st.form("form_nuevo_contraejemplo"):
        nuevo_tema = st.text_input("Categoría", placeholder="Ej. Topología - Separación")
        nueva_afirmacion = st.text_input("Implicación Falsa", placeholder="Ej. Todo espacio T2 es...")
        nuevo_contra = st.text_input("Contraejemplo Exacto", placeholder="Ej. Espacio X con tau...")
        nueva_explicacion = st.text_area("Explicación del Fallo", placeholder="Explica detalladamente por qué falla...")
        
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
        st.markdown(f"**Categoría:** `{row['tema']}`")
        st.markdown(f"**⚡ Contraejemplo Exacto:**")
        st.code(row['contraejemplo_exacto'], language="text")
        st.markdown("---")
        st.markdown(f"**💡 ¿Por qué falla la implicación?**\n\n{row['explicacion_detallada']}")
