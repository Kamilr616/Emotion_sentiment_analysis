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


def standardize_emotion_names(dataframe, emotion_dict):
    """
    Standardize the names of emotions in a DataFrame.

    Args:
    dataframe (pd.DataFrame): The DataFrame containing emotion labels.
    emotion_dict (dict): A dictionary mapping original emotion names to standardized names.

    Returns:
    pd.DataFrame: The DataFrame with standardized emotion names.
    """
    reverse_emotion_dict = {synonym: emotion for emotion, synonyms in emotion_dict.items() for synonym in synonyms}
    dataframe['emotion'] = dataframe['emotion'].replace(reverse_emotion_dict)
    return dataframe


# TODO: Complete a dictionary of emotions to standardize the names

emotions_dictionary = {
    'sadness': ['sad', 'sadness', 'depressed', 0],
    'happiness': ['happy', 'happiness', 'joy', 1],
    'neutral': ['neutral', 'indifferent', 'unbiased'],
    'worry': ['worry', 'anxiety', 'concern'],
    'surprise': ['surprise', 'astonishment', 'shock', 5],
    'love': ['love', 'affection', 'adoration', 2],
    'anger': ['angry', 'rage', 'outrage', 'anger', 3],
    'relief': ['relief', 'ease', 'comfort'],
    'fear': ['fear', 'dread', 'terror', 4],

    'empty': ['empty', 'void', 'hollow'],
    'fun': ['fun', 'joyful', 'amusing'],
    'hate': ['hate', 'detest', 'loathe'],
    'enthusiasm': ['enthusiastic', 'excited', 'eager'],
    'boredom': ['boredom', 'tedium', 'monotony']
}
if __name__ == '__main__':
    df_merged = concat_dataframes(load_datasets_from_file('../datasets/config/datasets.txt'))
    df_merged_std = standardize_column_names(df_merged, emotions_dictionary)
    print(df_merged_std.head())
