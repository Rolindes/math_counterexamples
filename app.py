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

# Base de datos masiva y completa con más de 40 elementos (Cálculo y Topología UPM)
DATOS_INICIALES = [
    # ==========================================
    # CÁLCULO - RELACIÓN 1 (REALES)
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
        "tema": "Cálculo - Rel. 1 (Reales)",
        "teorema": "Manipulación Incorrecta de Desigualdades",
        "hipotesis_rota": "Operar con inecuaciones multiplicando por variables sin estudiar su signo",
        "nombre_contraejemplo": "Falacia con (x+1)/(x-1) ≥ 1",
        "definicion_formal": "(x+1)/(x-1) ≥ 1 ⇒ x+1 ≥ x-1 ⇒ 1 ≥ -1",
        "explicacion_detallada": "Multiplicar por (x-1) requiere conocer su signo. Al no restringir el dominio, se opera de forma inválida, llevando a conclusiones erróneas para valores donde el denominador es negativo[cite: 89]."
    },
    {
        "tema": "Cálculo - Rel. 1 (Reales)",
        "teorema": "Caracterización del Cero con Épsilon",
        "hipotesis_rota": "Condición épsilon-acotada estricta para números no nulos",
        "nombre_contraejemplo": "Demostración de que x = 0",
        "definicion_formal": "Si 0 ≤ x < ε para todo ε > 0, entonces x = 0",
        "explicacion_detallada": "Si x fuera estrictamente mayor que cero, podríamos elegir ε = x/2 > 0, lo cual contradice la hipótesis de que es menor que cualquier épsilon positivo[cite: 89, 90]."
    },
    {
        "tema": "Cálculo - Rel. 1 (Reales)",
        "teorema": "Naturaleza de los Números Irracionales",
        "hipotesis_rota": "La suma o producto de irracionales no siempre es un número irracional",
        "nombre_contraejemplo": "Suma y producto algebraico de irracionales",
        "definicion_formal": "√2 + (-√2) = 0 ∈ ℚ, o bien √2 · √2 = 2 ∈ ℚ",
        "explicacion_detallada": "Mientras que sumar un racional con un irracional siempre da irracional, la suma o el producto de dos números irracionales puede resultar perfectamente en un número racional[cite: 90]."
    },
    {
        "tema": "Cálculo - Rel. 1 (Reales)",
        "teorema": "Existencia de Elementos bajo el Supremo",
        "hipotesis_rota": "La existencia de un elemento en el conjunto estrictamente menor que s y mayor que s - ε",
        "nombre_contraejemplo": "Conjuntos discretos o acotados singulares",
        "definicion_formal": "Dado s = sup A y ε > 0, ¿existe a ∈ A tal que s - ε < a < s?",
        "explicacion_detallada": "Si A es un conjunto finito, el supremo pertenece al conjunto y no se pueden encontrar elementos estrictamente intermedios menores que el propio máximo[cite: 91]."
    },
    {
        "tema": "Cálculo - Rel. 1 (Reales)",
        "teorema": "Desigualdades Estrictas en Suma de Conjuntos",
        "hipotesis_rota": "Las cotas de subconjuntos finitos indexados pueden ser estrictas",
        "nombre_contraejemplo": "Conjuntos finitos C frente a A + B",
        "definicion_formal": "C = {x_1 + y_1, ..., x_n + y_n}, donde sup C ≤ sup A + sup B de forma estricta",
        "explicacion_detallada": "Aunque para conjuntos generales se cumple la igualdad en supremos e ínfimos, al restringirnos a sumas puntuales indexadas finitas las desigualdades pueden cumplirse estrictamente[cite: 91]."
    },

    # ==========================================
    # CÁLCULO - RELACIÓN 2 (SUCESIONES)
    # ==========================================
    {
        "tema": "Cálculo - Rel. 2 (Sucesiones)",
        "teorema": "Convergencia del Valor Absoluto",
        "hipotesis_rota": "El recíproco no es cierto: |a_n| convergente no implica que a_n sea convergente",
        "nombre_contraejemplo": "Sucesión alternada a_n = (-1)^n",
        "definicion_formal": "a_n = (-1)^n",
        "explicacion_detallada": "El valor absoluto |(-1)^n| = 1 es una sucesión constante que converge a 1. Sin embargo, la sucesión original oscila perpetuamente entre -1 y 1, por lo que diverge[cite: 92]."
    },
    {
        "tema": "Cálculo - Rel. 2 (Sucesiones)",
        "teorema": "Suma de Sucesiones Convergente y No Convergente",
        "hipotesis_rota": "La suma de una sucesión convergente y una divergente es siempre divergente",
        "nombre_contraejemplo": "x_n convergente y y_n divergente",
        "definicion_formal": "x_n = 1/n (converge a 0) y y_n = (-1)^n (diverge)",
        "explicacion_detallada": "La suma x_n + y_n resulta en una sucesión oscilante que no converge. Si x_n tiende a un límite no nulo, el producto x_n y_n también diverge[cite: 92]."
    },
    {
        "tema": "Cálculo - Rel. 2 (Sucesiones)",
        "teorema": "Conservación de Límites en Intervalos Abiertos",
        "hipotesis_rota": "El límite de una sucesión contenida en un intervalo abierto puede caer en la frontera",
        "nombre_contraejemplo": "Sucesión en el intervalo abierto (0, 1)",
        "definicion_formal": "a_n = 1/n ∈ (0, 1) con lim a_n = 0",
        "explicacion_detallada": "Si a_n ∈ [0, 1] cerrado, el límite pertenece al intervalo. Si el intervalo es abierto (0, 1), la sucesión está contenida pero su límite (0) está en la frontera exterior[cite: 92]."
    },
    {
        "tema": "Cálculo - Rel. 2 (Sucesiones)",
        "teorema": "Convergencia en Media (Teorema de Cesàro)",
        "hipotesis_rota": "S_n / n converge a l, pero el término general a_n no necesariamente converge",
        "nombre_contraejemplo": "Sucesión a_n = (-1)^n",
        "definicion_formal": "S_n = a_1 + ... + a_n, donde lim (S_n / n) = 0",
        "explicacion_detallada": "Aunque a_n diverge, la media aritmética de sus sumas parciales S_n / n converge a 0. El recíproco es falso[cite: 92, 93]."
    },
    {
        "tema": "Cálculo - Rel. 2 (Sucesiones)",
        "teorema": "Subsucesiones Convergentes y Límite Único",
        "hipotesis_rota": "Convergencia conjunta de subsucesiones pares, impares y múltiplos de 3",
        "nombre_contraejemplo": "Sucesión con subsucesiones u_{2n}, u_{2n+1} y u_{3n} convergentes",
        "definicion_formal": "Subsucesiones de índices entrelazados que convergen al mismo punto",
        "explicacion_detallada": "Si las subsucesiones u_{2n}, u_{2n+1} y u_{3n} convergen todas al mismo límite l, entonces la sucesión completa u_n converge necesariamente a l[cite: 94]."
    },
    {
        "tema": "Cálculo - Rel. 2 (Sucesiones)",
        "teorema": "Sucesiones Definidas por Recurrencia",
        "hipotesis_rota": "La convergencia depende estrictamente del valor de partida x_1",
        "nombre_contraejemplo": "7x_{n+1} = x_n^3 + 6",
        "definicion_formal": "Evolución de límites según x_1 = 1/2, 3/2 o 5/2",
        "explicacion_detallada": "Dependiendo del valor inicial x_1, la sucesión recurrente puede converger a puntos fijos diferentes o divergir hacia el infinito[cite: 94]."
    },

    # ==========================================
    # CÁLCULO - RELACIÓN 3 (SERIES)
    # ==========================================
    {
        "tema": "Cálculo - Rel. 3 (Series)",
        "teorema": "Condición Necesaria de Convergencia en Series",
        "hipotesis_rota": "Que el término general a_n tienda a 0 no garantiza que la serie converja",
        "nombre_contraejemplo": "Serie Armónica Σ (1/n)",
        "definicion_formal": "Σ_{n=1}^∞ (1/n)",
        "explicacion_detallada": "El término general tiende a 0 cuando n → ∞. No obstante, las sumas parciales crecen de forma logarítmica y la serie diverge[cite: 95]."
    },
    {
        "tema": "Cálculo - Rel. 3 (Series)",
        "teorema": "Cociente de Series con Términos Positivos",
        "hipotesis_rota": "Si Σ a_n diverge, la serie modificada a_n / (1 + a_n) puede no divergir",
        "nombre_contraejemplo": "Modificación de series divergentes",
        "definicion_formal": "Σ a_n diverge ⇒ Σ [a_n / (1 + a_n)]",
        "explicacion_detallada": "Analiza el comportamiento de series con términos positivos donde el cociente modificado altera el carácter de divergencia original[cite: 95, 96]."
    },
    {
        "tema": "Cálculo - Rel. 3 (Series)",
        "teorema": "Convergencia Absoluta frente a Condicional",
        "hipotesis_rota": "Series alternadas que convergen pero fallan en hacerlo en valor absoluto",
        "nombre_contraejemplo": "Serie armónica alternada Σ [(-1)^n / ln(n+1)]",
        "definicion_formal": "Σ_{n=1}^∞ [(-1)^n / ln(n+1)]",
        "explicacion_detallada": "Por el criterio de Leibniz, la serie converge condicionalmente; sin embargo, en valor absoluto se convierte en la serie armónica logarítmica divergente[cite: 96]."
    },
    {
        "tema": "Cálculo - Rel. 3 (Series)",
        "teorema": "Series con Signos Alternados y Polinomios",
        "hipotesis_rota": "Decrecimiento y tendencia a cero en términos racionales con signos alternados",
        "nombre_contraejemplo": "Σ (-1)^n (a + n) / n^2",
        "definicion_formal": "Σ_{n=1}^∞ (-1)^n [(a + n) / n^2], (a ≥ 0)",
        "explicacion_detallada": "Dependiendo del parámetro a, la serie estudia su convergencia condicional o absoluta mediante el criterio de Leibniz[cite: 96]."
    },
    {
        "tema": "Cálculo - Rel. 3 (Series)",
        "teorema": "Series Trigonométricas con Parámetros",
        "hipotesis_rota": "Convergencia condicionada por ángulos reales x",
        "nombre_contraejemplo": "Σ [sin(nx) / n^2]",
        "definicion_formal": "Σ_{n=1}^∞ [sin(nx) / n^2], (x ∈ ℝ)",
        "explicacion_detallada": "Mediante el criterio de Weierstrass con la serie p-ádica Σ (1/n^2), se demuestra que converge absoluta y uniformemente para todo x real[cite: 96]."
    },
    {
        "tema": "Cálculo - Rel. 3 (Series)",
        "teorema": "Sucesiones de Cauchy en Espacios Métricos",
        "hipotesis_rota": "Acotación de diferencias sucesivas que garantizan la condición de Cauchy",
        "nombre_contraejemplo": "|x_{n+1} - x_n| ≤ r^n con 0 < r < 1",
        "definicion_formal": "Sucesión real con acotación exponencial decreciente",
        "explicacion_detallada": "Demuestra mediante la desigualdad triangular y suma geométrica que cualquier sucesión que satisfaga esta acotación geométrica es de Cauchy y, por ende, convergente[cite: 94]."
    },
    {
        "tema": "Cálculo - Rel. 3 (Series)",
        "teorema": "Series Telescópicas y Sumas Exactas",
        "hipotesis_rota": "Cancelación de términos intermedios en sumas parciales",
        "nombre_contraejemplo": "Σ [1 / (n(n+1))]",
        "definicion_formal": "Σ_{n=1}^∞ [1 / (n(n+1))] = Σ [1/n - 1/(n+1)]",
        "explicacion_detallada": "Al descomponer en fracciones simples, los términos se cancelan telescópicamente dejando únicamente el primer término, resultando en una suma exacta igual a 1[cite: 95]."
    },

    # ==========================================
    # TOPOLOGÍA - HOJA 1 Y MÉTRICAS ESPECIALES
    # ==========================================
    {
        "tema": "Topología - Hoja 1 (Métricas)",
        "teorema": "Métrica Discreta y Triángulo Equilátero",
        "hipotesis_rota": "En espacios métricos generales, la noción geométrica de triángulo equilátero se cumple bajo la métrica discreta",
        "nombre_contraejemplo": "Espacio con Métrica Discreta d_dis",
        "definicion_formal": "d_dis(x,y) = 1 si x ≠ y, y 0 si x = y",
        "explicacion_detallada": "Para cualesquiera x, y, z en X distintos, se cumple siempre que d_dis(x,y) = d_dis(x,z) = d_dis(y,z) = 1, haciendo que 'todo triángulo sea equilátero'[cite: 99]."
    },
    {
        "tema": "Topología - Hoja 1 (Métricas)",
        "teorema": "Métrica de Correos (Post Office Metric)",
        "hipotesis_rota": "Espacio métrico donde las distancias pasan obligatoriamente por el origen fijado",
        "nombre_contraejemplo": "Métrica de Correos d_C en ℝ^n",
        "definicion_formal": "d_C(x,y) = 0 si x=y, y d_2(x,0) + d_2(0,y) si x ≠ y",
        "explicacion_detallada": "Modifica la geometría euclidiana clásica obligando a que cualquier trayecto entre dos puntos distintos pase de forma obligatoria por el origen de coordenadas[cite: 99]."
    },
    {
        "tema": "Topología - Hoja 1 (Métricas)",
        "teorema": "Invalidez de Métricas con Exponentes Menores que 1",
        "hipotesis_rota": "La desigualdad triangular falla cuando el exponente p es estrictamente menor que 1",
        "nombre_contraejemplo": "Métrica d_{1/2} en ℝ^n",
        "definicion_formal": "d_{1/2}(x,y) = ( Σ |x_i - y_i|^{1/2} )^2",
        "explicacion_detallada": "Falla la desigualdad triangular para p en (0, 1) en dimensiones n ≥ 2, por lo que d_{1/2} no constituye una distancia matemática válida[cite: 100, 102]."
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
        "definicion_formal": "A es cerrado ⟺ ∂A ⊆ A  //  A es abierto ⟺ ∂A ∩ A = ∅  //  Abierto y cerrado ⟺ ∂A = ∅",
        "explicacion_detallada": "Basado en Hoja 2 (Ejercicio 23)[cite: 107]: Un conjunto es cerrado si y solo si contiene a toda su frontera. Es abierto si su frontera está completamente disjunta de él. Si la frontera es vacía, el conjunto es simultáneamente abierto y cerrado[cite: 107]."
    },

    # ==========================================
    # TOPOLOGÍA - AXIOMAS (1AN, 2AN, T_i, SEPARABILIDAD Y METRIZABILIDAD)
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
        "explicacion_detallada": "Basado en Hoja 3 (Ejercicio 34)[cite: 118]: Las bases locales ℬ(x) = {[x, x + 1/n)} son numerables (1AN) y ℚ es denso (separable)[cite: 21, 40, 44]. Sin embargo, se demuestra por reducción al absurdo que si fuera metrizable, implicaría que es 2AN, lo cual es falso[cite: 44, 118]."
    },
    {
        "tema": "Topología - Axiomas de Separación (T_i)",
        "teorema": "Axioma T1 frente a Hausdorff (T2)",
        "hipotesis_rota": "Un espacio T1 no es necesariamente Hausdorff (T2) ni metrizable",
        "nombre_contraejemplo": "Topología Cofinita en un conjunto infinito (ℝ, τ_{cf})",
        "definicion_formal": "τ_{cf} = {U ⊂ ℝ | ℝ \\ U es finito} ∪ {∅}",
        "explicacion_detallada": "Basado en Hoja 3 (Ejercicio 13)[cite: 113]: Los cerrados propios son los conjuntos finitos[cite: 7]. Dados x ≠ y, se pueden aislar de forma unilateral mediante complementarios finitos (cumple T1). No obstante, dos abiertos no vacíos cualesquiera se intersecan, por lo que no es Hausdorff (T2) ni metrizable[cite: 31, 34, 47, 113]."
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
        "tema": "Topología - Axiomas de Numerabilidad",
        "teorema": "Axiomas de Numerabilidad (1AN vs 2AN)",
        "hipotesis_rota": "Todo espacio 1-anumerable no es necesariamente 2-anumerable",
        "nombre_contraejemplo": "Espacio Discreto No Numerable (X, τ_dis)",
        "definicion_formal": "X es un conjunto infinito no numerable dotado de τ_dis = 𝒫(X)",
        "explicacion_detallada": "Las bases locales de singletons ℬ(x) = {{x}} son numerables, cumpliendo 1AN[cite: 20, 26]. No obstante, cualquier base de abiertos ℬ debe contener obligatoriamente a todos los singletons {x}. Al ser X no numerable, ℬ es no numerable, violando 2AN[cite: 23, 24]."
    },

    # ==========================================
    # TOPOLOGÍA - TOPOLOGÍAS ESPECIALES Y PROPIEDADES (HOJAS 2 Y 3)
    # ==========================================
    {
        "tema": "Topología - Hoja 2 y 3 (Especiales)",
        "teorema": "Topología Divisor Z (τ_div)",
        "hipotesis_rota": "Topologías aritméticas basadas en divisores enteros que no provienen de métricas tradicionales",
        "nombre_contraejemplo": "Espacio (ℤ, τ_div) con bases de entornos basadas en divisores D(n)",
        "definicion_formal": "𝒩(n) = {U ⊆ ℤ | D(n) ⊆ U}",
        "explicacion_detallada": "Los cerrados corresponden a conjuntos que contienen a los múltiplos de todos sus elementos, estructurando una topología aritmética singular sobre los números enteros[cite: 105, 106]."
    },
    {
        "tema": "Topología - Hoja 2 y 3 (Especiales)",
        "teorema": "Topología con Espaciado Especial (Michael)",
        "hipotesis_rota": "Topología construida uniendo abiertos usuales con conjuntos de números irracionales",
        "nombre_contraejemplo": "Recta de Michael (ℝ, τ_M)",
        "definicion_formal": "τ_M = {U ∪ B | U ∈ τ_u, B ⊆ 𝕀}",
        "explicacion_detallada": "Modifica la recta usual permitiendo singletons abiertos en los puntos irracionales, alterando drásticamente las propiedades de contabilidad y separabilidad[cite: 112]."
    },
    {
        "tema": "Topología - Hoja 2 y 3 (Especiales)",
        "teorema": "Topología del Punto Particular",
        "hipotesis_rota": "Espacios topológicos donde un punto específico pertenece obligatoriamente a todo abierto no vacío",
        "nombre_contraejemplo": "Espacio (X, τ_p)",
        "definicion_formal": "τ_p = {∅} ∪ {U ⊆ X | p ∈ U}",
        "explicacion_detallada": "Genera un comportamiento topológico extremo donde las adherencias de conjuntos propios que no contienen al punto particular se colapsan al vacío[cite: 111]."
    },
    {
        "tema": "Topología - Propiedades Globales",
        "teorema": "Conexidad y Conexidad por Caminos",
        "hipotesis_rota": "Todo espacio conexo por caminos es conexo, pero el recíproco falla",
        "nombre_contraejemplo": "El Seno del Topólogo",
        "definicion_formal": "A = {(x, sin(1/x)) | x ∈ (0, 1]} ∪ {(0, y) | y ∈ [-1, 1]}",
        "explicacion_detallada": "El conjunto es conexo por ser la adherencia de la gráfica de una función continua. Sin embargo, no es conexo por caminos porque ninguna curva continua puede unir el origen (0,0) con la curva oscilante sin que las infinitas oscilaciones rompan la continuidad en el límite[cite: 6, 10, 21]."
    },
    {
        "tema": "Topología - Propiedades Globales",
        "teorema": "Continuidad de la Aplicación Identidad",
        "hipotesis_rota": "La identidad entre espacios con distinta topología no es continua en ambas direcciones",
        "nombre_contraejemplo": "id: (ℝ, τ_S) → (ℝ, τ_u) frente a su inversa",
        "definicion_formal": "id: (ℝ, τ_u) → (ℝ, τ_S) y su recíproco",
        "explicacion_detallada": "id: (ℝ, τ_S) → (ℝ, τ_u) es continua porque todo abierto usual es abierto en Sorgenfrey. En cambio, id: (ℝ, τ_u) → (ℝ, τ_S) no es continua en ningún punto porque los básicos [a, b) no contienen entornos usuales simétricos[cite: 97]."
    }
]

def load_data():
    df_inicial = pd.DataFrame(DATOS_INICIALES)
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            try:
                data_cargada = json.load(f)
                df_guardado = pd.DataFrame(data_cargada)
                # Unimos sin duplicar para asegurar que cargan los más de 40 elementos iniciales y los nuevos
                df_total = pd.concat([df_inicial, df_guardado]).drop_duplicates(subset=["teorema", "nombre_contraejemplo"]).reset_index(drop=True)
                return df_total
