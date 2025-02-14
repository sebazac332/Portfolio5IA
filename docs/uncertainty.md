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

## Inferência usando distribuições conjuntas completas

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

## Independência

Supondo que adicone uma variável D à distribuição anterior, transformando-se em P(A, B, C, D), para encontrar a relação entre ambas as distribuições e como o valor de P(A, B, C) está relacionado ao valor de P(A, B, C, D) pode ser iniciado usando a regra de produto. [1]

P(A,B,C,D) = P(D|A,B,C)P(A,B,C).

Agora, assumindo que A, B e C não influenciam o resultado de D pode-se assumir:

P(D|A,B,C) = P(D)

Depois se deduz:

P(A,B,C,D) = P(D)P(A,B,C)

A propriedade usada aqui é conhecida como independência (independência marginal ou independência absoluta). Pode ser escrita de forma geral assim:

**Independência de preposições (Preposições a e b):**

- P(a|b) = P(a)
- P(b|a) = P(b)
- P(a ∧ b) = P(a)P(b)

Todas essas formas são equivalentes.

**Independência de variáveis (Variáveis X e Y):**

- P(X|Y) = P(X)
- P(Y|X) = P(Y)
- P(X,Y) = P(X)P(Y)

Todas essas formas são equivalentes.

Identificação de independência geralmente é baseada em conhecimento de domínio. Enquanto independências são muito úteis, reduzindo o tamanho da representação de domínio e a complexidade do problema de inferência no entanto separações limpas por independência entre subgrupos de variáveis são uy raro encontrar isso porque se existe uma conexão não importa qual debil ou indireta entre duas variáveis a independência falhará. [1]

## Regra de Bayes​

O Teorema de Bayes é uma fórmula matemática que ajuda a determinar a probabilidade condicional de um evento com base no conhecimento prévio e em novas evidências. Ele ajusta as probabilidades quando surgem novas informações e ajuda a tomar melhores decisões em situações incertas. É usada para determinar a probabilidade condicional do evento A quando o evento B já ocorreu. [6]
O enunciado geral do teorema de Bayes é: “A probabilidade condicional de um evento A, dada a ocorrência de outro evento B, é igual ao produto do evento B, dado A e a probabilidade de A dividida pela probabilidade do evento B.” [6]

### Fórmula

P(A|B) = P(B|A) ⋅ P(A) / P(B)

- P(A) e P(B) são as probabilidades dos eventos A e B. Além disso, P(B) nunca é igual a zero.
- P(A|B) é a probabilidade do evento A quando o evento B acontece.
- P(B|A) é a probabilidade do evento B quando A acontece.

**Para encontrar causa e efeito:**

P(causa|efeito) = P(efeito|causa) ⋅ P(causa) / P(efeito)

- A probabilidade condicional P(efeito | causa) quantifica a relação na direção causal. 
- Enquanto P(causa | efeito) descreve a direção do diagnóstico.

Observação: O conhecimento de diagnóstico geralmente é mais frágil do que o conhecimento causal.

**Forma geral com normalização:**

P(Y|X) = αP(X|Y)P(Y)

- α é a constante de normalização necessária para fazer com que as entradas em P(Y|X) somem 1.
- Usado para evitar a avaliação da probabilidade anterior da evidência, calculando uma probabilidade posterior para cada valor da variável de consulta e, em seguida, normalizando os resultados.

**Combinação de evidências:**

Se tem duas ou mais peças de evidência:

P(A|B ∧ C) = αP(B ∧ C|A)P(A)

Propriedade de independência condicional de A e B dada C:

P(B ∧ C|A) = P(B|A)P(C|A)

CAVITY - A
TOOTHACHE - B
CATCH - C

Equação de probabilidade de independência pode ser inserida na equação acima:

P(A|B ∧ C) = αP(B|A)P(C|A)P(A)

Definição geral de independência condicional entre duas variáveis X, Y dada uma variável Z:

P(X,Y|Z) = P(X|Z)P(Y|Z)

Notação de independência absoluta:

- P(X|Y,Z)=P(X|Z)
- P(Y|X,Z)=P(Y|Z)

Ambos são equivalentes.

Forma completa do domínio:

P(B,C,A) = P(B,C|A)P(A) = P(B|A)P(C|A)P(A)

**Aplicações da regra de Bayes:**

- **Testes médicos:** Encontrar a probabilidade real de ter uma doença após um teste positivo.
- **Filtros de spam:** Verificar se um e-mail é spam com base em palavras-chave.
- **Previsão do tempo:** Atualização da chance de chuva com base em novos dados.
- **IA e aprendizado de máquina:** Usado em classificadores Naïve Bayes para prever resultados.

## Modelo de Bayes Ingênuo​

Os classificadores Naive Bayes são algoritmos de aprendizado de máquina supervisionados usados para tarefas de classificação, com base no Teorema de Bayes para encontrar probabilidades. A ideia principal por trás do classificador Naive Bayes é usar o Teorema de Bayes para classificar os dados com base nas probabilidades de diferentes classes, considerando os recursos dos dados. Ele é usado principalmente na classificação de textos de alta dimensão. [7]

A distribuição conjunta completa pode ser escrita como​:

$$
P(\text{Causa}, \text{Efeito}_1, \dots, \text{Efeito}_n) = P(\text{Causa}) \cdot \prod_{i} P(\text{Efeito}_i \mid \text{Causa})
$$

- **\(P(\text{Causa})\)**: Probabilidade do evento "Causa" ocorrer.
- **\(P(\text{Efeito}_i \mid \text{Causa})\)**: Probabilidade condicional de cada efeito dado que a causa ocorreu.
- **Multiplicação dos termos**: Assume que os efeitos \( \text{Efeito}_1, ..., \text{Efeito}_n \) são **independentes condicionalmente** à causa.

Para usar um modelo Bayes ingênuo, podemos aplicar a equação anterior para obter a probabilidade da causa com base em alguns efeitos observados. Chame os efeitos observados de E=e, enquanto as demais variáveis de efeito Y não são observadas.

$$
P(\text{Causa} \mid e) = \alpha \sum_{y} P(\text{Causa}, e, y)
$$

- **\( P(\text{Causa} \mid e) \)**: Probabilidade da Causa após observar \( e \).
- **\( P(\text{Causa}, e, y) \)**: Probabilidade conjunta da Causa, da evidência \( e \) e de uma variável oculta \( y \).
- **Marginalização**: A soma sobre \( y \) nos permite obter a probabilidade total, levando em conta todas as possibilidades dessa variável oculta.
- **Normalização**: \( \alpha \) é um fator de escala que garante que a soma de todas as probabilidades seja 1.

Finalmente temos:

$$
P(\text{Cause} \mid e) = \alpha \sum_{y} P(\text{Cause}) P(y \mid \text{Cause}) \prod_{j} P(e_j \mid \text{Cause})
$$

Como \( \sum_{y} P(y \mid \text{Cause}) = 1 \), a equação pode ser simplificada para:

$$
P(\text{Cause} \mid e) = \alpha P(\text{Cause}) \prod_{j} P(e_j \mid \text{Cause})
$$

- **\( P(\text{Cause} \mid e) \)**: Probabilidade da causa após observar a evidência.
- **\( P(\text{Cause}) \)**: Probabilidade inicial (prior) da causa.
- **\( P(y \mid \text{Cause}) \)**: Probabilidade da variável oculta \( y \) dado a causa.
- **\( P(e_j \mid \text{Cause}) \)**: Probabilidade condicional de cada evidência \( e_j \) dado a causa.
- **\( \alpha \)**: Fator de normalização para garantir que as probabilidades somem 1.

## Por que ele é chamado de ingênuo

- Ele é chamado de ingênuo porque presume que a presença de um recurso não afeta outros recursos. [7]
- Pressupõe que todos os recursos contribuem igualmente para o resultado. [8]
- Muitas vezes é usada como uma suposição simplificadora;​ nos casos em que as variáveis ​​de “efeito” não são estritamente independente dada a variável causa.​ [1]

## Suposição de Bayes Ingênuo​

O pressuposto fundamental do Naive Bayes é que cada recurso faz uma análise:

- **Independência de recursos:** Isso significa que, quando estamos tentando classificar algo, presumimos que cada recurso (ou informação) nos dados não afeta nenhum outro recurso. [7]
- **Os recursos contínuos são distribuídos normalmente:** Se um recurso for contínuo, presume-se que ele seja normalmente distribuído em cada classe. [7]
- **Os recursos discretos têm distribuições multinomiais:** Se um recurso for discreto, presume-se que ele tenha uma distribuição multinomial dentro de cada classe. [7]
- **Os recursos são igualmente importantes:** presume-se que todos os recursos contribuam igualmente para a previsão do rótulo da classe. [7]
- **Não há dados ausentes:** Os dados não devem conter valores ausentes. [7]

### Aplicações do classificador Naive Bayes

- **Filtragem de e-mails de spam:** Classifica e-mails como spam ou não spam com base em recursos. [7]
- **Classificação de texto:** Usado na análise de sentimentos, categorização de documentos e classificação de tópicos. [7]
- **Diagnóstico médico:** ajuda a prever a probabilidade de uma doença com base nos sintomas. [7]
- **Pontuação de crédito:** Avalia a capacidade de crédito de indivíduos para aprovação de empréstimos. [7]
- **Previsão do tempo:** Classifica as condições climáticas com base em vários fatores. [7]

### Tipos de Bayes Ingênuo​

- **Gaussiano Naive Bayes:** No Gaussian Naive Bayes, presume-se que os valores contínuos associados a cada recurso sejam distribuídos de acordo com uma distribuição gaussiana. Uma distribuição gaussiana também é chamada de distribuição normal. [7]

- **Multinomial Naive Bayes:** O Multinomial Naive Bayes é usado quando os recursos representam a frequência de termos (como contagem de palavras) em um documento. É comumente aplicado na classificação de textos, em que as frequências de termos são importantes. [7] Essa variante é útil ao usar dados discretos, como contagens de frequência, e é normalmente aplicada em casos de uso de processamento de linguagem natural, como classificação de spam. [8]

- **Bernoulli Naive Bayes:** O Bernoulli Naive Bayes lida com recursos binários, em que cada recurso indica se uma palavra aparece ou não em um documento. Ele é adequado para cenários em que a presença ou ausência de termos é mais relevante do que sua frequência. Ambos os modelos são amplamente usados em tarefas de classificação de documentos. [7]