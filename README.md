# 🧠 Unimed Data Intelligence – Predição de Risco e Otimização de Visitas

## 📘 Introdução

O projeto **Unimed Data Intelligence** foi desenvolvido durante o **Hackathon Unimed Ponta Grossa** com o objetivo de **analisar dados de beneficiários**, prever o **risco de reinternação hospitalar** e **otimizar a rota de visitas domiciliares** para pacientes de alto risco.  

A solução utiliza **técnicas de Machine Learning** e **integração com APIs do Google** para apoiar equipes médicas e administrativas na priorização do atendimento.

> 💡 *A base de dados utilizada neste projeto foi gerada artificialmente com auxílio de Inteligência Artificial para fins de demonstração, sem conter dados reais de pacientes.*

---

## 📋 Sumário
- [Visão Geral do Projeto](#visão-geral-do-projeto)
- [Arquitetura e Fluxo de Dados](#arquitetura-e-fluxo-de-dados)
- [Funcionalidades Principais](#funcionalidades-principais)
- [Modelo Preditivo](#modelo-preditivo)
- [Dashboard e Filtros Interativos](#dashboard-e-filtros-interativos)
- [Otimização de Rotas com Google Maps](#otimização-de-rotas-com-google-maps)
- [Requisitos e Instalação](#requisitos-e-instalação)
- [Uso do Sistema](#uso-do-sistema)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Resultados de Exemplo](#resultados-de-exemplo)
- [Créditos e Autores](#créditos-e-autores)
- [Licença](#licença)

---

## 🧩 Visão Geral do Projeto

O **Unimed Data Intelligence** permite prever o risco de reinternação de beneficiários e planejar visitas domiciliares com base em critérios de prioridade e eficiência logística.  
A solução combina **análise preditiva** e **geoprocessamento inteligente** para aumentar a eficácia no acompanhamento de pacientes crônicos e de alto risco.

---

## 🏗️ Arquitetura e Fluxo de Dados

1. **Entrada de Dados (Base Sintética):**  
   - Geração artificial de pacientes e características clínicas (idade, gênero, custo mensal, CID, etc.).  
   - Armazenamento em planilha Google Sheets ou CSV.

2. **Pré-processamento e Treinamento:**  
   - Pipeline de *Machine Learning* com `scikit-learn` e `GradientBoostingClassifier`.  
   - Normalização de variáveis e codificação categórica automática.

3. **Geração de Previsões:**  
   - Cálculo do `ScoreRisco_Preditivo` (probabilidade de reinternação em 30 dias).  
   - Exportação dos resultados ordenados para CSV e Google Sheets.

4. **Dashboard Interativo:**  
   - Exibição de pacientes ordenados pelo score.  
   - Filtros por idade e gênero.  
   - Seleção de pacientes para geração de rota.  
   - Controle de visitas realizadas.

5. **Otimização de Rotas:**  
   - Uso da Google Maps API para cálculo de distâncias.  
   - Algoritmo Branch and Bound (TSP) para determinar a rota mais eficiente.

---

## ⚙️ Funcionalidades Principais

✅ Leitura direta da planilha Google Sheets  
✅ Treinamento e avaliação de modelo preditivo  
✅ Exportação automática de resultados  
✅ Dashboard moderno com filtros combinados  
✅ Seleção de pacientes e geração de rota otimizada  
✅ Controle de visitas realizadas em tempo real  

---

## 🤖 Modelo Preditivo

O **Score de Risco** é calculado com base em um modelo supervisionado de *Machine Learning*, treinado a partir de dados simulados com comportamento estatístico realista.

### 🔹 Etapa 1: Fórmula Base (Regras de Negócio)
Critérios iniciais inspirados em políticas de saúde suplementar:
- `2 × ticket_médio ≤ custo_mensal < 10 × ticket_médio`
- E um dos seguintes:
  - Internações > 0  
  - Diagnóstico CID crônico  
  - Consultas > 3  
  - Consultas de emergência > 1  

### 🔹 Etapa 2: Modelo Preditivo Final
O modelo de **Gradient Boosting** aprendeu padrões complexos e calculou a probabilidade de reinternação em 30 dias.

> 🧮 Exemplo:  
> `ScoreRisco_Preditivo = 0.92` → 92% de chance de nova internação.

### 🔹 Métricas Obtidas
- **Recall:** ~72%  
- **AUC-ROC:** ~0.84  

---

## 🧭 Dashboard e Filtros Interativos

O painel (frontend) exibe os pacientes de forma dinâmica e interativa:

| Função | Descrição |
|--------|------------|
| 🔍 Filtro por idade | Ordena pacientes de maior para menor (ou vice-versa). |
| 🚻 Filtro por gênero | Mostra Masculino, Feminino ou ambos. |
| ✅ Seleção de pacientes | Escolhe quais entrarão na rota de visitas. |
| 📊 Score de risco | Mostra a probabilidade preditiva individual. |
| 🗺️ Gerar rota | Cria rota otimizada via Google Maps. |
| 🏁 Visita realizada | Atualiza o status e move o paciente para “Visitados Hoje”. |

---

## 🗺️ Otimização de Rotas com Google Maps

A função de rotas utiliza a **Distance Matrix API** do Google Maps e um algoritmo **Branch and Bound (TSP)** para definir a sequência de visitas mais eficiente.

🔑 **Observação:**  
A chave da API (`GOOGLE_MAPS_API_KEY`) deve ser armazenada com segurança, nunca diretamente no código-fonte.

---

## 🧩 Requisitos e Instalação

### 🔧 Requisitos
- Python 3.8+
- Conta Google com acesso a Google Sheets API
- Chave válida para Google Maps API

### 📦 Dependências
```bash
pip install pandas scikit-learn seaborn matplotlib gspread google-auth google-auth-oauthlib
```

### 🧠 Treinamento e Exportação
```bash
python analiseunimed.py
```

### 🌐 Dashboard
Implementação em React/TypeScript, consumindo os dados diretamente da planilha Google Sheets publicada em formato CSV.

---

## 🧮 Estrutura do Projeto

```
📂 UnimedDataIntelligence/
├── analiseunimed.py              # Script de análise e exportação
├── unimed_corrigido.csv          # Base sintética de pacientes
├── ResultadosUnimed.pdf          # Relatório de saída com previsões
├── previsoes_finais.csv          # Resultado gerado pelo modelo
└── README.md                     # Documentação do projeto
```

---

## 📊 Resultados de Exemplo

| Nome             | Carteirinha  | Idade | Gênero | Tipo Contrato | ScoreRisco_Preditivo |
|------------------|--------------|--------|---------|----------------|----------------------|
| Sophia Martins   | 69176732845  | 78     | Feminino | Familiar       | 0.93 |
| Heitor Silva     | 69402783162  | 80     | Masculino | Familiar      | 0.92 |
| Alice Rodrigues  | 69402404623  | 85     | Feminino | Coletivo      | 0.90 |
| Gabriel Souza    | 69352309595  | 78     | Masculino | Familiar      | 0.91 |

---

## 🧠 Análise Preditiva Baseada em IA

O <em>Score de Risco</em> é uma probabilidade calculada por um modelo de Machine Learning que avalia:

⬇️ **Principais Parâmetros Considerados:**
- 🧓 Idade e histórico clínico  
- 💰 Custo mensal e ticket médio  
- 🏥 Número de internações e consultas  
- 💉 Diagnósticos (CID)  
- ⏱️ Recência de atendimentos e urgências  

---

## 👥 Créditos e Autores

Este projeto foi desenvolvido durante o **Hackathon Unimed Ponta Grossa**  
por:

- **André Martins da Silva**  
- **Fernanda Pacheco Bento**  
- **Pedro Silveira Carvalho**

---

## 📜 Licença

Distribuído sob a **Licença MIT**.  
Uso, modificação e redistribuição são permitidos, desde que mantidos os devidos créditos.

---

✨ *Projeto criado com base em Inteligência Artificial aplicada à saúde suplementar, com foco em eficiência e cuidado personalizado.*
