# DS 5010 Project

## Purpose of package:

The purpose of this package is to simplify the process of importing, cleaning, standardizing, and visualizing basketball data. The goal is to bridge data science techniques with sports analytics by enabling users to quickly organize basketball statistics and produce clear visualizations of key performance metrics.

## How the package is organized:

### **1. Dataset Module (`dataset.py`)**

Contains two classes:

#### **`CareerPlayerStats`**

This class is meant to be used with one player's career per-game statistics. 
Key functionality: 
- Loads and standardizes a player's career CSV 
- Maps common column names - Returns lists of available stats 
- Extracts the values of a single stat across the player's career 
- Returns a copy of the original dataframe

#### **`SeasonPlayerStats`**

This class is mean to be used for all players in a single NBA season (per-game stats). 
Key functionality: 
- Loads and standardizes a season-wide CSV 
- Lists all players in the season 
- Returns lists of available stats 
- Returns a dataframe comparing two selected players 
- Returns a copy of the original dataframe

(***Both classes rely on pandas and numpy***)

### **2. Visualization Module (`visualization.py`)**

This module contains 2 helper functions and 2 plotting functions:

#### **`prep_career_stats`** helper function

-   Extracts seasons and values for a single statistic across a player's career

#### **`prep_two_player_stats`** helper function

-   Returns the available per-game stats for two players from a single season

#### **`plot_career_stat_line`** visualization function

-   Examples provided below

#### **`plot_two_player_bar`** visualization function

-   Examples provided below

(***Both visualzation functions use matplotlib***)

## Additional Notes:
- CSV files must contain a "SEASON" column (career stats) or a "PLAYER" column (season stats)
- Missing values are standardized using NaN

## Examples:
### **Loading a player's career stats**:
```
from dataset import CareerPlayerStats

career = CareerPlayerStats.from_csv("lebron_careerplayerstats.csv", "LeBron James")

print(career.available_stats())
print(career.get_stat_season("PTS"))
```

### **Loading a season's player stats and comparing two players**:
```
from dataset import SeasonPlayerStats

season = SeasonPlayerStats.from_csv("2024_25_season_playerstats.csv", "2024-25")

comparison_df = season.two_players_comp("LeBron James", "Stephen Curry")
print(comparison_df)
```
### **Visualizing the stat line trend**:
```
from visualization import plot_career_stat_line
import matplotlib.pyplot as plt

fig, ax = plot_career_stat_line(career, "PTS")
plt.show()
```

### **Visualizing a two-player comparison**:
```
from visualization import plot_two_player_bar
import matplotlib.pyplot as plt

fig, ax = plot_two_player_bar(season, "LeBron James", "Stephen Curry")
plt.show()
```