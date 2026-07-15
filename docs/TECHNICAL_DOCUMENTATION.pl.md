# Dokumentacja techniczna

## Zakres

Repozytorium zawiera proces treningowy Google Colab/Jupyter, który przypisuje
krótkiemu angielskiemu tekstowi jedną z 14 etykiet emocji. Cały eksperyment
znajduje się w source/Emotion_Sentiment_Analysis_tool.ipynb. Nie jest to wdrożona
usługa inferencyjna, a repozytorium nie rozpowszechnia wytrenowanego modelu ani
zbiorów danych.

## Przepływ danych

~~~mermaid
flowchart LR
    CFG["Konfiguracja zbiorów"] --> KG["Pobranie z Kaggle"]
    KG --> MAP["Walidacja kolumn i etykiet"]
    MAP --> CLEAN["Regex + skróty + stop-słowa"]
    CLEAN --> MERGE["Normalizacja + scalenie + deduplikacja"]
    MERGE --> SPLIT["Stratyfikowany podział 80/10/10"]
    SPLIT --> TOK["Tokenizer dopasowany tylko do treningu"]
    TOK --> MODEL["Embedding + BiLSTM"]
    MODEL --> EVAL["Walidacja + niezależny test"]
    EVAL --> ART["Model + metadane inferencji"]
~~~

Identyfikatory Kaggle pochodzą z source/config/datasets_source.txt, a oczekiwane
nazwy CSV z source/config/datasets.txt. Błąd pobierania lub odczytu przerywa
wykonanie; pipeline nie kontynuuje już pracy z niepełnym zbiorem.

Każda ramka jest kopiowana przed modyfikacją. Nazwy kolumn i etykiety emocji są
normalizowane, wymagane kolumny walidowane, a nieznane klasy przerywają pracę.
Usuwane są braki, puste teksty i duplikaty. Aktywna gałąź wykonuje następnie
czyszczenie wzmianek/URL/symboli, rozwijanie skrótów czatowych, usuwanie
angielskich stop-słów bez rozróżniania wielkości liter oraz normalizację odstępów.

## Etykiety i reprezentacja

Oczekiwane klasy to sadness, happiness, neutral, worry, surprise, love, anger,
relief, fear, empty, fun, hate, enthusiasm i boredom.

LabelEncoder ustala deterministyczną kolejność klas. Dane są dzielone z ziarnem
42 i stratyfikacją na 80% treningu, 10% walidacji i 10% testu. Tokenizer Keras ma
limit 60 000 tokenów, token OOV i długość sekwencji 100. Jest dopasowywany
wyłącznie do treningu, więc słownictwo walidacji i testu nie może na niego
wpłynąć.

## Model i trening

Model zawiera:

1. embedding o wymiarze 100;
2. SpatialDropout1D ze współczynnikiem 0,2;
3. dwukierunkowy LSTM ze 128 jednostkami;
4. batch normalization i dropout 0,5;
5. wyjście softmax o rozmiarze wynikającym z encodera etykiet.

Trening używa Adama, kategorycznej entropii krzyżowej, batcha 64 i maksymalnie 10
epok. Zbalansowane wagi klas są obliczane wyłącznie z etykiet treningowych.
EarlyStopping obserwuje stratę walidacyjną z patience 2 i przywraca najlepsze
wagi. Końcowa accuracy oraz raport per klasa są liczone jeden raz na niezależnym
zbiorze testowym.

## Wyniki archiwalne i porównywalność

Raport z kursu zapisuje accuracy 97,69%, ważone precision/recall/F1
0,98/0,98/0,98 oraz makro precision/recall/F1 0,91/0,88/0,89. Wartości pochodzą
z pierwotnego przebiegu, który używał tej samej części 20% do walidacji i
ewaluacji, dopasowywał tokenizer przed podziałem i omijał dwa kroki
preprocessingu.

Utrzymywany pipeline naprawia te problemy, dlatego archiwalne liczby nie są
przedstawiane jako wyniki bieżącego kodu. Wiersz Boredom w raporcie źródłowym
(precision 1,00, recall 0,99, F1 0,95) jest również matematycznie niespójny i
pozostaje wyłącznie elementem historii źródłowej.

## Zależności

requirements.txt zawiera utrzymywane zgodne zakresy. Bezpośrednie wersje pakietów
wydrukowane w pierwotnym środowisku Colab z Pythonem 3.10 zachowano w
requirements-recorded.txt. Zewnętrzne wersje zbiorów Kaggle mogą się zmieniać,
więc odtwarzalność przyszłych uruchomień nadal ma ograniczenia.

## Uruchamianie notatnika

1. Otwórz source/Emotion_Sentiment_Analysis_tool.ipynb w Google Colab.
2. Wgraj kaggle.json, datasets.txt i datasets_source.txt.
3. Wykonaj komórki po kolei w środowisku z siecią, miejscem na dysku i
   obsługą TensorFlow.

Wynik uploadu jest przypisywany zamiast wyświetlany. Credential jest kopiowany do
katalogu konfiguracji Kaggle z prawami 0600, używany do uwierzytelnienia i
usuwany z katalogu roboczego. Dane oraz artefakty modelu są ignorowane przez Git.

## Artefakty inferencji

Po treningu katalog artifacts zawiera:

- emotion_classification_model.keras;
- tokenizer.json;
- labels.json;
- preprocessing_config.json.

Tokenizer, uporządkowana lista klas, limit słownika i długość sekwencji są więc
dostępne razem z modelem. Wygenerowane artefakty celowo nie są commitowane.

## Walidacja i bezpieczeństwo

scripts/validate_notebook.py sprawdza możliwość odczytu JSON, składnię Python po
pominięciu magii notebooka, wyczyszczone outputy i liczniki wykonania oraz wzorce
sekretów o wysokiej pewności. Workflow GitHub Actions Notebook quality uruchamia
go dla main, develop i pull requestów.

Outputy muszą pozostać wyczyszczone, mimo że komórka uploadu nie renderuje już
bajtów credentiala. Każdy credential, który kiedykolwiek trafił do commita,
trzeba unieważnić; usunięcie go w późniejszym commicie nie wystarcza. Zgłaszanie
problemów opisuje SECURITY.md.

## Licencje i przetwarzanie danych

Licencja MIT obejmuje wyłącznie oryginalny kod i dokumentację repozytorium.
THIRD_PARTY_NOTICES.md zapisuje licencje zależności i metadane zbiorów Kaggle.
Zbiory nie są redystrybuowane. Jedno źródło deklaruje obecnie jedynie niejasną
licencję Other, dlatego przed redystrybucją trzeba wyjaśnić warunki u wydawcy.

Korpusy wejściowe zawierają teksty z mediów społecznościowych. Użytkownik
odpowiada za warunki zbiorów, wymagania prywatności i właściwe zastosowanie.
