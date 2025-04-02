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

# Step 5: Plot price distribution
plt.figure(figsize=(8, 5))
plt.hist(df['Price'], bins=5, edgecolor='black')
plt.title("Price Distribution of Books")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.grid(True)
plt.tight_layout()