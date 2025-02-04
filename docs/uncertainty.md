# Incerteza
# Agindo sob incerteza

No mundo real a incerteza é algo que é praticamente inevitável, por isso os agentes devem ser capazes de agir efetivamente apesar disso. Um dos métodos que se usa para isso é manter estados de crença, estes são representações de todos os possíveis estados em que pode estar, a partir destes se gera planos de contingência para cada situação que possa apresentar. Embora este método funcione para problemas simples, quando introduzido em ambientes mais complexos apresenta dificuldades, isto é principalmente devido a três fatores. [1]

- Estado de crenças de grande porte cheio de situações improváveis, isto porque você deve considerar todas as situações possíveis. [1]

- Planos de contingência incrivelmente grandes para lidar com todas as situações, mesmo aquelas com baixa probabilidade. [1]

- Incapacidade de comparar os méritos de planos que não garantem atingir o objetivo. [1]

**Problema de qualificação lógica:** Não se pode inferir se um plano será bem sucedido ou não, porque há uma quantidade incomensurável de condições que não podem ser deduzidas com precisão. [1]

Tentar criar regras absolutas usando a lógica como base é impossível, isto devido a três razões:

- **Complexidade:** O número completo de antecedentes e consequentes que são necessários para criar uma regra sem exceções é muito grande e as regras resultantes destes seriam muito difíceis de usar. [1]

- **Desconhecimento teórico:** Muitos campos não têm a teoria completa para seu domínio. [1]

- **Desconhecimento prático:** Mesmo se todas as regras são conhecidas, não pode ser totalmente certo porque os testes necessários de uma determinada situação não foram ou não podem ser realizados. [1]

**Grau de crença:** Os graus de crença representam formalmente a força com que um agente acredita na verdade de várias proposições. Quanto mais alto for o grau de crença de um agente em uma determinada proposição, maior será sua confiança na verdade dessa proposição. [2] Estas probabilidades nas sentenças relevantes é o melhor que pode ser alcançado com o conhecimento do agente. [1]

## Teoria da probabilidade

É um ramo avançado da matemática que lida com a medição da probabilidade de ocorrência de eventos. Ela fornece ferramentas para analisar situações que envolvem incerteza e ajuda a determinar a probabilidade de certos resultados. Essa teoria usa os conceitos de variáveis aleatórias, espaço amostral, distribuições de probabilidade e outros para determinar o resultado de qualquer situação. [3] Esta será nossa principal ferramenta para lidar com os graus de crença. [1]

### Abordagens na teoria da probabilidade

**Probabilidade teórica:** A probabilidade teórica trata com suposições para evitar a repetição inviável ou dispendiosa de experimentos. [3]
A fórmula de probabilidade teórica usada para calcular a probabilidade de um evento A é: P(A) = (Número de resultados favoráveis ao Evento A) / (Número de todos os resultados possíveis) [3]

**Probabilidade experimental:** A probabilidade experimental é encontrada por meio da realização de uma série de experimentos e da observação de seus resultados. Esses experimentos aleatórios também são conhecidos como tentativas. A fórmula experimental de probabilidade para um evento A é: P(E) = (Número de vezes que o evento A ocorreu) / (Número total de tentativas) [3]

**Probabilidade subjetiva:** Refere-se à probabilidade de ocorrência de um evento, conforme estimada por um indivíduo com base em suas crenças, experiências, intuição ou conhecimento pessoal, e não em dados estatísticos objetivos ou modelos matemáticos formais. [3]

### Fundamentos da teoria da probabilidade

- **Experimento aleatório:** Qualquer evento que possa ser repetido várias vezes e cujo resultado não seja prejudicado pela repetição é chamado de experimento aleatório. [3]

- **Espaço amostral:** O conjunto de todos os resultados possíveis para qualquer experimento aleatório é chamado de espaço amostral. [3]

- **Evento:** O resultado de qualquer experimento é chamado de evento. [3]

    - **Eventos independentes:** Eventos cujos resultados não são afetados pelos resultados de outros eventos futuros e/ou passados. [3]
    - **Eventos dependentes:** Eventos cujos resultados são afetados pelo resultado de outros eventos. [3]
    - **Eventos mutuamente exclusivos:** Eventos que não podem ocorrer simultaneamente. [3]
    - **Eventos igualmente prováveis:** Eventos que têm a mesma chance ou probabilidade de acontecer [3]

### Fórmulas

- **Fórmula da probabilidade teórica:** (Número de resultados favoráveis) / (Número de resultados totais)
- **Fórmula de probabilidade empírica:** (Número de vezes que o evento A ocorreu) / (Número total de tentativas)
- **Regra de adição de probabilidade:** P(A ∪ B) = P(A) + P(B) - P(A∩B)
- **Regra complementar de probabilidade:** P(A') = 1 - P(A)
- **Eventos independentes:** P(A∩B) = P(A) ⋅ P(B)
- **Probabilidade condicional:** P(A | B) = P(A∩B) / P(B)
- **Teorema de Bayes:** P(A | B) = P(B | A) ⋅ P(A) / P(B)

## Decisões racionais (utilidade)

Há uma grande quantidade de planos com diferentes probabilidades de sucesso e com múltiplas consequências ligadas a eles, o agente deve ter uma forma de escolher um destes tentando conseguir um equilíbrio entre a probabilidade de sucesso e consequências que podem ser desejáveis ou indesejáveis. [1]

**Preferência:** Refere-se à tendência dos agentes de escolher certos planos sobre outros. A prioridade geralmente depende das condições que cercam as soluções desses planos. [1]

### Teoria da utilidade

Esta teoria sugere que cada possível resultado de uma decisão é atribuído um valor que representa quão satisfeito se esta com o resultado. O objetivo é obter o maior valor esperado, que é a média dos valores de todos os resultados possíveis, levando em conta a probabilidade de cada um deles acontecer. [4] Na inteligência artificial, pode-se dizer que cada estado (ou sequência de estados) tem um grau de utilidade para um agente e que o agente preferirá estados com maior utilidade. [1] Essa utilidade é relativa ao agente, ou seja, um estado que pode ser considerado de alta utilidade para um agente pode ser considerado de baixa utilidade para outro que tem um objetivo e condições desejadas diferentes. [1]

### Teoria da decisão

Combina o valor de utilidade dado pela teoria da utilidade de um estado junto com a probabilidade desse estado ocorrer, depois faz decisões levando estes dois fatores em conta. A ideia fundamental da teoria da decisão é que um agente é racional se e somente se ele escolher a ação que produz a maior utilidade esperada, calculada a média de todos os resultados possíveis da ação. Isso é chamado de princípio da utilidade máxima esperada (MEU). [1]

## Notação básica de probabilidade​

Refere-se aos símbolos e convenções usados para representar e manipular probabilidades e conceitos estatísticos. Essa notação é fundamental em campos como estatística, aprendizado de máquina e inteligência artificial, onde lidar com a incerteza e a variabilidade é crucial. [5]

### Notações

- Probabilidade de um evento A ocorrer: P(A)
    - Conjunto de probabilidades de todos os possíveis valores de A é conhecida como distribuição de probabilidade.
    - Probabilidade de todos os possíveis resultados de um evento A:
        - P(A = a) = 0.25 (25% de probabilidade do resultado de A ser a)
        - P(A = b) = 0.25 (25% de probabilidade do resultado de A ser b)
        - P(A = c) = 0.25 (25% de probabilidade do resultado de A ser b)
        - P(A = d) = 0.25 (25% de probabilidade do resultado de A ser b)
    - Forma abreviada de todos os possíveis resultados:
        - P(A) = <0.25,0.25,0.25,0.25>
    - Quando se tem um rango finito e discreto, se conhece como distribuição categórica.
    - O conjunto de todos os valores possíveis de A quando A é uma variável contínua:
        - P(A = x) = Uniform(x,10,18)
    - Significa que os valores de A estão uniformemente distribuídos entre 10 e 18.
    - Essa representação é conhecida como função de densidade de probabilidade.
- Probabilidade de um evento A não ocorrer: P(¬A)
    - Relação entre a probabilidade de um evento acontecer e a probabilidade de não acontecer:
        - P(¬A) = 1 - P(A)
- Probabilidade de um evento A e um evento B ocorrerem ao mesmo tempo: P(A ∧ B)
    - Representação de todos os valores possíveis de A e B: P(A,B) = P(A|B)P(B)
    - Essa representação é conhecida como distribuição conjunta de probabilidade e é a distribuição da probabilidade de que os eventos A e B ocorram simultaneamente.
    - Um modelo de probabilidade é completamente determinado pela distribuição conjunta de todas as variáveis ​​aleatórias, as chamadas distribuição de probabilidade conjunta completa. [1]
- Probabilidade de um evento A ou evento B ocorrer: P(A ∨ B)
    - Para calcular a probabilidade da disjunção P(A ∨ B) usa-se o princípio de inclusão-exclusão:
        - P(A ∨ B) = P(A) + P(B) − P(A ∧ B) .
- Probabilidade de um evento A acontecer e um evento B não acontecer: P(A ∧ ¬B)
- Probabilidade de não ocorrer um evento A ou ocorrer um evento B: P(¬A ∨ B)
- A probabilidade de ocorrência do evento A, considerando que o evento B tenha ocorrido (Probabilidade condicional): P(A|B) -> P(A ∧ B)/P(B)
    - Forma alternativa chamada regra de produto: P(A ∧ B) = P(A|B)P(B)
- Teorema de Bayes, que fornece uma maneira de atualizar as probabilidades com base em novos dados: P(A|B) = P(B)P(B∣A)*P(A)

### Inferência usando distribuições conjuntas completas

Domínio composto por 3 variáveis A, B e C:

|             |               B           |             ¬B            |
| ----------- | ----------- | ----------- | ----------- | ----------- |
|             |       C     |     ¬C      |     C       |     ¬C      |
|     A       |    0.108    |    0.012    |   0.072     |    0.008    |
|    ¬A       |    0.016    |    0.064    |   0.144     |    0.576    |

**Calcular probabilidade de A ou B:**
Soma as probabilidades onde A é verdadeiro e B falso com as probabilidades onde A é falso e B verdadeiro.
P(A ∨ B) = 0.18 + 0.016 + 0.012 + 0.064 + 0.072 + 0.008 = 0.28

**Calcular probabilidade de A:**
Soma as probabilidades onde A é verdadeiro.
P(A) = 0.108 + 0.012 + 0.072 + 0.008 = 0.2

Esse processo onde todas as probabilidades são somadas é conhecido como marginalização. Esta tem a forma geral: [1]
$$
P(Y) = \sum_{z} P(Y, Z = z)
$$

Onde Y e Z são variáveis.

Substituindo P(Y,z) por P(Y|z)P(z) você obtém outra regra chamada condicionamento. [1]
$$
P(Y) = \sum_{z} P(Y \mid Z = z) \, P(Z = z)
$$

Onde Y e Z são variáveis.

**Para calcular a probabilidade condicional de A dada evidência de B:**

P(A|B) = P(A ∨ B)/P(B) = (0.108 + 0.012)/(0.108 + 0.012 + 0.016 + 0.064) = 0.6

**Para calcular a probabilidade condicional de A não acontecer dada evidência de B:**

P(¬A|B) = P(¬A ∨ B)/P(B) = (0.016 + 0.064)/(0.108 + 0.012 + 0.016 + 0.064) = 0.4

**Para obter a normalização de probabilidades:**

P(A|B) = αP(A, B) = α[P(A, B, C)+P(A, B, ¬C)] = α[<0.108,0.016> + <0.012,0.064>] = α<0.12,0.08> = <0.6,0.4>

Usando isso você pode obter P(A|B) sem saber o valor de P(B).

**Processo geral de inferência:**

$$
P(X \mid e) = \alpha \, P(X, e) = \alpha \sum_{y} P(X, e, y)
$$

Onde X e variável, E a lista de variáveis de evidência, e a lista de valores observados para elas e Y as variáveis não observadas restantes.