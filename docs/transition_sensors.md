#  Modelo de transição e modelos de sensores

O modelo de transição especifica a distribuição de probabilidade sobre as variáveis de estado mais recentes, dados os valores anteriores, ou seja, \( P(X_t | X_{0:t-1}) \). Aqui, usamos a suposição de Markov para que o estado atual dependa apenas de um número fixo e finito de estados anteriores. Os processos que atendem a essa premissa são chamados de processos de Markov ou cadeias de Markov. [1]

## Processo de Markov de primeira ordem

Aqui, o estado atual depende apenas do estado anterior e não de nenhum estado anterior. Em outras palavras, um estado fornece informações suficientes para tornar o futuro condicionalmente independente do passado. [1]

\[
P(X_t | X_{0:t-1}) = P(X_t | X_{t-1})
\]

- O modelo de transição é a distribuição condicional \( P(X_t | X_{t-1}) \).

## Processo de Markov de segunda ordem

Aqui, o estado atual depende de dois estados anteriores.

\[
P(X_t | X_{0:t-1}) = P(X_t | X_{t-2}, X_{t-1})
\]

- O modelo de transição para um processo de Markov de segunda ordem é a distribuição condicional \( P(X_t | X_{t-2}, X_{t-1}) \).

Para os processos de Markov, presumimos que as mudanças no estado do mundo são causadas por um processo homogêneo no tempo, ou seja, um processo de mudança que é regido por leis que não mudam com o tempo. [1]

## Pressuposto de Markov do sensor

\[
P(E_t | X_{0:t}, E_{1:t-1}) = P(E_t | X_t)
\]

- \( P(E_t | X_t) \) é o modelo de sensor (às vezes chamado de modelo de observação).
- As variáveis \( E_t \) podem depender de variáveis anteriores, bem como das variáveis do estado atual.

## Prior probability distribution at time 0

\[
P(X_{0:t}, E_{1:t}) = P(X_0) \prod_{i=1}^{t} P(X_i | X_{i-1}) P(E_i | X_i)
\]

- Modelo de estado inicial \( P(X_0) \) 
- O modelo de transição \( P(X_i | X_{i-1}) \) 
- Modelo de sensor \( P(E_i | X_i) \)

Essa equação define a semântica da família de modelos temporais representados pelos três termos.

**Há duas maneiras de melhorar a precisão da aproximação:**

- Aumentar a ordem do modelo do processo de Markov. [1]
- Aumentar o conjunto de variáveis de estado. [1]