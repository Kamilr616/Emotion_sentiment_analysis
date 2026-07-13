# 😊 Analiza emocji i sentymentu tekstu

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Bi--LSTM-FF6F00?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
![NLP](https://img.shields.io/badge/NLP-klasyfikacja%20tekstu-green)
[![Licencja: MIT](https://img.shields.io/badge/Licencja-MIT-yellow.svg)](LICENSE)

> 🇬🇧 [English version](README.md)

> 🗓️ **Okres realizacji:** 2024

> 📘 [Dokumentacja techniczna](docs/TECHNICAL_DOCUMENTATION.pl.md)

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

Klasyfikator to **rekurencyjna sieć neuronowa (RNN)** z rdzeniem **dwukierunkowego LSTM**, zbudowana w **TensorFlow/Keras**. Łączy warstwę embeddingu, dwukierunkowy LSTM, dropout i normalizację wsadową oraz gęstą warstwę wyjściową, aby poprawić dokładność i ograniczyć przeuczenie.

- **Dane** — ~**382 000** próbek tekstu zagregowanych z powyższych zbiorów Kaggle, w **14 klasach emocji**, oczyszczonych ze wzmianek/URL/znaków niealfanumerycznych, znormalizowanych, stokenizowanych, dopełnionych i zakodowanych przed podziałem **80/20**. Notatnik definiuje rozwijanie skrótów czatowych i usuwanie stop-słów, ale zapisana gałąź przepływu nie przekazuje tych wyników pośrednich do treningu; szczegóły opisuje dokumentacja techniczna.
- **Trening** — 10 epok; raport projektowy podaje końcową **dokładność 97,69% na 20-procentowym zbiorze ewaluacyjnym** (ogólna ≈ 98%).
- **Średnie** — ważona precyzja / czułość / F1 = **0,98 / 0,98 / 0,98**; makro-średnia precyzja / czułość / F1 = **0,91 / 0,88 / 0,89**.

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

Są to wyniki zapisane w dołączonym sprawozdaniu z przedmiotu Big Data. Zbiór jest silnie niezbalansowany na korzyść klasy `neutral`, dlatego wyniki per klasa i makro-średnie są bardziej miarodajne niż sama accuracy; ponowny trening może dać nieznacznie inne wartości.

> **Uwaga o źródle:** sprawozdanie podaje dla klasy `Boredom` precyzję 1,00, czułość 0,99 i F1 0,95. Wartość F1 nie jest matematycznie spójna z podaną precyzją i czułością; pozostawiono ją bez zmian, ponieważ w repozytorium nie ma wyniku notatnika pozwalającego ją ponownie obliczyć.

Po wytrenowaniu model przewiduje emocję nowego zdania — np. radosna wiadomość → *happiness*, pełna niepokoju → *fear*. Pełna metodyka znajduje się w [raporcie z przedmiotu Big Data](documents/).

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
2. Otwórz `source/Emotion_Sentiment_Analysis_tool.ipynb` w **Google Colab**.
3. W komórce uploadu przekaż własny `kaggle.json` oraz dwa pliki z `source/config/`.
4. Wykonaj komórki od góry do dołu. Nie zapisuj ani nie commituj outputu komórki wgrywającej dane dostępowe.

## 🧰 Stos technologiczny

Python · TensorFlow / Keras · pandas · NumPy · NLTK · Jupyter Notebook · Kaggle API

## 📄 Licencja

Projekt udostępniony na licencji [MIT](LICENSE).

## 👤 Autor

**Kamil Rataj** — [GitHub](https://github.com/Kamilr616) · [LinkedIn](https://www.linkedin.com/in/kamil-r-153ab7121/)
