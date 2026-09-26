# Metodologia

## 1. Fonte

A base principal é o **Cadastro Nacional de Endereços para Fins Estatísticos (CNEFE)** do Censo Demográfico 2022, disponibilizado pelo IBGE para o município de Piracicaba/SP (código 3538709).

Arquivo:
`3538709_PIRACICABA.zip`

URL oficial:
https://ftp.ibge.gov.br/Cadastro_Nacional_de_Enderecos_para_Fins_Estatisticos/Censo_Demografico_2022/Arquivos_CNEFE/CSV/Municipio/35_SP/3538709_PIRACICABA.zip

A base contém **224.750 registros de endereço**.

## 2. Unidade de análise

Como o CNEFE contém um registro por endereço, uma mesma rua aparece muitas vezes. Para analisar a nomenclatura, foram usadas duas unidades:

### Denominação única de logradouro

Combinação de:

- `NOM_TIPO_SEGLOGR`
- `NOM_TITULO_SEGLOGR`
- `NOM_SEGLOGR`

Essa redução produz **4.086 denominações únicas** no arquivo analisado.

Ela é usada para contagens gerais de títulos como "Doutor", "Professor" etc.

### Denominação por localidade

Combinação de:

- `DSC_LOCALIDADE`
- `NOM_TIPO_SEGLOGR`
- `NOM_TITULO_SEGLOGR`
- `NOM_SEGLOGR`

Essa visão preserva o contexto territorial e produz **5.603 combinações localidade–logradouro**, sendo usada para investigar padrões temáticos por bairro/localidade.

## 3. Limpeza

O processamento:

1. lê o CSV com separador `;`;
2. mantém as colunas de localidade, tipo, título e nome;
3. substitui valores ausentes por texto vazio;
4. remove espaços nas extremidades;
5. cria o nome completo do logradouro;
6. remove duplicatas de acordo com a unidade de análise.

O script em `src/build_streets.py` reproduz essa etapa.

## 4. Títulos honoríficos

Os títulos são contados diretamente em `NOM_TITULO_SEGLOGR`.

Na tabela de denominações únicas:

| Título | Ocorrências |
|---|---:|
| Doutor | 102 |
| Doutora | 1 |
| Professor | 74 |
| Professora | 29 |

Esses valores **não representam o total de homens e mulheres homenageados**. Eles medem apenas a presença explícita desses títulos na nomenclatura.

## 5. Sobrenomes recorrentes

Para a exploração de sobrenomes, a busca é textual no campo `NOM_SEGLOGR`. Quando uma mesma homenagem aparece como tipos de via diferentes, ela pode ser consolidada para evitar dupla contagem do mesmo nome.

Por isso, a análise de sobrenomes deve ser interpretada como **recorrência de nomes homenageados no cadastro**, não como prova de parentesco entre pessoas.

## 6. Temas por bairro

As categorias como flores, aves, árvores, pedras, países e peixes foram obtidas por análise exploratória dos nomes dentro das localidades.

O procedimento combina:

- agrupamento por `DSC_LOCALIDADE`;
- busca por vocabulários temáticos;
- inspeção manual dos resultados;
- revisão de falsos positivos.

Essas categorias são descritivas. Para afirmar a intenção histórica oficial da nomeação, é necessário consultar legislação municipal, processos de denominação ou documentação histórica.

## 7. Limitações

O CNEFE:

- não informa quem propôs a homenagem;
- não informa a biografia do homenageado;
- não garante que pessoas com o mesmo sobrenome sejam parentes;
- pode conter grafias alternativas ou duplicidades cadastrais;
- registra a situação observada no Censo 2022, não a evolução histórica completa da nomenclatura.

Por isso, o projeto separa **padrões encontrados nos dados** de **interpretações históricas que exigem validação documental**.
