OpenSpace Seating Arrangement
This is a tool that arranges seating in an openspace. It was created as the first project during my AI and data science course at BeCode Brussels.

Installation
Clone the repository to your local computer:

bash
Copy code
git clone https://github.com/your-username/OpenSpace-Seating.git

Usage
1. Prepare Names File
Before using the tool, you need to create a CSV file containing a list of names. Each name should be on a separate line in the file. The tool will read this file to assign seats. A sample file called "colleagues.csv" is included.

2. Run the Application
Run the application by executing the main.py script:

bash
Copy code
python main.py
3. Input Parameters
The application will prompt you for the following information:

Number of Seats per Table: Enter the desired number of seats per table.

Allow Individuals to Sit Alone: Enter yes for True or no for False. 

4. View and Store Seating Arrangement
After providing the input parameters, the application will:

Organize the seating arrangement.
Display the seating arrangement in the console.
Store the seating arrangement in an Excel file named seatings.xlsx.
Example
Here's an example of how to use the tool:

bash
Copy code
How many seats per table? 4
Can people sit alone? (yes=True, no=False) yes
This example specifies that each table should have 4 seats, and individuals are allowed to sit alone. The tool will then organize, display, and store the seating arrangement.
