# Portifolio Manager

## Sobre o projeto

### Introdução
O projeto consiste em desenvolver um processo automatizado para monitorar uma carteira de investimentos com diversas classes de ativos, gerando a visualização dos dados via Power BI. O objetivo é trazer eficiência e precisão à gestão dos investimentos, controlando os riscos e obtendo resultados satisfatórios.

### Objetivo
O objetivo é construir um pipeline capaz de monitorar e consolidar a carteira de investimentos a partir de arquivos .csv com as movimentações e os valores dos saldos dos ativos de cada mês. Em seguida, os resultados serão visualizados através do Power BI, gerando gráficos, tabelas e análises de inteligência de portfólio. As informações serão recorrentes, então o pipeline deve ser projetado para ser executado novamente no futuro.

### Ferramentas usadas
Para resolver esse desafio, foi utilizado Python para criar o pipeline de dados e o Power BI para visualizar os dados.

### Fonte de dados
Para o desenvolvimento deste projeto, foi utilizado os arquivos .csv em anexo contendo as movimentações (subscrições e resgates de cada investimento) e saldos (valor dos ativos a cada mês) de uma carteira de investimentos.

## Sobre os dados

- balance = dados do balanço consolidado do portifolio
- movement = dados dos movimentos de caixa do portifolio
- portifolio_manager.ipynb = jupyter com análise e manipulação de dados
- pipeline.py = pipeline para integração com o Power BI

*Alguns arquivos .csv são referente a base de dados individuais para no PowerBI*
