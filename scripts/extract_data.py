import typer
from pathlib import Path
from zipfile import ZipFile


def partition():
    pass

def main(data_loc: Path, out_dir: Path):
    """Extract train/test/dev split from corpus .zip archive."""
    """
    list_corpus = ['output_annotated_corpus/data_split_n3/train.conll',
                   'output_annotated_corpus/data_split_n3/dev.conll',
                   'output_annotated_corpus/data_split_n3/test.conll']
    with ZipFile(data_loc, mode='r') as zipObject:
        list_filenames = zipObject.namelist()
        for file in list_filenames:
            if file in list_corpus:
                zipObject.extract(file, out_dir)
    """
    # extract the dataset from zip archive
    corpus_to_extract = 'output_annotated_corpus/all_reduced.conll'
    with ZipFile(data_loc, mode='r') as zipObject:
        list_filenames = zipObject.namelist()
        for file in list_filenames:
            if file == corpus_to_extract:
                zipObject.extract(file, "assets/conll")

    # then partition file:
    fraction = 0.2
    seed = 0
    import random
    random.seed(0)
    phrases = []
    # read the input file and count empty lines
    with open(f'assets/conll/{corpus_to_extract}', mode='r', encoding='utf-8') as f:
        lines = f.readlines()
        # number of phrases = number of \t\n lines
        phrase = []
        for line in lines:
            if line == '\t\n':
                phrase.append(line.replace('\t', ''))
                phrases.append(phrase)
                phrase = []
            else:
                phrase.append(line.replace('\t', ' '))

    num_phrases = len(phrases)
    print(f'{num_phrases} phrases detected in dataset.')

    random.shuffle(phrases)
    dev_size = int(fraction * num_phrases)
    test_size = int(fraction * num_phrases)
    train_size = (num_phrases - dev_size) - test_size

    def get_percent(v1: int, v2: int) -> int:
        return int((v1*100)/v2)

    print(f'Total phrases in train data: {train_size} - {get_percent(train_size, num_phrases)} %')
    print(f'Total phrases in dev data: {dev_size} - {get_percent(dev_size, num_phrases)} %')
    print(f'Total phrases in test data: {test_size} - {get_percent(test_size, num_phrases)} %')

    # train
    train = phrases[:train_size]
    # dev
    dev = phrases[train_size:train_size+dev_size]
    # test
    test = phrases[train_size+dev_size:]

    if out_dir.is_dir():
        print(f"{out_dir} exists.")
    else:
        print(f"Create a new {out_dir}")
        out_dir.mkdir(parents=True)
    with (out_dir / "train.iob").open("w", encoding="utf-8") as file_:
        for sentence in train:
            file_.write("".join(sentence))
    with (out_dir / "dev.iob").open("w", encoding="utf-8") as file_:
        for sentence in dev:
            file_.write("".join(sentence))
    with (out_dir / "test.iob").open("w", encoding="utf-8") as file_:
        for sentence in test:
            file_.write("".join(sentence))


    # remove old dataset


if __name__ == "__main__":
    typer.run(main)
    #main(data_loc=Path("../assets/output_annotated_corpus.zip"),out_dir=Path("../assets/conll"))