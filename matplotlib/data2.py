import matplotlib.pyplot as plt
import pandas as pd

# Your data
data = [
    {"UserID": 1,  "Age": 25, "Country": "USA",    "SessionTime": 12.5, "Purchases": 1},
    {"UserID": 2,  "Age": 30, "Country": "Canada", "SessionTime": 8.0,  "Purchases": 0},
    {"UserID": 3,  "Age": 22, "Country": "USA",    "SessionTime": 15.3, "Purchases": 2},
    {"UserID": 4,  "Age": 40, "Country": "UK",     "SessionTime": 7.2,  "Purchases": 1},
    {"UserID": 5,  "Age": 35, "Country": "Germany","SessionTime": 20.1, "Purchases": 3},
    {"UserID": 6,  "Age": 28, "Country": "USA",    "SessionTime": 9.5,  "Purchases": 0},
    {"UserID": 7,  "Age": 45, "Country": "Canada", "SessionTime": 13.4, "Purchases": 2},
    {"UserID": 8,  "Age": 23, "Country": "USA",    "SessionTime": 18.2, "Purchases": 4},
    {"UserID": 9,  "Age": 38, "Country": "UK",     "SessionTime": 11.0, "Purchases": 1},
    {"UserID": 10, "Age": 26, "Country": "Germany","SessionTime": 14.7, "Purchases": 2},
    {"UserID": 11, "Age": 31, "Country": "USA",    "SessionTime": 16.9, "Purchases": 3},
    {"UserID": 12, "Age": 29, "Country": "Canada", "SessionTime": 10.5, "Purchases": 1},
    {"UserID": 13, "Age": 50, "Country": "UK",     "SessionTime": 5.2,  "Purchases": 0},
    {"UserID": 14, "Age": 41, "Country": "Germany","SessionTime": 19.5, "Purchases": 4},
    {"UserID": 15, "Age": 27, "Country": "USA",    "SessionTime": 13.8, "Purchases": 2},
    {"UserID": 16, "Age": 36, "Country": "Canada", "SessionTime": 12.1, "Purchases": 1},
    {"UserID": 17, "Age": 24, "Country": "UK",     "SessionTime": 17.6, "Purchases": 3},
    {"UserID": 18, "Age": 32, "Country": "Germany","SessionTime": 9.9,  "Purchases": 0},
    {"UserID": 19, "Age": 39, "Country": "USA",    "SessionTime": 21.3, "Purchases": 5},
    {"UserID": 20, "Age": 34, "Country": "Canada", "SessionTime": 14.2, "Purchases": 2},
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Aggregate by Country
country_group = df.groupby("Country").agg({
    "SessionTime": "mean",
    "Purchases": "sum",
    "UserID": "count"  # count of users
}).rename(columns={"UserID": "UserCount"})

# Create subplots (2 rows × 3 cols)
fig, axs = plt.subplots(2, 3, figsize=(18, 10))

# 1. Histogram of Age
axs[0, 0].hist(df["Age"], bins=8, color="skyblue", edgecolor="black")
axs[0, 0].set_title("Age Distribution")
axs[0, 0].set_xlabel("Age")
axs[0, 0].set_ylabel("Count")

# 2. Histogram of Session Time
axs[0, 1].hist(df["SessionTime"], color="lightgreen", edgecolor="black")
axs[0, 1].set_title("Session Time Distribution")
axs[0, 1].set_xlabel("Session Time (minutes)")
axs[0, 1].set_ylabel("Count")

# 3. Bar chart: Average Session Time per Country
axs[0, 2].bar(country_group.index, country_group["SessionTime"], color=["blue", "red", "green", "orange"])
axs[0, 2].set_title("Avg Session Time by Country")
axs[0, 2].set_xlabel("Country")
axs[0, 2].set_ylabel("Avg Session Time (min)")

# 4. Scatter: Age vs SessionTime
axs[1, 0].scatter(df["Age"], df["SessionTime"], c="purple", s=50, alpha=0.7)
axs[1, 0].set_title("Age vs Session Time")
axs[1, 0].set_xlabel("Age")
axs[1, 0].set_ylabel("Session Time (min)")

# 5. Bar chart: Total Purchases by Country
axs[1, 1].bar(country_group.index, country_group["Purchases"], color=["cyan", "magenta", "yellow", "grey"])
axs[1, 1].set_title("Total Purchases by Country")
axs[1, 1].set_xlabel("Country")
axs[1, 1].set_ylabel("Purchases")

# 6. Scatter / Correlation: SessionTime vs Purchases
axs[1, 2].scatter(df["SessionTime"], df["Purchases"], c="teal", s=70, alpha=0.6)
axs[1, 2].set_title("Session Time vs Purchases")
axs[1, 2].set_xlabel("Session Time (min)")
axs[1, 2].set_ylabel("Purchases")

# Layout adjustments
plt.tight_layout()
fig.suptitle("User Behavior Dashboard", fontsize=18, y=1.02)

plt.show()