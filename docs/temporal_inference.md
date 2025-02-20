# Inferência em modelos temporais

Os modelos temporais desempenham um papel fundamental na análise e previsão de fenômenos dependentes do tempo. Eles capturam relações dinâmicas e dependências entre variáveis ao longo do tempo, o que os torna indispensáveis em áreas como finanças, saúde e ciência climática. A inferência em modelos temporais envolve a estimativa de estados ocultos, parâmetros de modelos e observações futuras com base em dados observados. [11]

## Principais componentes dos modelos temporais:

- **Estados:** Representam as possíveis condições do sistema em diferentes momentos. [11]
- **Observações:** São os pontos de dados que são medidos ou percebidos diretamente. [11]
- **Transições:** São as probabilidades de um estado para outro ao longo do tempo. [11]
- **Emissões:** São as probabilidades de observar determinados dados, considerando o estado do sistema. [11]

## Tipos de modelos temporais

- **Modelos autorregressivos (AR):** Esses modelos preveem valores futuros com base em uma combinação linear de valores passados da variável. A ordem do modelo (denotada como p) indica quantos valores passados são considerados. [11]
- **Modelos de média móvel (MA):** Os modelos de média móvel usam erros de previsão anteriores em um modelo semelhante a uma regressão. Ele pressupõe que a variável de saída depende linearmente dos valores atuais e de vários valores anteriores dos termos estocásticos (determinados aleatoriamente). [11]
- **Média móvel integrada autorregressiva (ARIMA):** Os modelos ARIMA combinam termos autorregressivos e termos de média móvel e incluem diferenciação para tornar a série temporal estacionária (ou seja, a média, a variância e a autocorrelação são constantes ao longo do tempo). [11]
- **ARIMA sazonal (SARIMA):** Amplia o ARIMA adicionando elementos sazonais ao modelo, que são importantes para conjuntos de dados com padrões sazonais claros. [11]
- **Modelos de Markov ocultos (HMMs):** São modelos estatísticos em que o sistema que está sendo modelado é considerado um processo de Markov com estados não observados (ocultos). Os HMMs são particularmente conhecidos por sua aplicação no reconhecimento de padrões temporais, como fala, escrita à mão, reconhecimento de gestos, marcação de parte da fala e bioinformática. [11]
- **Redes Bayesianas Dinâmicas (DBNs):** São modelos para dados de séries temporais que generalizam as redes bayesianas para processos dinâmicos. Diferentemente das redes bayesianas simples, as DBNs podem representar dependências condicionais entre diferentes pontos de tempo. [11]
- **Modelos de espaço de estado e filtros de Kalman:** Esses são modelos recursivos que estimam o estado do sistema dinâmico linear a partir de uma série de medições com ruído. São amplamente usados em engenharia, especialmente para processamento de sinais e sistemas de controle. [11]

## Métodos de inferência para modelos temporais

### Filtragem

É a tarefa de calcular o estado de crença \( P(X_t | e_{1:t}) \), a distribuição posterior sobre o estado mais recente, considerando todas as evidências até o momento. Filtragem é o que um agente racional faz para manter o controle do estado atual, de modo que decisões racionais possam ser tomadas. [1] Isso é particularmente útil no processamento em tempo real, em que o estado precisa ser estimado à medida que novos dados são recebidos. [11]

**Representação matemática:**

\[
P(X_t | O_1, O_2, ..., O_t)
\]

- \( X_t \)  é o estado no momento t.
- \( O_1, O_2, ..., O_t \)  são as observações até o momento t.

**Implementação:**

- **Inicialização:** Comece com uma distribuição de probabilidade inicial para o primeiro estado. [11]
- **Recursão:** Atualizar a probabilidade do estado usando as probabilidades de transição e a nova observação. [11]

**Métodos comuns de filtragem:**

- **Filtro de Kalman:** Um filtro recursivo eficiente para modelos lineares de espaço de estado gaussiano que minimiza o erro quadrático médio. [11]
- **Filtro de Kalman estendido (EKF):** Uma extensão não linear do filtro de Kalman que lineariza os modelos de estado e observação em torno da estimativa atual. [11]
- **Filtro de partículas:** Um método Monte Carlo sequencial que aproxima a distribuição posterior dos estados ocultos usando amostras ponderadas, adequado para modelos não lineares e não gaussianos. [11]

### Predição

Essa é a tarefa de calcular a distribuição posterior sobre o estado futuro, Previsão, considerando todas as evidências até o momento. Ou seja, queremos calcular \( P(X_{t+k} | e_{1:t}) \) para algum k > 0. A previsão é útil para avaliar possíveis cursos de ação com base em seus resultados esperados. [1]

**Representação matemática:**

\[
P(X_{t+k} | O_1, O_2, ..., O_t)
\]

- k é o número de etapas à frente do tempo atual t.

**Tipos de previsão:**

- **Previsão de um passo à frente:** Prevê a próxima observação com base na estimativa do estado atual. [11]
- **Previsão em várias etapas:** Estende o horizonte de previsão ao prever várias observações futuras, geralmente usando métodos iterativos ou modelando diretamente as dependências de várias etapas. [11]

**Fórmula de filtragem e previsão:**

\[
P(X_{t+1} | e_{1:t+1}) = \alpha P(e_{t+1} | X_{t+1}) \sum_{x_t} P(X_{t+1} | x_t, e_{1:t}) P(x_t | e_{1:t})
\]

### Suavização

Essa é a tarefa de calcular a distribuição posterior sobre um estado passado, considerando todas as evidências até o presente. Ou seja, desejamos calcular \( P(X_k | e_{1:t}) \) para algum k tal que 0 ≤ k < t. A suavização fornece uma estimativa melhor do estado no momento k, pois incorpora mais evidências. [1]

**Representação matemática:**

\[
P(X_t | O_1, O_2, ..., O_N)
\]

- N é o número total de observações.

**Representação mais detalhada:**

\[
P(e_{k+1:t} | X_k) = \sum_{x_{k+1}} P(e_{k+1} | x_{k+1}) P(e_{k+2:t} | x_{k+1}) P(x_{k+1} | X_k)
\]

**Métodos de suavização**

- **Suavizador de Kalman:** Amplia o filtro de Kalman para modelos gaussianos lineares para fornecer estimativas de estado suavizadas. [11]
- **Suavizador Rauch-Tung-Striebel (RTS):** Uma implementação específica do suavizador de Kalman que opera em duas passagens: filtragem para frente e suavização para trás. [11]
- **Suavização de atraso fixo:** estima estados ocultos com um atraso de tempo fixo, equilibrando precisão e eficiência computacional. [11]

### Explicação mais provável

Dada uma sequência de observações, podemos querer encontrar a sequência de estados com maior probabilidade de ter gerado essas observações. Ou seja, queremos calcular \( \arg\max_{x_{1:t}} P(x_{1:t} | e_{1:t}) \). Os algoritmos para essa tarefa são úteis em muitas aplicações, incluindo o reconhecimento de fala, em que o objetivo é encontrar a sequência mais provável de palavras, dada uma série de sons, e a reconstrução de cadeias de bits transmitidas por um canal com ruído. [1]

**Representação matemática:**

\[
\max_{X_1, ..., X_T} P(X_1, ..., X_T | O_1, ..., O_T)
\]

**Representação mais detalhada**

\[
m_{1:t+1} = P(e_{t+1} | X_{t+1}) \max_{x_{t}} P(X_{t+1} | x_{t}) \max_{x_{1:t-1}} P(x_{1:t-1}, x_{t}, e_{1:t})
\]

**Etapas de implementação:**

- **Inicialização:** Configurar as probabilidades iniciais do estado. [11]
- **Recursão:** Para cada estado, calcule a probabilidade máxima de cada estado que leva a ele. [11]
- **Encerramento:** Determine o estado final de probabilidade máxima e rastreie o caminho mais provável. [11]

### Aprendizado

Os modelos de transição e de sensor, se ainda não forem conhecidos, podem ser aprendidos com as observações. Assim como nas redes bayesianas estáticas, o aprendizado dinâmico da rede Bayes pode ser feito como um subproduto da inferência. A inferência fornece uma estimativa de quais transições realmente ocorreram e de quais estados geraram as leituras do sensor, e essas estimativas podem ser usadas para aprender os modelos. O processo de aprendizado pode operar por meio de um algoritmo de atualização iterativo chamado de maximização de expectativa ou EM, ou pode resultar da atualização bayesiana dos parâmetros do modelo com base nas evidências. [1]