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

st.title("📐 Explorador Definitivo y Masivo: Cálculo y Topología UPM")
st.markdown("Catálogo exhaustivo con teoría de puntos, separabilidad, axiomas T_i, metrizabilidad, 1AN, 2AN y Cálculo.")

# Base de datos completa, unificada y rigurosa basada en teoría y hojas oficiales UPM
@st.cache_data
def load_data():
    data = [
        # ==========================================
        # TOPOLOGÍA - SEPARABILIDAD Y METRIZABILIDAD (HOJAS 2 Y 3)
        # ==========================================
        {
            "tema": "Topología - Separabilidad y Metrizabilidad",
            "teorema": "Todo espacio metrizable separable es 2AN",
            "hipotesis_rota": "La existencia de un subconjunto denso numerable garantiza base numerable en espacios métricos",
            "nombre_contraejemplo": "Espacio métrico separable (X, τ_d) con A = {a_n} denso numerable",
            "definicion_formal": "ℬ = {B_d(a_n; 1/m) | n, m ∈ ℕ} es base numerable de la topología",
            "explicacion_detallada": "Basado en Hoja 3 (Ejercicio 20)[cite: 114]: Si (X, τ_d) es metrizable y posee un subconjunto denso numerable A, la familia de bolas con radios racionales centradas en A forma una base numerable de la topología, demostrando que todo espacio métrico separable es 2AN[cite: 114]."
        },
        {
            "tema": "Topología - Separabilidad y Metrizabilidad",
            "teorema": "La Recta de Sorgenfrey NO es Metrizable ni 2AN",
            "hipotesis_rota": "Un espacio separable y 1-anumerable no es necesariamente metrizable",
            "nombre_contraejemplo": "Recta de Sorgenfrey (ℝ, τ_S)",
            "definicion_formal": "ℬ_S = {[a, b) | a < b} como base de abiertos",
            "explicacion_detallada": "Basado en Hoja 3 (Ejercicio 34)[cite: 118]: Las bases locales ℬ(x) = {[x, x + 1/n)} son numerables (cumple 1AN) y ℚ es denso (separable)[cite: 21, 40, 44]. Sin embargo, se demuestra por reducción al absurdo que si fuera metrizable, implicaría que es 2AN, lo cual es falso porque cualquier base de Sorgenfrey debe contener un abierto básico con ínfimo en cada real a[cite: 44, 118]."
        },
        {
            "tema": "Topología - Separabilidad y Metrizabilidad",
            "teorema": "Espacio Separable y No Separable",
            "hipotesis_rota": "Todo subespacio de un espacio separable es separable",
            "nombre_contraejemplo": "Subespacios discretos no separables en espacios métricos generales",
            "definicion_formal": "Existencia de subconjuntos no numerables discretos dotados de τ_dis",
            "explicacion_detallada": "Basado en teoría de espacios métricos[cite: 44]: Aunque el espacio total métrico o de Sorgenfrey pueda ser separable, existen subespacios interiores dentro del mismo que, al inducir la topología discreta de forma no numerable, pierden por completo la separabilidad[cite: 44]."
        },

        # ==========================================
        # TOPOLOGÍA - AXIOMAS DE SEPARACIÓN (T_0, T_1, T_2, T_3, T_4)
        # ==========================================
        {
            "tema": "Topología - Axiomas de Separación (T_i)",
            "teorema": "Axioma T1 frente a Hausdorff (T2)",
            "hipotesis_rota": "Un espacio T1 no es necesariamente Hausdorff (T2) ni metrizable",
            "nombre_contraejemplo": "Topología Cofinita en un conjunto infinito (ℝ, τ_{cf})",
            "definicion_formal": "τ_{cf} = {U ⊂ ℝ | ℝ \\ U es finito} ∪ {∅}",
            "explicacion_detallada": "Basado en Hoja 3 (Ejercicio 13)[cite: 113]: Los cerrados propios son los conjuntos finitos[cite: 7]. Dados x ≠ y, se pueden aislar de forma unilateral mediante complementarios finitos (cumple T1). No obstante, dos abiertos no vacíos cualesquiera tienen complementarios finitos, por lo que su intersección nunca puede ser vacía. Por tanto, no es Hausdorff (T2) y no es metrizable[cite: 31, 34, 47, 113]."
        },
        {
            "tema": "Topología - Axiomas de Separación (T_i)",
            "teorema": "Espacios Normales y T4 en Métricas",
            "hipotesis_rota": "Todo espacio métrico es un espacio normal y cumple la propiedad de separación T4",
            "nombre_contraejemplo": "Espacios métricos (X, τ_d)",
            "definicion_formal": "Separación de cerrados disjuntos mediante entornos abiertos disjuntos",
            "explicacion_detallada": "Basado en Hoja 3 (Ejercicio 37)[cite: 119]: Se demuestra formalmente utilizando la distancia a subconjuntos que todo espacio metrizable es un espacio T4, garantizando que cualesquiera dos cerrados disjuntos pueden encerrarse en abiertos disjuntos[cite: 113, 119]."
        },
        {
            "tema": "Topología - Axiomas de Separación (T_i)",
            "teorema": "Hausdorff y Unicidad de Límites",
            "hipotesis_rota": "La convergencia de sucesiones a un límite único exige la propiedad Hausdorff (T2)",
            "nombre_contraejemplo": "Espacios no Hausdorff (como Indiscreto o Cofinito)",
            "definicion_formal": "Si x_n → x y x_n → y con x ≠ y",
            "explicacion_detallada": "Basado en teoría de espacios topológicos[cite: 34]: En un espacio Hausdorff (T2), toda sucesión convergente tiene un límite único. Si el espacio no es Hausdorff, una misma sucesión puede converger simultáneamente a múltiples puntos distintos[cite: 34]."
        },

        # ==========================================
        # TOPOLOGÍA - TEORÍA DE PUNTOS Y OPERACIONES (HOJA 2)
        # ==========================================
        {
            "tema": "Topología - Hoja 2 (Puntos y Operaciones)",
            "teorema": "Caracterización de Punto Interior y Negación",
            "hipotesis_rota": "Un punto no es interior si cualquier entorno básico intercepta al complementario",
            "nombre_contraejemplo": "Punto frontera o exterior respecto al interior de A",
            "definicion_formal": "x ∉ Int(A) ⟺ Para todo entorno U^x ∈ 𝒩(x), se tiene U^x ⊄ A (o U^x ∩ (X \\ A) ≠ ∅)",
            "explicacion_detallada": "Basado en Hoja 2 (Ejercicio 14-15)[cite: 106]: No es necesario que los entornos sean abiertos para definir el interior; basta con que exista algún entorno completo contenido en A. Su negación implica que todo entorno de x se sale del conjunto A[cite: 106]."
        },
        {
            "tema": "Topología - Hoja 2 (Puntos y Operaciones)",
            "teorema": "Caracterización de Punto Adherente y Clausura",
            "hipotesis_rota": "Todo entorno de un punto adherente debe cortar de forma no vacía al conjunto",
            "nombre_contraejemplo": "Puntos en la adherencia Cl(A) frente a puntos exteriores",
            "definicion_formal": "x ∈ Cl(A) ⟺ Para todo entorno U^x ∈ 𝒩(x), se cumple U^x ∩ A ≠ ∅",
            "explicacion_detallada": "Basado en Hoja 2 (Ejercicio 15b)[cite: 106]: Un punto pertenece a la adherencia de A si ningún entorno suyo logra 'separarlo' de A sin tocarlo. Su negación (x ∉ Cl(A)) significa que existe un entorno disjunto de A (punto exterior)[cite: 106, 117]."
        },
        {
            "tema": "Topología - Hoja 2 (Puntos y Operaciones)",
            "teorema": "Caracterización de Punto Frontera",
            "hipotesis_rota": "Los puntos frontera cortan simultáneamente al conjunto y a su complementario",
            "nombre_contraejemplo": "Fr(A) = Cl(A) ∩ Cl(X \\ A)",
            "definicion_formal": "x ∈ ∂A ⟺ Para todo entorno U^x ∈ 𝒩(x), U^x ∩ A ≠ ∅ y U^x ∩ (X \\ A) ≠ ∅",
            "explicacion_detallada": "Basado en Hoja 2 (Ejercicio 15c, 22)[cite: 106, 107]: La frontera agrupa aquellos puntos que se encuentran 'en la valla'. Se relaciona directamente con las operaciones fundamentales mediante Cl(A) = Int(A) ⊔ ∂A y Ext(A) = Int(X \\ A)[cite: 107, 117]."
        },
        {
            "tema": "Topología - Hoja 2 (Puntos y Operaciones)",
            "teorema": "Puntos Aislados frente a Puntos de Acumulación",
            "hipotesis_rota": "Distinción entre aislamiento puntual e acumulación por entornos perforados",
            "nombre_contraejemplo": "Ais(A) frente a A' (Derivado)",
            "definicion_formal": "x ∈ Ais(A) ⟺ ∃U^x t.q. U^x ∩ A = {x}  //  x ∈ A' ⟺ ∀U^x, (U^x \\ {x}) ∩ A ≠ ∅",
            "explicacion_detallada": "Basado en Hoja 2 (Ejercicio 15d, 15e, 24)[cite: 106, 108]: Un punto aislado pertenece a A pero puede separarse solitario en un entorno. Un punto de acumulación (A') exige que cualquier entorno perforado contenga puntos de A. La adherencia cumple Cl(A) = A' ⊔ Ais(A)[cite: 108]."
        },
        {
            "tema": "Topología - Hoja 2 (Puntos y Operaciones)",
            "teorema": "Criterios de Abierto y Cerrado con Frontera",
            "hipotesis_rota": "Condiciones estrictas de cerradura y apertura basadas en la frontera",
            "nombre_contraejemplo": "Criterio de cerradura ∂A ⊆ A y apertura ∂A ∩ A = ∅",
            "definicion_formal": "A es cerrado ⟺ ∂A ⊆ A  //  A es abierto ⟺ ∂A ∩ A = ∅",
            "explicacion_detallada": "Basado en Hoja 2 (Ejercicio 23)[cite: 107]: Un conjunto es cerrado si y solo si contiene a toda su frontera. Es abierto si su frontera está completamente disjunta de él. Si la frontera es vacía, el conjunto es simultáneamente abierto y cerrado[cite: 107]."
        },

        # ==========================================
        # CÁLCULO - REALES, SUCESIONES Y SERIES
        # ==========================================
        {
            "tema": "Cálculo - Rel. 1 (Reales)",
            "teorema": "Falacia en Simplificación Algebraica",
            "hipotesis_rota": "Cancelar factores algebraicos nulos (división entre cero)",
            "nombre_contraejemplo": "Demostración falsa de 2 = 1",
            "definicion_formal": "Si x = y, entonces x^2 = xy ⇒ x^2 - y^2 = xy - y^2 ⇒ (x-y)(x+y) = y(x-y) ⇒ x+y = y ⇒ 2y = y ⇒ 2 = 1",
            "explicacion_detallada": "El error radica en pasar de (x-y)(x+y) = y(x-y) a x+y = y dividiendo entre (x-y). Como se asumió x = y, entonces x - y = 0, lo cual constituye una división ilegal por cero[cite: 89]."
        },
        {
            "tema": "Cálculo - Rel. 2 (Sucesiones)",
            "teorema": "Convergencia del Valor Absoluto",
            "hipotesis_rota": "El recíproco no es cierto: |a_n| convergente no implica que a_n sea convergente",
            "nombre_contraejemplo": "Sucesión alternada a_n = (-1)^n",
            "definicion_formal": "a_n = (-1)^n",
            "explicacion_detallada": "El valor absoluto |(-1)^n| = 1 es una sucesión constante que converge a 1. Sin embargo, la sucesión original oscila perpetuamente entre -1 y 1, por lo que diverge[cite: 92]."
        },
        {
            "tema": "Cálculo - Rel. 3 (Series)",
            "teorema": "Condición Necesaria de Convergencia en Series",
            "hipotesis_rota": "Que el término general a_n tienda a 0 no garantiza que la serie converja",
            "nombre_contraejemplo": "Serie Armónica Σ (1/n)",
            "definicion_formal": "Σ_{n=1}^∞ (1/n)",
            "explicacion_detallada": "El término general tiende a 0 cuando n → ∞. No obstante, las sumas parciales crecen de forma logarítmica y la serie diverge[cite: 95]."
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
    
    busqueda = st.sidebar.text_input("🔍 Buscar Teorema o Contraejemplo:", placeholder="Ej. Separabilidad, Metrizable, Interior...")
    if busqueda:
        df_filtrado = df_filtrado[
            df_filtrado['teorema'].str.contains(busqueda, case=False, na=False) |
            df_filtrado['nombre_contraejemplo'].str.contains(busqueda, case=False, na=False) |
            df_filtrado['explicacion_detallada'].str.contains(busqueda, case=False, na=False)
        ]

    st.sidebar.markdown("---")
    st.sidebar.metric(label="Total elementos en la app", value=len(df_filtrado))

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
