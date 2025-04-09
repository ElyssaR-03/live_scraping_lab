import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the scraped CSV
df = pd.read_csv("books.csv")

# Step 2: Clean price data (remove £ and convert to float)
df['Price'] = df['Price'].str.replace('£', '').astype(float)

# Step 3: Show basic summary
print("🎯 Book Data Summary")
print("-" * 30)
print(f"Total books: {len(df)}")
print(f"Average price: £{df['Price'].mean():.2f}")
print(f"Most expensive book: {df.loc[df['Price'].idxmax()]['Title']}")
print(f"Cheapest book: {df.loc[df['Price'].idxmin()]['Title']}")

# Step 4: Availability count
availability_counts = df['Availability'].value_counts()
print("\n📦Availability Breakdown:")
print(availability_counts)

#Plot availability breakdown
plt.figure(figsize=(8, 5))
availability_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Availability Breakdown")
plt.xlabel("Availability Status")
plt.ylabel("Number of Books")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("availability_breakdown.png") #Svae the chart as an image
plt.show()

# Step 5: Plot price distribution
plt.figure(figsize=(8, 5))
plt.hist(df['Price'], bins=5, edgecolor='black')
plt.title("Price Distribution of Books")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.grid(True)
plt.tight_layout()
plt.savefig("price_distribution.png") #Save the chart as an image
plt.show()

#Step 6: highliht books over a certain price threshold
price_threshold = 30.0 #Set the threshold
expensive_books = df[df['Price'] > price_threshold]
print(f"\n📚 Books over £{price_threshold}:")
print(expensive_books[['Title', 'Price']])

#Step 7: Export summary stats to a new CSV or HTML report
summary_stats = {
    'Total Books': len(df),
    'Average Price': df['Price'].mean(),
    'Most Expensive Book': df.loc[df['Price'].idxmax()]['Title'],
    'Cheapest Book': df.loc[df['Price'].idxmin()]['Title'],
}

summary_df = pd.DataFrame(summary_stats)
summary_df.to_csv("Summary_stats.csv", index=False)
