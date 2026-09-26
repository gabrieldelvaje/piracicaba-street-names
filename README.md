# Piracicaba Street Names — padrões escondidos nas ruas da cidade

Projeto de **análise exploratória e data storytelling** sobre os nomes dos logradouros de Piracicaba (SP).

A pergunta central é simples:

> **Os nomes das ruas de Piracicaba são aleatórios ou existem padrões territoriais, familiares e históricos escondidos no mapa da cidade?**

A análise usa o **CNEFE — Cadastro Nacional de Endereços para Fins Estatísticos**, do **Censo Demográfico 2022 / IBGE**, para organizar os logradouros por localidade, eliminar repetições de endereços e investigar temas recorrentes, sobrenomes, títulos e outros padrões de nomenclatura.

![Capa do carrossel](assets/carousel/01-cover.jpg)

## Pergunta de pesquisa

**Quando os nomes das ruas são organizados por região, quais padrões aparecem e o que eles podem revelar sobre a memória urbana de Piracicaba?**

O projeto não tenta reconstruir sozinho a história oficial de cada denominação. O objetivo é usar o cadastro de endereços como ponto de partida para localizar padrões que podem ser aprofundados posteriormente com legislação municipal, arquivos históricos e biografias dos homenageados.

## Base utilizada

Fonte principal:

**IBGE — CNEFE, Censo Demográfico 2022**  
Município: **Piracicaba/SP**  
Código IBGE: **3538709**

Arquivo municipal:

`3538709_PIRACICABA.zip`

Download oficial:

https://ftp.ibge.gov.br/Cadastro_Nacional_de_Enderecos_para_Fins_Estatisticos/Censo_Demografico_2022/Arquivos_CNEFE/CSV/Municipio/35_SP/3538709_PIRACICABA.zip

Na versão analisada:

| Etapa | Registros |
|---|---:|
| Endereços do CNEFE | **224.750** |
| Denominações únicas de logradouro | **4.086** |
| Combinações localidade–logradouro | **5.603** |

> O CNEFE é uma base de **endereços**. Uma mesma rua pode aparecer centenas de vezes porque cada número/endereço é uma observação. Por isso, a primeira etapa da análise é transformar a base de endereços em uma base de **nomes de logradouros únicos**.

## Principais achados

### 1. Alguns bairros/localidades funcionam como coleções temáticas

Na análise exploratória, vários agrupamentos territoriais apresentaram conjuntos de nomes com um tema recorrente:

- **Nova Piracicaba:** 32 nomes associados a flores/plantas e 23 a aves;
- **Mário Dedini:** 16 nomes associados a árvores e 8 a pedras/gemas;
- **Cidade Jardim:** 9 países identificados nas placas;
- **Jupiá:** 8 nomes associados a peixes.

Isso sugere que, em diversas partes da cidade, a lógica de nomeação não é aleatória.

### 2. Nova Piracicaba tem forte presença de referências à natureza

Foram identificados **32 nomes de flores/plantas** e **23 nomes de aves**.

Entre os exemplos encontrados estão:

`Orquídeas`, `Tulipas`, `Violetas`, `Girassóis`, `Araras`, `Sabiás` e `Beija-Flores`.

### 3. Cidade Jardim funciona quase como um mapa-múndi

Foram identificados **9 países** na nomenclatura local:

- Alemanha
- Brasil
- Espanha
- Estados Unidos
- França
- Holanda
- Itália
- Portugal
- Suíça

### 4. Sobrenomes se repetem nas homenagens

Os sobrenomes mais recorrentes na exploração foram:

| Sobrenome | Homenagens distintas |
|---|---:|
| Furlan | **22** |
| Trevisan | **19** |
| Ometto | **9** |
| Dedini | **8** |
| Pecorari | **8** |

A repetição é um achado de nomenclatura, **não uma prova de parentesco**. Pessoas diferentes podem compartilhar um sobrenome sem pertencer à mesma família, e a relação histórica entre os homenageados precisa ser investigada em fontes documentais.

### 5. Os títulos usados nas vias também revelam um padrão

Entre as denominações únicas:

| Título | Ocorrências |
|---|---:|
| Doutor | **102** |
| Doutora | **1** |
| Professor | **74** |
| Professora | **29** |

Também aparecem títulos como `Padre`, `Coronel`, `Capitão`, `Barão` e outros.

Esses números medem **o título explícito escrito no nome da via**. Eles **não equivalem** ao total de homens e mulheres homenageados.

### 6. Homenagens pessoais são um componente importante da toponímia

A inspeção exploratória mostra que uma parcela relevante dos logradouros homenageia pessoas e que nomes masculinos aparecem com forte predominância.

Como o CNEFE não contém uma variável de gênero nem a biografia dos homenageados, o projeto **não transforma essa observação em uma estimativa demográfica precisa**. O carrossel resume o padrão qualitativamente, enquanto a validação histórica completa exigiria consulta individual às leis de denominação e às biografias.

## Carrossel

As sete imagens abaixo são as artes finais do projeto.

### 1. As ruas de Piracicaba têm padrões escondidos

![Slide 1](assets/carousel/01-cover.jpg)

### 2. Em muitos bairros, os nomes não são aleatórios

![Slide 2](assets/carousel/02-bairros-tematicos.jpg)

### 3. Nova Piracicaba virou um jardim

![Slide 3](assets/carousel/03-nova-piracicaba.jpg)

### 4. Cidade Jardim esconde um mapa-múndi

![Slide 4](assets/carousel/04-cidade-jardim.jpg)

### 5. As ruas também guardam famílias

![Slide 5](assets/carousel/05-sobrenomes.jpg)

### 6. O mapa revela quem era homenageado

![Slide 6](assets/carousel/06-titulos.jpg)

### 7. Em resumo

![Slide 7](assets/carousel/07-resumo.jpg)

## Metodologia

### 1. Leitura da base bruta

O arquivo municipal do CNEFE contém **224.750 registros de endereço**.

As colunas centrais usadas na análise são:

- `DSC_LOCALIDADE`
- `NOM_TIPO_SEGLOGR`
- `NOM_TITULO_SEGLOGR`
- `NOM_SEGLOGR`

### 2. Padronização textual

Antes da análise:

- valores ausentes são substituídos por texto vazio;
- espaços nas extremidades são removidos;
- tipo, título e nome são concatenados para formar o nome completo do logradouro;
- as comparações exploratórias podem usar versões normalizadas em caixa alta e sem diferenças triviais de espaçamento.

A base original não é sobrescrita.

### 3. Remoção da repetição causada pelos endereços

O CNEFE registra endereços, e não uma linha por rua. Por isso são construídas duas tabelas analíticas.

**Denominação única de logradouro**

Chave:

```text
NOM_TIPO_SEGLOGR
+ NOM_TITULO_SEGLOGR
+ NOM_SEGLOGR
```

Resultado: **4.086 denominações únicas**.

Essa visão é usada para análises gerais, como títulos recorrentes.

**Denominação por localidade**

Chave:

```text
DSC_LOCALIDADE
+ NOM_TIPO_SEGLOGR
+ NOM_TITULO_SEGLOGR
+ NOM_SEGLOGR
```

Resultado: **5.603 combinações localidade–logradouro**.

Essa visão preserva o contexto territorial e é usada para procurar temas locais.

### 4. Agrupamento territorial

Os padrões temáticos são investigados a partir de `DSC_LOCALIDADE`.

No carrossel, o termo **“bairro”** é usado editorialmente para facilitar a leitura. Tecnicamente, o agrupamento vem do campo de **localidade do CNEFE**, que não deve ser tratado automaticamente como uma delimitação oficial de bairro sem validação com o cadastro municipal.

### 5. Identificação dos temas

Os nomes foram explorados por grupos semânticos, como:

- flores e plantas;
- aves;
- árvores;
- pedras e gemas;
- países;
- peixes;
- religião;
- datas;
- lugares;
- homenagens pessoais.

O processo combina:

1. busca por palavras e listas temáticas;
2. agrupamento por localidade;
3. contagem de denominações únicas;
4. inspeção manual dos resultados;
5. remoção de falsos positivos evidentes.

As categorias são **exploratórias**, e não uma classificação oficial do município.

### 6. Sobrenomes

A recorrência de sobrenomes foi calculada sobre nomes de logradouros deduplicados.

O objetivo é responder:

> **Quais sobrenomes aparecem repetidamente nas homenagens do mapa de Piracicaba?**

A contagem não permite concluir, sozinha, que os homenageados pertencem à mesma família.

### 7. Títulos

Os títulos foram extraídos diretamente do campo:

`NOM_TITULO_SEGLOGR`

Por isso, números como `Doutor = 102` representam **denominações que trazem explicitamente esse título**.

Eles não devem ser interpretados como:

- quantidade total de médicos;
- quantidade total de homens;
- quantidade total de pessoas homenageadas.

### 8. Gênero das homenagens

O CNEFE **não informa gênero**.

A leitura sobre predominância masculina é uma conclusão exploratória baseada no conjunto de homenagens pessoais, nomes próprios e títulos observados. Uma classificação quantitativa definitiva exigiria validar os homenageados individualmente em fontes históricas.

Por essa razão, o repositório não publica uma porcentagem de homens versus mulheres sem uma etapa adicional de validação.

### 9. Validação

Os valores apresentados no carrossel são armazenados em arquivos CSV do repositório.

O script de validação verifica:

- quantidade de registros do CNEFE registrada no projeto;
- quantidade de denominações únicas;
- quantidade de combinações localidade–logradouro;
- métricas usadas nos slides;
- presença dos sete arquivos do carrossel.

## O que os dados medem — e o que não medem

### Medem

- nomes cadastrados no CNEFE;
- recorrência textual de títulos e sobrenomes;
- agrupamentos de nomes por localidade;
- padrões temáticos encontrados na nomenclatura.

### Não medem diretamente

- intenção oficial de quem nomeou cada rua;
- parentesco entre homenageados;
- profissão real de uma pessoa quando o título não está explícito;
- gênero oficial de todos os homenageados;
- importância histórica de uma pessoa;
- limites oficiais de bairro;
- ano em que cada rua recebeu o nome.

Essas perguntas exigem fontes adicionais, como leis municipais, arquivos da Câmara, mapas históricos e biografias.

## Estrutura do repositório

```text
assets/
  carousel/
    01-cover.jpg
    02-bairros-tematicos.jpg
    03-nova-piracicaba.jpg
    04-cidade-jardim.jpg
    05-sobrenomes.jpg
    06-titulos.jpg
    07-resumo.jpg

data/
  insights_summary.csv
  carousel_metrics.csv

docs/
  methodology.md
  sources.md
  data-validation.md

src/
  build_streets.py
  validate_metrics.py

README.md
requirements.txt
.gitignore
```

## Reprodução

Instale as dependências:

```bash
pip install -r requirements.txt
```

Para baixar o CNEFE e gerar as tabelas deduplicadas:

```bash
python src/build_streets.py
```

O script cria:

```text
data/processed/streets_unique.csv
data/processed/streets_by_locality.csv
```

Os arquivos gerados em `data/processed/` não precisam ser versionados, pois podem ser reconstruídos a partir da fonte oficial.

Para conferir as métricas documentadas no repositório:

```bash
python src/validate_metrics.py
```

## Validação e limitações

Alguns cuidados são essenciais para interpretar o projeto:

1. **CNEFE não é uma base histórica de homenagens.** Ele informa o nome cadastrado do logradouro.
2. **Localidade não é necessariamente sinônimo de bairro oficial.**
3. **Sobrenome repetido não comprova família.**
4. **Título não comprova profissão nem gênero de todos os homenageados.**
5. **Categorias temáticas dependem de classificação exploratória.**
6. **A predominância masculina é apresentada qualitativamente enquanto não houver validação biográfica individual.**
7. **Os resultados descrevem o cadastro do Censo 2022**, e não toda a história das ruas de Piracicaba.

Mais detalhes:

- [`docs/methodology.md`](docs/methodology.md)
- [`docs/data-validation.md`](docs/data-validation.md)
- [`docs/sources.md`](docs/sources.md)

## Possíveis extensões

Este projeto pode ser aprofundado com:

- leis municipais de denominação;
- ano de criação ou renomeação de cada via;
- biografia dos homenageados;
- classificação validada de gênero;
- profissão e área de atuação;
- comparação entre bairros antigos e loteamentos recentes;
- geometria das ruas em GIS;
- mapa interativo por categoria;
- evolução histórica da memória urbana de Piracicaba.

## Fonte

**IBGE — Cadastro Nacional de Endereços para Fins Estatísticos (CNEFE), Censo Demográfico 2022.**

Documentação e links estão em [`docs/sources.md`](docs/sources.md).

## Autor

**Gabriel Delvaje**  
Data analysis & data storytelling — *Piracicaba Data Stories*.
