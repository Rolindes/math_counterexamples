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

st.title("📐 Explorador Definitivo: Cálculo y Topología UPM")
st.markdown("Catálogo exhaustivo de contraejemplos y ejercicios universitarios con notación limpia.")

# Base de datos masiva (Exactamente 20 de Cálculo y 20 de Topología)
@st.cache_data
def load_data():
    data = [
        # ==========================================
        # CÁLCULO (RELACIONES 1, 2 y 3) -> 20 ITEMS
        # ==========================================
        {
            "tema": "Cálculo - Rel. 1 (Reales)",
            "teorema": "Falacia en Simplificación Algebraica",
            "hipotesis_rota": "Cancelar factores algebraicos nulos (división entre cero)",
            "nombre_contraejemplo": "Demostración falsa de 2 = 1",
            "definicion_formal": "Si x = y, entonces x^2 = xy ⇒ x^2 - y^2 = xy - y^2 ⇒ (x-y)(x+y) = y(x-y) ⇒ x+y = y ⇒ 2y = y ⇒ 2 = 1",
            "explicacion_detallada": "El error radica en pasar de (x-y)(x+y) = y(x-y) a x+y = y dividiendo entre (x-y). Como se asumió x = y, entonces x - y = 0, lo cual constituye una división ilegal por cero."
        },
        {
            "tema": "Cálculo - Rel. 1 (Reales)",
            "teorema": "Manipulación Incorrecta de Desigualdades",
            "hipotesis_rota": "Operar con inecuaciones multiplicando por variables sin estudiar su signo",
            "nombre_contraejemplo": "Falacia con (x+1)/(x-1) ≥ 1",
            "definicion_formal": "(x+1)/(x-1) ≥ 1 ⇒ x+1 ≥ x-1 ⇒ 1 ≥ -1",
            "explicacion_detallada": "Multiplicar por (x-1) requiere conocer su signo. Al no restringir el dominio, se opera de forma inválida, llevando a conclusiones erróneas para valores donde el denominador es negativo."
        },
        {
            "tema": "Cálculo - Rel. 1 (Reales)",
            "teorema": "Caracterización del Cero con Épsilon",
            "hipotesis_rota": "Condición épsilon-acotada estricta para números no nulos",
            "nombre_contraejemplo": "Demostración de que x = 0",
            "definicion_formal": "Si 0 ≤ x < ε para todo ε > 0, entonces x = 0",
            "explicacion_detallada": "Si x fuera estrictamente mayor que cero, podríamos elegir ε = x/2 > 0, lo cual contradice la hipótesis de que es menor que cualquier épsilon positivo."
        },
        {
            "tema": "Cálculo - Rel. 1 (Reales)",
            "teorema": "Naturaleza de los Números Irracionales",
            "hipotesis_rota": "La suma o producto de irracionales no siempre es un número irracional",
            "nombre_contraejemplo": "Suma y producto algebraico de irracionales",
            "definicion_formal": "√2 + (-√2) = 0 ∈ ℚ, o bien √2 · √2 = 2 ∈ ℚ",
            "explicacion_detallada": "Mientras que sumar un racional con un irracional siempre da irracional, la suma o el producto de dos números irracionales puede resultar perfectamente en un número racional."
        },
        {
            "tema": "Cálculo - Rel. 1 (Reales)",
            "teorema": "Existencia de Elementos bajo el Supremo",
            "hipotesis_rota": "La existencia de un elemento en el conjunto estrictamente menor que s y mayor que s - ε",
            "nombre_contraejemplo": "Conjuntos discretos o acotados singulares",
            "definicion_formal": "Dado s = sup A y ε > 0, ¿existe a ∈ A tal que s - ε < a < s?",
            "explicacion_detallada": "Si A es un conjunto finito, el supremo pertenece al conjunto y no se pueden encontrar elementos estrictamente intermedios menores que el propio máximo."
        },
        {
            "tema": "Cálculo - Rel. 1 (Reales)",
            "teorema": "Desigualdades Estrictas en Suma de Conjuntos",
            "hipotesis_rota": "Las cotas de subconjuntos finitos indexados pueden ser estrictas",
            "nombre_contraejemplo": "Conjuntos finitos C frente a A + B",
            "definicion_formal": "C = {x_1 + y_1, ..., x_n + y_n}, donde sup C ≤ sup A + sup B de forma estricta",
            "explicacion_detallada": "Aunque para conjuntos generales se cumple la igualdad en supremos e ínfimos, al restringirnos a sumas puntuales indexadas finitas las desigualdades pueden cumplirse estrictamente."
        },
        {
            "tema": "Cálculo - Rel. 2 (Sucesiones)",
            "teorema": "Convergencia del Valor Absoluto",
            "hipotesis_rota": "El recíproco no es cierto: |a_n| convergente no implica que a_n sea convergente",
            "nombre_contraejemplo": "Sucesión alternada a_n = (-1)^n",
            "definicion_formal": "a_n = (-1)^n",
            "explicacion_detallada": "El valor absoluto |(-1)^n| = 1 es una sucesión constante que converge a 1. Sin embargo, la sucesión original oscila perpetuamente entre -1 y 1, por lo que diverge."
        },
        {
            "tema": "Cálculo - Rel. 2 (Sucesiones)",
            "teorema": "Suma de Sucesiones Convergente y No Convergente",
            "hipotesis_rota": "La suma de una sucesión convergente y una divergente es siempre divergente",
            "nombre_contraejemplo": "x_n convergente y y_n divergente",
            "definicion_formal": "x_n = 1/n (converge a 0) y y_n = (-1)^n (diverge)",
            "explicacion_detallada": "La suma x_n + y_n resulta en una sucesión oscilante que no converge. Si x_n tiende a un límite no nulo, el producto x_n y_n también diverge."
        },
        {
            "tema": "Cálculo - Rel. 2 (Sucesiones)",
            "teorema": "Conservación de Límites en Intervalos Abiertos",
            "hipotesis_rota": "El límite de una sucesión contenida en un intervalo abierto puede caer en la frontera",
            "nombre_contraejemplo": "Sucesión en el intervalo abierto (0, 1)",
            "definicion_formal": "a_n = 1/n ∈ (0, 1) con lim a_n = 0",
            "explicacion_detallada": "Si a_n ∈ [0, 1] cerrado, el límite pertenece al intervalo. Si el intervalo es abierto (0, 1), la sucesión está contenida pero su límite (0) está en la frontera exterior."
        },
        {
            "tema": "Cálculo - Rel. 2 (Sucesiones)",
            "teorema": "Convergencia en Media (Teorema de Cesàro)",
            "hipotesis_rota": "S_n / n converge a l, pero el término general a_n no necesariamente converge",
            "nombre_contraejemplo": "Sucesión a_n = (-1)^n",
            "definicion_formal": "S_n = a_1 + ... + a_n, donde lim (S_n / n) = 0",
            "explicacion_detallada": "Aunque a_n diverge, la media aritmética de sus sumas parciales S_n / n converge a 0. El recíproco es falso."
        },
        {
            "tema": "Cálculo - Rel. 2 (Sucesiones)",
            "teorema": "Subsucesiones Convergentes y Límite Único",
            "hipotesis_rota": "Convergencia conjunta de subsucesiones pares, impares y múltiplos de 3",
            "nombre_contraejemplo": "Sucesión con subsucesiones u_{2n}, u_{2n+1} y u_{3n} convergentes",
            "definicion_formal": "Subsucesiones de índices entrelazados que convergen al mismo punto",
            "explicacion_detallada": "Si las subsucesiones u_{2n}, u_{2n+1} y u_{3n} convergen todas al mismo límite l, entonces la sucesión completa u_n converge necesariamente a l."
        },
        {
            "tema": "Cálculo - Rel. 2 (Sucesiones)",
            "teorema": "Sucesiones Definidas por Recurrencia",
            "hipotesis_rota": "La convergencia depende estrictamente del valor de partida x_1",
            "nombre_contraejemplo": "7x_{n+1} = x_n^3 + 6",
            "definicion_formal": "Evolución de límites según x_1 = 1/2, 3/2 o 5/2",
            "explicacion_detallada": "Dependiendo del valor inicial x_1, la sucesión recurrente puede converger a puntos fijos diferentes o divergir hacia el infinito."
        },
        {
            "tema": "Cálculo - Rel. 3 (Series)",
            "teorema": "Condición Necesaria de Convergencia en Series",
            "hipotesis_rota": "Que el término general a_n tienda a 0 no garantiza que la serie converja",
            "nombre_contraejemplo": "Serie Armónica Σ (1/n)",
            "definicion_formal": "Σ_{n=1}^∞ (1/n)",
            "explicacion_detallada": "El término general tiende a 0 cuando n → ∞. No obstante, las sumas parciales crecen de forma logarítmica y la serie diverge."
        },
        {
            "tema": "Cálculo - Rel. 3 (Series)",
            "teorema": "Cociente de Series con Términos Positivos",
            "hipotesis_rota": "Si Σ a_n diverge, la serie modificada a_n / (1 + a_n) puede no divergir",
            "nombre_contraejemplo": "Modificación de series divergentes",
            "definicion_formal": "Σ a_n diverge ⇒ Σ [a_n / (1 + a_n)]",
            "explicacion_detallada": "Analiza el comportamiento de series con términos positivos donde el cociente modificado altera el carácter de divergencia original."
        },
        {
            "tema": "Cálculo - Rel. 3 (Series)",
            "teorema": "Convergencia Absoluta frente a Condicional",
            "hipotesis_rota": "Series alternadas que convergen pero fallan en hacerlo en valor absoluto",
            "nombre_contraejemplo": "Serie armónica alternada Σ [(-1)^n / ln(n+1)]",
            "definicion_formal": "Σ_{n=1}^∞ [(-1)^n / ln(n+1)]",
            "explicacion_detallada": "Por el criterio de Leibniz, la serie converge condicionalmente; sin embargo, en valor absoluto se convierte en la serie armónica logarítmica divergente."
        },
        {
            "tema": "Cálculo - Rel. 3 (Series)",
            "teorema": "Series con Signos Alternados y Polinomios",
            "hipotesis_rota": "Decrecimiento y tendencia a cero en términos racionales con signos alternados",
            "nombre_contraejemplo": "Σ (-1)^n (a + n) / n^2",
            "definicion_formal": "Σ_{n=1}^∞ (-1)^n [(a + n) / n^2], (a ≥ 0)",
            "explicacion_detallada": "Dependiendo del parámetro a, la serie estudia su convergencia condicional o absoluta mediante el criterio de Leibniz."
        },
        {
            "tema": "Cálculo - Rel. 3 (Series)",
            "teorema": "Series Trigonométricas con Parámetros",
            "hipotesis_rota": "Convergencia condicionada por ángulos reales x",
            "nombre_contraejemplo": "Σ [sin(nx) / n^2]",
            "definicion_formal": "Σ_{n=1}^∞ [sin(nx) / n^2], (x ∈ ℝ)",
            "explicacion_detallada": "Mediante el criterio de Weierstrass con la serie p-ádica Σ (1/n^2), se demuestra que converge absoluta y uniformemente para todo x real."
        },
        {
            "tema": "Cálculo - Rel. 3 (Series)",
            "teorema": "Sucesiones de Cauchy en Espacios Métricos",
            "hipotesis_rota": "Acotación de diferencias sucesivas que garantizan la condición de Cauchy",
            "nombre_contraejemplo": "|x_{n+1} - x_n| ≤ r^n con 0 < r < 1",
            "definicion_formal": "Sucesión real con acotación exponencial decreciente",
            "explicacion_detallada": "Demuestra mediante la desigualdad triangular y suma geométrica que cualquier sucesión que satisfaga esta acotación geométrica es de Cauchy y, por ende, convergente."
        },
        {
            "tema": "Cálculo - Rel. 3 (Series)",
            "teorema": "Series Telescópicas y Sumas Exactas",
            "hipotesis_rota": "Cancelación de términos intermedios en sumas parciales",
            "nombre_contraejemplo": "Σ [1 / (n(n+1))]",
            "definicion_formal": "Σ_{n=1}^∞ [1 / (n(n+1))] = Σ [1/n - 1/(n+1)]",
            "explicacion_detallada": "Al descomponer en fracciones simples, los términos se cancelan telescópicamente dejando únicamente el primer término, resultando en una suma exacta igual a 1."
        },
        {
            "tema": "Cálculo - Rel. 3 (Series)",
            "teorema": "Criterio de la Raíz y del Cociente en Casos Límite",
            "hipotesis_rota": "Indeterminación cuando el límite del cociente o raíz es exactamente igual a 1",
            "nombre_contraejemplo": "Series con cociente unitario límite",
            "definicion_formal": "lim (a_{n+1} / a_n) = 1",
            "explicacion_detallada": "Cuando el criterio del cociente arroja un límite igual a 1, el criterio no decide, requiriendo métodos más finos como comparación asintótica."
        },

        # ==========================================
        # TOPOLOGÍA GENERAL (TEMAS 1, 2, 3 Y HOJA 3) -> 20 ITEMS
        # ==========================================
        {
            "tema": "Topología - Hoja 3",
            "teorema": "Continuidad de la Aplicación Identidad",
            "hipotesis_rota": "La identidad entre espacios con distinta topología no es continua en ambas direcciones",
            "nombre_contraejemplo": "id: (ℝ, τ_S) → (ℝ, τ_u) frente a su inversa",
            "definicion_formal": "id: (ℝ, τ_u) → (ℝ, τ_S) y su recíproco",
            "explicacion_detallada": "id: (ℝ, τ_S) → (ℝ, τ_u) es continua porque todo abierto usual es abierto en Sorgenfrey. En cambio, id: (ℝ, τ_u) → (ℝ, τ_S) no es continua en ningún punto porque los básicos [a, b) no contienen entornos usuales simétricos."
        },
        {
            "tema": "Topología - Hoja 3",
            "teorema": "Invarianza Topológica: La Continuidad NO Preserva la Acotación",
            "hipotesis_rota": "Una función continua con dominio acotado genera una imagen no acotada",
            "nombre_contraejemplo": "f(x) = 1/x en el intervalo acotado (0, 1]",
            "definicion_formal": "f: (0, 1] → ℝ con f(x) = 1/x",
            "explicacion_detallada": "El dominio (0, 1] es acotado y la función es continua. No obstante, su imagen es [1, +∞), que es no acotada, demostrando que la acotación no es un invariante topológico."
        },
        {
            "tema": "Topología - Hoja 3",
            "teorema": "Caracterización de Continuidad en Topología Cofinita",
            "hipotesis_rota": "Una función entre espacios cofinitos es continua si sus fibras cumplen una condición de finitud",
            "nombre_contraejemplo": "Aplicación f con fibras finitas o infinitas",
            "definicion_formal": "f: (X, τ_{cf}) → (Y, τ_{cf})",
            "explicacion_detallada": "f es continua en x si y solo si la imagen inversa de cada punto exterior, f^{-1}({y}), es un conjunto finito para todo y ≠ f(x). Globalmente, es continua si y solo si es constante o todas sus fibras son finitas."
        },
        {
            "tema": "Topología - Hoja 3",
            "teorema": "Topología de Rayos a Izquierda (τ_←)",
            "hipotesis_rota": "Funciones continuas en topologías no Hausdorff son obligatoriamente no decrecientes",
            "nombre_contraejemplo": "f(x) = x^2, g(x) = ⌊x⌋ en (ℝ, τ_←)",
            "definicion_formal": "τ_← = {∅, ℝ} ∪ {(-∞, a) | a ∈ ℝ}",
            "explicacion_detallada": "Toda aplicación continua u: ℝ → ℝ con esta topología es no decreciente. Funciones como la parte entera presentan discontinuidades direccionales características."
        },
        {
            "tema": "Topología - Hoja 3",
            "teorema": "Función Característica y Fronteras",
            "hipotesis_rota": "La continuidad de la función característica depende exclusivamente de la frontera del conjunto",
            "nombre_contraejemplo": "χ_ℚ (Función de Dirichlet) con topología discreta en {0, 1}",
            "definicion_formal": "χ_A(x) = 1 si x ∈ A, y 0 si x ∉ A",
            "explicacion_detallada": "Los puntos de discontinuidad de χ_A coinciden exactamente con la frontera Fr(A). Para A = ℚ en ℝ, Fr(ℚ) = ℝ, por lo que es discontinua en todo punto."
        },
        {
            "tema": "Topología - Temas 1-2",
            "teorema": "Metrizabilidad y Axiomas de Numerabilidad",
            "hipotesis_rota": "Un espacio separable y 1-anumerable no es necesariamente metrizable ni 2-anumerable",
            "nombre_contraejemplo": "Recta de Sorgenfrey (ℝ, τ_S)",
            "definicion_formal": "ℝ dotada de la base de abiertos ℬ_S = {[a, b) | a < b}",
            "explicacion_detallada": "Las bases locales ℬ(x) = {[x, x + 1/n)} son numerables (1AN) y ℚ es denso (separable). Sin embargo, no es 2-anumerable porque cualquier base debe contener un abierto básico con ínfimo en cada real a. Como todo espacio métrico separable debe ser 2-anumerable, no es metrizable."
        },
        {
            "tema": "Topología - Temas 1-2",
            "teorema": "Axiomas de Separación (Hausdorff vs T1)",
            "hipotesis_rota": "Un espacio T1 no es necesariamente Hausdorff (T2) ni metrizable",
            "nombre_contraejemplo": "Topología Cofinita en un conjunto infinito (ℝ, τ_{cf})",
            "definicion_formal": "τ_{cf} = {U ⊂ ℝ | ℝ \\ U es finito} ∪ {∅}",
            "explicacion_detallada": "Los cerrados propios son los conjuntos finitos. Dados x ≠ y, se pueden aislar de forma unilateral mediante complementarios finitos (es T1). No obstante, dos abiertos no vacíos cualesquiera tienen complementarios finitos, por lo que su intersección nunca puede ser vacía. Por tanto, no es Hausdorff (T2) y no es metrizable."
        },
        {
            "tema": "Topología - Temas 1-2",
            "teorema": "Conexidad y Conexidad por Caminos",
            "hipotesis_rota": "Todo espacio conexo por caminos es conexo, pero el recíproco falla",
            "nombre_contraejemplo": "El Seno del Topólogo",
            "definicion_formal": "A = {(x, sin(1/x)) | x ∈ (0, 1]} ∪ {(0, y) | y ∈ [-1, 1]}",
            "explicacion_detallada": "El conjunto es conexo por ser la adherencia de la gráfica de una función continua. Sin embargo, no es conexo por caminos porque ninguna curva continua puede unir el origen (0,0) con la curva oscilante sin que las infinitas oscilaciones rompan la continuidad en el límite."
        },
        {
            "tema": "Topología - Temas 1-2",
            "teorema": "Axioma de Separación Hausdorff (T2)",
            "hipotesis_rota": "Espacios con bases locales simétricas que fallan en separar puntos globales",
            "nombre_contraejemplo": "La Recta de Dos Orígenes",
            "definicion_formal": "X = ℝ ⊔ {*}, con base que duplica el punto 0 añadiendo entornos con dos orígenes",
            "explicacion_detallada": "Los dos orígenes 0 y * comparten idénticos entornos básicos sin el punto central, haciendo imposible encontrar abiertos disjuntos que los separen. El espacio no es Hausdorff, por ende no es metrizable."
        },
        {
            "tema": "Topología - Temas 1-2",
            "teorema": "Axiomas de Numerabilidad (1AN vs 2AN)",
            "hipotesis_rota": "Todo espacio 1-anumerable no es necesariamente 2-anumerable",
            "nombre_contraejemplo": "Espacio Discreto No Numerable (X, τ_{dis})",
            "definicion_formal": "X es un conjunto infinito no numerable dotado de τ_{dis} = 𝒫(X)",
            "explicacion_detallada": "Las bases locales de singletons ℬ(x) = {{x}} son numerables, cumpliendo 1AN. No obstante, cualquier base de abiertos ℬ debe contener obligatoriamente a todos los singletons {x}. Al ser X no numerable, ℬ es no numerable, violando 2AN."
        },
        {
            "tema": "Topología - Hoja 3",
            "teorema": "Imagen Inversa de Abiertos y Continuidad",
            "hipotesis_rota": "La imagen inversa de un abierto es abierta, pero la imagen directa de un abierto no es necesariamente abierta",
            "nombre_contraejemplo": "Proyección o función cuadrática continua",
            "definicion_formal": "f: X → Y es continua ⟺ f^{-1}(V) es abierto para todo V abierto en Y",
            "explicacion_detallada": "Mientras la definición formal de continuidad exige que los abiertos tengan imagen inversa abierta, la imagen directa de un conjunto abierto mediante una función continua (ej. f(x) = x^2) puede convertir un abierto en un intervalo no abierto."
        },
        {
            "tema": "Topología - Hoja 3",
            "teorema": "Composición de Funciones Continuas en Puntos",
            "hipotesis_rota": "La continuidad puntual se propaga mediante composiciones",
            "nombre_contraejemplo": "g ∘ f continua en a si f es continua en a y g en f(a)",
            "definicion_formal": "f: X → Y continua en a, g: Y → Z continua en f(a) ⇒ g ∘ f continua en a",
            "explicacion_detallada": "Demostración directa utilizando bases de entornos o entornos abiertos anidados para probar que los entornos de z se retrotraen correctamente al dominio X."
        },
        {
            "tema": "Topología - Hoja 3",
            "teorema": "Conjuntos de Nivel Abiertos y Cerrados",
            "hipotesis_rota": "Los conjuntos donde una función continua se anula o es positiva tienen propiedades topológicas fijas",
            "nombre_contraejemplo": "V_f = {x ∈ X : f(x) = 0} y S_f = {x ∈ X : f(x) > 0}",
            "definicion_formal": "f: X → ℝ continua con topología usual",
            "explicacion_detallada": "V_f es siempre un conjunto cerrado en X por ser la imagen inversa del cerrado {0}. S_f es abierto por ser la imagen inversa del rayo abierto (0, +∞)."
        },
        {
            "tema": "Topología - Temas 1-2",
            "teorema": "Espacios Compactos y Continuidad",
            "hipotesis_rota": "La imagen continua de un espacio compacto es compacta, pero el dominio no compacto puede fallar",
            "nombre_contraejemplo": "f(x) = arctan(x) de ℝ a (-π/2, π/2)",
            "definicion_formal": "f: ℝ → (-π/2, π/2)",
            "explicacion_detallada": "El dominio ℝ no es compacto en la topología usual. Aunque la función es continua, su imagen es el intervalo abierto acotado (-π/2, π/2), que no es compacto en ℝ."
        },
        {
            "tema": "Topología - Temas 1-2",
            "teorema": "Espacios Conexos y Homeomorfismos",
            "hipotesis_rota": "La conexidad es un invariante topológico absoluto",
            "nombre_contraejemplo": "Eliminación de puntos en ℝ frente a ℝ^2",
            "definicion_formal": "Espacio X \\ {x}",
            "explicacion_detallada": "Si eliminamos un punto de la recta real ℝ, el espacio resultante deja de ser conexo. Sin embargo, si eliminamos un punto de ℝ^2, el plano sigue siendo conexo, demostrando rigurosamente que ℝ y ℝ^2 no pueden ser homeomorfos."
        },
        {
            "tema": "Topología - Temas 1-2",
            "teorema": "Interior y Adherencia bajo Aplicaciones",
            "hipotesis_rota": "Una aplicación continua no transforma necesariamente conjuntos cerrados en cerrados",
            "nombre_contraejemplo": "f(x) = sin(x) de ℝ en [-1, 1]",
            "definicion_formal": "f: ℝ → ℝ con f(x) = sin(x)",
            "explicacion_detallada": "El dominio completo ℝ es cerrado. Su imagen directa es el intervalo cerrado [-1, 1], pero funciones continuas acotadas en dominios abiertos pueden mapear cerrados en conjuntos no cerrados."
        },
        {
            "tema": "Topología - Temas 1-2",
            "teorema": "Espacios Métricos Completos y Homeomorfismos",
            "hipotesis_rota": "La completitud métrica no es un invariante topológico",
            "nombre_contraejemplo": "(0, 1) homeomorfo a ℝ",
            "definicion_formal": "f(x) = tan(π(x - 1/2))",
            "explicacion_detallada": "El intervalo abierto (0, 1) no es un espacio métrico completo. Sin embargo, es homeomorfo a todo el espacio ℝ, que sí es completo. Esto prueba que la completitud depende de la métrica y no de la topología."
        },
        {
            "tema": "Topología - Temas 1-2",
            "teorema": "Topología Inducida y Separabilidad",
            "hipotesis_rota": "Todo subespacio de un espacio separable es separable",
            "nombre_contraejemplo": "Subespacios discretos no separables en la recta de Sorgenfrey",
            "definicion_formal": "Subespacio no separable en (ℝ, τ_S)",
            "explicacion_detallada": "Aunque ℝ con la topología de Sorgenfrey es separable, existen subespacios dentro de la misma recta (como ciertos conjuntos no numerables con la topología discreta inducida) que no son separables."
        },
        {
            "tema": "Topología - Temas 1-2",
            "teorema": "Bases de Entornos y Primer Axioma en Subespacios",
            "hipotesis_rota": "La herencia de propiedades de contabilidad en subespacios",
            "nombre_contraejemplo": "Subespacio 1AN que preserva bases locales",
            "definicion_formal": "Si X es 1AN, todo subespacio Y ⊂ X es 1AN",
            "explicacion_detallada": "Si ℬ(x) = {U_n} es una base de entornos numerable para un punto x en X, entonces la familia {U_n ∩ Y} constituye una base de entornos numerable para x en el subespacio Y."
        },
        {
            "tema": "Topología - Temas 1-2",
            "teorema": "Fronteras y Clausuras en Topologías",
            "hipotesis_rota": "La clausura de una unión infinita no es la unión de las clausuras",
            "nombre_contraejemplo": "Familia de intervalos abiertos en ℝ",
            "definicion_formal": "Cl(⋃_{n=1}^∞ A_n) frente a ⋃_{n=1}^∞ Cl(A_n)",
            "explicacion_detallada": "Mientras que para una cantidad finita se cumple la igualdad, para una infinidad numerable de conjuntos abiertos la inclusión puede ser estricta, fallando la igualdad directa."
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
    
    busqueda = st.sidebar.text_input("🔍 Buscar Teorema o Contraejemplo:", placeholder="Ej. Sorgenfrey, Cesàro, Fibras...")
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
