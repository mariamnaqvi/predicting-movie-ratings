# Predicting Movie Ratings

## Objective
Build models to predict the rating for any film in the IMDB database, given a set of data representing the film's characteristics. Create a series of supervised machine-learning models, and evaluate each model's performance using RMSE and R-Squared measures.

## Methods
Clean and prepare the data for modeling, splitting the data into 3 sets (Train, Validate and Test). Explore relationships between variables to find the best drivers of movie ratings. Use these drivers to create various models to predict film ratings. These models were then evaluated against a baseline to determine their performance. 

## Results
Compare the RMSE and R-Squared values, such that the best-performing model will exhibit the highest R-Squared and lowest RSME values. In this analysis, the optimal model was the OLS Linear Regression Model, with an RMSE of 4.153175e-15 (essentially 0) and an R-Squared of 1. This outperformed the other models as well as the baseline RMSE and R-Squared, which were 0.34 and 0, respectively.

## Conclusions & Next Steps
According to the analysis, the best-performing model made use of OLS Linear Regression, and beat the baseline RMSE and R-Squared values.

The model depended on drivers such as Ranking, Year, Date, Runtime, Score, Votes and Gross Value, which proved effective in predicting a movie's ratings.

With more time, we could remove outliers and evaluate the impact on model performance as well as try scaling methods.

## Reproducing this Report
- Download the dataset from [here](https://www.kaggle.com/mustafacicek/imdb-top-250-lists-1996-2020)
- Import the acquire, prepare and explore scripts
- Work through the steps in the [notebook](https://github.com/mariamnaqvi/predicting-movie-ratings/blob/main/final_report_imdb_ratings.ipynb)

## Initial Hypotheses
*Hypotheses 1:* I rejected the null hypotheses; movies with runtimes lower than 150mins have lower ratings.
* Confidence level = 0.95 
* Alpha = 1 - Confidence level = 0.05
* H<sub>0</sub>: Mean rating for movies with runtime less than 150mins is equivalent to those with more than 150mins runtime
* H<sub>1</sub>: Mean rating for movies with runtime less than 150mins is lower than those with more than 150mins runtime

## Data Dictionary
Name | Datatype | Definition | Possible Values 
--- | --- | --- | --- 
Ranking |  int64  | The ranking for the movie | Numeric value
IMDByear  | int64  | Year the movie was released |Numeric value
IMDBlink  | object | Link to the movie on IMDB | Hyperlink
Title     | object | Title of the movie | String
Date      | int64  | Date the movie was created | String
RunTime   | int64  | Length of the movie | Numeric value
Genre     | object | Genre of the movie | String
Rating    | float64 | The movie's rating | Numeric value
Score     | float64 | The overall score of the movie | Numeric value
Votes     | int64  | Number of Votes for the movie | Numeric value
Gross     | float64 | Money made by the movie (gross) | Numeric value
Director  | object | The name of the movie's director | String
Cast1     | object | Primary cast member's name | String
Cast2     | object | Secondary cast member's name | String
Cast3     | object | Tertiary cast member's name | String
Cast4     | object | Quadernary cast member's name | String
