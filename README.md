<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00FFFF,100:000000&height=200&section=header&text=Monitoramento%20De%20Preços%20Amazon&fontSize=45&fontColor=ffffff&animation=fadeIn" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Selenium-4.0+-43B02A?style=for-the-badge&logo=selenium&logoColor=white" />
  <img src="https://img.shields.io/badge/Web%20Scraping-FF6B35?style=for-the-badge&logo=web-scraper&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Ativo-brightgreen?style=for-the-badge" />
</p>

<h2 align="center">📊 Monitoramento Inteligente de Preços da Amazon</h2>
Um projeto de aprendizado em automação web com Selenium


# 📝 Descrição do Projeto

## Este projeto é uma aplicação web construída com **Streamlit** que utiliza **Selenium** para realizar a raspagem de dados (web scraping) na Amazon Brasil. O objetivo é buscar um produto especificado pelo usuário e extrair os preços dos primeiros resultados, fornecendo uma análise estatística rápida e a opção de download dos dados.

A ferramenta é útil para monitorar rapidamente a variação de preços e identificar as melhores ofertas para um determinado item na Amazon.

## 🎯 Por Que Fiz Este Projeto?
Como desenvolvedor em aprendizado, queria:
- Aplicar Selenium em um projeto real
- Entender desafios de web scraping
- Criar algo útil que poderia evoluir para um monitor de preços
# Tecnologias
## ✅Automação & Web Scraping
- Selenium WebDriver 4.15+: Automação avançada do navegador Chrome
- CSS Selectors Avançados: Localização robusta de elementos dinâmicos
- XPath Expressions: Seleção alternativa para elementos complexos
- WebDriverWait + Expected Conditions: Espera inteligente para carregamento dinâmico
- ActionChains: Simulação de interações de usuário realistas

## ✅Desenvolvimento Web & Interface

- Streamlit 1.28+: Framework para criar aplicações web em Python
- Session State: Gerenciamento de estado entre interações do usuário
- Streamlit Components: Botões, inputs, métricas e containers interativos
- CSS Personalizado: Estilização da interface via markdown HTML
## ✅Processamento & Análise de Dados

- Pandas 2.1.4+: Manipulação e análise estruturada de dados
- DataFrames: Estruturação tabular dos produtos coletados
- Operações Vetorizadas: Cálculos eficientes de estatísticas
- Data Cleaning: Limpeza e transformação de strings para numéricos
  ### 1. Tela Inicial

Aqui o usuário insere o termo de pesquisa (Ex: "Brinquedo") e inicia a busca.

![Captura de Tela da Interface Inicial](assets/foto1.png)
### 2. Resultados e Análise

Exibição dos 5 produtos encontrados, o resumo estatístico e o botão para download do CSV.

![Captura de Tela dos Resultados e Métricas](assets/foto2.png)

## ⚙️ Tecnologias Utilizadas

* **Python 3.x**
* **Streamlit**: Framework para criação rápida da interface web.
* **Selenium**: Utilizado para automação do navegador (Chrome) e coleta dos dados na página da Amazon.
* **datetime** e **time**: Para manipulação de tempo e criação de nomes de arquivos dinâmicos.

 ## ⚠️ Se o código parar de funcionar, provavelmente as classes (a-price-whole, a-size-base-plus.a-color-base.a-text-normal) da Amazon mudaram.⚠️
 
 ### 🧑‍💻 AutorDesenvolvido por Vinicius Santos - Tech.
