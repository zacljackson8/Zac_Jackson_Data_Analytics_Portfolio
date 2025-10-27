import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
import numpy as np

# ---------------- Settings ----------------
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_context("talk")

# ---------------- Load Data ----------------
file_path = "football_analysis.xlsx"
team_stats = pd.read_excel(file_path, sheet_name="Sheet2")

print("✅ Data Loaded Successfully")
print(team_stats.head())

# ---------------- PIE CHART: Average Possession per Team ----------------
team_possession_sorted = team_stats.sort_values(by='Poss', ascending=False)

plt.figure(figsize=(9, 9))

# Draw pie chart
wedges, texts, autotexts = plt.pie(
    team_possession_sorted['Poss'],
    labels=None,  # no labels for now
    autopct=lambda p: f'{p:.1f}%' if p > 4 else '',  # percentages >4%
    startangle=90,
    wedgeprops={'edgecolor': 'white'}
)

# Reduce percentage font size
for autotext in autotexts:
    autotext.set_fontsize(8)

# Add a legend for all teams
plt.legend(
    wedges,
    team_possession_sorted['Squad'],
    title="Teams",
    bbox_to_anchor=(1, 0.5),
    loc="center left"
)

# Annotate top 5 teams directly on slices
top5 = team_possession_sorted.head(5)
for i, (team, value) in enumerate(zip(top5['Squad'], top5['Poss'])):
    angle = (wedges[i].theta2 + wedges[i].theta1) / 2
    x = wedges[i].r * 1.15 * np.cos(angle * np.pi / 180)
    y = wedges[i].r * 1.15 * np.sin(angle * np.pi / 180)
    plt.text(x, y, f"{team}\n{value:.1f}%", ha='center', va='center',
             fontsize=9, weight='bold', color='black')

plt.title("Average Possession per Team – Premier League 2024/25", fontsize=14, pad=20)
plt.tight_layout()
plt.savefig("1_average_possession_per_team_2425.png", dpi=300)
plt.show()

# ---------------- FUNCTION: Annotated Bar Chart with Continuous Color ----------------
def bar_chart_with_continuous_color(df, x, y, color_col, 
                                    horizontal=False, 
                                    figsize=(10,6), 
                                    cmap='viridis',
                                    title=None,
                                    xlabel=None,
                                    ylabel=None,
                                    annotate=True,
                                    save_path=None,
                                    dpi=300):
    """
    Create a bar chart with bars colored by a numeric column and optional annotations.
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Normalize color values
    norm = mcolors.Normalize(vmin=df[color_col].min(), vmax=df[color_col].max())
    colors = plt.colormaps[cmap](norm(df[color_col]))
    
    # Plot bars
    if horizontal:
        bars = ax.barh(df[x], df[y], color=colors)
        if annotate:
            for bar in bars:
                ax.text(bar.get_width() + 0.02, bar.get_y() + bar.get_height()/2,
                        f'{bar.get_width():.2f}', va='center', fontsize=8)
    else:
        bars = ax.bar(df[x], df[y], color=colors)
        ax.set_xticks(range(len(df[x])))
        ax.set_xticklabels(df[x], rotation=45, ha='right')
        if annotate:
            for bar in bars:
                ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
                        f'{bar.get_height():.2f}', ha='center', fontsize=8)
    
    # Titles and labels
    if title: ax.set_title(title, fontsize=14)
    if xlabel: ax.set_xlabel(xlabel)
    if ylabel: ax.set_ylabel(ylabel)
    
    # Colorbar
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    fig.colorbar(sm, ax=ax, label=color_col)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=dpi)
    
    plt.show()


# ---------------- FUNCTION: Scatter Plot with Labels ----------------
def scatter_with_labels(df, x, y, color='blue', label_col='Squad', title=None, xlabel=None, ylabel=None, save_path=None):
    plt.figure(figsize=(8,6))
    sns.regplot(data=df, x=x, y=y, scatter_kws={'s':70, 'color':color})
    for i in range(len(df)):
        plt.text(df[x][i]+0.1, df[y][i]+0.1, df[label_col][i], fontsize=8)
    if title: plt.title(title)
    if xlabel: plt.xlabel(xlabel)
    if ylabel: plt.ylabel(ylabel)
    plt.tight_layout()
    if save_path: plt.savefig(save_path, dpi=300)
    plt.show()


# ---------------- Charts 1-6: Scatter Plots ----------------
scatter_with_labels(team_stats, 'Poss', 'Points', title="Possession vs Points – Premier League 2024/25",
                    xlabel="Average Possession (%)", ylabel="Total Points", save_path="2_possession_vs_points.png")

scatter_with_labels(team_stats, 'Poss', 'Goals_For', color='green', title="Possession vs Goals Scored – Premier League 2024/25",
                    xlabel="Average Possession (%)", ylabel="Goals Scored", save_path="3_possession_vs_goals_for.png")

scatter_with_labels(team_stats, 'Poss', 'Goals_Against', color='red', title="Possession vs Goals Conceded – Premier League 2024/25",
                    xlabel="Average Possession (%)", ylabel="Goals Conceded", save_path="4_possession_vs_goals_against.png")

scatter_with_labels(team_stats, 'xG', 'Goals_For', color='blue', title="xG vs Actual Goals – Premier League 2024/25",
                    xlabel="Expected Goals (xG)", ylabel="Actual Goals Scored", save_path="5_xg_vs_goals_for.png")

scatter_with_labels(team_stats, 'xGA', 'Goals_Against', color='orange', title="xGA vs Goals Conceded – Premier League 2024/25",
                    xlabel="Expected Goals Against (xGA)", ylabel="Actual Goals Conceded", save_path="6_xga_vs_goals_conceded.png")

# ---------------- Chart 7: Possession vs xGD ----------------
scatter_with_labels(team_stats, 'Poss', 'xGD', color='purple', title="Possession vs Expected Goal Difference – Premier League 2024/25",
                    xlabel="Average Possession (%)", ylabel="Expected Goal Difference (xGD)", save_path="7_possession_vs_xgd.png")

# ---------------- Chart 8: Points per Match (Horizontal Bar) ----------------
team_stats_sorted = team_stats.sort_values(by='Points/Match_Played', ascending=True)
bar_chart_with_continuous_color(team_stats_sorted, x='Squad', y='Points/Match_Played', color_col='Poss',
                                horizontal=True, title="Points per Match by Team (Color = Possession %) ",
                                xlabel="Points per Match", ylabel="Team", annotate=True,
                                save_path="8_points_per_match_colored_by_possession.png")

print("\n✅ All charts successfully generated and saved!\n")
