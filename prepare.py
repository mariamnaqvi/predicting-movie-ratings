import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# function to clean original df
def prep_data(df):
    # check for duplicates 
    num_dups = df.duplicated().sum()
    # if we found duplicate rows, we will remove them, log accordingly and proceed
    if num_dups > 0:
        print(f'There are {num_dups} duplicate rows in your dataset - these will be dropped.')
        print ('----------------')
        # remove the duplicates found
        df = df.drop_duplicates()

    else:
        # otherwise, we log that there are no dupes, and proceed with our process
        print(f'There are no duplicate rows in your dataset.')
        print('----------------')

    # check how many rows with null values
    null_rows = df.isnull().any(axis=1).sum()
    if null_rows > 0:
        print(f'There are {null_rows} rows with null values in your dataset - these will be replaced.')
        print ('----------------')
        # remove the null values found
        df = df.dropna()

    else:
        # otherwise, we log that there are no null values, and proceed with our process
        print(f'There are no rows with null values in your dataset.')
        print('----------------')

    # handling nulls in Score
    # find the median score 
    median_score = df.Score.median()

    # replace null values with the median score
    df.Score = df.Score.replace(np.NaN, median_score)

    # handling nulls in Gross
    # find the median value 
    median_gross = df.Gross.median()

    # replace null values with the median score
    df.Gross = df.Gross.replace(np.NaN, median_gross)

    # drop the cast columns with nulls
    df = df.drop(columns=['Cast3', 'Cast4'])  

    # return info about cleaned df
    df.info()
    # return cleaned df
    return df 



def split_data(df, seed=123):
    '''
    This function takes in a pandas dataframe and a random seed. It splits the original
    data into train, test and split dataframes, prints out their shapes and returns the splits.
    Test dataset is 20% of the original dataset
    Train is 56% (0.7 * 0.8 = .56) of the original dataset
    Validate is 24% (0.3 * 0.7 = 0.24) of the original dataset
    '''
    train, test = train_test_split(df, train_size=0.8, random_state=seed)
    train, validate = train_test_split(train, train_size=0.7, random_state=seed)

    # Now that we have our 3 dataframes, print their shapes and return them    
    
    print(f'Shape of train split: {train.shape}')

    print ('----------------')

    print(f'Shape of test split: {validate.shape}')

    print ('----------------')

    print(f'Shape of validate split: {test.shape}')

    print ('----------------')

    return train, validate, test

