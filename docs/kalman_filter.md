# Filtros de Kalman

O filtro de Kalman é um algoritmo usado para estimar o estado do sistema dinâmico a partir de uma série de medições com ruído. Ele é amplamente usado em vários campos, como robótica, navegação e finanças, para tarefas como rastreamento e previsão. O filtro de Kalman fornece um meio de combinar medições observadas com o conhecimento prévio sobre o sistema para produzir estimativas mais precisas. [13]

O filtro de Kalman é um algoritmo recursivo ideal que estima o estado do sistema dinâmico linear usando a série de medições com ruído. Ele opera em duas etapas: previsão e atualização. Na etapa de previsão, o algoritmo usa a estimativa do estado atual para prever o próximo estado. Na etapa de atualização, ele incorpora novas medições para refinar essa previsão, minimizando a média do erro quadrático. [13]

**Abordagem passo a passo:**

- **Defina as matrizes:** Configure a matriz de transição de estado (A), a matriz de controle (B), a matriz de observação (H), a covariância de ruído do processo (Q) e a covariância de ruído de medição (R). [13]
- **Estado inicial:** Inicialize a estimativa de estado e a matriz de covariância de erro. [13]
    - **Estimativa inicial do estado (X₀):** Melhor suposição do estado inicial.
    - **Matriz de covariância do erro inicial (P₀):** Define a incerteza inicial da estimativa.
- **Etapa de previsão:** Prever o próximo estado e a covariância usando o modelo de transição de estado. [13]
    - **Previsão do estado:** \[\hat{X}_t^- = A \hat{X}_{t-1} + B U_t\].
    - **Previsão da covariância:** \[P_t^- = A P_{t-1} A^T + Q\].
- **Etapa de atualização:** Incorporar a nova medição para atualizar a estimativa do estado e a covariância. [13]
    - \[K_t = P_t^- H^T (H P_t^- H^T + R)^{-1}\]
    - \[\hat{X}_t = \hat{X}_t^- + K_t (Z_t - H \hat{X}_t^-)\]
    - \[P_t = (I - K_t H) P_t^-\]
    - (\( K_t \)) e o Ganho de Kalman.
    - \[ Z_t - H \hat{X}_t^-\] é a inovação, ou erro de medição.
- **Repetir:** Iterar as etapas de previsão e atualização para cada medição subsequente. [13]