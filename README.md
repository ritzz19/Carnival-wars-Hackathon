# Carnival-wars-Hackathon

It was a hackathon conducted by HackerEarth. Our main motto was to predict the selling price for different products.
Secured rank in the top 5% of the leaderboard. 

Link to the hackathon:
https://www.hackerearth.com/challenges/competitive/hackerearth-machine-learning-challenge-predict-selling-price/

Rank: https://www.hackerearth.com/challenges/competitive/hackerearth-machine-learning-challenge-predict-selling-price/leaderboard/predict-the-price-5-fe7f8735/page/2/
(91/2144)

# Analysis:
Tableau link: https://public.tableau.com/profile/swati.thapa#!/vizhome/Carnival-hackathon/Analysis

For data analysis, I have used Tableau to get a better insight into the training data provided. Following were the observations: 
1. Selling price has negative values.
2. Technology has the highest number of charges.
3. Linear relationship is observed between the minimum and maximum price.
4. Product category has increased with respect to quarter and the year.
5. Loyal customer tends to purchase more.
6. Market category 23,24,58,452 and 358 has the highest number of the selling price.
7. Grade '0' tends to have the most number of selling price and Grade '1' has the least number of the selling price.

![2021-01-23_15-43-51](https://user-images.githubusercontent.com/30840805/105609646-b5d2bd80-5dd0-11eb-9d32-25fd6562e1ff.png)

# Modeling: (Carnival-Hackathon.ipynb file)
I have used python for further data analysis and modeling. Data cleaning applied:
1. To remove the outlier in minimum and selling price features.
2. Used correlation and ANOVA test to decide which feature to drop.
3. For modeling RandomForest Regressor gave the best result. 
4. Used hyperparameter tuning to get a more optimized result. I was able to get 99.87% RMSLE for training data and 91.37% RMSLE in test data.

# Deployment:
Deployment link: https://halloween-carnival-price.herokuapp.com/
1. I have used the Heroku platform to deploy the model.
2. I have used HTML and CSS for the frontend and FLASK as the backend for the website.

![2021-01-23_23-13-30](https://user-images.githubusercontent.com/30840805/105609651-bc613500-5dd0-11eb-8e02-4919421be9f7.png)

