#!/usr/bin/env python
# -*- coding: utf-8 -*-
# datasets_import.py


__author__ = "Kamil Rataj"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Kamil Rataj"
__status__ = "Development"

import pandas as pd


def load_datasets_from_file(filename):
    """
    Reads filenames from a text file, each pointing to a dataset.
    Each dataset is loaded into a pandas DataFrame and all DataFrames
    are returned in a list.

    Args:
    filename (str): The path to the text file containing dataset paths.

    Returns:
    list of pd.DataFrame: A list containing all the DataFrames loaded.
    """
    dataframes = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:  # Ensures that blank lines are skipped
                    try:
                        # Load the dataset into a DataFrame
                        line = f"../datasets/{line}"
                        dframe = pd.read_csv(line)
                        dataframes.append(dframe)
                    except Exception as e:
                        print(f"Failed to load {line}: {e}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred while reading {filename}: {e}")

    return dataframes


if __name__ == '__main__':
    for df in load_datasets_from_file('../datasets/config/datasets.txt'):
        print(df.head())
