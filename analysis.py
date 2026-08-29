import pandas as pd
import matplotlib.pyplot as plt
import os

# -----------------------------------
# 1. Create images folder if needed
# -----------------------------------

os.makedirs("images", exist_ok=True)


# -----------------------------------
# 2. Load the cleaned dataset
# -----------------------------------

df = pd.read_csv("data/matches_clean.csv")

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)


# -----------------------------------
# 3. TOP 10 TEAMS BY TOTAL GOALS
# -----------------------------------

# Home goals
home_goals = df.groupby("HomeTeam")["FTHG"].sum()

# Away goals
away_goals = df.groupby("AwayTeam")["FTAG"].sum()

# Combine home and away goals
total_goals = home_goals.add(away_goals, fill_value=0)

# Sort from highest to lowest
total_goals = total_goals.sort_values(ascending=False)

# Get top 10
top10 = total_goals.head(10)

print("\nTop 10 Teams by Total Goals:")
print(top10)


# Create bar chart
plt.figure(figsize=(10, 5))

top10.plot(kind="bar")

plt.title("Top 10 Teams by Total Goals")
plt.xlabel("Team")
plt.ylabel("Goals")

plt.tight_layout()

plt.savefig("images/top_teams_goals.png")

plt.show()


# -----------------------------------
# 4. HOME ADVANTAGE
# -----------------------------------

results = df["FTR"].value_counts()

# Rename the results
results.index = ["Home Win", "Away Win", "Draw"]

print("\nMatch Results:")
print(results)


# Create pie chart
plt.figure(figsize=(6, 6))

results.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Home Wins vs Away Wins vs Draws")

plt.ylabel("")

plt.tight_layout()

plt.savefig("images/home_advantage_pie.png")

plt.show()


# -----------------------------------
# 5. GOALS BY MONTH
# -----------------------------------

# Convert Date to datetime
df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)

# Extract month
df["Month"] = df["Date"].dt.month_name()

# Calculate total goals
df["TotalGoals"] = df["FTHG"] + df["FTAG"]

# Calculate average goals per month
monthly_goals = df.groupby("Month")["TotalGoals"].mean()

# Correct calendar order
months = [
    "August",
    "September",
    "October",
    "November",
    "December",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July"
]

monthly_goals = monthly_goals.reindex(
    [month for month in months if month in monthly_goals.index]
)

print("\nAverage Goals by Month:")
print(monthly_goals)


# Find highest month
highest_month = monthly_goals.idxmax()

highest_average = monthly_goals.max()

print("\nHighest-scoring month:")
print(highest_month)

print("Average goals:", round(highest_average, 2))


# Create line chart
plt.figure(figsize=(10, 5))

monthly_goals.plot(marker="o")

plt.title("Average Goals per Match by Month")
plt.xlabel("Month")
plt.ylabel("Average Goals")

plt.tight_layout()

plt.savefig("images/monthly_goals.png")

plt.show()


# -----------------------------------
# 6. FINAL SUMMARY
# -----------------------------------

print("\n==============================")
print("FINAL PROJECT SUMMARY")
print("==============================")

print(f"Total matches analyzed: {len(df)}")

print(
    f"Home wins: {results['Home Win']} "
    f"({results['Home Win'] / len(df) * 100:.1f}%)"
)

print(
    f"Away wins: {results['Away Win']} "
    f"({results['Away Win'] / len(df) * 100:.1f}%)"
)

print(
    f"Draws: {results['Draw']} "
    f"({results['Draw'] / len(df) * 100:.1f}%)"
)

print(
    f"Highest average-goal month: {highest_month} "
    f"({highest_average:.2f} goals)"
)

print("\nAnalysis complete!")