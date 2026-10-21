import streamlit as st
import pandas as pd
import json
import os

# Configuración de la página
st.set_page_config(
    page_title="MathCounterexamples - Cálculo y Topología UPM", 
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

DB_FILE = "contraejemplos_50_totales.json"

# Base de datos masiva con los 50 contraejemplos puros (Cálculo y Topología)
DATOS_INICIALES = [
    # ==========================================
    # CÁLCULO - RELACIÓN 1 (NÚMEROS REALES) [1-10]
    # ==========================================
    {
        "tema": "Cálculo - Rel. 1 (Reales)",
        "afirmacion_falsa": "Si se cumple que x = y, es algebraicamente válido dividir entre (x-y) para concluir que x + y = y.",
        "contraejemplo_exacto": "Falacia de demostración algebraica de que 2 = 1.",
        "explicacion_detallada": "Falla porque al asumir x = y, se tiene que x - y = 0. Operar dividiendo entre (x-y) constituye una división ilegal por cero, generando conclusiones absurdas."
    },
    {
        "tema": "Cálculo - Rel. 1 (Reales)",
        "afirmacion_falsa": "Multiplicar una desigualdad por una variable genérica (x-1) preserva siempre el sentido de la inecuación.",
        "contraejemplo_exacto": "Inecuación (x+1)/(x-1) ≥ 1 que lleva erróneamente a 1 ≥ -1.",
        "explicacion_detallada": "Falla al no estudiar el signo del factor. Multiplicar una desigualdad por expresiones negativas invierte el sentido de la inecuación."
    },
    {
        "tema": "Cálculo - Rel. 1 (Reales)",
        "afirmacion_falsa": "La suma o el producto de dos números irracionales da siempre como resultado otro número irracional.",
        "contraejemplo_exacto": "Suma: √2 + (-√2) = 0 (racional). Producto: √2 · √2 = 2 (racional).",
        "explicacion_detallada": "El conjunto de los números irracionales no es cerrado ni respecto a la suma ni respecto al producto algebraico."
    },
    {
        "tema": "Cálculo - Rel. 1 (Reales)",
        "afirmacion_falsa": "Dado un conjunto acotado superiormente A y su supremo s = sup(A), siempre existe un elemento en A estrictamente menor que s y mayor que s - ε para cualquier conjunto finito.",
        "contraejemplo_exacto": "Conjunto finito A = {1, 2, 3} con supremo s = 3 y ε = 0.5.",
        "explicacion_detallada": "Si A es un conjunto finito, el supremo pertenece al propio conjunto (es su máximo), por lo que no existen elementos en A estrictamente intermedios entre 3 - 0.5 y 3."
    },
    {
        "tema": "Cálculo - Rel. 1 (Reales)",
        "afirmacion_falsa": "La función valor absoluto respeta siempre la suma estricta de intervalos sin desigualdad triangular estricta.",
        "contraejemplo_exacto": "Desigualdad triangular |a + b| ≤ |a| + |b| con a = 1 y b = -1.",
        "explicacion_detallada": "Se cumple con igualdad estricta en un lado, demostrando que la desigualdad puede no ser estricta para números de signos opuestos."
    },
    {
        "tema": "Cálculo - Rel. 1 (Reales)",
        "afirmacion_falsa": "El producto de dos cotas inferiores de un subconjunto no acotado es siempre otra cota inferior válida.",
        "contraejemplo_exacto": "Subconjuntos con elementos negativos amplificados al elevar al cuadrado.",
        "explicacion_detallada": "Elevar al cuadrado o multiplicar cotas negativas descoloca el orden de las desigualdades si no se estudian los signos."
    },
    {
        "tema": "Cálculo - Rel. 1 (Reales)",
        "afirmacion_falsa": "Todo subconjunto infinito de números reales acotado inferiormente posee un elemento mínimo dentro del conjunto.",
        "contraejemplo_exacto": "El intervalo abierto (0, 1) con cota inferior 0.",
        "explicacion_detallada": "Posee ínfimo (0), pero el 0 no pertenece al conjunto, por lo que carece de elemento mínimo."
    },
    {
        "tema": "Cálculo - Rel. 1 (Reales)",
        "afirmacion_falsa": "Si x^2 < y^2 para dos números reales, entonces x < y de forma universal.",
        "contraejemplo_exacto": "x = -3 e y = 1 ((-3)^2 = 9 y 1^2 = 1).",
        "explicacion_detallada": "Al trabajar con números negativos, elevar al cuadrado invierte las relaciones de orden si no se acotan los dominios a positivos."
    },
    {
        "tema": "Cálculo - Rel. 1 (Reales)",
        "afirmacion_falsa": "La unión de dos intervalos abiertos acotados es siempre un único intervalo abierto.",
        "contraejemplo_exacto": "(0, 1) ∪ (2, 3).",
        "explicacion_detallada": "La unión de conjuntos disjuntos genera un conjunto abierto desconectado formado por dos componentes conexas separadas."
    },
    {
        "tema": "Cálculo - Rel. 1 (Reales)",
        "afirmacion_falsa": "Cualquier número real no nulo admite una única representación decimal finita o infinita.",
        "contraejemplo_exacto": "El número 1 representado como 1.000... y como 0.9999...",
        "explicacion_detallada": "Los decimales infinitos periódicos en 9 admiten representaciones dobles equivalentes en el sistema real."
    },

    # ==========================================
    # CÁLCULO - RELACIÓN 2 (SUCESIONES) [11-20]
    # ==========================================
    {
        "tema": "Cálculo - Rel. 2 (Sucesiones)",
        "afirmacion_falsa": "Si el valor absoluto de una sucesión (|a_n|) converge, entonces la sucesión original (a_n) es obligatoriamente convergente.",
        "contraejemplo_exacto": "Sucesión alternada a_n = (-1)^n.",
        "explicacion_detallada": "El valor absoluto |(-1)^n| = 1 es una sucesión constante que converge a 1. Sin embargo, la sucesión original a_n oscila perpetuamente entre -1 y 1, por lo que diverge."
    },
    {
        "tema": "Cálculo - Rel. 2 (Sucesiones)",
        "afirmacion_falsa": "La suma de una sucesión convergente y una divergente da siempre como resultado una sucesión divergente a infinito.",
        "contraejemplo_exacto": "x_n = 1/n (converge a 0) y y_n = (-1)^n (oscila/diverge).",
        "explicacion_detallada": "La suma x_n + y_n resulta en una sucesión oscilante que no converge, pero tampoco diverge a infinito de forma estructurada."
    },
    {
        "tema": "Cálculo - Rel. 2 (Sucesiones)",
        "afirmacion_falsa": "Si una sucesión a_n está contenida estrictamente en un intervalo abierto (0, 1), su límite debe pertenecer obligatoriamente al interior del intervalo abierto.",
        "contraejemplo_exacto": "Sucesión a_n = 1/n ∈ (0, 1) con lim(a_n) = 0.",
        "explicacion_detallada": "El límite de una sucesión contenida en un conjunto abierto puede colapsar y caer exactamente en la frontera exterior del intervalo."
    },
    {
        "tema": "Cálculo - Rel. 2 (Sucesiones)",
        "afirmacion_falsa": "Si la media de Cesàro de una sucesión (S_n / n) converge, el término general a_n de la sucesión original también converge obligatoriamente.",
        "contraejemplo_exacto": "Sucesión a_n = (-1)^n.",
        "explicacion_detallada": "El término general a_n diverge oscilando, pero la media aritmética de sus sumas parciales S_n / n converge a 0. El recíproco del teorema de Cesàro es falso."
    },
    {
        "tema": "Cálculo - Rel. 2 (Sucesiones)",
        "afirmacion_falsa": "Toda sucesión acotada en ℝ posee un único punto de acumulación o límite.",
        "contraejemplo_exacto": "Sucesión oscilante a_n = (-1)^n.",
        "explicacion_detallada": "Posee dos puntos de acumulación distintos (-1 y 1), demostrando que la acotación no garantiza unicidad de límites subsucesionales."
    },
    {
        "tema": "Cálculo - Rel. 2 (Sucesiones)",
        "afirmacion_falsa": "Si una sucesión es de Cauchy, sus términos crecen indefinidamente en valor absoluto.",
        "contraejemplo_exacto": "Sucesión convergente a_n = 1/n.",
        "explicacion_detallada": "Toda sucesión de Cauchy en los números reales es convergente, por lo que está acotada y sus términos tienden a estabilizarse, no a crecer."
    },
    {
        "tema": "Cálculo - Rel. 2 (Sucesiones)",
        "afirmacion_falsa": "El producto de dos sucesiones divergentes es siempre una sucesión divergente.",
        "contraejemplo_exacto": "x_n = n y y_n = 1/n (ambas divergen conceptualmente o interactúan con ceros).",
        "explicacion_detallada": "Al multiplicar una sucesión que tiende a infinito por su inversa que tiende a cero, el producto puede converger perfectamente a 1."
    },
    {
        "tema": "Cálculo - Rel. 2 (Sucesiones)",
        "afirmacion_falsa": "Si a_n < b_n para todo n y ambas convergen, los límites cumplen estricta desigualdad lim(a_n) < lim(b_n).",
        "contraejemplo_exacto": "a_n = 0 y b_n = 1/n.",
        "explicacion_detallada": "Se cumple a_n < b_n para todo n positivo, pero al pasar al límite ambos convergen al mismo valor (0), perdiéndose la strictitud."
    },
    {
        "tema": "Cálculo - Rel. 2 (Sucesiones)",
        "afirmacion_falsa": "Toda sucesión monótona y acotada en ℝ puede converger a varios límites diferentes según la subsucesy.",
        "contraejemplo_exacto": "Sucesión monótona creciente a_n = 1 - 1/n.",
        "explicacion_detallada": "Por el teorema de convergencia monótona, toda sucesión monótona y acotada posee un límite único exacto (en este caso, 1)."
    },
    {
        "tema": "Cálculo - Rel. 2 (Sucesiones)",
        "afirmacion_falsa": "Si una sucesión no tiene límite, entonces no posee ninguna subsucesión convergente.",
        "contraejemplo_exacto": "Sucesión divergente oscilante acotada.",
        "explicacion_detallada": "Por el teorema de Bolzano-Weierstrass, toda sucesión acotada posee al menos una subsucesión convergente, aunque la sucesión general oscile."
    },

    # ==========================================
    # CÁLCULO - RELACIÓN 3 (SERIES) [21-30]
    # ==========================================
    {
        "tema": "Cálculo - Rel. 3 (Series)",
        "afirmacion_falsa": "Si el término general de una serie tiende a cero (lim a_n = 0), entonces la serie numérica converge obligatoriamente.",
        "contraejemplo_exacto": "La serie armónica clásica Σ (1/n).",
        "explicacion_detallada": "La condición lim a_n = 0 es estrictamente necesaria pero no suficiente. Las sumas parciales de la armónica crecen de forma logarítmica y divergen."
    },
    {
        "tema": "Cálculo - Rel. 3 (Series)",
        "afirmacion_falsa": "Si una serie con términos positivos Σ a_n diverge, la serie modificada Σ [a_n / (1 + a_n)] también diverge de forma obligatoria.",
        "contraejemplo_exacto": "Series divergentes de crecimiento extremadamente lento.",
        "explicacion_detallada": "El cociente modificado introduce un denominador que puede alterar y frenar el carácter de divergencia original de la serie."
    },
    {
        "tema": "Cálculo - Rel. 3 (Series)",
        "afirmacion_falsa": "Una serie alternada que converge condicionalmente también converge de manera absoluta al tomar valores absolutos.",
        "contraejemplo_exacto": "Serie armónica alternada Σ [(-1)^n / ln(n+1)].",
        "explicacion_detallada": "Por el criterio de Leibniz converge condicionalmente, pero al tomar valor absoluto se convierte en la serie armónica logarítmica, la cual diverge."
    },
    {
        "tema": "Cálculo - Rel. 3 (Series)",
        "afirmacion_falsa": "Si el criterio de la raíz o del cociente arroja un límite igual a 1, la serie converge de manera absoluta.",
        "contraejemplo_exacto": "Series armónicas con cociente límite igual a 1 (ej. Σ 1/n y Σ 1/n^2).",
        "explicacion_detallada": "Cuando el límite del cociente o de la raíz es exactamente igual a 1, el criterio no decide (caso de indeterminación), pudiendo ser tanto convergente como divergente."
    },
    {
        "tema": "Cálculo - Rel. 3 (Series)",
        "afirmacion_falsa": "Reordenar los términos de una serie convergente condicionalmente preserva siempre su suma exacta.",
        "contraejemplo_exacto": "Teorema de reordenamiento de Riemann con la serie armónica alternada.",
        "explicacion_detallada": "Mediante un reordenamiento adecuado de una serie convergente condicional, se puede conseguir que sume cualquier número real arbitrario o diverja a infinito."
    },
    {
        "tema": "Cálculo - Rel. 3 (Series)",
        "afirmacion_falsa": "La suma de dos series divergentes da siempre una serie divergente.",
        "contraejemplo_exacto": "Σ 1 y Σ (-1) combinadas.",
        "explicacion_detallada": "Al sumar término a término series divergentes de signos opuestos se pueden cancelar los crecimientos, generando sumas parciales acotadas o convergentes en casos patológicos."
    },
    {
        "tema": "Cálculo - Rel. 3 (Series)",
        "afirmacion_falsa": "Toda serie geométrica de razón r converge para cualquier valor real de r.",
        "contraejemplo_exacto": "Serie geométrica con razón r = 2.",
        "explicacion_detallada": "Una serie geométrica Σ r^n converge única y exclusivamente si el valor absoluto de la razón es estricta menor que uno (|r| < 1)."
    },
    {
        "tema": "Cálculo - Rel. 3 (Series)",
        "afirmacion_falsa": "Si una serie de términos positivos converge, la serie formada por sus cuadrados converge más lentamente.",
        "contraejemplo_exacto": "Serie p-ádica con p = 2 (Σ 1/n^2).",
        "explicacion_detallada": "Al elevar al cuadrado los términos de una serie convergente con a_n < 1, los términos decrecen mucho más rápido, acelerando la convergencia."
    },
    {
        "tema": "Cálculo - Rel. 3 (Series)",
        "afirmacion_falsa": "El criterio de comparación directa requiere que las series tengan términos negativos obligatoriamente.",
        "contraejemplo_exacto": "Series de términos positivos.",
        "explicacion_detallada": "El criterio de comparación directa está diseñado y formulado estrictamente para series de términos no negativos."
    },
    {
        "tema": "Cálculo - Rel. 3 (Series)",
        "afirmacion_falsa": "Una serie de potencias tiene un radio de convergencia nulo si no converge en ningún punto.",
        "contraejemplo_exacto": "Serie de potencias con radio R = 0 (ej. Σ n! x^n).",
        "explicacion_detallada": "Si el radio es R = 0, la serie converge únicamente en su centro x = 0, lo cual es perfectamente coherente y válido."
    },

    # ==========================================
    # TOPOLOGÍA - AXIOMAS DE SEPARACIÓN (T_i) [31-38]
    # ==========================================
    {
        "tema": "Topología - Axiomas de Separación (T_i)",
        "afirmacion_falsa": "Todo espacio topológico que cumple el axioma T_0 es necesariamente un espacio T_1.",
        "contraejemplo_exacto": "El espacio de Sierpinski (\\{0, 1\\}, \\{\\emptyset, \\{0\\}, \\{0, 1\\}\\}) o la Topología del Punto Particular.",
        "explicacion_detallada": "En el espacio de Sierpinski, dados 0 y 1, el abierto \\{0\\} contiene al 0 pero no al 1 (cumple T_0). Sin embargo, el punto 1 no posee ningún abierto que lo contenga sin incluir al 0, por lo que los singletons no son cerrados y **no es T_1**."
    },
    {
        "tema": "Topología - Axiomas de Separación (T_i)",
        "afirmacion_falsa": "Todo espacio topológico que cumple el axioma T_1 es obligatoriamente un espacio Hausdorff (T_2).",
        "contraejemplo_exacto": "Un conjunto infinito X dotado de la Topología Cofinita (X, \\tau_{cf}).",
        "explicacion_detallada": "Los cerrados propios son los conjuntos finitos. Como todo singleton es finito, es un cerrado, garantizando **T_1**. No obstante, dos abiertos no vacíos cualesquiera siempre se intersecan en un conjunto infinito, impidiendo hallar entornos disjuntos que separen dos puntos; por tanto, **no es T_2**."
    },
    {
        "tema": "Topología - Axiomas de Separación (T_i)",
        "afirmacion_falsa": "Todo espacio normal (T_4) es obligatoriamente un espacio metrizable.",
        "contraejemplo_exacto": "La Recta de Sorgenfrey (ℝ, \\tau_S).",
        "explicacion_detallada": "La recta de Sorgenfrey es un espacio normal (**T_4**). Sin embargo, se demuestra analíticamente que **no es metrizable**, ya que si lo fuera implicaría ser 2AN, condición que viola de forma flagrante."
    },
    {
        "tema": "Topología - Axiomas de Separación (T_i)",
        "afirmacion_falsa": "Todo espacio métrico o metrizable es un espacio compacto.",
        "contraejemplo_exacto": "La recta real ℝ con la métrica euclidiana usual.",
        "explicacion_detallada": "ℝ es un espacio métrico plenamente válido, pero no es compacto en la topología usual al carecer de acotación."
    },
    {
        "tema": "Topología - Axiomas de Separación (T_i)",
        "afirmacion_falsa": "En un espacio topológico no Hausdorff, los límites de las sucesiones convergentes son únicos.",
        "contraejemplo_exacto": "Espacio con Topología Indiscreta (X, \\tau_{indis}) con al menos dos puntos.",
        "explicacion_detallada": "Al no ser Hausdorff, los entornos de puntos distintos coinciden con todo el espacio, provocando que cualquier sucesión converja simultáneamente a absolutamente todos los puntos del espacio."
    },
    {
        "tema": "Topología - Axiomas de Separación (T_i)",
        "afirmacion_falsa": "Todo subespacio de un espacio Hausdorff es un espacio no Hausdorff.",
        "contraejemplo_exacto": "Subespacios de espacios Hausdorff.",
        "explicacion_detallada": "Falso; cualquier subespacio de un espacio Hausdorff (T_2) es automáticamente Hausdorff, heredando la propiedad de separación."
    },
    {
        "tema": "Topología - Axiomas de Separación (T_i)",
        "afirmacion_falsa": "Si un espacio topológico es T_1, sus puntos son necesariamente conjuntos abiertos.",
        "contraejemplo_exacto": "Topología usual en la recta real ℝ.",
        "explicacion_detallada": "En un espacio T_1 los puntos son cerrados, no abiertos (si fuesen abiertos discretos estaríamos ante la topología discreta)."
    },
    {
        "tema": "Topología - Axiomas de Separación (T_i)",
        "afirmacion_falsa": "Los espacios regulares (T_3) no pueden admitir bases numerables.",
        "contraejemplo_exacto": "Espacios métricos separables.",
        "explicacion_detallada": "Todos los espacios métricos son regulares (T_3) y normales (T_4), y muchos de ellos poseen bases numerables de forma nativa."
    },

    # ==========================================
    # TOPOLOGÍA - SEPARABILIDAD Y METRIZABILIDAD [39-44]
    # ==========================================
    {
        "tema": "Topología - Separabilidad y Metrizabilidad",
        "afirmacion_falsa": "Todo espacio topológico separable (con subconjunto denso numerable) es necesariamente un espacio metrizable.",
        "contraejemplo_exacto": "La Recta de Sorgenfrey (ℝ, \\tau_S) o la Topología Cofinita.",
        "explicacion_detallada": "El conjunto de los números racionales ℚ es denso en la recta de Sorgenfrey (es separable) y cumple 1AN. Sin embargo, **no es metrizable**, puesto que no es 2AN."
    },
    {
        "tema": "Topología - Separabilidad y Metrizabilidad",
        "afirmacion_falsa": "Todo espacio metrizable es obligatoriamente un espacio separable.",
        "contraejemplo_exacto": "Un conjunto no numerable X dotado de la Métrica Discreta (X, d_{dis}).",
        "explicacion_detallada": "El espacio métrico discreto sobre un conjunto no numerable es perfectamente metrizable. No obstante, al ser cada punto abierto, el único subconjunto denso es el espacio total, impidiendo poseer un subconjunto denso numerable; por tanto, **no es separable**."
    },
    {
        "tema": "Topología - Separabilidad y Metrizabilidad",
        "afirmacion_falsa": "Todo subespacio de un espacio separable es siempre un espacio separable.",
        "contraejemplo_exacto": "Subespacios discretos no numerables inmersos dentro de la Recta de Sorgenfrey.",
        "explicacion_detallada": "Aunque el espacio total (ℝ con Sorgenfrey) es separable gracias a ℚ, existen subespacios dentro de la misma recta que, al inducir la topología discreta de forma no numerable, pierden por completo la separabilidad."
    },
    {
        "tema": "Topología - Separabilidad y Metrizabilidad",
        "afirmacion_falsa": "La completitud métrica es una propiedad estrictamente topológica (invariante por homeomorfismos).",
        "contraejemplo_exacto": "El intervalo abierto (0, 1) homeomorfo a la recta real ℝ.",
        "explicacion_detallada": "(0, 1) no es completo como espacio métrico usual. Sin embargo, es homeomorfo a ℝ, que sí es completo. Esto demuestra que la completitud depende de la métrica, no de la topología."
    },
    {
        "tema": "Topología - Separabilidad y Metrizabilidad",
        "afirmacion_falsa": "Toda bola abierta en un espacio métrico arbitrario es un conjunto cerrado.",
        "contraejemplo_exacto": "Bolas abiertas en espacios métricos generales (por ejemplo, en ℝ).",
        "explicacion_detallada": "La bola abierta B(0; 1) en ℝ es el intervalo (-1, 1), cuyo conjunto cerrado correspondiente (clausura) es [-1, 1]. Al ser distintos, la bola abierta no es cerrada."
    },
    {
        "tema": "Topología - Separabilidad y Metrizabilidad",
        "afirmacion_falsa": "La clausura de una bola abierta en cualquier espacio métrico coincide siempre exactamente con el disco cerrado del mismo radio y centro.",
        "contraejemplo_exacto": "Espacios con Métrica Discreta (X, d_{dis}).",
        "explicacion_detallada": "Bajo la métrica discreta con radio ε = 1, la bola abierta B(x; 1) es únicamente el conjunto {x}, cuya adherencia es {x}. No obstante, la bola cerrada D(x; 1) es todo el espacio X."
    },

    # ==========================================
    # TOPOLOGÍA - AXIOMAS DE CONTABILIDAD Y PROPIEDADES [45-50]
    # ==========================================
    {
        "tema": "Topología - Contabilidad (1AN y 2AN)",
        "afirmacion_falsa": "Todo espacio topológico que cumple el primer axioma de contabilidad (1AN) cumple también el segundo axioma de contabilidad (2AN).",
        "contraejemplo_exacto": "Espacio Discreto No Numerable (X, \\tau_{dis}) donde X es infinito no numerable.",
        "explicacion_detallada": "Las bases locales de singletons son numerables, cumpliendo 1AN. No obstante, cualquier base de abiertos debe contener a todos los singletons; al ser X no numerable, la base total es no numerable, violando 2AN."
    },
    {
        "tema": "Topología - Contabilidad (1AN y 2AN)",
        "afirmacion_falsa": "Todo espacio topológico que cumple el segundo axioma de contabilidad (2AN) es 1AN.",
        "contraejemplo_exacto": "Cualquier espacio 2AN (como ℝ con la topología usual).",
        "explicacion_detallada": "La implicación sí es cierta (toda base numerable general contiene bases locales numerables para cada punto). El error común es creer que 1AN implica 2AN."
    },
    {
        "tema": "Topología - Compacidad y Conexidad",
        "afirmacion_falsa": "Todo espacio topológico conexo por caminos es obligatoriamente un espacio compacto.",
        "contraejemplo_exacto": "La recta real (ℝ, \\tau_u) o el espacio euclidiano ℝ^n.",
        "explicacion_detallada": "ℝ es conexo por caminos porque cualquier par de puntos se une mediante un segmento lineal continuo. Sin embargo, no es compacto al carecer de acotación."
    },
    {
        "tema": "Topología - Compacidad y Conexidad",
        "afirmacion_falsa": "Todo espacio topológico compacto es necesariamente metrizable.",
        "contraejemplo_exacto": "Espacio compacto con topología indiscreta (X, \\tau_{indis}) con más de un punto.",
        "explicacion_detallada": "Es compacto debido a la finitud de abiertos en la topología indiscreta. No obstante, al no ser Hausdorff (T_2), incumple una condición indispensable de los espacios métricos, por lo que no es metrizable."
    },
    {
        "tema": "Topología - Compacidad y Conexidad",
        "afirmacion_falsa": "Todo espacio topológico conexo es obligatoriamente un espacio conexo por caminos.",
        "contraejemplo_exacto": "El Seno del Topólogo.",
        "explicacion_detallada": "El conjunto es conexo por ser la adherencia de la gráfica de una función continua. Sin embargo, no es conexo por caminos porque ninguna curva continua puede unir el origen con la gráfica oscilante sin romper la continuidad."
    },
    {
        "tema": "Topología - Topologías Especiales",
        "afirmacion_falsa": "En la topología del punto particular (X, \\tau_p), los puntos distintos de p son conjuntos cerrados.",
        "contraejemplo_exacto": "Singletons \\{x\\} con x ≠ p en (X, \\tau_p).",
        "explicacion_detallada": "El complementario de \\{x\\} contiene obligatoriamente al punto particular p. Por definición de \\tau_p, todo conjunto que contenga a p es abierto, haciendo que su complementario sea abierto y, por ende, \\{x\\} sea un conjunto abierto y no cerrado."
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

st.title("📐 Catálogo Masivo (50 Contraejemplos): Cálculo y Topología UPM")
st.markdown("Repositorio completo con exactamente 50 contraejemplos puros y rigurosos de Cálculo y Topología.")

# --- BARRA LATERAL: NAVEGACIÓN Y FILTROS ---
st.sidebar.header("🧭 Filtros de Búsqueda")

temas_disponibles = ['Todos los Bloques'] + list(df['tema'].unique())
tema_seleccionado = st.sidebar.selectbox("📂 Selecciona la Materia o Bloque:", temas_disponibles)

if tema_seleccionado != 'Todos los Bloques':
    df_filtrado = df[df['tema'] == tema_seleccionado]
else:
    df_filtrado = df

busqueda = st.sidebar.text_input("🔍 Buscar Contraejemplo:", placeholder="Ej. Sorgenfrey, Cesàro, T1, Series...")
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
        nuevo_tema = st.text_input("Bloque / Materia", placeholder="Ej. Cálculo - Rel. 3 (Series)")
        nueva_afirmacion = st.text_input("Afirmación Falsa", placeholder="Ej. Toda serie...")
        nuevo_contra = st.text_input("Contraejemplo Exacto", placeholder="Ej. Serie armónica...")
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
        st.markdown(f"**Bloque / Materia:** `{row['tema']}`")
        st.markdown(f"**⚡ Contraejemplo Exacto:**")
        st.code(row['contraejemplo_exacto'], language="text")
        st.markdown("---")
        st.markdown(f"**💡 ¿Por qué falla la afirmación?**\n\n{row['explicacion_detallada']}")
