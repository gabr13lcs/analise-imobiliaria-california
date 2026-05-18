# 🏠 Análise do Mercado Imobiliário da Califórnia — Power BI

> Dashboard interativo para exploração do mercado imobiliário californiano com base em dados do Census de 1990.

---

## 📌 Sobre o Projeto

Este projeto transforma dados brutos de 20.640 blocos residenciais da Califórnia em um dashboard interativo no Power BI, permitindo explorar a relação entre preço dos imóveis, renda dos moradores e localização geográfica.

---

## 🎯 Objetivos

- Analisar o preço médio dos imóveis por região geográfica
- Identificar a correlação entre renda mediana e preço dos imóveis
- Explorar como a idade das residências impacta o valor e a renda do entorno
- Entregar uma experiência visual focada em Data Storytelling

---

## 🛠️ Como foi feito

### Extração dos dados
- Dataset obtido via biblioteca `scikit-learn` do Python (`fetch_california_housing`)
- Exportado como `.csv` com o script Python incluído neste repositório

### Transformação (Power Query)
- Criação de colunas calculadas: **Preços (USD)**, **Renda Mediana (USD)**
- Criação de colunas de segmentação: **Faixa de Renda**, **Faixa de Preço**, **Região**
- Padronização de tipos e formatos numéricos

### Métricas e KPIs (DAX)
- População Total
- Blocos Analisados
- Renda Média
- Preço Médio
- Preço Máximo

### Visualizações
- Mapa geográfico colorido por região (Norte, Centro, Sul)
- Dispersão: Renda Mediana × Preço
- Dispersão: Preço × Latitude com linha de tendência
- Barras: Preço médio por Faixa de Renda e por Região
- Linha: Preço por idade das residências
- Filtros interativos por Faixa de Renda, Faixa de Preço e Região

---

## 💡 Principais Insights

- A região **Norte** (São Francisco) lidera em preço médio
- **Quanto maior a renda do bairro, maior o preço do imóvel** — correlação positiva confirmada
- Blocos com casas mais antigas concentram renda mediana menor
- O **Sul** (Los Angeles) concentra a maior densidade de blocos
- Imóveis em regiões de renda **Muito Alta** custam em média 3x mais que os de renda **Baixa**

---

## 🗂️ Arquivos do Repositório

| Arquivo | Descrição |
|---|---|
| `analise imobiliario.pbix` | Dashboard completo no Power BI |
| `california_housing.csv` | Dataset exportado via Python |

---

## 🧰 Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat&logo=powerbi&logoColor=black)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)

---

## 👤 Autor

**Gabriel Silva**
Estudante de Arquitetura de Dados | Python • SQL • Power BI

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gabriel-silva-br/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/gabr13lcs)
