import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def explore_univariate(df, cat_vars, cont_vars):
    '''
    This function takes in categorical and continuous variables from a dataframe.
    It returns a bar plot for each categorical variable
    and a histogram and boxplot for each continuous variable.
    '''
    # plot frequencies for each categorical variable
    for var in cat_vars: 
        print('Bar Plot of ' + var)
        bp = df[var].hist()
        plt.xlabel(var)
        plt.ylabel('count')
        bp.grid(False)
        plt.show()
        
    # print histogram for each continuous variable
    for var in cont_vars:
        generate_hist(df, var)
        # creating boxplot for each variable
        plt.figure(figsize=(10,5))
        sns.boxplot(x=var, data=df,  palette="twilight_shifted")
        plt.title('Distribution of ' + var)
        plt.show()


def generate_hist(df, var):
    '''
    Helper function. Given a dataframe DF and a variable to plot, this function will 
    generate and display a histogram for that variable.
    '''
    print ('Distribution of ' + var)
    df[var].hist(bins=100)
    plt.grid(False)
    plt.xlabel(var)
    plt.ylabel('Number of Movies')
    plt.show()

def generate_barplot(df, target, var):
    '''
    Helper function to generate barplots. Given a dataframe df, a target column and a 
    variable, this will generate and draw a barplot for that data set.
    '''
    overall_mean = df[target].mean()
    sns.barplot(var, target, data=df, palette="twilight_shifted")
    plt.xlabel('')
    plt.ylabel('Rating')
    plt.title('Bar plot of ' + var + ' vs ' + target)
    plt.axhline(overall_mean, ls = '--', color = 'grey')
    plt.show()

def generate_scatterplot(df, target, var):
    '''
    This function takes in a dataframe, the target variable and the independent variable which are both continuous. 
    It creates a scatter plot with the predictor as the x variable and the target as the y variable.
    '''
    sns.relplot(x=var, y=target, data=df)

def generate_boxplot(df,target, var):
    '''
    Given a dataframe df, a target column and a variable to plot, this helper function
    will generate and display a boxplot comparing the given data elements.
    '''
    plt.figure(figsize=(10,5))
    sns.boxplot(y=var, x=target, data=df,  palette="twilight_shifted")
    plt.title('Boxplot of ' + var)
    plt.show()

def generate_countplot(df, target, var):
    '''
    Another helper function used to display a plot. Given a dataframe df, a target
    column and a variable, this function will create and display a countplot.
    '''
    sns.countplot(data=df, x=var, hue=target,  palette="twilight_shifted")
    plt.tight_layout()
    plt.show()   


def explore_bivariate(df, target, cat_vars, cont_vars):
    '''
    This function takes in takes in a dataframe, the name of the binary target variable, a list of 
    the names of the categorical variables and a list of the names of the quantitative variables. It returns
    bar plots for categorical variables and scatterplots for quantitative(continuous) variables.
    For each categorical variable, the bar plot shows the tax value for each class in each category
    with a dotted line for the average overall tax value. 
    The scatterplots show the relationship between quantitative variables and the target variable.
    '''
    for var in cat_vars:
        # bar plot with overall horizontal line
        generate_barplot(df, target, var)
    for var in cont_vars:
        # creates scatterplot with regression line
        generate_scatterplot(df, target, var)


def explore_multivariate(train, target, cat_vars, cont_vars):
    '''
    This function takes in takes in a dataframe, the name of the binary target variable, a list of 
    the names of the categorical variables and a list of the names of the quantitative variables.
    It generates scatterplots showing the target variable for each class of the categorical variables 
    against the continuous variables.
    '''
    for cat in cat_vars:
        for cont in cont_vars:
            sns.relplot(x=cont, y=target, data=train, hue=cat, palette ='twilight_shifted')
            plt.xlabel(cont)
            plt.ylabel(target)
            plt.title(cont + ' vs ' + target + ' by ' + cat)
            plt.show()

def create_heatmap(train, cols):
    '''
    This function takes in the training split as well as the columns to find correlation for. 
    It creates a correlation matrix and then displays a heatmap showing all of the correlations. 
    The highest correlation values have the darkest colors in this heatmap.
    '''
    corr_matrix = train[cols].corr()
    plt.figure(figsize=(15,8))
    sns.heatmap(corr_matrix, cmap='twilight_shifted', annot=True, linewidth=0.5, mask= np.triu(corr_matrix))
    plt.title('Correlation with the target and among features in the train split')
    plt.show()