# ⚽ Football Match Analysis

## Project Overview

This project analyzes football match data using Python, Pandas, and Matplotlib.

The purpose of the project is to explore football match results, team goal-scoring performance, home advantage, and goal-scoring patterns across different months.

## Dataset

The dataset contains football match information, including:

* Match date
* Home team
* Away team
* Home team goals
* Away team goals
* Full-time result
* Other match statistics and betting information

The original dataset contained **7,404 rows and 104 columns**.

After cleaning, the dataset contained **7,403 matches and 70 columns**.

## Data Cleaning

The following cleaning steps were performed:

1. Checked for duplicate rows.
2. Found no duplicate rows.
3. Removed one completely empty row.
4. Removed 34 columns containing more than 80% missing values.
5. Saved the cleaned data as `matches_clean.csv`.

## Analysis Performed

### 1. Top 10 Teams by Total Goals

Home and away goals were combined to calculate the total goals scored by each team.

Arsenal ranked first in the dataset, followed by Manchester United.

### 2. Home Advantage

The match result column (`FTR`) was analyzed to compare home wins, away wins, and draws.

Results:

* Home wins: **3,428 (46.3%)**
* Away wins: **2,111 (28.5%)**
* Draws: **1,864 (25.2%)**

The results suggest that home teams had a significant advantage in the matches analyzed.

### 3. Average Goals by Month

The match dates were converted into datetime values and the month was extracted.

The total goals in each match were calculated using:

`Home Goals + Away Goals`

The average number of goals was then calculated for each month.

The month with the highest average number of goals in this dataset was **July**, with **2.94 goals per match across 66 matches**.

## Visualizations

The project produces three main visualizations:

1. Top 10 Teams by Total Goals
2. Home Wins vs Away Wins vs Draws
3. Average Goals per Match by Month

All visualizations are stored in the `images` folder.

## Technologies Used

* Python
* Pandas
* Matplotlib
* VS Code

## How to Run the Project

Install the required libraries:

```bash
pip3 install -r requirements.txt
```

Then run:

```bash
python3 analysis.py
```

## Key Findings

The analysis shows that:

* Arsenal was the highest-scoring team in the dataset.
* Manchester United ranked second in total goals.
* Home teams won **46.3%** of the matches analyzed.
* Away teams won **28.5%** of the matches analyzed.
* July had the highest average goals per match at **2.94**.

## Conclusion

This project demonstrates a basic Data Science workflow:

**Data Collection → Data Cleaning → Exploratory Data Analysis → Data Visualization → Interpretation**

The project was developed as a beginner Data Science project using real football match data.
