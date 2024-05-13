#!/usr/bin/env python
# -*- coding: utf-8 -*-
# datasets_download.py


__author__ = "Kamil Rataj"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Kamil Rataj"
__status__ = "Development"

import kaggle


def download_kaggle_datasets(dataset_list):
    """
    Download each dataset specified in the list from Kaggle using the Kaggle API.

    Args:
    dataset_list (list of str): A list of dataset identifiers on Kaggle.
    """
    try:
        with open(dataset_list, 'r') as file:
            for line in file:
                line = line.strip()
                if line:  # Ensures that blank lines are skipped
                    try:
                        kaggle.api.dataset_download_files(line, path='../datasets/', unzip=True)
                        print(f"Successfully downloaded {line}")
                    except Exception as e:
                        print(f"Failed to load {line}: {e}")
    except FileNotFoundError:
        print(f"File {dataset_list} not found.")
    except Exception as e:
        print(f"An error occurred while reading {dataset_list}: {e}")


if __name__ == "__main__":
    download_kaggle_datasets('../datasets/config/datasets_source.txt')
