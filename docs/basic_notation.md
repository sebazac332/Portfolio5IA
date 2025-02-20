# Notação básica de probabilidade​

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

|             |      B      |       B     |      ¬B     |     ¬B      |
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
