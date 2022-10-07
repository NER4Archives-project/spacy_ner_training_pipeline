import os
import shutil
import typer


def main():
    directories_to_clean = [
        './training/',
        './corpus/',
        './packages/'
    ]
    for dir in directories_to_clean:
        for ele in os.listdir(dir):
            ele_to_remove = dir+ele
            if os.path.isfile(ele_to_remove):
                os.remove(ele_to_remove)
            if os.path.isdir(ele_to_remove):
                shutil.rmtree(ele_to_remove)

if __name__ == "__main__":
    typer.run(main)