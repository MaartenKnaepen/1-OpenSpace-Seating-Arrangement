
# OpenSpace Organizer

Welcome to the OpenSpace Seating Arrangement tool! This Python application helps you organize and display seating arrangements for an open space, allowing customization based on the number of seats per table, whether individuals can sit alone, and dynamically accommodating latecomers.

## Installation

Clone the repository to your local machine:

```
git clone https://github.com/your-username/OpenSpace-Seating.git
```
## 1. Prepare Names File

Before using the tool, you need to create a CSV file containing a list of names. Each name should be on a separate line in the file. The tool will read this file to assign seats. There is a sample file colleagues.csv to try the application.

## 2. Run the Application

Run the application by executing the main.py script:

```
python main.py
```
## 3. Input Parameters

The application will prompt you for the following information:

Provide the file path.

How many people can you fit in this room? 

Enter the maximum capacity of the room.

Number of Seats per Table: Enter the desired number of seats per table.

Allow Individuals to Sit Alone: Enter yes or no.


## 4. View and Store Seating Arrangement
After providing the input parameters, the application will:

Close if the amount of seats needed exceeds the capacity of the room

Organize the seating arrangement.

Display the seating arrangement in the console.

Store the seating arrangement in an Excel file named seatings.xlsx.

Afterwards you get an opportunity to add latecomers. Note that latecomers will be placed at a new table if all tables are full. Even if the option to not have people sit alone was selected. This is a feature since we don't want the latecomers to bother the people who arrived on time.

After each time an arrangement is generated, the user will be informed about the number of occupied and remaining seats.

Example
Here's an example of how to use the tool:
```
How many people can you fit in this room? 30
Please provide the path of the file with the names: colleagues.csv
How many seats per table? 4
If you want people to sit alone type yes, if not, type no: yes

A dataframe will be generated and saved.

Add the name of 1 person who is late:\n If there is nobody to add enter nobody: Sam
Add the name of 1 person who is late:\n If there is nobody to add enter nobody: ' nobody

```
This example specifies that each table should have 4 seats, and individuals are allowed to sit alone. The tool will then organize, display, and store the seating arrangement.
