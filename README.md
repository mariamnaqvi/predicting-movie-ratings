# predicting-movie-ratings

## OBJECTIVE
Build models to predict the rating for any film in the IMDB database, given a set of data representing the film's characteristics. Create a series of supervised machine-learning models, and evaluate each model's performance using RMSE and R-Squared measures.

## METHODS
Clean and prepare the data for modeling, splitting the data into 3 sets (Train, Validate and Test). Explore relationships between variables to find the best drivers of movie ratings. Use these drivers to create various models to predict film ratings. These models were then evaluated against a baseline to determine their performance. 

## RESULTS
Compare the RMSE and R-Squared values, such that the best-performing model will exhibit the highest R-Squared and lowest RSME values. In this analysis, the optimal model was <>, with an RMSE of <> and an R-Squared of <>. This outperformed the other models as well as the baseline RMSE and R-Squared, which were <> and <> respectively.

## CONCLUSIONS
The selected drivers were <effective/ineffective> in predicting a movie's ratings.

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
