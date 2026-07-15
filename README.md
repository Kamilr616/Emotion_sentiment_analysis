# 😊 Emotion & Sentiment Analysis

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Bi--LSTM-FF6F00?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
![NLP](https://img.shields.io/badge/NLP-text%20classification-green)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> 🇵🇱 [Polish version](README.pl.md)

> 🗓️ **Project period:** 2024 · maintained publication workflow: 2026

> 📘 [Technical documentation](docs/TECHNICAL_DOCUMENTATION.md)

> 📄 [Big Data course report](<docs/Projekt - BigData.pdf>) (in Polish)

A text emotion-classification project implemented as a Google Colab/Jupyter
Notebook. It trains a bidirectional LSTM in TensorFlow/Keras over approximately
382,000 samples aggregated from public Kaggle datasets and predicts one of
14 emotion classes. The project was created for a Big Data course and is
published as an educational portfolio project, not a production service.

## 📊 Datasets

| Dataset | Kaggle source |
|---|---|
| Emotion analysis based on text | [simaanjali/emotion-analysis-based-on-text](https://www.kaggle.com/datasets/simaanjali/emotion-analysis-based-on-text) |
| Text emotion recognition | [shreejitcheela/text-emotion-recognition](https://www.kaggle.com/datasets/shreejitcheela/text-emotion-recognition) |
| Emotion detection from text | [pashupatigupta/emotion-detection-from-text](https://www.kaggle.com/datasets/pashupatigupta/emotion-detection-from-text) |
| Emotions | [nelgiriyewithana/emotions](https://www.kaggle.com/datasets/nelgiriyewithana/emotions) |
| Emotion dataset | [abdallahwagih/emotion-dataset](https://www.kaggle.com/datasets/abdallahwagih/emotion-dataset) |

Dataset filenames are configured in
[source/config/datasets.txt](source/config/datasets.txt), and Kaggle references
in [source/config/datasets_source.txt](source/config/datasets_source.txt).
Dataset files are downloaded at runtime and are not distributed in this
repository. Licence details and cautions are recorded in
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

<p align="center">
  <img src="docs/emotion-distribution.png" alt="Emotion class distribution" width="640"/>
</p>

*Archived combined-data distribution across 14 classes. The maintained workflow
uses balanced class weights and reports per-class and macro-average metrics.*

## 🧠 Maintained workflow

The notebook now applies one consistent preprocessing and evaluation path:

- validates the required text and emotion columns and fails on unknown labels;
- removes missing, empty and duplicate texts, then applies regex cleaning,
  chat-abbreviation expansion, case-insensitive stop-word removal and whitespace
  normalization;
- uses seed 42 and a stratified 80/10/10 train/validation/test split;
- fits the tokenizer only on training text and maps unseen words to an OOV token;
- trains the embedding + bidirectional LSTM with balanced class weights and early
  stopping on the validation split;
- evaluates the model once on the independent test split;
- exports the Keras model, tokenizer, label order and preprocessing settings
  needed for standalone inference.

No new full training run is committed with this maintenance update. A rerun will
produce metrics that are not directly comparable with the archived experiment,
because the data path and evaluation protocol were corrected.

## 📋 Archived 2024 results

The included [Big Data course report](<docs/Projekt - BigData.pdf>) (in Polish)
records results from the original 80/20 workflow:

- accuracy: 97.69%;
- weighted precision / recall / F1: 0.98 / 0.98 / 0.98;
- macro precision / recall / F1: 0.91 / 0.88 / 0.89.

<details>
<summary><b>Per-class report reproduced from the course report</b></summary>

| Emotion | Precision | Recall | F1-score |
|---|---:|---:|---:|
| Anger | 0.85 | 0.75 | 0.79 |
| Boredom | 1.00 | 0.99 | 0.95 |
| Empty | 0.99 | 0.99 | 0.99 |
| Enthusiasm | 0.98 | 0.99 | 0.98 |
| Fear | 0.98 | 0.92 | 0.95 |
| Fun | 0.98 | 0.98 | 0.98 |
| Happiness | 0.99 | 0.99 | 0.99 |
| Hate | 0.98 | 0.98 | 0.98 |
| Love | 0.98 | 0.99 | 0.98 |
| Neutral | 0.98 | 0.99 | 0.99 |
| Relief | 0.98 | 0.98 | 0.98 |
| Sadness | 0.99 | 0.99 | 0.99 |
| Surprise | 1.00 | 1.00 | 1.00 |
| Worry | 0.99 | 0.95 | 0.97 |

</details>

The report's Boredom row is internally inconsistent: precision 1.00 and recall
0.99 cannot yield F1 0.95. The value is retained as an archived source value and
must not be interpreted as a newly verified result.

## 📂 Repository structure

| Path | Description |
|---|---|
| source/Emotion_Sentiment_Analysis_tool.ipynb | Complete loading, ETL, training, evaluation and export workflow |
| source/config/ | Dataset filename and Kaggle-source configuration |
| requirements.txt | Maintained compatible dependency ranges |
| requirements-recorded.txt | Direct versions observed in the archived 2024 Colab run |
| scripts/validate_notebook.py | Static notebook syntax, output and secret check |
| docs/ | Technical documentation, original Big Data course report and class-distribution chart |
| THIRD_PARTY_NOTICES.md | External dependency and dataset notices |

## 🚀 Getting started

1. Clone the repository.

~~~bash
git clone https://github.com/Kamilr616/Emotion_sentiment_analysis.git
cd Emotion_sentiment_analysis
~~~

2. Open source/Emotion_Sentiment_Analysis_tool.ipynb in Google Colab.
3. Upload your own kaggle.json and both files from source/config/ when prompted.
4. Run cells from top to bottom.

The upload result is assigned to a variable so credential bytes are not rendered.
The notebook copies the credential to the Kaggle configuration directory with
0600 permissions and removes the uploaded working copy. Never commit credentials,
downloaded datasets, notebook outputs or generated model artifacts.

For local execution, install requirements.txt. To approximate the original 2024
environment, use Python 3.10 and requirements-recorded.txt.

## 🔒 Validation and security

The Notebook quality GitHub Actions workflow runs
scripts/validate_notebook.py on main, develop and pull requests. It rejects
committed outputs, non-null execution counters, invalid Python syntax and
high-confidence secret patterns. See [SECURITY.md](SECURITY.md) for reporting.

## 📄 Licence

Original repository code and documentation are licensed under the
[MIT License](LICENSE). External datasets and runtime dependencies are not
relicensed by MIT; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## 👤 Author

**Kamil Rataj** — [GitHub](https://github.com/Kamilr616) ·
[LinkedIn](https://www.linkedin.com/in/kamil-r-153ab7121/)
