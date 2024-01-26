
# OpenSpace Organizer

Welcome to the OpenSpace Seating Arrangement tool! This Python application helps you organize and display seating arrangements for an open space, allowing customization based on the number of seats per table and whether individuals can sit alone.

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

Number of Seats per Table: Enter the desired number of seats per table.

Allow Individuals to Sit Alone: Enter yes for True or no for False. This option determines whether individuals can sit alone at a table.

## 4. View and Store Seating Arrangement
After providing the input parameters, the application will:

Organize the seating arrangement.
Display the seating arrangement in the console.
Store the seating arrangement in an Excel file named seatings.xlsx.
Example
Here's an example of how to use the tool:
```
Please provide the path of the file with the names: colleagues.csv
How many seats per table? 4
Can people sit alone? (yes=True, no=False) yes
```
This example specifies that each table should have 4 seats, and individuals are allowed to sit alone. The tool will then organize, display, and store the seating arrangement.
