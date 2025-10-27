Project 1 – Premier League 2024/25 Football Analysis (Python)

Created by: Zac Jackson
Date: October 2025
Tools Used: Python (Pandas, Matplotlib, Seaborn, NumPy)

---

Objective

To analyze key performance metrics from the 2024/25 English Premier League season, exploring how team possession correlates with performance indicators such as point, goals scored, goals conceded, and expected goal metrics (xG, xGA, xGD).

The project aims to uncover whether maintaining higher possession consistently translates into better results — and what this reveals about tactical styles across clubs.

---

Datasets Used

1. `football_data_games.xlsx`

Match-level statistics including:

| Column                      | Description                    |
| --------------------------- | ------------------------------ |
| Date, Time                  | Fixture schedule               |
| HomeTeam, AwayTeam          | Competing clubs                |
| Full Time / Half Time Goals | Scores for each side           |
| Shots, Shots on Target      | Team attacking metrics         |
| Fouls, Corners, Cards       | Discipline and set-piece stats |
| Referee                     | Match official                 |

2. `football_analysis.xlsx`

Team-level season summary including:

| Column                                    | Description                      |
| ----------------------------------------- | -------------------------------- |
| Rank, Squad                               | League table order and team name |
| Poss                                      | Average possession (%)           |
| Matches_Played, Win, Draw, Loss           | Season record                    |
| Goals_For, Goals_Against, Goal_Difference | Offensive & defensive output     |
| Points, Points/Match_Played               | League performance               |
| xG, xGA, xGD, xGD/90                      | Expected goals metrics           |

---

Methods & Process

1. Imported and cleaned both datasets using Pandas.
2. Created visualizations with Matplotlib and Seaborn.
3. Explored relationships between:

   * Possession and total points
   * Possession and goals scored/conceded
   * Expected vs actual goals (xG vs Goals)
   * Points per match, colored by possession percentage
4. Applied custom functions for reusable plotting:

   * `scatter_with_labels()` – for annotated scatter plots
   * `bar_chart_with_continuous_color()` – for gradient-colored bars

---

Visualizations

| Visualization                                 | Description                                                                 |
| --------------------------------------------- | --------------------------------------------------------------------------- |
| 1. Average Possession per Team                | Pie chart showing team dominance in possession (top 5 highlighted).         |
| 2. Possession vs Points                       | Positive trend — teams with higher possession tend to earn more points.     |
| 3. Possession vs Goals Scored                 | Moderate correlation — attacking strength linked to control of play.        |
| 4. Possession vs Goals Conceded               | Negative correlation — higher possession teams usually concede fewer goals. |
| 5. xG vs Actual Goals                         | Demonstrates efficiency in finishing chances.                               |
| 6. xGA vs Goals Conceded                      | Highlights defensive performance relative to expected goals against.        |
| 7. Possession vs xGD                          | Shows how ball control affects expected goal difference.                    |
| 8. Points per Match (Colored by Possession)   | Horizontal bar chart ranking teams — color intensity reflects possession.   |

---

Key Insights

* Clubs like Manchester City, Arsenal, and Liverpool combine high possession with low goals conceded, reflecting dominant tactical control.
* Tottenham Hotspur and Manchester United have high possession but underperform relative to it — indicating inefficiency in converting dominance into results.
* Teams such as Brentford, Nottingham Forest, and Crystal Palace adopt more counter-attacking styles, thriving with less possession.
* Clear trend: possession positively correlates with success, but efficiency and defensive structure remain decisive.

---

Project Learnings

* Data cleaning and preprocessing of real-world football data using Pandas.
* Advanced Matplotlib & Seaborn visualization design (annotations, regression, color gradients).
* Statistical interpretation of sports data for performance evaluation.
* Storytelling through analytics — transforming raw stats into tactical insights.

---

Deliverables

| File                           | Description                           |
| ------------------------------ | ------------------------------------- |
| `football_analysis.xlsx`       | Season summary data                   |
| `football_data_games.xlsx`     | Individual match data                 |
| `football_analysis_project.py` | Full Python analysis script           |
| `charts/`                      | Folder containing all generated plots |
| `README.md`                    | Documentation and summary (this file) |

---

Summary

Project 1 – Premier League 2024/25 Football Analysis (Python)

A comprehensive Python-based analysis of the 2024/25 Premier League season.
Explored how possession, xG, and goals interrelate to overall team success.
Demonstrated proficiency in data manipulation, visualization, and analytical storytelling.

Skills demonstrated:
`Python`, `Pandas`, `Matplotlib`, `Seaborn`, `Sports Analytics`, `Data Visualization`, `Analytical Storytelling`

---

Would you like me to also create a portfolio layout guide next — showing how to combine Project 1, 2, and 4 into one polished portfolio (with folder structure and display ideas for Power BI, Excel, and Python)?
