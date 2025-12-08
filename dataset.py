import pandas as pd
import numpy as np

"""
    DS 5010
    Fall 2025
    Project - Dataset Module
    David Cuellar
"""

class CareerPlayerStats:
    """
    This class will standardize a single player's career stats over the course of 
    their NBA career into a dataframe using the pandas and math package.
    """

    # The standardized columns
    MY_COLUMNS = [
        "SEASON", "TEAM", "MP", "PTS", "AST", "REB", 
        "STL", "BLK", "TOV", "FG%", "3P%", "FT%"
        ]
    
    # Common column headers that could be found in other CSV files
    COLUMN_ALIASES = {
        "YEAR" : "SEASON",
        "BY YEAR" : "SEASON",
        "MIN": "MP",
        "TRB": "REB",
        "RB": "REB",
    }

    # Initializes class using df and player_name provided by user 
    def __init__(self, df, player_name=None):
        self.df = df
        self.player_name = player_name

    # The class method decorator allows this method to access
    # other class methods and attributes
    @classmethod
    def from_csv(cls, path, player_name=None):
        """
        This method reads a CSV file for a single player's career
        and return a standardized CareerPlayerStats instance
        """
        df = pd.read_csv(path)
        
        # Making column names strings and uppercase
        new_columns = []
        for column in df.columns:
            new_columns.append(str(column).upper())
        df.columns = new_columns

        # Checking if aliases are found in df, and then renaming them
        # to the standardized version
        renamed_columns = []
        for column in df.columns:
            if column in cls.COLUMN_ALIASES:
                renamed_columns.append(cls.COLUMN_ALIASES[column])
            else:
                renamed_columns.append(column)
        df.columns = renamed_columns

        # Checking to see if we have the SEASON column
        if "SEASON" not in df.columns:
            raise ValueError("Input CSV must have a SEASON column")
        
        # Keeping and ordering the standardized columns
        standard_columns = []
        for column in cls.MY_COLUMNS:
            if column in df.columns:
                standard_columns.append(column)
        df = df[standard_columns]

        # Ensuring values are floats and rounded to 2 decimal places
        for column in df.columns:
            if column not in ["SEASON", "TEAM"]:
                df[column] = pd.to_numeric(df[column], errors="coerce")
                df[column] = df[column].round(2)

        # Replacing error/missing values with NaN
        df.replace(["", "NA", "N/A", "null", "None"], np.nan, inplace=True)

        # Returning a standardized class 
        return cls(df=df, player_name=player_name)
    
    def available_stats(self):
        """
        This method returns a list of stat columns excluding the SEASON
        and TEAM columns.
        """  
        stats = []
        for column in self.df.columns:
            if column not in ["SEASON", "TEAM"]:
                stats.append(column)
        return stats

    def get_stat_season(self, stat):
        """
        This method returns a dataframe with the SEASON and stat columns
        for the given stat.
        """
        if stat not in self.df.columns:
            raise ValueError(f"Stat: {stat}, not found")
        return self.df[["SEASON", stat]].copy()

    def copy_df(self):
        """
        This method returns a copy of the initialized dataframe
        """
        return self.df.copy()

class SeasonPlayerStats:
    """
    This class will standardize a single season players stats
    into a dataframe where each row will represent a player.
    """
    # The standardized columns
    MY_COLUMNS = [
        "PLAYER", "MP", "PTS", "AST", "REB", 
        "STL", "BLK", "TOV", "FG%", "3P%", "FT%"
        ]
    
    # Common column headers that could be found in other CSV files
    COLUMN_ALIASES = {
        "MIN": "MP",
        "TRB": "REB",
        "RB": "REB",
    }

    # Initializes class using df and season_label provided by user
    def __init__(self, df, season_label=None):
        self.df = df
        self.season_label = season_label

    # The class method decorator allows this method to access
    # other class methods and attributes
    @classmethod
    def from_csv(cls, path, season_label=None):
        """
        This method reads a CSV file that has all active player's stats from
        the league for that specific season and returns a standardized 
        SeasonPlayerStats instance
        """
        df = pd.read_csv(path)
        
        # Making column names strings and uppercase
        new_columns = []
        for column in df.columns:
            new_columns.append(str(column).upper())
        df.columns = new_columns

        # Checking if aliases are found in df, and then renaming them
        # to the standardized version
        renamed_columns = []
        for column in df.columns:
            if column in cls.COLUMN_ALIASES:
                renamed_columns.append(cls.COLUMN_ALIASES[column])
            else:
                renamed_columns.append(column)
        df.columns = renamed_columns

        # Checking to see if we have the PLAYER column
        if "PLAYER" not in df.columns:
            raise ValueError("Input CSV must have a PLAYER column")
        
        # Keeping and ordering the standardized columns
        standard_columns = []
        for column in cls.MY_COLUMNS:
            if column in df.columns:
                standard_columns.append(column)
        df = df[standard_columns]

        # Ensuring values are floats and rounded to 2 decimal places
        for column in df.columns:
            if column != "PLAYER":
                df[column] = pd.to_numeric(df[column], errors="coerce")
                df[column] = df[column].round(2)

        # Replacing error/missing values with NaN
        df.replace(["", "NA", "N/A", "null", "None"], np.nan, inplace=True)

        # Returning a standardized class 
        return cls(df=df, season_label=season_label)
    
    def available_stats(self):
        """
        This method returns a list of stat columns excluding the
        PLAYER column.
        """  
        stats = []
        for column in self.df.columns:
            if column != "PLAYER":
                stats.append(column)
        return stats

    def list_players(self):
        """
        This method returns a sorted list of all player names in this season
        """
        sorted_players = sorted(self.df["PLAYER"].tolist())
        return sorted_players

    def two_players_comp(self, player1, player2):
        """
        This method returns a new dataframe comparing two player's stats
        """
        players = [player1, player2]

        # Checking that both players exist
        missing_players = []
        for name in players:
            if name not in self.df["PLAYER"].values:
                missing_players.append(name)
        if missing_players: # empty list will evaluate to false
            raise ValueError(f"A player wasn't found in this season data: {missing_players}")

        # Creating new dataframe comparing both players
        new_dataframe = self.df[self.df["PLAYER"].isin(players)].copy()
        return new_dataframe

    def copy_df(self):
        """
        This method returns a copy of the initialized dataframe
        """
        return self.df.copy()