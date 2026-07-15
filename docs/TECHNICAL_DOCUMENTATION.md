# Technical documentation

## Scope

The repository contains a Google Colab/Jupyter training workflow that assigns one
of 14 emotion labels to short English text. The complete experiment lives in
source/Emotion_Sentiment_Analysis_tool.ipynb. It is not a deployed inference
service, and no trained model or dataset is distributed in the repository.

## Data flow

~~~mermaid
flowchart LR
    CFG["Dataset configuration"] --> KG["Kaggle download"]
    KG --> MAP["Column and label validation"]
    MAP --> CLEAN["Regex + chat words + stop words"]
    CLEAN --> MERGE["Normalize + merge + deduplicate"]
    MERGE --> SPLIT["Stratified 80/10/10 split"]
    SPLIT --> TOK["Fit tokenizer on train only"]
    TOK --> MODEL["Embedding + BiLSTM"]
    MODEL --> EVAL["Validation + independent test"]
    EVAL --> ART["Model + inference metadata"]
~~~

Kaggle references come from source/config/datasets_source.txt and expected CSV
names from source/config/datasets.txt. Download or load failures stop execution;
the workflow no longer continues with a silently incomplete dataset.

Each frame is copied before mutation. Column names and emotion labels are
normalized, required columns are validated, and unexpected output labels stop
the run. Missing values, empty texts and duplicate texts are removed. The active
branch then applies mention/URL/symbol cleaning, chat-abbreviation expansion,
case-insensitive English stop-word removal and whitespace normalization.

## Labels and representation

The expected classes are sadness, happiness, neutral, worry, surprise, love,
anger, relief, fear, empty, fun, hate, enthusiasm and boredom.

LabelEncoder establishes a deterministic class order. The data is split with
seed 42 and class stratification into 80% training, 10% validation and 10% test.
The Keras Tokenizer has a 60,000-token limit, an OOV token and a sequence length
of 100. It is fitted only on training text; validation and test vocabulary cannot
influence it.

## Model and training

The model contains:

1. a 100-dimensional embedding;
2. SpatialDropout1D with rate 0.2;
3. a bidirectional LSTM with 128 units;
4. batch normalization and dropout with rate 0.5;
5. a softmax output sized from the fitted label encoder.

Training uses Adam, categorical cross-entropy, batch size 64 and at most 10
epochs. Balanced class weights are computed from training labels only.
EarlyStopping monitors validation loss with patience 2 and restores the best
weights. Final accuracy and the per-class classification report are computed
once on the independent test split.

## Archived results and comparability

The course report records 97.69% accuracy, weighted precision/recall/F1 of
0.98/0.98/0.98 and macro precision/recall/F1 of 0.91/0.88/0.89. Those values came
from the original workflow, which used one 20% partition for validation and
evaluation, fitted the tokenizer before splitting and bypassed two preprocessing
steps.

The maintained pipeline fixes those issues, so the archived numbers are not
claimed as results of the current code. The source report's Boredom row
(precision 1.00, recall 0.99, F1 0.95) is also mathematically inconsistent and is
retained only as source history.

## Dependencies

requirements.txt contains maintained compatible ranges. The direct package
versions printed by the original Python 3.10 Colab runtime are preserved in
requirements-recorded.txt. External Kaggle dataset versions can still change, so
future runs remain reproducible within limits.

## Running the notebook

1. Open source/Emotion_Sentiment_Analysis_tool.ipynb in Google Colab.
2. Upload kaggle.json, datasets.txt and datasets_source.txt when prompted.
3. Run cells in order with network, disk space and a TensorFlow-capable runtime.

The upload return value is assigned rather than displayed. The credential is
copied to the Kaggle configuration directory with mode 0600, authenticated and
removed from the working directory. Dataset and model outputs are ignored by
Git.

## Inference artifacts

After training, the artifacts directory contains:

- emotion_classification_model.keras;
- tokenizer.json;
- labels.json;
- preprocessing_config.json.

The tokenizer, ordered class list, vocabulary limit and sequence length are
therefore available with the model. Generated artifacts are intentionally not
committed.

## Validation and security

scripts/validate_notebook.py verifies JSON-loadable notebook content, Python
syntax after excluding notebook magics, cleared outputs and execution counters,
and high-confidence secret patterns. The Notebook quality GitHub Actions workflow
runs it on main, develop and pull requests.

Notebook outputs must remain cleared even though the upload cell no longer
renders credential bytes. Any credential ever committed must be revoked; deleting
it from a later commit is not sufficient. Security reporting is described in
SECURITY.md.

## Licensing and data handling

The MIT licence applies to original repository code and documentation only.
THIRD_PARTY_NOTICES.md records dependency licences and Kaggle dataset metadata.
The datasets are not redistributed. One source currently declares only an
unclear Other licence on Kaggle, so its publisher's terms must be clarified
before any redistribution.

The input corpora include social-media text. Users remain responsible for
applicable dataset terms, privacy requirements and appropriate use.
