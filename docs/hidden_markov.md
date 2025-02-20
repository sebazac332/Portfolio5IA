# Modelo Oculto de Markov

É um modelo estatístico usado para descrever a relação probabilística entre uma sequência de observações e uma sequência de estados ocultos. Ike é frequentemente usado em situações em que o sistema ou processo subjacente que gera as observações é desconhecido ou oculto, daí o nome “Modelo de Markov Oculto”.  [12]

Um HMM consiste em dois tipos de variáveis: estados ocultos e observações.

- Os estados ocultos são as variáveis subjacentes que geram os dados observados, mas não são diretamente observáveis. [12]
- As observações são as variáveis que são medidas e observadas. [12]

A relação entre os estados ocultos e as observações é modelada usando uma distribuição de probabilidade. O modelo de Markov oculto (HMM) é a relação entre os estados ocultos e as observações usando dois conjuntos de probabilidades: as probabilidades de transição e as probabilidades de emissão. [12]

- As probabilidades de transição descrevem a probabilidade de transição de um estado oculto para outro. [12]
- As probabilidades de emissão descrevem a probabilidade de observar uma saída em um estado oculto. [12]

## Algoritmo do modelo de Markov oculto

- **Etapa 1:** Definir o espaço de estado e o espaço de observação: O espaço de estado é o conjunto de todos os estados ocultos possíveis, e o espaço de observação é o conjunto de todas as observações possíveis. [12]
- **Etapa 2:** definir a distribuição do estado inicial: Essa é a distribuição de probabilidade sobre o estado inicial. [12]
- **Etapa 3:** definir as probabilidades de transição de estado: Essas são as probabilidades de transição de um estado para outro. Isso forma a matriz de transição, que descreve a probabilidade de passar de um estado para outro. [12]
- **Etapa 4:** definir as probabilidades de observação: Essas são as probabilidades de gerar cada observação de cada estado. Isso forma a matriz de emissão, que descreve a probabilidade de gerar cada observação de cada estado. [12]
- **Etapa 5:** Treinar o modelo: Os parâmetros das probabilidades de transição de estado e as probabilidades de observação são estimados usando o algoritmo Baum-Welch ou o algoritmo forward-backward. Isso é feito por meio da atualização iterativa dos parâmetros até a convergência. [12]
- **Etapa 6:** Decodificar a sequência mais provável de estados ocultos: Com base nos dados observados, o algoritmo de Viterbi é usado para calcular a sequência mais provável de estados ocultos. Isso pode ser usado para prever observações futuras, classificar sequências ou detectar padrões em dados sequenciais. [12]
- **Etapa 7:** Avaliar o modelo: O desempenho do HMM pode ser avaliado por meio de várias métricas, como exatidão, precisão, recall ou pontuação F1. [12]

# Algoritmos Matriciais Simplificados​

**Probability of a transition from state i to state j**

\[
T_{i,j} = P(X_t = j \mid X_{t-1} = i)
\]

- A variável de estado \( X_t \) tem valores denotados por números inteiros 1, . . . ,S.
- S é o número de estados possíveis.
- O modelo de transição \( P(X_t | X_{t-1}) \) torna-se uma matriz S×S T.

Podemos fazer o mesmo com o modelo de sensor;, neste caso, como o valor da variável de evidência \( E_t \) é conhecida no tempo t, precisamos especificar para cada estado apenas, a probabilidade que o estado faz com que \( e_t \) apareça, ou seja, \( P(e_t | X_t = i) \)para cada estado i. [1]

Para tanto, criamos a matriz de observação Ot de dimensões SxS, uma para cada passo, a i-ésima entrada diagonal de \( O_t \) é \( P(e_t | X_t = i) \) e as outras entradas são 0.​ [1]

**Equação de avanço:**

\[
f_{1:t+1} = \alpha O_{t+1} T^\top f_{1:t}
\]


- \( f_{1:t} \) é a distribuição para frente até o tempo \( t \).
- \( T \) é a matriz de transição entre estados.
- \( O_{t+1} \) é a matriz de observação.
- \( \alpha \) é um fator de normalização.
​
**Equação regressiva**

\[
b_{k+1:t} = T O_{k+1} b_{k+2:t}
\]

- \( b_{k+1:t} \) é a distribuição para trás a partir do tempo \( k+1 \).
- \( T \) é a matriz de transição.
- \( O_{k+1} \) é a matriz de observação no tempo \( k+1 \).