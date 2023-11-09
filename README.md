
# Clothing Retail Recommender System

In this project, we are building a clothing retail recommender system using Python and Pandas. The goal is to provide recommendations for clothing items based on customer review ratings. We are using a dataset loaded from a CSV file ( from kaggle) containing information about items purchased and their corresponding review ratings.

## Code Description

### 1. Load data
```python
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("Fashion_Retail_Sales.csv")

# Display the first few rows of the DataFrame to understand the structure of the data
print(df.head())
