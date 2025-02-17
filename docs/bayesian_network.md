# Redes Bayesianas​

Uma rede bayesiana é um modelo gráfico que exibe variáveis em um conjunto de dados e as independências probabilísticas ou condicionais entre elas. As relações causais entre os nós podem ser representadas por uma rede bayesiana; entretanto, os links na rede não representam necessariamente causa e efeito diretos. Por exemplo, uma rede bayesiana pode ser usada para calcular a probabilidade de um paciente ter uma doença específica, dada a presença ou ausência de determinados sintomas e outros dados relevantes, se as independências probabilísticas entre os sintomas e a doença, conforme exibidas no gráfico, forem verdadeiras. As redes são muito robustas quando faltam informações e fazem a melhor previsão possível usando qualquer informação presente. [9]

## Usos de redes bayesianas

- Seleção de oportunidades de empréstimo com baixo risco de inadimplência. [9]
- Estimativa de quando o equipamento precisará de manutenção, peças ou substituição, com base na entrada do sensor e nos registros existentes. [9]
- Resolução de problemas de clientes por meio de ferramentas de solução de problemas on-line. [9]
- Diagnosticar e solucionar problemas de redes de telefonia celular em tempo real. [9]
- Avaliar os possíveis riscos e recompensas de projetos de pesquisa e desenvolvimento para concentrar os recursos nas melhores oportunidades. [9]

## Fórmula

$$
P(x_1, x_2, \dots, x_n) = \prod_{i=1}^{n} P(x_i \mid \text{parents}(X_i))
$$

- Probabilidade conjunta das variáveis \( X_1, \dots, X_n \) pode ser fatorada como o produto das probabilidades condicionais de cada variável \( X_i \), dado o conjunto de seus pais no grafo de dependência.
- Aqui parents(Xi) denota os valores de Parents(Xi) que aparecem em \( X_1, \dots, X_n \), cada entrada na distribuição conjunta é representada pelo produto dos elementos apropriados das distribuições condicionais locais na rede de Bayes.​
- Suponha que uma rede de Bayes contenha \( n \) variáveis \( X_1, \dots, X_n \). Uma entrada genérica na distribuição conjunta é representada por \[P(X_1 = x_1 \wedge \dots \wedge X_n = x_n)\]. Ou, de forma abreviada \[P(x_1, \dots, x_n)\].

**Exemplo de uso:**

P(j,m,a,¬b,¬e) = P(j|a)P(m|a)P(a|¬b∧¬e)P(¬b)P(¬e) = 0.90 × 0.70 × 0.01 × 0.999 × 0.998 = 0.00628

Os números que entram nas distribuições condicionais locais \( \theta(x_i \mid \text{parents}(X_i)) \) são exatamente as probabilidades condicionais \[P(x_i \mid \text{parents}(X_i))\] implícitas na distribuição conjunta que podem ser calculadas a partir da distribuição conjunta da seguinte forma. [1]

\[
P(x_i \mid \text{parents}(X_i)) \equiv \frac{P(x_i, \text{parents}(X_i))}{P(\text{parents}(X_i))}
\]

Que pode ser expressa como:

\[
P(x_i \mid \text{parents}(X_i)) =
\frac{\sum_{y} P(x_i, \text{parents}(X_i), y)}
{\sum_{x'_i, y} P(x'_i, \text{parents}(X_i), y)}
\]

- Em que y representa os valores de todas as variáveis que não sejam Xi e seus pais.
- A partir dessa última linha, é possível provar que \[P(x_i \mid \text{parents}(X_i))\] = \( \theta(x_i \mid \text{parents}(X_i)) \)

Levando em conta estes dois pontos, pode-se dizer que:

\[
P(x_1, \dots, x_n) = \prod_{i=1}^{n} P(x_i \mid \text{parents}(X_i))
\]

## Construção de redes Bayesianas

Primeiro, reescrevemos as entradas na distribuição conjunta em termos de probabilidade condicional, usando a regra do produto. [1]

\[
P(x_1, \dots, x_n) = P(x_n \mid x_{n-1}, \dots, x_1) P(x_{n-1}, \dots, x_1)
\]

Em seguida, repetimos o processo, reduzindo cada probabilidade conjunta a uma probabilidade condicional e a uma probabilidade conjunta em um conjunto menor de variáveis. [1]

\[
P(x_1, \dots, x_n) = P(x_n \mid x_{n-1}, \dots, x_1) P(x_{n-1} \mid x_{n-2}, \dots, x_1) \dots P(x_2 \mid x_1) P(x_1)
\]

Ou, de forma compacta:

\[
P(x_1, \dots, x_n) = \prod_{i=1}^{n} P(x_i \mid x_{i-1}, \dots, x_1)
\]

Essa identidade é chamada de regra da cadeia. Ela é válida para qualquer conjunto de variáveis aleatórias. Comparando-a com a equação anterior, vemos que a especificação da distribuição conjunta é equivalente à afirmação geral de que, para cada variável \( X_i \) na rede. [1]

\[
P(X_i \mid X_{i-1}, \dots, X_1) = P(X_i \mid \text{Parents}(X_i))
\]

Isso só se aplica se \[\text{Parents}(X_i) \subseteq \{ X_{i-1}, \dots, X_1 \}\]. Essa última condição é satisfeita ao numerar os nós da ordem topológica em ordem topológica, ou seja, em qualquer ordem consistente com a estrutura do gráfico direcionado. [1]

**Metodologia:**

- **Nós:** Primeiro, determine o conjunto de variáveis necessárias para modelar o domínio. Agora, ordene-as, \[\{X_1, \dots, X_n\}\]. Qualquer ordem funcionará, mas a rede resultante será mais compacta se as variáveis forem ordenadas de forma que as causas precedam os efeitos. [1]
- **Links:** De i = 1 até n faça:
    - Escolha um conjunto mínimo de pais para \( X_i \) de \[X_1, \dots, X_{i-1}\], de modo que a equação \[P(X_i \mid X_{i-1}, \dots, X_1) = P(X_i \mid \text{Parents}(X_i))\] seja satisfeita. [1]
    - Para cada pai, insira um link do pai para \( X_i \). [1]
    - CPTs: Escreva a tabela de probabilidade condicional, \[P(X_i \mid \text{Parents}(X_i))\]. [1]

- Como cada nó está conectado apenas aos nós anteriores, este método de construção garante que a rede é acíclica.
- Outra propriedade importante das redes de Bayes é que elas não contêm valores de probabilidade redundantes;.
- Se não houver redundância, então não há chance de inconsistência.

## Independência

**Propriedades de independência:**

- **Propriedade não-descendentes:** Cada variável é condicionalmente independente de seus não descendentes, dados seus genitores.​
- **Cobertor de Markov:** uma variável é condicionalmente independente de todos os outros nós da rede, dados seus genitores, filhos e genitores de filhos.

**Representação de distribuições condicionais:**

- **Nós determinísticos:** Um nó determinístico tem seu valor especificado exatamente pelos valores de seus pais, sem incerteza;​
- **Independência de contexto específico (CSI, context-specific Independence):** Uma distribuição condicional exibe CSI se uma variável é condicionalmente independente de alguns de seus pais dados certos valores de outros.​
- **OR-ruidoso:** O modelo OR ruidoso permite incerteza sobre a capacidade de cada genitor de causar o filho ser verdadeiro.

**Regra geral:**

\[
P(x_i \mid \text{parents}(X_i)) = 1 - \prod_{\{ j : X_j = \text{true} \}} q_j
\]

## Variáveis contínuas​

Para lidar com variáveis contínuas existem algumas alternativas:​

- **Discretização:** Dividir os valores possíveis em intervalos fixos, por exemplo, faixas de temperatura (<0°C, 0°C−100°C, e >100°C);​
- **Distribuições probabilísticas:** Outra abordagem é definir uma variável contínua usando uma das famílias padrão de funções de densidade de probabilidade, como a distribuição Gaussiana                       ;​
- **Não paramétrica:** Define a distribuição condicional implicitamente com uma coleção de instâncias, cada uma contendo valores das variáveis ​​genitoras e filho.

Para lidar com redes hibridas, precisamos aprender a converter variáveis genitoras contínuas em variáveis filhos discretas e vice versa.

Para trazer a informação de genitores discretos em filhos contínuos podemos utilizar estratégias como distribuição condicional linear-gaussiana em que o filho tem uma distribuição gaussiana cuja média µ varia linearmente com o valor do genitor e cujo desvio padrão σ é fixo.​

Para trazer informações de genitores contínuos em filhos discretos podemos usar funções de limiarização como a integral da distribuição normal até o valor x.