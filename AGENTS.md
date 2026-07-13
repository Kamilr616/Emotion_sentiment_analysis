# AGENTS.md

Guidance for AI coding agents working in this repository.

## Project
**Text emotion classification** built as a Jupyter Notebook. Trains a **bidirectional
LSTM (RNN)** in **TensorFlow/Keras** over ~382k samples aggregated from several public
Kaggle datasets, across **14 emotion classes**. Built for a *Big Data* course.

## Layout
- `source/Emotion_Sentiment_Analysis_tool.ipynb` — the whole pipeline (load → ETL →
  train → evaluate).
- `source/config/datasets.txt`, `datasets_source.txt` — dataset configuration.
- `docs/emotion-distribution.png` — class-distribution chart.
- `documents/` — the Big Data course report (methodology + recorded metrics).

## Build / run / test
- Open the notebook in **Google Colab**; upload your own `kaggle.json` plus the two
  `source/config/` files, then run cells top-to-bottom.

## Conventions & good practices
- **Never commit credentials.** Do not save or commit the output of the
  `files.upload()` / `kaggle.json` cell — clear all cell outputs before committing.
- The dataset is heavily imbalanced toward `neutral`; judge results by **per-class and
  macro-average** scores, not overall accuracy.
- Recorded metrics live in the course report; treat notebook re-runs as reproducible-ish
  (values may shift slightly).
- Update **both** `README.md` and `README.pl.md` together.

## Documentation
- [README.md](README.md) · [README.pl.md](README.pl.md)
- [Technical documentation](docs/TECHNICAL_DOCUMENTATION.md) · [Polski](docs/TECHNICAL_DOCUMENTATION.pl.md)
- Course report: [`documents/`](documents/)
- License: **MIT** — see [LICENSE](LICENSE).

_Educational / portfolio project._
