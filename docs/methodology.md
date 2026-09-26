# Metodologia

## Objetivo

Investigar padrões de nomenclatura nos logradouros de Piracicaba a partir do CNEFE/IBGE, transformando uma base de endereços em unidades adequadas para análise de nomes de vias.

## Fonte

IBGE — Cadastro Nacional de Endereços para Fins Estatísticos (CNEFE), Censo Demográfico 2022.

Município: Piracicaba/SP — código 3538709.

## Campos usados

- `DSC_LOCALIDADE`
- `NOM_TIPO_SEGLOGR`
- `NOM_TITULO_SEGLOGR`
- `NOM_SEGLOGR`

## Pipeline

### 1. Leitura

O CSV é lido como texto para preservar a grafia original.

### 2. Limpeza

- preenchimento de nulos com string vazia;
- remoção de espaços laterais;
- criação de `FULL_STREET_NAME`;
- preservação das colunas originais.

### 3. Deduplicação

O CNEFE tem uma linha por endereço. Por isso são criadas duas visões:

**Logradouro único**

`NOM_TIPO_SEGLOGR + NOM_TITULO_SEGLOGR + NOM_SEGLOGR`

Resultado: **4.086 denominações únicas**.

**Logradouro por localidade**

`DSC_LOCALIDADE + NOM_TIPO_SEGLOGR + NOM_TITULO_SEGLOGR + NOM_SEGLOGR`

Resultado: **5.603 combinações localidade–logradouro**.

### 4. Análise temática

Os nomes são agrupados por localidade e confrontados com vocabulários temáticos. Resultados são revisados manualmente para reduzir falsos positivos.

Categorias usadas no carrossel incluem natureza, aves, árvores, pedras/gemas, países e peixes.

### 5. Sobrenomes

A recorrência é calculada em nomes deduplicados. O resultado indica repetição textual e não parentesco.

### 6. Títulos

Os títulos são contados diretamente em `NOM_TITULO_SEGLOGR`. Assim, `Doutor`, `Doutora`, `Professor` e `Professora` representam apenas títulos explicitamente cadastrados.

### 7. Gênero

O CNEFE não possui campo de gênero. A leitura de predominância masculina permanece exploratória e qualitativa nesta versão do projeto. Uma estatística precisa exigiria validação individual dos homenageados.

## Unidade territorial

`DSC_LOCALIDADE` é o campo territorial do CNEFE usado nos agrupamentos. O carrossel usa “bairro” como simplificação editorial, mas o campo não deve ser confundido automaticamente com limites oficiais municipais.

## Reprodutibilidade

`src/build_streets.py` reconstrói as tabelas deduplicadas.

`src/validate_metrics.py` confere os principais números documentados e os arquivos do carrossel.
