# 🐱 Vendas Pet Shop — Análise de Dados com Python

Pipeline de dados com geração sintética, engenharia de atributos e análise de faturamento de um pet shop especializado em produtos para gatos.

## 📋 O que o projeto faz

- Gera 200 pedidos de vendas com dados realistas (produtos, cidades, preços, datas)
- Aplica engenharia de atributos criando colunas como `Receita_Total`, `Turno`, `Regiao`, `Faixa_Quantidade`
- Analisa o faturamento total por **estado** e por **categoria**
- Exporta os dados enriquecidos em `vendas.csv`

## 🗂️ Arquivos

| Arquivo | Descrição |
|---|---|
| `vendas.projeto.py` | Script principal — geração, engenharia e análise |
| `vendas.csv` | Dataset final gerado pelo script |

## ⚙️ Tecnologias

- Python 3.10+
- pandas
- numpy

## 🚀 Como rodar

**1. Instale as dependências:**
```
pip install pandas numpy
```

**2. Execute o script:**
```
python vendas.projeto.py
```

**3. Saída esperada no terminal:**
```
========================================
FATURAMENTO POR ESTADO
========================================
Estado  Faturamento (R$)
    MA    R$ 12,628.36
    ...

========================================
FATURAMENTO POR CATEGORIA
========================================
Categoria  Faturamento (R$)
    Ração    R$ 41,134.01
    ...
```

## 🛍️ Produtos analisados

| Produto | Categoria | Preço |
|---|---|---|
| PremieR Gatos Castrados | Ração | R$ 130,00 |
| N&D Prime | Ração | R$ 140,00 |
| Guabi Natural | Ração | R$ 110,00 |
| Catnip | Petisco | R$ 30,00 |
| Matatabi | Petisco | R$ 25,00 |
| Whiskas Temptations | Petisco | R$ 15,00 |
| Comedouros de Aço Inox | Material | R$ 35,00 |
| Comedouros Anti-Stress | Material | R$ 50,00 |

## 🗺️ Cidades cobertas

São Luís (MA), Teresina (PI), Manaus (AM), São Paulo (SP), Porto Alegre (RS), Cuiabá (MT)

---

> Dados 100% sintéticos gerados para fins educacionais.
