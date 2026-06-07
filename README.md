<p align="center">
  <a href="#-македонски">Македонски</a> •
  <a href="#-english">English</a>
</p>

---

# Иста задача, различен текст: робусност на LLM кон варијации на инструкција

> Проектна задача по предметот **Обработка на природните јазици (ОНПЈ)**
>
> Ментор: проф. Соња Гиевска
>
> Студенти:
> Тамара Стојаноска (231030)
> , Дона Костиќ (231195)
> , Мила Недановска (231106)

---

## Опис

Овој проект ја испитува **чувствителноста на големите јазични модели (LLM) на семантички еквивалентни варијации на инструкцијата (prompt)**. Со систематско конструирање на парафразирани prompt-ови за задача за стилски контролирано генерирање текст, се мери варијацијата во излезот преку семантички, лексички и стилски метрики.

Дополнително, се спроведува споредбена анализа меѓу модели од различни архитектурни семејства:

* **Decoder-only:** GPT2, Mistral-7B-Instruct
* **Encoder-decoder:** T5Gemma, FLAN-T5

---

## Структура на репото

```text
onpj-project/
│
├── gpt_model.ipynb                # Имплементација и евалуација на GPT2 модел
├── mistral_model.ipynb            # Имплементација и евалуација на Mistral-7B-Instruct
├── t5gemma_model.ipynb            # Имплементација и евалуација на T5Gemma
├── flant5_model.ipynb             # Имплементација и евалуација на FLAN-T5
│
├── dataset/                       # Множество на податоци: 1k_stories_100_genre.csv (~1000 кратки приказни)
├── graphics/                      # Генерирани графици и визуелизации на резултатите
├── generations_for_checkup/       # Генерирани текстови за рачна проверка
└── fixing_meta_widgets/           # Помошни скрипти за поправка на метаподатоци
```

---

## Модели

| Модел                    | Архитектура     | Notebook              |
| ------------------------ | --------------- | --------------------- |
| GPT-Oss (GPT-2)          | Decoder-only    | `gpt_model.ipynb`     |
| Mistral-7B-Instruct-v0.2 | Decoder-only    | `mistral_model.ipynb` |
| T5Gemma (t5gemma-2b)     | Encoder-decoder | `t5gemma_model.ipynb` |
| FLAN-T5                  | Encoder-decoder | `flant5_model.ipynb`  |

---

## Метрики за евалуација

| Метрика                        | Опис                                             |
| ------------------------------ | ------------------------------------------------ |
| **Косинусна сличност**         | Семантичка стабилност меѓу генерираните текстови |
| **Варијација на сентимент**    | Емоционална конзистентност                       |
| **Варијација на перплексност** | Јазична стабилност и природност на текстот       |
| **Стилска конзистентност**     | Процент на текстови во ист стил/жанр             |
| **Тип-токен сооднос (TTR)**    | Лексичка варијабилност                           |

---

## Клучни резултати

| Модел            | Косинусна сличност | Варијација на сентимент | Варијација на перплексност | Стилска конзистентност |
| ---------------- | ------------------ | ----------------------- | -------------------------- | ---------------------- |
| GPT2             | 0.2610             | 0.9354                  | 6.7028                     | 0.1920                 |
| Mistral-Instruct | **0.6113**         | **0.4352**              | 16.2034                    | **0.7653**             |
| T5Gemma          | 0.6112             | 0.8782                  | 11.5722                    | 0.6800                 |
| FLAN-T5          | 0.6016             | 0.8956                  | **3.5276**                 | 0.1333                 |

**Главни наоди:**

* **Mistral-Instruct** е најбалансиран модел според косинусна сличност, сентимент варијација и стилска конзистентност.
* **FLAN-T5** има најниска варијација на перплексност, но ниска стилска конзистентност.
* **GPT2** е најчувствителен на промени во prompt-от.
* **T5Gemma** покажува стабилни и балансирани резултати.

---

## Множество на податоци

Се користи множеството на податоци **`1k_stories_100_genre.csv`**, кое содржи околу 1000 кратки приказни распределени во повеќе жанрови. Од целото множество податоци се селектира случајно подмножество од **100 примероци** со `random_state=42` за репродуцибилност.

---

## Експериментален дизајн

* 5 семантички еквивалентни prompt-варијации
* 5 независни генерирања по prompt
* Идентични параметри: `max_new_tokens=120`, `temperature=0.7`
* 25 генерирани текстови по модел
* 100 генерирани текстови вкупно

---

## Инсталација и употреба

```bash
pip install transformers torch sentence-transformers scikit-learn pandas numpy
```

Потребна е Hugging Face автентикација:

```python
from huggingface_hub import login
login(token="YOUR_HF_TOKEN")
```

```bash
git clone https://github.com/tamara-00/onpj-project.git
cd onpj-project
```

---

## Користена литература

* Pecher et al. (2025). *Revisiting prompt sensitivity in large language models.*
* Liu et al. (2021). *Pre-train, Prompt, and Predict.*
* Reif et al. (2022). *A recipe for arbitrary text style transfer with LLMs.*
* Jiang et al. (2023). *Mistral 7B.*
* Chung et al. (2022). *Scaling instruction-finetuned language models.*

---

# Same Task, Different Text: LLM Robustness to Instruction Variations

> Project for the **Natural Language Processing (NLP)** course
> Mentor: Prof. Sonja Gievska
> Students: Tamara Stojanoska (231030), Dona Kostik (231195), Mila Nedanovska (231106)

---

## Overview

This project investigates the **sensitivity of Large Language Models (LLMs) to semantically equivalent instruction/prompt variations**. By systematically constructing paraphrased prompts for a style-controlled text generation task, the project measures output variation using semantic, lexical, and stylistic metrics.

A comparative analysis is conducted across models from different architectural families:

* **Decoder-only:** GPT2, Mistral-7B-Instruct
* **Encoder-decoder:** T5Gemma, FLAN-T5

---

## Repository Structure

```text
onpj-project/
│
├── gpt_model.ipynb                # GPT2 implementation and evaluation
├── mistral_model.ipynb            # Mistral-7B-Instruct implementation and evaluation
├── t5gemma_model.ipynb            # T5Gemma implementation and evaluation
├── flant5_model.ipynb             # FLAN-T5 implementation and evaluation
│
├── dataset/                       # Dataset: 1k_stories_100_genre.csv (~1000 short stories)
├── graphics/                      # Generated charts and result visualizations
├── generations_for_checkup/       # Generated texts for manual inspection
└── fixing_meta_widgets/           # Helper scripts for metadata fixes
```

---

## Models

| Model                    | Architecture    | Notebook              |
| ------------------------ | --------------- | --------------------- |
| GPT-Oss (GPT-2)          | Decoder-only    | `gpt_model.ipynb`     |
| Mistral-7B-Instruct-v0.2 | Decoder-only    | `mistral_model.ipynb` |
| T5Gemma (t5gemma-2b)     | Encoder-decoder | `t5gemma_model.ipynb` |
| FLAN-T5                  | Encoder-decoder | `flant5_model.ipynb`  |

---

## Evaluation Metrics

| Metric                     | Description                                 |
| -------------------------- | ------------------------------------------- |
| **Cosine Similarity**      | Semantic stability across generated texts   |
| **Sentiment Variation**    | Emotional consistency                       |
| **Perplexity Variation**   | Linguistic stability and naturalness        |
| **Style Consistency**      | Percentage of texts in the same style/genre |
| **Type-Token Ratio (TTR)** | Lexical variability                         |

---

## Key Results

| Model            | Cosine Similarity | Sentiment Variation | Perplexity Variation | Style Consistency |
| ---------------- | ----------------- | ------------------- | -------------------- | ----------------- |
| GPT2             | 0.2610            | 0.9354              | 6.7028               | 0.1920            |
| Mistral-Instruct | **0.6113**        | **0.4352**          | 16.2034              | **0.7653**        |
| T5Gemma          | 0.6112            | 0.8782              | 11.5722              | 0.6800            |
| FLAN-T5          | 0.6016            | 0.8956              | **3.5276**           | 0.1333            |

**Key findings:**

* **Mistral-Instruct** is the most balanced model in terms of cosine similarity, sentiment variation, and style consistency.
* **FLAN-T5** achieves the lowest perplexity variation, but has low style consistency.
* **GPT2** is the most sensitive to prompt changes.
* **T5Gemma** shows stable and balanced results.

---

## Dataset

The dataset **`1k_stories_100_genre.csv`** contains around 1000 short stories distributed across multiple genres. A random subset of **100 samples** is selected using `random_state=42` for reproducibility.

---

## Experimental Design

* 5 semantically equivalent prompt variations
* 5 independent generations per prompt
* Identical parameters: `max_new_tokens=120`, `temperature=0.7`
* 25 generated texts per model
* 100 generated texts in total

---

## Installation & Usage

```bash
pip install transformers torch sentence-transformers scikit-learn pandas numpy
```

Hugging Face authentication is required:

```python
from huggingface_hub import login
login(token="YOUR_HF_TOKEN")
```

```bash
git clone https://github.com/tamara-00/onpj-project.git
cd onpj-project
```

---

## References

* Pecher et al. (2025). *Revisiting prompt sensitivity in large language models.*
* Liu et al. (2021). *Pre-train, Prompt, and Predict.*
* Reif et al. (2022). *A recipe for arbitrary text style transfer with LLMs.*
* Jiang et al. (2023). *Mistral 7B.*
* Chung et al. (2022). *Scaling instruction-finetuned language models.*
