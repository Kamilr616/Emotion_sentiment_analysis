# 😊 Analiza emocji i sentymentu tekstu

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Bi--LSTM-FF6F00?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
![NLP](https://img.shields.io/badge/NLP-klasyfikacja%20tekstu-green)
[![Licencja: MIT](https://img.shields.io/badge/Licencja-MIT-yellow.svg)](LICENSE)

> 🇬🇧 [English version](README.md)

> 🗓️ **Okres realizacji:** 2024 · utrzymanie wersji publikacyjnej: 2026

> 📘 [Dokumentacja techniczna](docs/TECHNICAL_DOCUMENTATION.pl.md)

> 📄 [Sprawozdanie z projektu Big Data](<docs/Projekt - BigData.pdf>)

Projekt klasyfikacji emocji tekstu zaimplementowany jako notatnik Google
Colab/Jupyter. Trenuje dwukierunkowy LSTM w TensorFlow/Keras na około 382 000
próbek zagregowanych z publicznych zbiorów Kaggle i przewiduje jedną z 14 klas
emocji. Projekt powstał na przedmiot Big Data i jest publikowany jako projekt
edukacyjny/portfolio, a nie usługa produkcyjna.

## 📊 Zbiory danych

| Zbiór danych | Źródło Kaggle |
|---|---|
| Emotion analysis based on text | [simaanjali/emotion-analysis-based-on-text](https://www.kaggle.com/datasets/simaanjali/emotion-analysis-based-on-text) |
| Text emotion recognition | [shreejitcheela/text-emotion-recognition](https://www.kaggle.com/datasets/shreejitcheela/text-emotion-recognition) |
| Emotion detection from text | [pashupatigupta/emotion-detection-from-text](https://www.kaggle.com/datasets/pashupatigupta/emotion-detection-from-text) |
| Emotions | [nelgiriyewithana/emotions](https://www.kaggle.com/datasets/nelgiriyewithana/emotions) |
| Emotion dataset | [abdallahwagih/emotion-dataset](https://www.kaggle.com/datasets/abdallahwagih/emotion-dataset) |

Nazwy plików są skonfigurowane w
[source/config/datasets.txt](source/config/datasets.txt), a identyfikatory Kaggle
w [source/config/datasets_source.txt](source/config/datasets_source.txt). Zbiory
są pobierane podczas uruchomienia i nie są rozpowszechniane w repozytorium.
Licencje oraz zastrzeżenia opisuje
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

<p align="center">
  <img src="docs/emotion-distribution.png" alt="Rozkład klas emocji" width="640"/>
</p>

*Archiwalny rozkład połączonych danych w 14 klasach. Utrzymywany pipeline używa
zbalansowanych wag klas oraz raportuje metryki per klasa i makro-średnie.*

## 🧠 Utrzymywany pipeline

Notatnik korzysta teraz z jednego spójnego przebiegu przetwarzania i ewaluacji:

- sprawdza wymagane kolumny tekstu i emocji oraz przerywa pracę dla nieznanych
  etykiet;
- usuwa rekordy puste, niepełne i zduplikowane, a następnie wykonuje czyszczenie
  regex, rozwijanie skrótów czatowych, usuwanie stop-słów bez rozróżniania
  wielkości liter i normalizację odstępów;
- używa ziarna 42 oraz stratyfikowanego podziału 80/10/10 na trening, walidację i
  test;
- dopasowuje tokenizer wyłącznie do tekstów treningowych, a nieznane słowa mapuje
  na token OOV;
- trenuje embedding + dwukierunkowy LSTM ze zbalansowanymi wagami klas i early
  stoppingiem opartym na walidacji;
- wykonuje końcową ewaluację jeden raz na niezależnym zbiorze testowym;
- eksportuje model Keras, tokenizer, kolejność etykiet i ustawienia preprocessingu
  potrzebne do samodzielnej inferencji.

W tej aktualizacji utrzymaniowej nie zapisano nowego pełnego treningu. Ponowne
uruchomienie da metryki, których nie należy bezpośrednio porównywać z archiwalnym
eksperymentem, ponieważ poprawiono przepływ danych i protokół ewaluacji.

## 📋 Archiwalne wyniki z 2024 roku

Dołączone [sprawozdanie z projektu Big Data](<docs/Projekt - BigData.pdf>) zapisuje
wyniki pierwotnego przebiegu 80/20:

- accuracy: 97,69%;
- ważona precision / recall / F1: 0,98 / 0,98 / 0,98;
- makro precision / recall / F1: 0,91 / 0,88 / 0,89.

<details>
<summary><b>Raport per klasa przepisany ze sprawozdania</b></summary>

| Emocja | Precision | Recall | F1 |
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

Wiersz Boredom w raporcie jest wewnętrznie niespójny: precision 1,00 i recall
0,99 nie mogą dać F1 0,95. Wartość zachowano jako archiwalną wartość źródłową i
nie należy jej interpretować jako nowo zweryfikowanego wyniku.

## 📂 Struktura repozytorium

| Ścieżka | Opis |
|---|---|
| source/Emotion_Sentiment_Analysis_tool.ipynb | Wczytywanie, ETL, trening, ewaluacja i eksport |
| source/config/ | Konfiguracja nazw plików i źródeł Kaggle |
| requirements.txt | Utrzymywane zgodne zakresy zależności |
| requirements-recorded.txt | Bezpośrednie wersje zapisane w środowisku Colab 2024 |
| scripts/validate_notebook.py | Statyczna kontrola składni, outputów i sekretów |
| docs/ | Dokumentacja techniczna, oryginalne sprawozdanie Big Data i wykres rozkładu klas |
| THIRD_PARTY_NOTICES.md | Informacje o zewnętrznych zależnościach i danych |

## 🚀 Szybki start

1. Sklonuj repozytorium.

~~~bash
git clone https://github.com/Kamilr616/Emotion_sentiment_analysis.git
cd Emotion_sentiment_analysis
~~~

2. Otwórz source/Emotion_Sentiment_Analysis_tool.ipynb w Google Colab.
3. Po wyświetleniu formularza wgraj własny kaggle.json oraz oba pliki z
   source/config/.
4. Wykonaj komórki od góry do dołu.

Wynik uploadu jest przypisywany do zmiennej, więc bajty credentiala nie są
renderowane. Notatnik kopiuje credential do katalogu konfiguracji Kaggle z
prawami 0600 i usuwa przesłaną kopię roboczą. Nigdy nie commituj credentials,
pobranych danych, outputów notatnika ani wygenerowanych artefaktów modelu.

Przy uruchomieniu lokalnym zainstaluj requirements.txt. Aby odtworzyć środowisko
zbliżone do pierwotnego Colab z 2024 roku, użyj Pythona 3.10 i
requirements-recorded.txt.

## 🔒 Walidacja i bezpieczeństwo

Workflow GitHub Actions Notebook quality uruchamia
scripts/validate_notebook.py dla main, develop i pull requestów. Odrzuca zapisane
outputy, niezerowe liczniki wykonania, błędną składnię Python i wzorce sekretów o
wysokiej pewności. Zasady zgłaszania opisuje [SECURITY.md](SECURITY.md).

## 📄 Licencja

Oryginalny kod i dokumentacja repozytorium są udostępnione na
[licencji MIT](LICENSE). Zewnętrzne zbiory danych i zależności uruchomieniowe nie
są relicencjonowane przez MIT; zobacz
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## 👤 Autor

**Kamil Rataj** — [GitHub](https://github.com/Kamilr616) ·
[LinkedIn](https://www.linkedin.com/in/kamil-r-153ab7121/)
