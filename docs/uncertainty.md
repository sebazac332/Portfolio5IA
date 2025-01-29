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