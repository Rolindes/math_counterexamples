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

st.title("📐 Explorador Definitivo: +40 Contraejemplos y Ejercicios UPM")
st.markdown("Catálogo exhaustivo e interactivo basado en las relaciones de **Cálculo (1, 2 y 3)** y los bloques de **Topología General (Temas 1, 2 y 3 / Hoja 3)**.")

# Base de datos masiva con más de 40 entradas rigurosas
@st.cache_data
def load_data():
    data = [
        # ==========================================
        # CÁLCULO (RELACIONES 1, 2 y 3) -> ~20 ITEMS
        # ==========================================
        {
            "tema": "Cálculo - Rel. 1 (Reales)",
            "teorema": "Falacia en Simplificación Algebraica",
            "hipotesis_rota": "Cancelar factores algebraicos nulos (división entre cero)",
            "nombre_contraejemplo": "Demostración falsa de 2 = 1",
            "definicion_formal": "Si x = y, entonces x^2 = xy => x^2 - y^2 = xy - y^2 => (x-y)(x+y) = y(x-y) => x+y = y => 2y = y => 2 = 1",
            "explicacion_detallada": "Basado en Relación 1 (Ej. 1)[cite: 89]: El error radica en pasar de (x-y)(x+y) = y(x-y) a x+y = y dividiendo entre (x-y). Como se asumió x = y, entonces x-y = 0, lo cual constituye una división ilegal por cero[cite: 89]."
        },
        {
            "tema": "Cálculo - Rel. 1 (Reales)",
            "teorema": "Manipulación incorrecta de Desigualdades",
            "hipotesis_rota": "Operar con inecuaciones sin estudiar el signo del denominador",
            "nombre_contraejemplo": "Falacia de (x+1)/(x-1) >= 1",
            "definicion_formal": "(x+1)/(x-1) >= 1 => x+1 >= x-1 => 1 >= -1",
            "explicacion_detallada": "Basado en Relación 1 (Ej. 2)[cite: 89]: Multiplicar por x-1 requiere conocer su signo. Al no restringir el dominio, se opera de forma inválida, llevando a conclusiones erróneas para valores como x = -1[cite: 89]."
        },
        {
            "tema": "Cálculo - Rel. 1 (Reales)",
            "teorema": "Caracterización del Cero con Épsilon",
            "hipotesis_rota": "Condición épsilon-acotada estricta para números no nulos",
            "nombre_contraejemplo": "Demostración de x = 0",
            "definicion_formal": "Si 0 <= x < epsilon para todo epsilon > 0, entonces x = 0",
            "explicacion_detallada": "Basado en Relación 1 (Ej. 12)[cite: 89, 90]: Si x fuera estrictamente mayor que cero, podríamos elegir epsilon = x/2 > 0, lo cual contradice la hipótesis de que es menor que cualquier épsilon positivo[cite: 90]."
        },
        {
            "tema": "Cálculo - Rel. 1 (Reales)",
            "teorema": "Naturaleza de los Números Irracionales",
            "hipotesis_rota": "La suma o producto de irracionales no siempre es irracional",
            "nombre_contraejemplo": "Suma y producto de irracionales",
            "definicion_formal": "sqrt(2) + ( -sqrt(2) ) = 0 (Racional), o bien sqrt(2) * sqrt(2) = 2 (Racional)",
            "explicacion_detallada": "Basado en Relación 1 (Ej. 14)[cite: 90]: Mientras que sumar un racional con un irracional siempre da irracional, la suma o el producto de dos números irracionales puede resultar perfectamente en un número racional[cite: 90]."
        },
        {
            "tema": "Cálculo - Rel. 1 (Reales)",
            "teorema": "Existencia de Elementos bajo el Supremo",
            "hipotesis_rota": "La existencia de un elemento en el conjunto estrictamente menor que s y mayor que s - épsilon",
            "nombre_contraejemplo": "Conjuntos discretos o acotados singulares",
            "definicion_formal": "Dado s = sup A y epsilon > 0, ¿existe a en A tal que s - epsilon < a < s?",
            "explicacion_detallada": "Basado en Relación 1 (Ej. 17)[cite: 91]: Si A es un conjunto finito, el supremo pertenece al conjunto y no se pueden encontrar elementos estrictamente intermedios menores que el propio máximo[cite: 91]."
        },
        {
            "tema": "Cálculo - Rel. 1 (Reales)",
            "teorema": "Desigualdades Estrictas en Suma de Conjuntos",
            "hipotesis_rota": "Las cotas de subconjuntos finitos indexados pueden ser estrictas",
            "nombre_contraejemplo": "Conjuntos finitos C frente a A + B",
            "definicion_formal": "C = {x_1 + y_1, ..., x_n + y_n}, donde sup C <= sup A + sup B de forma estricta",
            "explicacion_detallada": "Basado en Relación 1 (Ej. 18-19)[cite: 91]: Aunque para conjuntos generales se cumple la igualdad en supremos e ínfimos, al restringirnos a sumas puntuales indexadas finitas las desigualdades pueden cumplirse estrictamente[cite: 91]."
        },
        {
            "tema": "Cálculo - Rel. 2 (Sucesiones)",
            "teorema": "Convergencia del Valor Absoluto",
            "hipotesis_rota": "El recíproco no es cierto: |a_n| convergente no implica a_n convergente",
            "nombre_contraejemplo": "Sucesión Alternada a_n = (-1)^n",
            "definicion_formal": "a_n = (-1)^n",
            "explicacion_detallada": "Basado en Relación 2 (Ej. 2)[cite: 92]: El valor absoluto |(-1)^n| = 1 es una sucesión constante que converge a 1[cite: 92]. Sin embargo, la sucesión original oscila perpetuamente entre -1 y 1, por lo que diverge[cite: 92]."
        },
        {
            "tema": "Cálculo - Rel. 2 (Sucesiones)",
            "teorema": "Suma de Sucesiones Convergente y No Convergente",
            "hipotesis_rota": "La suma de una sucesión convergente y una divergente es siempre divergente",
            "nombre_contraejemplo": "{x_n} convergente y {y_n} divergente",
            "definicion_formal": "x_n = 1/n (converge a 0) y y_n = (-1)^n (diverge)",
            "explicacion_detallada": "Basado en Relación 2 (Ej. 3)[cite: 92]: La suma x_n + y_n resulta en una sucesión oscilante que no converge[cite: 92]. Si x_n tiende a un límite no nulo, el producto x_n * y_n también diverge[cite: 92]."
        },
        {
            "tema": "Cálculo - Rel. 2 (Sucesiones)",
            "teorema": "Conservación de Límites en Intervalos Abiertos",
            "hipotesis_rota": "El límite de una sucesión en un intervalo abierto puede caer en la frontera",
            "nombre_contraejemplo": "Sucesión en el intervalo abierto (0, 1)",
            "definicion_formal": "a_n = 1/n en (0, 1) con lim a_n = 0",
            "explicacion_detallada": "Basado en Relación 2 (Ej. 5)[cite: 92]: Si a_n está en [0, 1] cerrado, el límite pertenece al intervalo[cite: 92]. Si el intervalo es abierto (0, 1), la sucesión está contenida pero su límite (0) está en la frontera exterior del intervalo abierto[cite: 92]."
        },
        {
            "tema": "Cálculo - Rel. 2 (Sucesiones)",
            "teorema": "Convergencia en Media (Teorema de Cesàro)",
            "hipotesis_rota": "S_n/n converge a l pero el término general a_n no converge",
            "nombre_contraejemplo": "Sucesión a_n = (-1)^n",
            "definicion_formal": "S_n = a_1 + ... + a_n, donde lim (S_n/n) = 0",
            "explicacion_detallada": "Basado en Relación 2 (Ej. 11)[cite: 92, 93]: Aunque a_n diverge[cite: 92], la media aritmética de sus sumas parciales S_n/n converge a 0[cite: 93]. El recíproco es falso[cite: 93]."
        },
        {
            "tema": "Cálculo - Rel. 2 (Sucesiones)",
            "teorema": "Subsucesiones Convergentes y Límite Único",
            "hipotesis_rota": "Convergencia conjunta de subsucesiones pares, impares y múltiplos de 3",
            "nombre_contraejemplo": "Sucesión con subsucesiones {u_2n}, {u_2n+1} y {u_3n} convergentes",
            "definicion_formal": "Subsucesiones de índices entrelazados que convergen al mismo punto",
            "explicacion_detallada": "Basado en Relación 2 (Ej. 14)[cite: 94]: Si las subsucesiones u_2n, u_2n+1 y u_3n convergen todas al mismo límite l, entonces la sucesión completa u_n converge necesariamente a l[cite: 94]."
        },
        {
            "tema": "Cálculo - Rel. 2 (Sucesiones)",
            "teorema": "Sucesiones Definidas por Recurrencia",
            "hipotesis_rota": "La convergencia depende estrictamente del término inicial x_1",
            "nombre_contraejemplo": "7x_{n+1} = x_n^3 + 6",
            "definicion_formal": "Evolución de límites según x_1 = 1/2, 3/2 o 5/2",
            "explicacion_detallada": "Basado en Relación 2 (Ej. 17)[cite: 94]: Dependiendo del valor de partida x_1, la sucesión recurrente puede converger a puntos fijos diferentes o divergir hacia el infinito[cite: 94]."
        },
        {
            "tema": "Cálculo - Rel. 3 (Series)",
            "teorema": "Condición Necesaria de Convergencia",
            "hipotesis_rota": "Que el término general a_n tienda a 0 no garantiza que la serie converja",
            "nombre_contraejemplo": "Serie Armónica sum (1/n)",
            "definicion_formal": "sum_{n=1}^infty (1/n)",
            "explicacion_detallada": "Basado en Relación 3 (Ej. 1)[cite: 95]: El término general tiende a 0 cuando n -> infinity. No obstante, las sumas parciales crecen de forma logarítmica y la serie diverge[cite: 95]."
        },
        {
            "tema": "Cálculo - Rel. 3 (Series)",
            "teorema": "Cociente de Series con Términos Positivos",
            "hipotesis_rota": "Si sum a_n diverge, la serie modificada a_n / (1 + a_n) puede no divergir",
            "nombre_contraejemplo": "Modificación de series divergentes",
            "definicion_formal": "sum a_n diverge => sum [a_n / (1 + a_n)]",
            "explicacion_detallada": "Basado en Relación 3 (Ej. 4)[cite: 95, 96]: Analiza el comportamiento de series con términos positivos donde el cociente modificado altera el carácter de divergencia original[cite: 95, 96]."
        },
        {
            "tema": "Cálculo - Rel. 3 (Series)",
            "teorema": "Convergencia Absoluta frente a Condicional",
            "hipotesis_rota": "Series alternadas que convergen pero fallan en hacerlo en valor absoluto",
            "nombre_contraejemplo": "Serie armónica alternada sum [(-1)^n / ln(n+1)]",
            "definicion_formal": "sum_{n=1}^infty [(-1)^n / ln(n+1)]",
            "explicacion_detallada": "Basado en Relación 3 (Ej. 6)[cite: 96]: Por el criterio de Leibniz, la serie converge condicionalmente; sin embargo, en valor absoluto se convierte en la serie armónica logarítmica divergente[cite: 96]."
        },
        {
            "tema": "Cálculo - Rel. 3 (Series)",
            "teorema": "Series con Signos Alternados y Polinomios",
            "hipotesis_rota": "Decrecimiento y tendencia a cero en términos racionales con signos alternados",
            "nombre_contraejemplo": "sum (-1)^n (a + n) / n^2",
            "definicion_formal": "sum_{n=1}^infty (-1)^n * [(a + n) / n^2]",
            "explicacion_detallada": "Basado en Relación 3 (Ej. 6b)[cite: 96]: Dependiendo del parámetro a >= 0, la serie estudia su convergencia condicional o absoluta mediante el criterio de Leibniz y comparación directa[cite: 96]."
        },
        {
            "tema": "Cálculo - Rel. 3 (Series)",
            "teorema": "Series Trigonométricas con Parámetros",
            "hipotesis_rota": "Convergencia condicionada por ángulos reales x",
            "nombre_contraejemplo": "sum [sin(nx) / n^2]",
            "definicion_formal": "sum_{n=1}^infty [sin(nx) / n^2]",
            "explicacion_detallada": "Basado en Relación 3 (Ej. 6d)[cite: 96]: Mediante el criterio de Weierstrass (m-test) con la serie armónica p-ádica sum (1/n^2), se demuestra que converge absoluta y uniformemente para todo x real[cite: 96]."
        },
        {
            "tema": "Cálculo - Rel. 3 (Series)",
            "teorema": "Sucesiones de Cauchy en Espacios Métricos",
            "hipotesis_rota": "Acotación de diferencias sucesivas que garantizan la condición de Cauchy",
            "nombre_contraejemplo": "|x_{n+1} - x_n| <= r^n con 0 < r < 1",
            "definicion_formal": "Sucesión real con acotación exponencial decreciente",
            "explicacion_detallada": "Basado en Relación 2 (Ej. 19)[cite: 94]: Demuestra mediante la desigualdad triangular y suma geométrica que cualquier sucesión que satisfaga esta acotación geométrica es de Cauchy y, por ende, convergente en R[cite: 94]."
        },
        {
            "tema": "Cálculo - Rel. 3 (Series)",
            "teorema": "Series Telescópicas y Sumas Exactas",
            "hipotesis_rota": "Cancelación de términos intermedios en sumas parciales",
            "nombre_contraejemplo": "sum [1 / (n(n+1))]",
            "definicion_formal": "sum_{n=1}^infty [1 / (n(n+1))] = sum [1/n - 1/(n+1)]",
            "explicacion_detallada": "Basado en Relación 3 (Ej. 2)[cite: 95]: Al descomponer en fracciones simples, los términos se cancelan telescópicamente dejando únicamente el primer término, resultando en una suma exacta igual a 1[cite: 95]."
        },
        {
            "tema": "Cálculo - Rel. 3 (Series)",
            "teorema": "Criterio de la Raíz y del Cociente en Casos Límite",
            "hipotesis_rota": "Indeterminación cuando el límite del cociente o raíz es exactamente igual a 1",
            "nombre_contraejemplo": "Series con cociente unitario límite",
            "definicion_formal": "lim (a_{n+1}/a_n) = 1",
            "explicacion_detallada": "Basado en Relación 3 (Ej. 1)[cite: 95]: Cuando el criterio del cociente arroja un límite igual a 1 (como ocurre en las series p-ádicas), el criterio no decide, requiriendo métodos más finos como Raabe o Gauss[cite: 95]."
        },

        # ==========================================
        # TOPOLOGÍA GENERAL (TEMAS 1, 2, 3 Y HOJA 3) -> ~20 ITEMS
        # ==========================================
        {
            "tema": "Topología - Hoja 3",
            "teorema": "Continuidad de la Aplicación Identidad",
            "hipotesis_rota": "La identidad entre espacios con distinta topología no es continua en ambas direcciones",
            "nombre_contraejemplo": "id: (R, tau_S) -> (R, tau_u) frente a su inversa",
            "definicion_formal": "id: (R, tau_u) -> (R, tau_S) y su recíproco",
            "explicacion_detallada": "Basado en Hoja 3 (Ej. 3)[cite: 97]: id: (R, tau_S) -> (R, tau_u) es continua porque todo abierto usual es abierto en Sorgenfrey[cite: 97]. En cambio, id: (R, tau_u) -> (R, tau_S) **no es continua en ningún punto** porque los básicos [a, b) no contienen entornos usuales simétricos[cite: 97]."
        },
        {
            "tema": "Topología - Hoja 3",
            "teorema": "Invarianza Topológica: La Continuidad NO Preserva la Acotación",
            "hipotesis_rota": "Una función continua con dominio acotado genera una imagen no acotada",
            "nombre_contraejemplo": "f(x) = 1/x en el intervalo acotado (0, 1]",
            "definicion_formal": "f: (0, 1] -> R con f(x) = 1/x",
            "explicacion_detallada": "Basado en propiedades de continuidad[cite: 97]: El dominio (0, 1] es acotado y la función es continua. No obstante, su imagen es [1, +infty), que es **no acotada**, demostrando que la acotación no es un invariante topológico[cite: 97]."
        },
        {
            "tema": "Topología - Hoja 3",
            "teorema": "Caracterización de Continuidad en Topología Cofinita",
            "hipotesis_rota": "Una función entre espacios cofinitos es continua si sus fibras son finitas",
            "nombre_contraejemplo": "Aplicación f con fibras infinitas",
            "definicion_formal": "f: (X, tau_cf) -> (Y, tau_cf) con f^{-1}({y}) infinito para algún y",
            "explicacion_detallada": "Basado en Hoja 3 (Ej. 6)[cite: 98]: f es continua en x si y solo si f^{-1}({y}) es finito para todo y != f(x)[cite: 98]. Globalmente, solo es continua si es constante o si todas sus fibras son finitas[cite: 98]."
        },
        {
            "tema": "Topología - Hoja 3",
            "teorema": "Topología de Rayos a Izquierda (tau_<-)",
            "hipotesis_rota": "Funciones continuas en topologías no Hausdorff son obligatoriamente monótonas",
            "nombre_contraejemplo": "f(x) = x^2, g(x) = floor(x) en (R, tau_<-)",
            "definicion_formal": "tau_<- = {emptyset, R} union {(-infty, a) | a in R}",
            "explicacion_detallada": "Basado en Hoja 3 (Ej. 7*)[cite: 98, 99]: Toda aplicación continua u: R -> R con esta topología es no decreciente[cite: 99]. Funciones como floor(x) presentan discontinuidades características debido a los saltos direccionales[cite: 98, 99]."
        },
        {
            "tema": "Topología - Hoja 3",
            "teorema": "Función Característica y Fronteras",
            "hipotesis_rota": "La continuidad de la función característica depende de la frontera del conjunto",
            "nombre_contraejemplo": "chi_Q (Función de Dirichlet) con topología discreta en {0, 1}",
            "definicion_formal": "chi_A(x) = 1 si x in A, y 0 si x not in A",
            "explicacion_detallada": "Basado en Hoja 3 (Ej. 4)[cite: 98]: Los puntos de discontinuidad de chi_A coinciden exactamente con la frontera Fr(A)[cite: 98]. Para A = Q en R, Fr(Q) = R, por lo que es discontinua en todo punto[cite: 98]."
        },
        {
            "tema": "Topología - Temas 1-2",
            "teorema": "Metrizabilidad y Axiomas de Numerabilidad",
            "hipotesis_rota": "Un espacio separable y 1-anumerable no es necesariamente metrizable ni 2-anumerable",
            "nombre_contraejemplo": "Recta de Sorgenfrey (R, tau_Sor)",
            "definicion_formal": "R dotada de la base de abiertos B_Sor = {[a, b) | a < b}",
            "explicacion_detallada": "Demostración: Las bases locales B(x) = {[x, x + 1/n)} son numerables (1AN) y Q es denso (separable)[cite: 21, 40, 44]. Sin embargo, no es 2-anumerable porque cualquier base debe contener un abierto básico con ínfimo en cada real a[cite: 44]. Como todo espacio métrico separable debe ser 2-anumerable, **no es metrizable**[cite: 34, 44]."
        },
        {
            "tema": "Topología - Temas 1-2",
            "teorema": "Axiomas de Separación (Hausdorff vs T1)",
            "hipotesis_rota": "Un espacio T1 no es necesariamente Hausdorff (T2) ni metrizable",
            "nombre_contraejemplo": "Topología Cofinita en un conjunto infinito (R, tau_cf)",
            "definicion_formal": "tau_cf = {U subset R | R \\ U is finite} unida con el vacío",
            "explicacion_detallada": "Demostración: Los cerrados propios son los conjuntos finitos[cite: 7]. Dados x != y, se pueden aislar de forma unilateral mediante complementarios finitos (es T1). No obstante, dos abiertos no vacíos cualesquiera tienen complementarios finitos, por lo que su intersección nunca puede ser vacía. Por tanto, **no es Hausdorff (T2)** y **no es metrizable**[cite: 31, 34, 47]."
        },
        {
            "tema": "Topología - Temas 1-2",
            "teorema": "Conexidad y Conexidad por Caminos",
            "hipotesis_rota": "Todo espacio conexo por caminos es conexo, pero el recíproco falla",
            "nombre_contraejemplo": "El Seno del Topólogo",
            "definicion_formal": "A = {(x, sin(1/x)) | x in (0, 1]} unida con el segmento vertical {(0, y) | y in [-1, 1]}",
            "explicacion_detallada": "Demostración: El conjunto es conexo por ser la adherencia de la gráfica de una función continua. Sin embargo, **no es conexo por caminos** porque ninguna curva continua puede unir el origen (0,0) con la curva oscilante sin que las infinitas oscilaciones rompan la continuidad en el límite[cite: 6, 10, 21]."
        },
        {
            "tema": "Topología - Temas 1-2",
            "teorema": "Axioma de Separación Hausdorff (T2)",
            "hipotesis_rota": "Espacios con bases locales simétricas que fallan en separar puntos globales",
            "nombre_contraejemplo": "La Recta de Dos Orígenes",
            "definicion_formal": "X = Rsqcup{*}, con base que duplica el punto 0 añadiendo entornos abiertos con dos orígenes",
            "explicacion_detallada": "Demostración: Los dos orígenes 0 y * comparten idénticos entornos básicos sin el punto central, haciendo imposible encontrar abiertos disjuntos que los separen. El espacio **no es Hausdorff**, por ende **no es metrizable**[cite: 34, 42, 45]."
        },
        {
            "tema": "Topología - Temas 1-2",
            "teorema": "Axiomas de Numerabilidad (1AN vs 2AN)",
            "hipotesis_rota": "Todo espacio 1-anumerable no es necesariamente 2-anumerable",
            "nombre_contraejemplo": "Espacio Discreto No Numerable (X, tau_dis)",
            "definicion_formal": "X es un conjunto infinito no numerable dotado de tau_dis = P(X)",
            "explicacion_detallada": "Demostración: Las bases locales de singletons B(x) = {{x}} son numerables, cumpliendo 1AN[cite: 20, 26]. No obstante, cualquier base de abiertos B debe contener obligatoriamente a todos los singletons {{x} | x in X}. Al ser X no numerable, B es no numerable, violando 2AN[cite: 23, 24]."
        },
        {
            "tema": "Topología - Hoja 3",
            "teorema": "Imagen Inversa de Abiertos y Continuidad",
            "hipotesis_rota": "La imagen inversa de un abierto es abierta, pero la imagen directa de un abierto no es necesariamente abierta",
            "nombre_contraejemplo": "Proyección o función constante/cuadrática",
            "definicion_formal": "f: X -> Y continua <=> f^{-1}(V) es abierto para todo V abierto en Y",
            "explicacion_detallada": "Basado en Hoja 3 (Ej. 2)[cite: 97]: Mientras la definición formal de continuidad exige que los abiertos tengan imagen inversa abierta, la imagen directa de un conjunto abierto mediante una función continua (ej. f(x) = x^2 en R) puede convertir un abierto en un intervalo no abierto[cite: 97]."
        },
        {
            "tema": "Topología - Hoja 3",
            "teorema": "Composición de Funciones Continuas en Puntos",
            "hipotesis_rota": "La continuidad puntual se propaga mediante composiciones",
            "nombre_contraejemplo": "g o f continua en a si f es continua en a y g en f(a)",
            "definicion_formal": "f: X -> Y continua en a, g: Y -> Z continua en f(a) => g o f continua en a",
            "explicacion_detallada": "Basado en Hoja 3 (Ej. 2c)[cite: 97]: Demostración directa utilizando bases de entornos o entornos abiertos anidados para probar que los entornos de z se retrotraen correctamente al dominio X[cite: 97]."
        },
        {
            "tema": "Topología - Hoja 3",
            "teorema": "Conjuntos de Nivel Abiertos y Cerrados",
            "hipotesis_rota": "Los conjuntos donde una función continua se anula o es positiva tienen propiedades topológicas fijas",
            "nombre_contraejemplo": "V_f = {x in X : f(x) = 0} y S_f = {x in X : f(x) > 0}",
            "definicion_formal": "f: X -> R continua con topología usual",
            "explicacion_detallada": "Basado en Hoja 3 (Ej. 5)[cite: 98]: V_f es siempre un conjunto cerrado en X por ser la imagen inversa del cerrado {0}. S_f es abierto por ser la imagen inversa del rayo abierto (0, +infty)[cite: 98]."
        },
        {
            "tema": "Topología - Temas 1-2",
            "teorema": "Espacios Compactos y Continuidad",
            "hipotesis_rota": "La imagen continua de un espacio compacto es compacta, pero el dominio no compacto puede fallar",
            "nombre_contraejemplo": "f(x) = arctan(x) de R a (-pi/2, pi/2)",
            "definicion_formal": "f: R -> (-pi/2, pi/2)",
            "explicacion_detallada": "Demostración: El dominio R no es compacto en la topología usual. Aunque la función es continua, su imagen es el intervalo abierto acotado (-pi/2, pi/2), que no es compacto en R (al no ser cerrado ni acotado en el sentido métrico tradicional)[cite: 35]."
        },
        {
            "tema": "Topología - Temas 1-2",
            "teorema": "Espacios Conexos y Homeomorfismos",
            "hipotesis_rota": "La conexidad es un invariante topológico absoluto",
            "nombre_contraejemplo": "Eliminación de puntos en R frente a R^2",
            "definicion_formal": "Espacio X con un punto extraído X \\ {x}",
            "explicacion_detallada": "Demostración: Si eliminamos un punto de la recta real R, el espacio resultante deja de ser conexo (se divide en dos componentes disjuntas). Sin embargo, si eliminamos un punto de R^2, el plano sigue siendo conexo, lo que demuestra rigurosamente que R y R^2 no pueden ser homeomorfos[cite: 35]."
        },
        {
            "tema": "Topología - Temas 1-2",
            "teorema": "Interior y Adherencia bajo Aplicaciones Abiertas",
            "hipotesis_rota": "Una aplicación continua no transforma necesariamente conjuntos cerrados en cerrados",
            "nombre_contraejemplo": "f(x) = sin(x) de R en [-1, 1]",
            "definicion_formal": "f: R -> R con f(x) = sin(x)",
            "explicacion_detallada": "Demostración: El dominio completo R es un conjunto cerrado en sí mismo. No obstante, su imagen directa bajo la función seno es el intervalo cerrado [-1, 1], pero si consideramos funciones continuas acotadas en dominios abiertos, la imagen de un cerrado puede dejar de ser cerrada (ej. f(x) = 1/(1+x^2) que mapea R cerrado en (0, 1] que no es cerrado)[cite: 35]."
        },
        {
            "tema": "Topología - Temas 1-2",
            "teorema": "Espacios Métricos Completos y Homeomorfismos",
            "hipotesis_rota": "La completitud métrica no es un invariante topológico",
            "nombre_contraejemplo": "(0, 1) homeomorfo a R",
            "definicion_formal": "f(x) = tan(pi * (x - 1/2))",
            "explicacion_detallada": "Demostración: El intervalo abierto (0, 1) con la métrica usual no es un espacio métrico completo (las sucesiones que se acercan a 0 o 1 no convergen dentro del espacio). Sin embargo, es homeomorfo a todo el espacio R, que sí es completo. Esto prueba que la completitud depende de la métrica y no de la topología intrínseca[cite: 35]."
        },
        {
            "tema": "Topología - Temas 1-2",
            "teorema": "Topología Inducida por Subespacios y Separabilidad",
            "hipotesis_rota": "Todo subespacio de un espacio separable es separable",
            "nombre_contraejemplo": "Recta de Sorgenfrey y subespacios discretos no separables",
            "definicion_formal": "Subespacio no separable en (R, tau_S)",
            "explicacion_detallada": "Demostración: Aunque R con la topología de Sorgenfrey es separable (contiene a Q denso), existen subespacios dentro de la misma recta (como ciertos conjuntos no numerables con la topología discreta inducida) que no son separables, demostrando que la separabilidad heredada no es universal para cualquier tipo de topología general[cite: 44]."
        },
        {
            "tema": "Topología - Temas 1-2",
            "teorema": "Bases de Entornos y Primer Axioma en Subespacios",
            "hipotesis_rota": "La herencia de propiedades de contabilidad en subespacios",
            "nombre_contraejemplo": "Subespacio 1AN que preserva bases locales",
            "definicion_formal": "Si X es 1AN, todo subespacio Y subset X es 1AN",
            "explicacion_detallada": "Demostración: Si B(x) = {U_n} es una base de entornos numerable para un punto x en X, entonces la familia de intersecciones {U_n cap Y} constituye una base de entornos numerable para x en el subespacio Y, cumpliendo rigurosamente la propiedad hereditaria de los espacios 1AN[cite: 26]."
        },
        {
            "tema": "Topología - Temas 1-2",
            "teorema": "Fronteras y Clausuras en Topologías Débiles",
            "hipotesis_rota": "La clausura de una unión infinita no es la unión de las clausuras",
            "nombre_contraejemplo": "Familia de intervalos abiertos en R",
            "definicion_formal": "Cl(union_{n=1}^infty A_n) vs union_{n=1}^infty Cl(A_n)",
            "explicacion_detallada": "Demostración: Mientras que para un número finito de conjuntos la clausura de la unión es la unión de las clausuras, para una infinidad numerable de conjuntos abiertos (como A_n = (1/n, 1)) la inclusión puede ser estricta, fallando la igualdad directa[cite: 35]."
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
    
    busqueda = st.sidebar.text_input("🔍 Buscar Teorema o Contraejemplo:", placeholder="Ej. Sorgenfrey, Cesàro, Falacia...")
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
                st.markdown(f"**Hipótesis que se rompe / Concepto:** ⚠️ _{row['hipotesis_rota']}_")
                st.markdown(f"**Definición / Ejemplo Formal:**")
                st.code(row['definicion_formal'], language="text")
            with col2:
                st.markdown(f"**Nivel:** Universitario (UPM)")
            
            st.markdown("---")
            st.markdown(f"**💡 Explicación y Demostración Detallada:**\n\n{row['explicacion_detallada']}")
