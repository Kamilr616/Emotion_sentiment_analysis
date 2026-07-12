# 😊 Analiza emocji i sentymentu tekstu

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Bi--LSTM-FF6F00?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![NLP](https://img.shields.io/badge/NLP-klasyfikacja%20tekstu-green)]()
[![Licencja: MIT](https://img.shields.io/badge/Licencja-MIT-yellow.svg)](LICENSE)

> 🇬🇧 [English version](README.md)

> 🗓️ **Okres realizacji:** 2024

Projekt **klasyfikacji emocji na podstawie tekstu** zrealizowany jako notatnik Jupyter. Trenuje **rekurencyjną sieć neuronową (dwukierunkowy LSTM)** w **TensorFlow/Keras**, aby rozpoznać emocję wyrażoną w krótkim tekście (np. tweecie, wiadomości), na ~382 tys. próbek zagregowanych z kilku publicznych zbiorów Kaggle. Powstał na przedmiot **Big Data**.

## 📊 Zbiory danych

Projekt agreguje kilka zbiorów tekstów z etykietami emocji z Kaggle:

| Zbiór danych | Źródło (Kaggle) |
|--------------|-----------------|
| Emotion analysis based on text | `simaanjali/emotion-analysis-based-on-text` |
| Text emotion recognition | `shreejitcheela/text-emotion-recognition` |
| Emotion detection from text | `pashupatigupta/emotion-detection-from-text` |
| Emotions | `nelgiriyewithana/emotions` |
| Emotion dataset | `abdallahwagih/emotion-dataset` |

Lista plików używanych przez notatnik jest skonfigurowana w [`source/config/datasets.txt`](source/config/datasets.txt), a ich źródła w [`source/config/datasets_source.txt`](source/config/datasets_source.txt).

<p align="center">
  <img src="docs/emotion-distribution.png" alt="Rozkład klas emocji" width="640"/>
</p>

*Połączony zbiór — rozkład 14 klas emocji (silnie niezbalansowany w stronę `neutral`), kluczowy czynnik uwzględniony podczas treningu.*

## 🧠 Model i wyniki

Klasyfikator to **rekurencyjna sieć neuronowa (RNN)** z rdzeniem **dwukierunkowego LSTM**, zbudowana w **TensorFlow/Keras**. Łączy warstwę embeddingu, dwukierunkowy LSTM, dropout i normalizację wsadową oraz warstwy gęste, aby poprawić dokładność i ograniczyć przeuczenie.

- **Dane** — ~**382 000** próbek tekstu zagregowanych z powyższych zbiorów Kaggle, w **14 klasach emocji**, przepuszczonych przez pełny pipeline ETL (usuwanie wzmianek/URL/interpunkcji, rozwijanie skrótów czatowych, usuwanie stop-słów, tokenizacja, padding, kodowanie etykiet) i podzielonych **80/20** na trening/test.
- **Trening** — 10 epok; końcowa **dokładność walidacyjna 97,69%** (ogólna ≈ 98%).
- **Średnie** — ważona precyzja / czułość / F1 = **0,98 / 0,98 / 0,98**; makro-średnia F1 = **0,89**.

<details>
<summary><b>📋 Raport klasyfikacji per klasa</b></summary>

| Emocja | Precyzja | Czułość | F1 |
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

Po wytrenowaniu model przewiduje emocję nowego zdania — np. radosna wiadomość → *joy*, pełna niepokoju → *fear*. Pełna metodyka znajduje się w [raporcie z przedmiotu Big Data](documents/).

## 📂 Struktura repozytorium

| Ścieżka | Opis |
|---------|------|
| `source/Emotion_Sentiment_Analysis_tool.ipynb` | Główny notatnik — wczytywanie danych, preprocessing, trening i ewaluacja |
| `source/config/` | Pliki konfiguracyjne zbiorów danych |
| `documents/` | Dokumentacja projektu (raport z przedmiotu Big Data) |

## 🚀 Szybki start

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/Kamilr616/Emotion_sentiment_analysis.git
   cd Emotion_sentiment_analysis
   ```
2. Pobierz z Kaggle zbiory danych wymienione w `source/config/datasets_source.txt` i umieść pliki CSV obok notatnika (lub zaktualizuj ścieżki w `datasets.txt`).
3. Uruchom notatnik:
   ```bash
   jupyter notebook source/Emotion_Sentiment_Analysis_tool.ipynb
   ```
4. Wykonuj komórki od góry do dołu — notatnik prowadzi przez przygotowanie danych, trening modelu i ewaluację.

## 🧰 Stos technologiczny

Python · TensorFlow / Keras · pandas · NumPy · NLTK · Jupyter Notebook · Kaggle API

## 📄 Licencja

Projekt udostępniony na licencji [MIT](LICENSE).

## 👤 Autor

**Kamil Rataj** — [GitHub](https://github.com/Kamilr616) · [LinkedIn](https://www.linkedin.com/in/kamil-r-153ab7121/)
