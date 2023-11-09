
:shirt: :womans_hat: :dress: 👖: 
# Clothing Retail Recommender System

This is a Clothing retail recommender system using Python and Pandas. The goal is to provide recommendations for clothing items based on customer review ratings. We are using a dataset loaded from a CSV file (from kaggle) containing information about items purchased and their corresponding review ratings.

## 

First we load the data from the "Fashion_Retail_Sales.csv" file into a Pandas DataFrame and display the initial rows to inspect the dataset's structure.
We then clean the data by removing rows with missing values in essential columns and filtering out review ratings that are not within the valid range (1 to 5).
Then calculate the average review ratings for each item, sort the items based on these ratings in descending order, and finally, select the top 5 recommended items.

```python
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("Fashion_Retail_Sales.csv")

# Display the first few rows of the DataFrame to understand the structure of the data
print(df.head())



