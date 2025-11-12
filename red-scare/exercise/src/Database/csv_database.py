import pandas as pd
from pathlib import Path

class CSVDatabase:
    """
    Simple class to interact with a csv.
    """
    
    COLUMNS = ["filename", "None", "Some", "Many", "Few", "Alternate"]
    
    def __init__(self, filepath: str):
        self.filepath = Path(filepath)
        if not filepath.exists():
            raise FileNotFoundError(f"CSV file not found: {filepath}")

        self.df = pd.read_csv(filepath)
    
    def addEntry(self, filename:str, **kwargs):

        # Entry exists, update provided fields
        if filename in self.df["filename"].values:
            for key, value in kwargs.items():
                if key in self.COLUMNS:
                   self.df.loc[self.df["filename"] == filename, key] = value # select correct row ("filename" == filename) and column (key)
        # Entry does not exist, create new row
        else:
            new_row = {col: None for col in self.COLUMNS} #
            new_row["filename"] = filename
            for key, value in kwargs.items():
                if key in self.COLUMNS: # only try to add if argument actually is a column name  
                    new_row[key] = value
            
            # Append the new row to the df
            self.df.loc[len(self.df)] = new_row

        self.df.to_csv(self.filepath, index=False)