# Inferência

A inferência em redes bayesianas envolve a resposta a consultas probabilísticas sobre a rede. Os tipos mais comuns de consultas são:

- **Marginalização:** Determinar a distribuição de probabilidade de um subconjunto de variáveis, ignorando os valores de todas as outras variáveis. [9]
- **Probabilidade condicional:** Computação da distribuição de probabilidade de um subconjunto de variáveis com base em evidências observadas em outras variáveis. [9]

Matematicamente, se X são as variáveis de consulta e E são as variáveis de evidência com valores observados e, o objetivo é calcular \[P(X \mid E = e)\].

## Inferência Exata

A inferência exata em redes bayesianas é um processo fundamental usado para calcular a distribuição de probabilidade de um subconjunto de variáveis, com base em evidências observadas em um conjunto de outras variáveis. [9]

### Métodos de inferência exata

#### Eliminação de variáveis

A eliminação de variáveis é uma técnica popular de inferência exata que resume sistematicamente as variáveis que não são de interesse. O processo envolve a manipulação e a combinação dos CPTs da rede para responder às consultas de forma eficiente. [9]

**Etapas:**

- **Fatoração:** Decompor a distribuição de probabilidade conjunta em um produto de fatores, cada um correspondendo a um CPT na rede. [9]
- **Eliminação:** Eliminar sequencialmente cada variável não relacionada à consulta e não relacionada à evidência, somando seus valores. Essa etapa reduz a dimensionalidade do problema. [9]
- **Normalização:** Após todas as eliminações, normalize a distribuição resultante para garantir que a soma seja igual a um. [9]

**Representação matemática:** Para calcular \[P(X \mid E = e)\], talvez seja necessário somar uma variável Z que não esteja em X ou E: \[P(X \mid E = e) = \alpha \sum_Z P(X, Z, E = e)\] em que α é uma constante de normalização. [9]

#### Algoritmo de árvore de junção

O Algoritmo de Árvore de Junção, também conhecido como Algoritmo de Árvore de Clique, é uma abordagem mais estruturada que converte a Rede Bayesiana em uma estrutura de árvore chamada “árvore de junção” ou “árvore de clique”, em que cada nó (clique) contém um subconjunto de variáveis que formam um subgrafo completo (totalmente conectado) na rede. [9]

**Etapas:**

- **Triangulação:** Modifique a rede para garantir que todo ciclo de quatro ou mais nós tenha uma corda (uma borda que não faz parte do ciclo, mas conecta dois nós do ciclo). [9]
- **Construção da árvore de junção:** Forme grupos de variáveis e organize-os em uma estrutura de árvore em que cada borda representa uma declaração de independência condicional. [9]
- **Passagem de mensagens:** Execute uma passagem de mensagens em duas fases (coleta e distribuição) para propagar informações por toda a árvore. [9]

**Representação matemática:** Durante a fase de passagem de mensagens, as mensagens (funções de probabilidades) são passadas entre os cliques. Se \( C_i \) e \( C_j \) são dois **cliques** conectados por um **separador**, a mensagem de \( C_i \) para \( C_j \) pode ser calculada como: [9]

\[
M_{i \rightarrow j}(S) = \sum_{C_i \setminus S} \phi_{C_i}(X_{C_i})
\]

- \( \phi_{C_i}(X_{C_i}) \) é o fator ou potencial associado ao clique \( C_i \).
- \( C_i \setminus S \) representa as variáveis de \( C_i \), excluindo as variáveis do separador \( S \).
- \( M_{i \rightarrow j}(S) \) é a mensagem passada do clique \( C_i \) para o clique \( C_j \).

#### Propagação de crença

A propagação de crenças (BP) é outro método de inferência exata usado principalmente em redes que formam uma estrutura de árvore ou que podem ser reestruturadas em uma forma de árvore usando o algoritmo de árvore de junção. Ele envolve a passagem de mensagens entre os nós e usa essas mensagens para calcular as probabilidades marginais em cada nó. [9]

**Etapas:**

- **Inicialização:** Cada nó inicializa as mensagens com base em suas evidências locais e probabilidades condicionais. [9]
- **Passagem de mensagens:** Os nós enviam e recebem mensagens de e para seus vizinhos. Cada mensagem representa uma crença sobre o estado do remetente, condicionada às evidências. [9]
- **Atualização da crença:** cada nó atualiza sua crença com base nas mensagens recebidas e em sua probabilidade inicial. [9]

## Inferência aproximada

A inferência exata em redes bayesianas geralmente é impraticável do ponto de vista computacional para redes grandes ou complexas devido ao crescimento exponencial dos requisitos computacionais. Os métodos de inferência aproximada são uma alternativa viável, oferecendo estimativas probabilísticas com custos computacionais significativamente reduzidos. [10]

### Métodos de inferência aproximada

#### Métodos de Monte Carlo

Os métodos de Monte Carlo usam amostragem aleatória para aproximar sistemas matemáticos ou físicos complexos. O princípio é gerar um grande número de amostras aleatórias de uma distribuição de probabilidade e usar essas amostras para estimar as propriedades da distribuição. [10]

Esse processo envolve as seguintes etapas:

- **Definir o problema:** Identificar a quantidade a ser estimada (por exemplo, uma integral ou uma probabilidade). [10]
- **Gerar amostras aleatórias:** Use um gerador de números aleatórios para produzir amostras da distribuição de interesse. [10]
- **Calcular a estimativa:** Calcule a quantidade desejada usando as amostras geradas, geralmente calculando a média dos resultados dos dados amostrados. [10]

#### Inferência variacional

A inferência variacional transforma o problema da inferência em um problema de otimização. Em vez de fazer uma amostragem da distribuição posterior, ela aproxima a distribuição por uma distribuição mais simples e otimiza os parâmetros dessa distribuição para que fiquem o mais próximo possível da distribuição posterior verdadeira. [10]

As etapas envolvidas são:

- **Escolha de uma família de distribuições:** Selecionar uma família de distribuições parametrizadas por parâmetros variacionais. [10]
- **Definir o objetivo variacional:** Normalmente, é o Limite Inferior de Evidência (ELBO), que é otimizado para tornar a distribuição aproximada próxima da posterior verdadeira. [10]
- **Otimizar o ELBO:** Use a descida de gradiente ou outras técnicas de otimização para encontrar os melhores parâmetros. [10]

Matematicamente, o ELBO é definido como:

\[
\text{ELBO} = \mathbb{E}_{q(z)} \left[ \log p(x, z) - \log q(z) \right]
\]

- q(z) é a posterioridade aproximada. [10]
- p(x,z) é a probabilidade conjunta dos dados observados x e das variáveis latentes z. [10]

#### Propagação de crença ciclica

O Loopy Belief Propagation (LBP) amplia o algoritmo Belief Propagation para redes bayesianas com ciclos (loops). [10]

O algoritmo envolve as seguintes etapas:

- **Inicialização:** Inicializar as mensagens nas bordas da rede. [10]
- **Transmissão de mensagens:** Atualizar iterativamente as mensagens passadas entre os nós com base nas mensagens vizinhas. [10]
- **Atualização da crença:** calcular as crenças (probabilidades marginais) em cada nó com base nas mensagens recebidas. [10]

Apesar de seu nome, o LBP nem sempre converge, especialmente em redes com muitos loops. Os problemas de convergência podem surgir devido a oscilações ou divergências nas atualizações de mensagens. Quando o LBP converge, ele geralmente fornece boas aproximações das probabilidades marginais. [10]