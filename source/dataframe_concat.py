#!/usr/bin/env python
# -*- coding: utf-8 -*-
# dataframe_concat.py

__author__ = "Kamil Rataj"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Kamil Rataj"
__status__ = "Development"

import pandas as pd
from datasets_import import load_datasets_from_file

column_mapping = {
    'text': ['text', 'content', "comment"],
    'emotion': ['emotion', 'label', 'sentiment']
}


# Function to rename columns based on mapping
def standardize_column_names(frame, column_map):
    # Convert all column names to lowercase
    frame.columns = map(str.lower, frame.columns)

    # Create a reverse mapping where each synonym maps to the standard name
    reverse_mapping = {synonym: standard for standard, synonyms in column_map.items() for synonym in synonyms}

    # Rename the columns in the DataFrame
    for old_name, new_name in reverse_mapping.items():
        if old_name in frame.columns:
            frame.rename(columns={old_name: new_name}, inplace=True)

    return frame


def concat_dataframes(dataframes):
    """
    Concatenate a list of DataFrames into a single DataFrame.

    Args:
    dataframes (list of pd.DataFrame): A list of DataFrames to concatenate.

    Returns:
    pd.DataFrame: A single DataFrame containing all the data from the input DataFrames.
    """
    final_dataset = []

    for df in dataframes:
        df_std = standardize_column_names(df, column_mapping)
        final_dataset.append(df_std[['text', 'emotion']])

    return pd.concat(final_dataset, ignore_index=True)


# TODO: standardize emotion names

if __name__ == '__main__':
    df_merged = concat_dataframes(load_datasets_from_file('../datasets/config/datasets.txt'))
    print(df_merged)
