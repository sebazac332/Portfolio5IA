# Regra de Bayes​

O Teorema de Bayes é uma fórmula matemática que ajuda a determinar a probabilidade condicional de um evento com base no conhecimento prévio e em novas evidências. Ele ajusta as probabilidades quando surgem novas informações e ajuda a tomar melhores decisões em situações incertas. É usada para determinar a probabilidade condicional do evento A quando o evento B já ocorreu. [6]
O enunciado geral do teorema de Bayes é: “A probabilidade condicional de um evento A, dada a ocorrência de outro evento B, é igual ao produto do evento B, dado A e a probabilidade de A dividida pela probabilidade do evento B.” [6]

## Fórmula

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

### Aplicações do Bayes Ingênuo​

- **Filtragem de e-mails de spam:** Classifica e-mails como spam ou não spam com base em recursos. [7]
- **Classificação de texto:** Usado na análise de sentimentos, categorização de documentos e classificação de tópicos. [7]
- **Diagnóstico médico:** ajuda a prever a probabilidade de uma doença com base nos sintomas. [7]
- **Pontuação de crédito:** Avalia a capacidade de crédito de indivíduos para aprovação de empréstimos. [7]
- **Previsão do tempo:** Classifica as condições climáticas com base em vários fatores. [7]

### Tipos de Bayes Ingênuo​

- **Gaussiano Naive Bayes:** No Gaussian Naive Bayes, presume-se que os valores contínuos associados a cada recurso sejam distribuídos de acordo com uma distribuição gaussiana. Uma distribuição gaussiana também é chamada de distribuição normal. [7]

- **Multinomial Naive Bayes:** O Multinomial Naive Bayes é usado quando os recursos representam a frequência de termos (como contagem de palavras) em um documento. É comumente aplicado na classificação de textos, em que as frequências de termos são importantes. [7] Essa variante é útil ao usar dados discretos, como contagens de frequência, e é normalmente aplicada em casos de uso de processamento de linguagem natural, como classificação de spam. [8]

- **Bernoulli Naive Bayes:** O Bernoulli Naive Bayes lida com recursos binários, em que cada recurso indica se uma palavra aparece ou não em um documento. Ele é adequado para cenários em que a presença ou ausência de termos é mais relevante do que sua frequência. Ambos os modelos são amplamente usados em tarefas de classificação de documentos. [7]