from src.table import Table
from src.table import Seat
import math
import random
import pandas as pd
from src.utils import sublists  
from src.utils import to_dict
from src.utils import import_csv

names = import_csv()

class OpenSpace:
    """
    Represents an open space arrangement with tables and seats.
    Allows for randomizing, organizing, displaying, and storing seat assignments.

    - randomize: Randomly shuffles the list of names and organizes them into sublists.
    - organize: Assigns names to seats in each table based on the randomized order.
    - display: Creates a Pandas DataFrame to display the seat assignments.
    - store: Saves the seat assignments to an Excel file.
    """
    def __init__(self, numseats, lonely):
        """
        Initializes an OpenSpace object.

        Parameters:
        - numseats (int): Number of seats per table.
        - lonely (bool): Flag to show if someone can sit alone at a table or not.
        """
        self.numseats = numseats
        self.lonely = lonely
        self.numtables = math.ceil(len(names) / self.numseats)

        # Warn if the number of tables is large
        if self.numtables > 6:
            print('Watch out, 7 or more tables might be too much for 1 room!')

        # Adjust numseats if lonely is False 
        if not self.lonely:
            while len(names) % self.numtables == 1:
                self.numseats += 1
            self.numtables = math.ceil(len(names) / self.numseats)

        # Create a list of Table objects
        self.tablelist = [Table(self.numseats) for _ in range(self.numtables)]

        # Create a list of strings representing the names of each table for in the dataframe
        self.tablestrings = [f"Table {k+1}" for k in range(self.numtables)]


    def randomize(self):
        """
        Randomly shuffles the list of names and organizes them into sublists.

        Returns:
        - list: List of sublists containing names.
        """
        random.shuffle(names)
        self.names_per_table = sublists(names, self.numseats)
        return self.names_per_table
    
    def organize(self):
        """
        Assigns names to seats in each table based on the randomized order.

        Returns:
        - list: List of sublists containing names assigned to each table.
        """
        self.randomize()  # Call randomize to set self.names_per_table
        for tbl, names in zip(self.tablelist, self.names_per_table):
            for name in names:
                tbl.assign_seat(name)
        return self.names_per_table

    def display(self):
        """
        Creates a Pandas DataFrame to display the seat assignments.

        Returns:
        - pandas.DataFrame: DataFrame representing the seat assignments.
        """
        self.table_names_dict = to_dict(self.tablestrings, self.names_per_table)
        self.df = pd.DataFrame.from_dict(self.table_names_dict)
        self.df.index = self.df.index + 1
        return self.df

    def store(self):
        """ 
        Saves the seat assignments to an Excel file named 'seatings.xlsx'.
        """
        self.df.to_excel('seatings.xlsx')