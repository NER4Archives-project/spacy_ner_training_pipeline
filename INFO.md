# Steps to training a new NER pipeline 

## Prerequisite

To send the models to Hugging Face (`step 7`), you must have an [HF account](https://huggingface.co/), have an HF token with the `write` right (on the HF account, display the `settings` section), and be part of the HF `ner4archives` organization.

### 1. Installation (to be done once)

#### 1.1 clone the spacy project

```bash
git clone https://github.com/NER4Archives-project/spacy_ner_trainning_pipeline.git
```
then 

```bash
cd spacy_ner_trainning_pipeline/
```

#### 1.2 create and activate a new virtual environnement (Python 3.8)

```bash
virtualenv --python=/usr/bin/python3.8 venv
```

then 

```bash
source venv/bin/activate
```

#### 1.3 install spaCy

```bash
pip install spacy==3.4.1
```

### 2. install other packages (to be done once)

After `step 1.`, launch command:

```bash
spacy project run install
```

### 3. Download the corpus (to do once or to download a new version)

After `step 2.`, launch command:

```bash
spacy project assets
```

## Next steps

### 4. change vars in `project.yml`

After `step 3.` and before training a new model it is important to check the variables to name the model for example:

In `project.yml` go to `vars` section and change `name` var with correct model name.

model naming conventions (all in lowercase !):

`ner4archives_(corpus version)_(pipeline type)`

- `corpus version`: version of corpus downloaded in `assets/`
- `pipeline type`: can be (except if you create a [new pipeline](#how-to-create-a-new-pipeline-for-the-project?)):
   - `default` if cpu_train_default; 
   - `with_vectors` if cpu_train_vectors; 
   - `trf_camembert_base` if gpu_train_trf_camembert-base

### 5. Train a new pipeline(s) 

After `step 4.`, on your local computer (except if you GPU), use CPU pipelines:

- cpu_train_default
- cpu_train_vectors

For GPU pipelines use cloud computing solution like Google colab notebook and use this file: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1nn9LxeYfpjd9GJjyTh1tiCLbiTqo2zO6?usp=sharing)

To start model training:

```bash
spacy project run [name of pipeline want to use eg. cpu_train_default]
```

### 6. Package the new model

After `step 5.`, when the training of the model is finished, it is necessary to package it, run the command:

```bash
spacy project run package
```

### 7. Push a new model & complete manually metadata in Hugging Face Hub

After `step 6.`, the newly created models are push on the hub of the Hugging Face organization, to psuh the new model, lunch:

```bash
spacy project run push_to_hub
```

Once the process is complete, go to [Hugging Face hub Ner4archives organisation](https://huggingface.co/ner4archives), click on new model and 
and complete the missing metadata:
click on `Edit model card` and edit this vars:

- `Sources`: French corpus for the NER task composed of finding aids in XML-EAD from the National Archives of France - [Check corpus version](https://github.com/NER4Archives-project/Corpus_TrainingData)
- `License`: CC-BY-4.0 license
- `Author`: Archives nationales / Inria-Almanach

### 8. clean your workspace

When the models are well versioned, you can clean up the working folders with:

```bash
spacy project run clean
```

# How to create a new pipeline for the project?

This section describes how to add a new model architecture for training to the `project.yml` file.

1) Create a new config in [configs/](./configs)
2) In `project.yml`, in section `vars` add your new pipeline like `cpu_efficiency_config` with path to the config file (.cfg)
3) In `project.yml`, in section `workflows` add your new pipeline (list of subcommands to chain)
4) In `project.yml`, in section `TRAINING MODEL COMMANDS` add a running command section like this: 

```
  - name: <Choose a name for your train command>
    help: "<Choose a description your train command>"
    script:
      - "python -m spacy debug config configs/${vars.<replace with var name of config path>} --paths.train corpus/train.spacy --paths.dev corpus/dev.spacy"
      - "python -m spacy debug data configs/${vars.<replace with var name of config path>} --paths.train corpus/train.spacy --paths.dev corpus/dev.spacy"
      - "python -m spacy train configs/${vars..<replace with var name of config path>} -o training/ --gpu-id ${vars.gpu} --paths.train corpus/train.spacy --paths.dev corpus/dev.spacy --verbose"
    deps:
      - "corpus/train.spacy"
      - "corpus/dev.spacy"
      - "configs/${vars.<replace with var name of config path>}"
    outputs:
      - "training/model-best"
```
5) Now you can start your new training workflow `$ spacy project run <name of new workflows>` and all the referenced subcommands will execute one by one.