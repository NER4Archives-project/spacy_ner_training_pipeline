<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: NER4Archives - *named entity recognition for archives* - INRIA/Archives nationales

 This spaCy project downloading and converting source data and training a named entity recognition model. The project uses the NER4Archives (N4A) corpus, which was constructed semi-automatically. The main advantage of this corpus is that it's freely available, so the data can be downloaded as a project asset.
## The NER4Archives corpus
The N4A corpus is distributed in CONLL format with IOB schema, a fairly common text encoding for sequence data. The `corpus` in assets/ is splitting into training, development and testing; then uses `spacy convert` to convert them into spaCy's binary format. You can then create/edit the config to try out different settings, and trigger training with the `train` subcommand. The project contains the last training model and use the last version of corpus. Models are available with meta on Hugging Face organisation (Free model hosting).

## ⚠️ Please read the steps carefully before using and launching this spaCy project ⚠️
Go to [INFO.md](./INFO.md)
## Important ressources
- :octocat: [Ner4archives corpus](https://github.com/NER4Archives-project/Corpus_TrainingData) - N4A Corpus version
- 🤗 [Ner4archives Hugging Face Hub organisation](https://huggingface.co/ner4archives) - N4A NER pipeline models


## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `install` | Install dependencies, log in to Hugging Face (use the first time you init the project), initialize git lfs, download vectors model (run first time) |
| `corpus` | Extract, partition (train, dev & test - Default: 0.6, 0.2, 0.2) and convert the data from zip to spaCy's format |
| `train` | Train default NER pipeline (efficiency) - optimized for CPU |
| `train-with-vectors` | Train default NER pipeline (accuracy) with fr_core_news_lg vectors - optimized for CPU |
| `train-with-camembert-base-fr` | Train transformer (camembert-base) NER pipeline - optimized for GPU |
| `evaluate` | Evaluate on the test data and save the metrics |
| `package` | Package the trained model so it can be installed |
| `push_to_hub` | Push the model to the Hub |
| `generate-documentation` | (Re-)generate project documentation. |
| `clean` | Remove intermediate files |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `cpu_train_default` | `corpus` &rarr; `train` &rarr; `evaluate` |
| `cpu_train_vectors` | `corpus` &rarr; `train-with-vectors` &rarr; `evaluate` |
| `gpu_train_trf_camembert-base` | `corpus` &rarr; `train-with-camembert-base-fr` &rarr; `evaluate` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| `assets/` | Git | Fetch corpus from GitHub repo NER4Archives-project/Corpus_TrainingData/ project using SSH auth. |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->
