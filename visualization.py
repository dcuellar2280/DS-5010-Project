from dataset import CareerPlayerStats, SeasonPlayerStats
import matplotlib.pyplot as plt
import numpy as np

"""
    DS 5010
    Fall 2025
    Project - Visualization Module
    David Cuellar
"""

def prep_career_stats(career, stat):
    """
    This function returns a tuple for a singluar stat over a 
    player's career
    - Use CareerPlayerStats class for this function

    Parameters: 1) career (CareerPlayerStats instance)
                2) stat (name of the stat as a string)
    """
    df = career.get_stat_season(stat)
    seasons = df["SEASON"].tolist()
    values = df[stat].tolist()
    
    return (seasons, values)

def prep_two_player_stats(season_stats, player1, player2):
    """
    This function returns a tuple comparing player 1 and player 2 
    per-game stats in a single season.
    - Use SeasonPlayerStats class for this function
    
    Parameters: 1) season_stats (SeasonPlayerStats instance)
                2) player1 (string)
                3) player2 (string)
    """
    df = season_stats.two_players_comp(player1, player2)

    # Using all available stats from the SeasonPlayerStats class
    stats = season_stats.available_stats()

    # Indexing by "PLAYER" to locate players' individual stats  
    df_index = df.set_index("PLAYER")
    player1_values = df_index.loc[player1, stats].tolist()
    player2_values = df_index.loc[player2, stats].tolist()

    return (stats, player1_values, player2_values)

def plot_career_stat_line(career, stat):
    """
    This function plots a line chart of a player's stat over all 
    the seasons they participated in their career
    - Use CareerPlayerStats class for this function
    """
    seasons, values = prep_career_stats(career, stat)

    # Using x variable to organize the ticks
    x = np.arange(len(seasons))
    fig, ax = plt.subplots(figsize=(8, 4))

    # Plotting line with markers
    ax.plot(x, values, marker="o", linestyle="-")

    # Setting axis labels
    ax.set_xlabel("SEASON")
    ax.set_ylabel(f"{stat} per game")

    # Checking to see if player_name is available 
    # to set up a title for the graph
    if career.player_name:
        ax.set_title(f"{career.player_name} {stat} over seasons")
    else:
        ax.set_title(f"{stat} over seasons")

    # Setting and rotating x-axis labels
    ax.set_xticks(x)
    ax.set_xticklabels(seasons, rotation=45, ha="right")

    # Adding a grid to the graph
    ax.grid(True, which="major", linestyle="--", alpha=0.5)

    return fig, ax

# -----------------------------------------------------------------------------

def plot_two_player_bar(season_stats, player1, player2):
    """
    This function plots the side-by-side bar chart comparing 
    all available stats from two players from a single season
    - Use SeasonPlayerStats class for this function
    """
    stats, values1, values2 = prep_two_player_stats(
        season_stats, player1, player2)

    fig, ax = plt.subplots(figsize=(10, 5))

    # Variable to help position and size the bars
    x = np.arange(len(stats))
    width = 0.35  

    # Creating the bars
    ax.bar(x - width / 2, values1, width, label=player1)
    ax.bar(x + width / 2, values2, width, label=player2)

    # Labeling the bar graph
    ax.set_xlabel("Statistic")
    ax.set_ylabel("Per-Game Value")
    season_label = getattr(season_stats, "season_label", None)

    # Setting the season label to the graph
    if season_label:
        ax.set_title(f"{player1} vs. {player2} - Season: {season_label}")
    else:
        ax.set_title(f"{player1} vs. {player2}")

    # Adding ticks and labels 
    ax.set_xticks(x)
    ax.set_xticklabels(stats, rotation=45, ha="right")

    # Adding a legend and grid
    ax.legend()
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    return fig, ax

"""
def main():
    # Line Plot example
    career = CareerPlayerStats.from_csv(
        "../lebron_careerplayerstats.csv"
    )
    print("Career dataframe (head):")
    print(career.df.head())
    print("\n")
    print("Available career stats:", career.available_stats())

    fig1, ax1 = plot_career_stat_line(career, "PTS")
    plt.show()  

    # ------------------------------------------------------------

    # Bar Chart example
    season_stats = SeasonPlayerStats.from_csv(
        "../seasonplayerstats_24-25.csv"
    , "2024-25")

    print("\n")
    print("Season dataframe (head):")
    print(season_stats.df.head())

    print("\n")
    print("Available season stats:", season_stats.available_stats())

    player1 = "LeBron James"
    player2 = "Stephen Curry"

    fig2, ax2 = plot_two_player_bar(season_stats, player1, player2)
    plt.show()  

if __name__ == "__main__":
    main()
"""