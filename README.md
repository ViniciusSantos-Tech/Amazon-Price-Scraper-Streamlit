<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00FFFF,100:000000&height=200&section=header&text=Amazon%20Kindle%20Price%20Tracker&fontSize=45&fontColor=ffffff&animation=fadeIn" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Selenium-4.0+-43B02A?style=for-the-badge&logo=selenium&logoColor=white" />
  <img src="https://img.shields.io/badge/Web%20Scraping-FF6B35?style=for-the-badge&logo=web-scraper&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Ativo-brightgreen?style=for-the-badge" />
</p>

<h2 align="center">📊 Monitoramento Inteligente de Preços da Amazon</h2>

**Um projeto de aprendizado em automação web com Selenium**

## 🎯 Por Que Fiz Este Projeto?
Como desenvolvedor em aprendizado, queria:
- Aplicar Selenium em um projeto real
- Entender desafios de web scraping
- Criar algo útil que poderia evoluir para um monitor de preços

## 🛠️ Tecnologias e Abordagem
- **Selenium WebDriver**: Para automação e coleta de dados
- **CSS Selectors**: Para localização robusta de elementos
- **WebDriverWait**: Para lidar com carregamento dinâmico
- **Estruturas de dados**: Listas e dicionários para organizar informação

## 🧠 Principais Aprendizados
### 1. Timing é Tudo
Aprendi a diferença entre `time.sleep()` e `WebDriverWait`, 
e quando usar cada um para evitar `ElementNotInteractableException`.

### 2. Scroll Necessário
Elementos podem estar fora da viewport - precisei implementar 
`execute_script("scrollIntoView")` antes de interagir.

### 3. Dados 
Transformar preços de texto ("R$ 1.599") para números (1599.0)
foi crucial para possibilitar análise comparativa.

### 4. Estruturação Progressiva
Comecei com print simples, evolui para listas, depois para 
dicionários - mostrando crescimento no pensamento de estruturação.

## 📊 Funcionalidades Implementadas
- ✅ Coleta automática dos 5 primeiros resultados  
- ✅ Conversão de preços para formato numérico  
- ✅ Identificação do produto mais barato e mais caro  
- ✅ Cálculo da média dos preços coletados
- ✅ Cálculo da diferença entre extremos  
- ✅ Saída formatada e organizada
## 💾 Exportação Profissional
- ✅ Geração automática de arquivos CSV
- ✅ Nomes únicos com timestamp (kindle_precos_YYYYMMDD_HHMMSS.csv)
- ✅ Formatação correta para Excel/Google Sheets
- ✅ Codificação UTF-8 para caracteres especiais

## 🚧 Desafios Enfrentados
- **Amazon muda constantemente**: Classes CSS podem alterar
- **Elementos dinâmicos**: Precisam de waits específicos
- **Formatação de preços**: Diferentes formatos (1.599 vs 1,599)

## 🔮 Como Poderia Evoluir
Este projeto é uma base que poderia se tornar:
1. **Monitor contínuo**: Rodar automaticamente todo dia
2. **Alertas**: Notificar quando preço baixar
3. **Dashboard**: Interface web para visualização
4. **Multi-mercado**: Comparar com Mercado Livre, Magalu

## 🏆 Habilidades Demonstradas
- Automação web com Selenium
- Manipulação de dados em Python
- Debug e resolução de problemas
- Organização de código em funções
- Documentação de projetos

## 💡 Para Iniciantes Como Eu
Se você tá começando com Selenium, este projeto mostra:
- Que é possível criar algo funcional rápido
- Que erros são oportunidades de aprendizado
- Que tutorial é só ponto de partida

---

**Autor**: Vinicius Santos  
**Objetivo**: Aprendizado prático de Selenium  
**Status**: Projeto de estudo - aberto a contribuições

### 🔧 Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/amazon-kindle-tracker.git
cd amazon-kindle-tracker
