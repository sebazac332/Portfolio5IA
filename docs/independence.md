# Independência

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
