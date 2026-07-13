# 😊 Emotion & Sentiment Analysis

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Bi--LSTM-FF6F00?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
![NLP](https://img.shields.io/badge/NLP-text%20classification-green)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> 🇵🇱 [Polish version](README.pl.md)

> 🗓️ **Project period:** 2024

> 📘 [Technical documentation](docs/TECHNICAL_DOCUMENTATION.md)

A **text-based emotion classification** project built as a Jupyter Notebook. It trains a **recurrent neural network (bidirectional LSTM)** in **TensorFlow/Keras** to recognize the emotion expressed in a short text (e.g. tweets and messages), using ~382k samples aggregated from several public Kaggle datasets. Built for a **Big Data** course.

## 📊 Datasets

The project aggregates multiple emotion-labelled text datasets from Kaggle:

| Dataset | Source (Kaggle) |
|---------|-----------------|
| Emotion analysis based on text | `simaanjali/emotion-analysis-based-on-text` |
| Text emotion recognition | `shreejitcheela/text-emotion-recognition` |
| Emotion detection from text | `pashupatigupta/emotion-detection-from-text` |
| Emotions | `nelgiriyewithana/emotions` |
| Emotion dataset | `abdallahwagih/emotion-dataset` |

The list of dataset files used by the notebook is configured in [`source/config/datasets.txt`](source/config/datasets.txt), and their sources in [`source/config/datasets_source.txt`](source/config/datasets_source.txt).

<p align="center">
  <img src="docs/emotion-distribution.png" alt="Emotion class distribution" width="640"/>
</p>

*Combined dataset — distribution across the 14 emotion classes (heavily imbalanced toward `neutral`), a key factor handled during training.*

## 🧠 Model & results

The classifier is a **recurrent neural network (RNN)** with a **bidirectional LSTM** core, built in **TensorFlow/Keras**. It stacks an embedding layer, bidirectional LSTM, dropout and batch-normalisation, and a dense output layer to improve accuracy and curb overfitting.

- **Data** — ~**382,000** text samples aggregated from the Kaggle datasets above, across **14 emotion classes**, cleaned of mentions/URLs/non-alphanumeric characters, normalised, tokenised, padded and label-encoded before an **80/20** split. The notebook defines chat-word expansion and stop-word removal, but its recorded data-flow branch does not feed those intermediate results into training; see the technical documentation.
- **Training** — 10 epochs; the project report records a final **accuracy of 97.69% on the 20% evaluation split** (overall ≈ 98%).
- **Averages** — weighted precision / recall / F1 = **0.98 / 0.98 / 0.98**; macro-average precision / recall / F1 = **0.91 / 0.88 / 0.89**.

<details>
<summary><b>📋 Per-class classification report</b></summary>

| Emotion | Precision | Recall | F1-score |
|---|---|---|---|
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

These are the results recorded in the included Big Data course report. Because the dataset is strongly imbalanced toward `neutral`, the per-class and macro-average scores are more informative than overall accuracy alone; retraining may produce slightly different values.

> **Source note:** the report lists `Boredom` as precision 1.00, recall 0.99 and F1 0.95. The F1 value is not mathematically consistent with the reported precision and recall; it is retained here unchanged because the notebook output needed to recalculate it is not included.

Once trained, the model predicts the emotion of a new sentence — e.g. a cheerful message → *happiness*, an anxious one → *fear*. Full methodology is in the [Big Data course report](documents/).

## 📂 Repository structure

| Path | Description |
|------|-------------|
| `source/Emotion_Sentiment_Analysis_tool.ipynb` | Main notebook — data loading, preprocessing, training, and evaluation |
| `source/config/` | Dataset configuration files |
| `documents/` | Project documentation (Big Data course report) |

## 🚀 Getting started

1. Clone the repository:
   ```bash
   git clone https://github.com/Kamilr616/Emotion_sentiment_analysis.git
   cd Emotion_sentiment_analysis
   ```
2. Open `source/Emotion_Sentiment_Analysis_tool.ipynb` in **Google Colab**.
3. Use the upload cell to provide your own `kaggle.json` plus the two files from `source/config/`.
4. Run the cells top-to-bottom. Never save or commit the output of the credentials-upload cell.

## 🧰 Tech stack

Python · TensorFlow / Keras · pandas · NumPy · NLTK · Jupyter Notebook · Kaggle API

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 👤 Author

**Kamil Rataj** — [GitHub](https://github.com/Kamilr616) · [LinkedIn](https://www.linkedin.com/in/kamil-r-153ab7121/)
