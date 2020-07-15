# Aprendizagem de enxames

Atividade realizada na cadeira de "Aprendizagem de Enxames" da pós graduação do Centro de Informática (CIN) - UFPE. Nessa atividade foram realizados experimentos utilizando dois algoritmos de aprendizagem de enxames, o Particle Swarm Optimization (PSO) e o Artificial Bee Colony (ABC). Além dos dois algorítmos base também foram realizados experimentos em uma variação de cada algoritmo.

## Métodos

### Particle Swarm Optimization (PSO)
Implementação do algoritmo base do PSO.

#### Equações
Velocidade da Partícula:

![pso_velocidade](img/pso_velocidade.jpg)

Atualização da Partícula:

![pso_atualizacao_particula](img/pso_atualizacao_particula.jpg)

#### Parâmetros
```
num_particulas  = Número de partículas
stop_criterion  = Número de épocas sem atualizar o gbest
v_i             = Velocidade da i-ésima partícula
x_i             = Posição da i-ésima partícula
pbest_i         = Melhor posição da i-ésima partícula
g_best          = Melhor posição entre todas as partículas
w               = Ponderação de inércia, momentum
c_1             = Controla quão rápido a partícula vai convergir para 'pbest'
c_2             = Controla quão rápido a partícula vai convergir para 'gbest'
r               = Número aleatório entre 0 e 1
```

#### Fluxograma
![fluxograma_pso](img/pso.jpg)

### Particle Swarm Optimization (PSO) - Variação
Como variação do PSO foi implementado a versão em que as particulas são reinicializadas para posições aleatórias sempre que o 'g_best' fica 'n' iterações sem melhora. Essa melhoria da ao PSO a capacidade de fugir de mínimos locais.  

#### Novos Parâmetros
```
n_reboot = Número de Reinicializações
```

#### Fluxograma
 ![fluxograma_pso_variacao](img/pso_variacao.jpg)

### Artificial Bee Colony (ABC)
Implementação do algoritmo base do ABC.

#### Equações

Inicialização das fontes de comidas:

![abc_inicializacao](img/abc_eq_inicializacao.jpg)

Atualização da fonte de comida:

![abc_atualizacao](img/abc_eq_update.jpg)

Fitness:

![abc_fitness](img/abc_eq_fit.jpg)

Probabilidade:

![abc_probabilidade](img/abc_eq_probabilidade.jpg)


#### Parâmetros
```
NP          = Tamanho da Colônia
n_epocas    = Número de Épocas
D           = Número de parâmetros a serem otimizados
limit       = Limite até abandonar uma fonte de comida. [default = (NP*D)/2]
food_number = Quantidade de fonte de comidas. [default = NP/2]
lb          = Limite inferior dos parâmetros
ub          = Limite superior dos parâmetros
x_i         = i-ésima fonte de comida
Φ           = Número aleatório entre -1 e 1
```

#### Algoritmo
```
for(run=0;run<bee.runtime;run++)
{
    bee.initial();
    bee.MemorizeBestSource();
    for (iter=0;iter<bee.maxCycle;iter++)
    {
        bee.SendEmployedBees();
        bee.CalculateProbabilities();
        bee.SendOnlookerBees();
        bee.MemorizeBestSource();
        bee.SendScoutBees();
    }
}
```
### Artificial Bee Colony (ABC) - Variação
A variação do ABC implementada faz a mudança do número fixo de épocas 'n_epocas' para otimização do algoritmo por um limite de épocas sem atualização da melhor fonte de alimento. Essa mudança permite que a otimização dos parâmetros não seja interrompida antes de se chegar em um mínimo local/global. Outro benefício dessa variação do ABC é a economia de recursos computacionais quando o algoritmo se encontra preso em um mínimo local, pois em vez de ter que rodar todas as épocas restantes, ele vai persistir somente até que o limiar estabelecido de épocas sem melhora da melhor fonte de comida.
  
#### Novos Parâmetros
```
n_epocas_melhora = Número máximo de épocas sem que a melhor fonte de alimento seja melhorada.
```

## Benchmarks
Os métodos de swarm descritos acima foram testados em 6 benchmarks diferentes: Ackley function, Alpine function, Schwefel function, Happy Cat function, Brown function e Exponential function.

### Ackley Function

#### Equação

![ackley_equation](img/ackley_eq.jpg)

Dominio: [-32, 32]

Mínimo Global: [0, ..., 0]

#### Gráfico

![ackley_graph1](img/ackley_graph1.jpg)

![ackley_graph2](img/ackley_graph2.jpg)

![ackley_graph3](img/ackley_graph3.jpg)

### Alpine Function

#### Equação

![alpine_equation](img/alpine_eq.jpg)

Dominio: [0, 10]

Mínimo Global: [0, ..., 0]

#### Gráfico

![alpine_graph1](img/alpine_graph1.jpg)

![alpine_graph2](img/alpine_graph2.jpg)

![alpine_graph3](img/alpine_graph3.jpg)

![alpine_graph4](img/alpine_graph4.jpg)

### Schwefel Function

#### Equação

![schwefel_equation](img/schwefel_eq.jpg)

Dominio: [-500, 500]

Mínimo Global: [420.9687, ..., 420.9687]

#### Gráfico

![schwefel_graph1](img/schwefel_graph1.jpg)

### Happy Cat Function

#### Equação

![happy_cat_equation](img/happy_cat_eq.jpg)

Dominio: [-2, 2]

Mínimo Global: [-1, ..., -1]

#### Gráfico

![happy_cat_graph1](img/happy_cat_graph1.jpg)

![happy_cat_graph2](img/happy_cat_graph2.jpg)

![happy_cat_graph3](img/happy_cat_graph3.jpg)

![happy_cat_graph4](img/happy_cat_graph4.jpg)

### Brown Function

#### Equação

![brown_equation](img/brown_eq.jpg)

Dominio: [-1, 4]

Mínimo Global: [0, ..., 0]

#### Gráfico

![brown_graph1](img/brown_graph1.jpg)

![brown_graph2](img/brown_graph2.jpg)

![brown_graph3](img/brown_graph3.jpg)

### Exponential Function

#### Equação

![exponential_equation](img/exponential_eq.jpg)

Dominio: [-1, 1]

Mínimo Global: [0, ..., 0]

#### Gráfico

![exponential_graph1](img/exponential_graph1.jpg)

![exponential_graph2](img/exponential_graph2.jpg)

![exponential_graph3](img/exponential_graph3.jpg)

## Experimentos
Nesta atividade foram realizados experimentos para testar a influência dos parâmetros dos métodos descritos no resultado final da otimização. Para isso foram análisados o fitness da solução final e o tempo que o algoritmo levou para convergir até o resultado final.

Em cada experimento foram realizadas 100 repetições do algoritmo com cada combinação de parâmetros. O resultado expresso do fitness é referente a repetição que obteve o menor (melhor) fitness entre todas as execuções. Ainda, o resultado do tempo de convergência é expresso em segundos e é referente ao tempo gasto para rodar todas as 100 repetições do algoritmo.

Além dos experimentos para testar a influência dos parâmetros de cada método, também foram realizados experimentos para determinar a eficácia de cada método, PSO, ABC e suas variações, nos benchmarks descritos acima. Nesse caso, cada benchmark foi testado utilizando 10, 20 e 50 atributos. Assim como nos experimentos para determinar a influência dos parâmetros, os resultados expressos nesse experimentos são referentes aos valores obtidos após 100 execuções de cada método com um conjunto fixo de parâmetros. Desta forma o valor de fitness é o menor encontrado em todas as 100 execuções e o tempo de convergência é referente a soma do tempo das 100 execuções.

Abaixo segue os parâmetros testados no método base do PSO e do ABC.   

### Particle Swarm Optimization (PSO)
 
```
stop_criterion      = número de épocas sem atualização de g_best
c1                  = c_pbest, influência do p_best na convergência do método
c2                  = c_gbest, influência do g_best na convergência do método
w                   = momentum, quanto a última velocidade vai influênciar na velocidade atual da partícula
num_particulas      = número de partículas utilizadas na convergência
```

### Artificial Bee Colony (ABC)
```
n_epocas            = número de épocas utilizadas
limit               = limite até abandonar uma fonte de comida
NP                  = tamanho da colônia
```

## Resultados

### Particle Swarm Optimization (PSO)
Resultados para o método base do PSO.

#### - stop_criterion

Neste experimento foi testado cinco valores diferentes do parâmentro stop_criterion, que variou no intervalo de 20 a 100 em passos de tamanho 20. 

##### Configuração
```
benchmark       = Ackley function
num_particulas  = 100
dim_particulas  = 10, # dimensão das partículas
w               = 0.5 # momentum
c1              = 0.5 # c_pbest
c2              = 0.5 # c_gbest
num_repeticoes  = 100 # número de repetições do experimento
```
##### Resultados
stop_criterion  | 20    | 40    | 60    | 80    | 100
--------------- | ----- | ----- | ----- | ----- | -----
fitness         | 0.0833| 0.0038| 0.0039| 0.1171| 0.0799
tempo           | 266s  | 263s  | 305s  | 316s  | 355s

A partir dos resultados da tabela acima é possível ver que um stop_criterion muito pequeno pode atrapalhar a convergência do método, o impedindo de alcançar melhores resultados. Entretanto, quanto maior o stop_criterion utilizado, maior o tempo de convergência do algoritmo. Também é possível verificar que o aumento do stop_criterion só ajuda o fitness até certo ponto, no experimento realizado o melhor valor de stop_criterion é 40, pois apresenta o melhor trade off entre fitness e tempo de converência.

#### - c_gbest

Nesse experimento foi verificado a influência do parâmetro c_gbest na convergência do algoritmo. Foram testados cinco valores para c_gbest, são eles 0.2, 0.4, 0.5, 0.6 e 0.8.

##### Configuração
```
benchmark       = Ackley function
stop_criterion  = 40
num_particulas  = 100
dim_particulas  = 10,       # dimensão das partículas
w               = 0.5       # momentum
c1              = 1 - c2    # c_pbest
num_repeticoes  = 100       # número de repetições do experimento
```
##### Resultados
c_gbest         | 0.2    | 0.4  | 0.5   | 0.6   | 0.8
--------------- | ----- | ----- | ----- | ----- | -----
fitness         | 2.4004| 0.0762| 0.0584| 0.0012| 0.0212
tempo           | 193s  | 261s  | 258s  | 282s  | 196s

Os resultados obtidos nesse experimento levam a acreditar que para essa configuração testada nesse benchmark o melhor valor de c_gbest é o 0.6. Ainda, valores de c_gbest muito próximos de 0 ou 1 aparentam levar a uma convergência prematura do algoritmo. Isso pode ser observado pelo aumento do fitness para esses valores (c_gbest = [0.2, 0.8]) ao mesmo tempo em que se mostra uma queda no tempo de convergência do algoritmo.

#### - momentum
Nesse experimento foi testado a influência do momentum na convergência do algoritmo. Foram realizados experimentos variando o momentum entre 0 e 0.8 em passos de 0.2.

##### Configuração
```
benchmark       = Ackley function
stop_criterion  = 40
num_particulas  = 100
dim_particulas  = 10,       # dimensão das partículas
c1              = 1 - c2    # c_pbest
c2              = 0.6       # c_gbest
num_repeticoes  = 100       # número de repetições do experimento
```
##### Resultados
momentum        | 0     | 0.2   | 0.4   | 0.6   | 0.8
--------------- | ----- | ----- | ----- | ----- | -----
fitness         | 1.2473| 2.9358| 0.2283| 0.0077| 9.3079
tempo           | 163s  | 150s  | 245s  | 94s  | 53s

Para esse experimento o valor de momentum que trouxe o melhor resultado de fitness foi 0.6. Ainda, parece haver uma tendência ao uma convergência cada vez mais rápida a medida que o valor do parâmetro momentum é aumentado. Todavia, essa convergência rápida não reflete necessariamente em um bom valor do fitness, como é o caso de momentum=0.8 que embora tenha tido a convergência mais rápida desse experimento, obteve também o pior valor de fitness.

#### - num_particulas
Nesse experimento é avaliado a influência do número de partículas do PSO. Para isso foram feitos testes com 20, 40, 60, 80 e 100 partículas.

##### Configuração
```
benchmark       = Ackley function
stop_criterion  = 40
momentum        = 0.6
dim_particulas  = 10,       # dimensão das partículas
c1              = 1 - c2    # c_pbest
c2              = 0.6       # c_gbest
num_repeticoes  = 100       # número de repetições do experimento
```
##### Resultados
num_particulas  | 20    | 40    | 60    | 80    | 100
--------------- | ----- | ----- | ----- | ----- | -----
fitness         | 3.2313| 0.0327| 0.0343| 0.0015| 0.0014
tempo           | 32s  | 57s  | 80s  | 123s  | 157s

Os resultados desse experimento mostraram que no intervalo testado para essa configuração de parâmetros/benchmark, o aumento no número de partículas refletiu diretamente na diminuição (melhora) do fitness. De forma natural, também é pertinente se atentar que o aumento do número de partículas tem uma relação direta com o aumento do tempo de convergência do algoritmo. Desta forma, é aconselhavel avaliar um trade off entre fitness e custo computacional fazer a escolher desse parâmetro. De toda forma, o valor do num_particulas que obteve o melhor fitness nesse experimento foi num_particulas = 100.

#### Benchmark / Dimensão das partículas
Nesse experimento o PSO foi executado com os melhores parâmetros achados a partir dos experimentos realizados anteriormente. Nele é possível ver a performance do PSO nos benchmarks apresentados anteriormente. Para cada benchmark o PSO é testado utilizando partículas de tamanho 10, 20 e 50.

##### Configuração
```
num_particulas  = 100
stop_criterion  = 40
momentum        = 0.6
c1              = 1 - c2    # c_pbest
c2              = 0.6       # c_gbest
num_repeticoes  = 100       # número de repetições do experimento
```
##### Resultados
dim_particulas = 10

benchmark       | Ackley| Alpine|Schwefel   |Happy Cat  | Brown     | Exponential
--------------- | ----- | ----- | -----     | -----     | -----     |  ----
fitness         | 0.0004| 0.0250| 419.17  | 0.2713    | 6.32e-14  | -0.9999
tempo           | 146s   | 29s   | 44s       | 38s      | 420s      | 26s

dim_particulas = 20

benchmark       | Ackley| Alpine|Schwefel   |Happy Cat  | Brown     | Exponential
--------------- | ----- | ----- | -----     | -----     | -----     |  ----
fitness         | 3.1827| 0.8767| 2681.49   | 0.5454    | 0.7963    | -0.9987
tempo           | 220s   | 125s   | 98s      | 38s      | 987s      | 61s

dim_particulas = 50

benchmark       | Ackley| Alpine|Schwefel   |Happy Cat  | Brown     | Exponential
--------------- | ----- | ----- | -----     | -----     | -----     |  ----
fitness         | 14.9323| 21.3232| 9677.24   | 0.8787    | 46.1067 | -0.6461
tempo           | 47s   | 432s   | 100s      | 39s      | 2213s      | 10s

Nesse experimento é possível ver que o aumento da dimensão das partículas dificulta o processo de otimização, aumentando (piorando) o fitness e o tempo de convergência das funções. Em relação aos benchmarks, o Schwefel parece ser o mais difícil entre eles enquanto o Happy Cat aparenta ser o mais fácil de otimizar.

### Particle Swarm Optimization (PSO) - Variação
Resultados para variação do PSO.


#### Benchmark / Dimensão das partículas
Nesse experimento a variação do PSO foi executada com os melhores parâmetros achados a partir dos experimentos realizados anteriormente. Nele é possível ver a performance do PSO nos benchmarks apresentados anteriormente. Para cada benchmark a variação do PSO é testada utilizando partículas de tamanho 10, 20 e 50.



##### Configuração
```
num_repeticoes  = 20        # número de reinicializações randomicas para variação do PSO
num_particulas  = 100
stop_criterion  = 40
momentum        = 0.6
c1              = 1 - c2    # c_pbest
c2              = 0.6       # c_gbest
num_repeticoes  = 100       # número de repetições do experimento
```

##### Resultados
dim_particulas = 10

benchmark       | Ackley| Alpine|Schwefel   |Happy Cat  | Brown     | Exponential
--------------- | ----- | ----- | -----     | -----     | -----     |  ----
fitness         | 1.96e-5| 0    | 454.90    | 0.1687    | 2.32e-14  | -0.9999
tempo           | 301s   | 208s   | 182s       | 237s      | 1189s      | 181s

dim_particulas = 20

benchmark       | Ackley| Alpine|Schwefel   |Happy Cat  | Brown     | Exponential
--------------- | ----- | ----- | -----     | -----     | -----     |  ----
fitness         | 0.0049| 0.2471| 1717.38   | 0.3259    | 1.04e-8    | -0.9999
tempo           | 454s   | 486s   | 256s      | 247s      | 3470s      | 304s

dim_particulas = 50

benchmark       | Ackley| Alpine|Schwefel   |Happy Cat  | Brown     | Exponential
--------------- | ----- | ----- | -----     | -----     | -----     |  ----
fitness         | 9.4798| 10.8680| 7470.23   | 0.6754    | 7.0297 | -0.9999
tempo           | 337s   | 742s   | 345s      | 260s      | 6491s      | 237s

Em geral, os resultados adquiridos nos experimentos com o a variação PSO mostram uma melhora no fitness das funções quando comparado com os resultados do PSO tradicional. Isso pode ser explicado pela reinicialização aleatória das partículas para fugir dos mínimos locais. Entretando essa alteração na condição de parada do algoritmo também trás impactos no tempo de convergência do método, pode-se dizer que em todos os benchmarks tivemos um aumento considerável no tempo de convergência do método.

### Artificial Bee Colony (ABC)
Resultados para o ABC padrão.

#### - n_epocas
Nesse experimento foi testado a influência do número de épocas na convergência do ABC. O número de épocas foi variado entre os valores: 100, 200, 400, 600 e 800.
##### Configuração
```
benchmark       = Ackley function
NP              = 200       # tamanho da colônia
dim_problema    = 10        # dimensão do problema, quantos atributos a serem otimizados
limit           = 20        # limite até abandonar uma fonte de alimento
num_repeticoes  = 100       # número de repetições do experimento
```

##### Resultados
n_epocas        | 100   | 200   | 400   | 600   | 800
--------------- | ----- | ----- | ----- | ----- | -----
fitness         | 1.4390| 0.9704| 0.3283| 0.3860| 0.3198
tempo           | 209s  | 409s  | 848s  | 1286s | 1726s

Nos resultados acima pode-se ver uma tendência a uma melhora do fitness quando se aumenta o número de épocas na convergência do algoritmo. Essa melhora no fitness é acompanhada pelo maior esforço computacional do algoritmo o que reflete também no tempo de convergência, quanto mais épocas mais o algoritmo vai demorar para retornar uma resposta. Também é razóavel acreditar que exista um limite no número de épocas utilizadas, onde o fitness não vai obter nenhuma melhora, pois já terá convergido para algum valor. Dessa forma é bom avaliar o trade off entre fitness e tempo de resposta ao se escolher o número de épocas. No nosso caso escolhemos n_epocas = 100 como melhor resultado pelo motivo dos outros valores de épocas testados consumirem muito tempo para convergência.

#### - limit
Nesse experimento foi análisado a variável 'limit' que controla quando as abelhas irão abandonar uma fonte de alimento e partir para outra. Nos experimentos realizados testamos a variável 'limit' com os valores: 5, 10, 20, 30 e 40.
 
##### Configuração
```
benchmark       = Ackley function
NP              = 200       # tamanho da colônia
dim_problema    = 10        # dimensão do problema, quantos atributos a serem otimizados
n_epocas        = 100       # número de épocas para convergência
num_repeticoes  = 100       # número de repetições do experimento
```

##### Resultados
limit           | 5     | 10    | 20    | 30    | 40
--------------- | ----- | ----- | ----- | ----- | -----
fitness         | 0.5231| 1.2120| 1.8024| 1.7953| 1.7383
tempo           | 219s  | 211s  | 207s  | 209s | 206s

Os resultados do experimento variando o parâmetro 'limit' mostram que valores mais baixos de 'limit' conseguem obter melhores resultados de fitness. Isso pode ser explicado por as abelhas não perderem muito tempo nas fontes de alimento sem conseguir melhora-las. Valores baixos de 'limit' possibilitam as abelhas as explorarem mais fontes de alimento o que consequentemente aumenta as chances de se encontrar uma fonte de alimento melhor. É importante mencionar que o valor de 'limit' utilizado não tem impacto no tempo de convergência do algoritmo, apenas na qualidade da convergência. O melhor valor que encontramos nesse experimento foi 'limit=5' que conseguiu chegar a um fitness de 0.5231 no benchmark Ackley.


#### - NP
Nesse experimento avaliamos como o número de abelhas influência na convergência do algoritmo. Para isso testamos cinco valores diferentes de NP, foram eles: 20, 50, 100, 200 e 300.

##### Configuração
```
benchmark       = Ackley function
limit           = 5       # limite até abandonar uma fonte de alimento
dim_problema    = 10      # dimensão do problema, quantos atributos a serem otimizados
n_epocas        = 100     # número de épocas para convergência
num_repeticoes  = 100     # número de repetições do experimento
```

##### Resultados
NP              | 20    | 50    | 100   | 200   | 300
--------------- | ----- | ----- | ----- | ----- | -----
fitness         | 5.6308| 3.0853| 1.3094| 0.9966| 0.6839
tempo           | 21s   | 51s   | 105s  | 208s  | 314s

Nos experimentos variando o tamanho da colônia (NP) é possível ver que colônias maiores tendem a encontrar um valor de fitness melhor. Isso pode ser explicado pelo motivo de colônias maiores terem mais fontes de alimentos sendo exploradas ao mesmo tempo. É possível que também exista um limite para o tamanho da colônia onde a partir dele não se veja resultado significativo no fitness do algoritmo, porém com os valores de NP testados aqui não conseguimos chegar a esse limite. Outro fato a ser observado é que quanto maior a colônia, maior será o custo computacional do algoritmo elevando assim seu tempo de execução, então o trade off entre fitness e tempo de execuçáo também tem que ser considerado ao escolher o tamanho da colônia. Para seguir nossos experimentos, escolhemos 'NP = 200', como melhor valor pois ele conseguiu um bom valor de fitness em um tempo razoável para nós. 

#### Benchmark / Dimensão das partículas
Nesse experimentos testamos como o ABC se comporta nos diferentes benchmarks apresentados anteriormente. Também foi análisado o impacto da dimensão do problema (número de atríbutos a serem otimizados) no resultado final do algoritmo.

##### Configuração
```
NP              = 200     # tamanho da colônia
limit           = 5       # limite até abandonar uma fonte de alimento
n_epocas        = 100     # número de épocas para convergência
num_repeticoes  = 100     # número de repetições do experimento
```

##### Resultados
dim_problema = 10

benchmark       | Ackley| Alpine|Schwefel   |Happy Cat  | Brown     | Exponential
--------------- | ----- | ----- | -----     | -----     | -----     |  ----
fitness         | 1.1918| 0.0301| 1.9002    | 0.1931    | 0.0010    | -0.9999
tempo           | 207s  | 167s  | 168s      | 191s      | 282s      | 170s

dim_problema = 20

benchmark       | Ackley| Alpine|Schwefel   |Happy Cat  | Brown     | Exponential
--------------- | ----- | ----- | -----     | -----     | -----     |  ----
fitness         | 2.4237| 0.0823| 17.7931   | 0.4220    | 0.0066    | -0.9996
tempo           | 208s  | 167s  | 168s      | 192s      | 420s      | 170s

dim_problema = 50

benchmark       | Ackley| Alpine|Schwefel   |Happy Cat  | Brown     | Exponential
--------------- | ----- | ----- | -----     | -----     | -----     |  ----
fitness         |12.7170| 8.0740| 3861.17   | 0.6775    | 2.9196    | -0.8193
tempo           | 210s  | 168s  | 170s      | 194s      | 832s      | 172s

Assim como no PSO, também é possível se ver um reflexo no fitness do ABC quando se aumenta o número de atributos a serem otimizados por ele, quanto mais atributos mais complexo fica o processo de otimização o que resulta em um fitness maior. Para o ABC o benchmark Schwefel se apresenta como sendo o mais desafiador, assim como aconteceu com o PSO. Entretanto, o ABC foi capaz de encontrar uma solução melhor do que a do PSO  no Schwefel.


### Artificial Bee Colony (ABC) - Variação
Resultados para a variação do ABC onde é estabelecido um critério de parada alternativo. Nela, em vez de se rodar o algoritmo por um número fixo de épocas, ele é rodado até que a melhor solução não melhore por um número 'n' de épocas. Essa adaptação pode permitir que o ABC encontre soluções melhores sem ser sabotado pelo limite no número de épocas.


#### Benchmark / Dimensão das partículas
Nesse experimentos testamos como a variação do ABC se comporta nos diferentes benchmarks apresentados anteriormente. Também foi análisado o impacto da dimensão do problema (número de atríbutos a serem otimizados) no resultado final do algoritmo.

##### Configuração
```
NP                  = 200     # tamanho da colônia
limit               = 5       # limite até abandonar uma fonte de alimento
n_epocas_melhora    = 20      # número de épocas sem melhora da melhor solução
num_repeticoes      = 100     # número de repetições do experimento
```

##### Resultados

dim_problema = 10

benchmark       | Ackley| Alpine|Schwefel   |Happy Cat  | Brown     | Exponential
--------------- | ----- | ----- | -----     | -----     | -----     |  ----
fitness         | 1.4953| 0.0129| 4.3000    | 0.2081    | 0.0008    | -0.9999
tempo           | 196s  | 178s  | 164s      | 83s       | 255s      | 143s

dim_problema = 20

benchmark       | Ackley| Alpine|Schwefel   |Happy Cat  | Brown     | Exponential
--------------- | ----- | ----- | -----     | -----     | -----     |  ----
fitness         | 0.8705| 0.0315| 2.8007    | 0.4965    | 0.0015    | -0.9999
tempo           | 367s  | 380s  | 345s      | 75s       | 564s      | 324s

dim_problema = 50

benchmark       | Ackley| Alpine|Schwefel   |Happy Cat  | Brown     | Exponential
--------------- | ----- | ----- | -----     | -----     | -----     |  ----
fitness         | 5.4210| 2.6845| 481.42    | 0.7726    | 5.1532    | -0.9922
tempo           | 393s  | 270s  | 332s      | 94s       | 292s      | 275s

Os resultados da variação do ABC, mostram que a adaptação feita não tem um efeito muito significante quando o problema a ser otimizado não é tão complexo, por exemplo quando o benchmark é fácil e/ou se tem poucos atributos a serem otimizados. Isso pode ser explicado pelo fato do número fixo de épocas que utilizamos anteriormente no ABC padrão já ser suficiente para encontrar uma boa solução nesses casos. Ainda assim, em problemas mais complexos com mais variáveis a serem otimizadas e/ou em um benchmark mais difícil, a variação escolhida do ABC consegue mostrar melhores resultados, pois o número fixo de épocas que escolhemos anteriormente pode não ser suficiente para se obter uma boa otimização nesses casos. Como exemplo temos os resultados do benchmark Schwefel que melhoraram significativamente na variação do ABC em comparação aos resultados obtidos com o ABC padrão.

## Conclusão

falar do pso que foi necessário adicionar um limite máximo de épocas pq o gbest continuava melhorando por muito tempo, ele melhorava mas era muito pouco

