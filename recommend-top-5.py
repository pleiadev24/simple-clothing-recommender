import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("Fashion_Retail_Sales.csv")

# Display the first few rows of the DataFrame to understand the structure of the data
print(df.head())

# Remove rows with missing or NaN values in the required columns
df = df.dropna(subset=['Item Purchased', 'Review Rating'])

# Convert 'Review Rating' column to numeric type
df['Review Rating'] = pd.to_numeric(df['Review Rating'], errors='coerce')

# Filter out rows with invalid review ratings (less than 1 or greater than 5)
df = df[(df['Review Rating'] >= 1) & (df['Review Rating'] <= 5)]

# Calculate the average review ratings for each item
average_ratings = df.groupby('Item Purchased')['Review Rating'].mean().reset_index()

# Sort items based on average ratings in descending order
sorted_items = average_ratings.sort_values(by='Review Rating', ascending=False)

# Get the top N recommended items
top_n_items = 5
recommended_items = sorted_items.head(top_n_items)

# Display the recommended items
print("Top 5 Recommended Items:")
print(recommended_items)
