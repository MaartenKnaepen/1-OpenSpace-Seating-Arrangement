from src.table import Table
import math
import random
import pandas as pd
from src.utils import sublists  
from src.utils import to_dict
from src.utils import import_csv

# Collecting variables to make the code work
maxppl = int(input('How many people can you fit in this room?'))
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
        - lonely (str): Flag to show if someone can sit alone at a table or not.
        """
        self.numseats = numseats
        self.names = names
        self.lonely = lonely
        
        self.numtables = math.ceil(len(self.names) / self.numseats)
        self.maxppl = maxppl

        # Stop if the room's capacity is too low
        if self.maxppl < (len(self.names)):
            exit(f"This room's max capacity is only {self.maxppl}. Please reduce the number of people or find a bigger room")
                
        # Create a list of Table objects
        self.tablelist = [Table(self.numseats) for _ in range(self.numtables)]

        # Create a list of strings representing the names of each table for in the dataframe
        self.tablestrings = [f"Table {k+1}" for k in range(self.numtables)]


    def randomize(self):
        """
        Randomizes the input and divides into sublist based on nr of chairs per table
        """
        random.shuffle(names)
        self.names_per_table = sublists(names, self.numseats)
        return self.names_per_table
    
    def organize(self):
        """
        Assigns names to seats in each table based on the randomized order.
        """
        self.randomize()  # Call randomize to set self.names_per_table
        # Adjust numseats if lonely is False 
        if self.lonely == 'no':
            while len(self.names_per_table[-1]) == 1:
                self.numseats = self.numseats + 1
                self.names_per_table = sublists(self.names, self.numseats)
        for tbl, names in zip(self.tablelist, self.names_per_table):
            for name in names:
                tbl.assign_seat(name)
        return self.names_per_table

    def display(self):
        """
        Creates a Pandas DataFrame to display the seat assignments.
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
    def late(self, lt):
        """
        Add a latecomer to the seating arrangement. Add 1 by 1, new tables will be created automatically
        """
        self.lt = lt
        # Check if the latecomer's name is 'nobody'
        if self.lt == 'nobody':
            return'Nobody to add'

        # Update the seating arrangement with the latecomer
    
        self.names.append(lt)
        if self.maxppl < (len(self.names)):
            exit(f"This room's max capacity is only {self.maxppl}. Please reduce the number of people or find a bigger room")
        self.numtables = math.ceil(len(self.names) / self.numseats)
    
        # Create new tables based on the updated number of names
        self.tablelist = [Table(self.numseats) for _ in range(self.numtables)]
        self.tablestrings = [f"Table {k+1}" for k in range(self.numtables)]

        # Organize the updated names into sublists for each table
        self.names_per_table = sublists(self.names, self.numseats)

        # Assign seats to the latecomer in the existing tables
        for tbl, names in zip(self.tablelist, self.names_per_table):
            for name in names:
                tbl.assign_seat(name)

        # Display the updated seating arrangement
        self.display()
        print(self.df)

        # Store the updated seating arrangement
        self.store()

    def num_people(self):
        """
        Counts the number of people by checking the length of self.names
        """
        return f'{len(self.names)} people seated in this arrangement'
    
    def remaining_seats(self):
        '''
        Displays the room's capacity and calculates how many seats are remaining
        '''
        return f'You have a maximal capacity of {self.maxppl}. Currently {len(self.names)} are occupied. That means {self.maxppl - len(self.names)} are available.'
