# module imports
import pandas as pd
import numpy as np

def get_data():
    '''
    This function returns the csv file as a pandas dataframe. The csv file can be downloaded from https://www.kaggle.com/mustafacicek/imdb-top-250-lists-1996-2020.
    '''
    imdb_df = pd.read_csv('imdbTop250.csv')
    #return the dataframe 
    return imdb_df


def summarize(df):
    '''
    This function will take in a single argument (a pandas dataframe) and 
    output to console various statistices on said dataframe, including:
    # .shape
    # .info()
    # observation of nulls in the dataframe
    '''
    # Print out the "shape" of our dataframe - the rows and columns we have to work with
    print(f'The IMDB dataframe has {df.shape[0]} rows and {df.shape[1]} columns.')
    print('')
    print('-------------------')

    # print the number of missing values in our dataframe
    print(f'There are total of {df.isna().sum().sum()} missing values in the entire dataframe.')
    print('')
    print('-------------------')

    # print information regarding column datatypes and non null counts
    df.info()
    print('')
    print('-------------------')
