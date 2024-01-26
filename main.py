from src.openspace import OpenSpace

def main():
    """
    Main function to interactively create, organize, display, and store an OpenSpace arrangement.
    - Asks the user for the number of seats per table and whether people can sit alone.
    - Creates an OpenSpace object with the specified parameters.
    - Organizes the seat assignments, displays the arrangement, and stores it in an Excel file.
    """
    numseats = int(input('How many seats per table?'))
    lonely = str(input('If you want people to sit alone type yes, if not, type no: '))
    openspacetest = OpenSpace(numseats, lonely)
    openspacetest.organize()
    print(openspacetest.display())
    print(openspacetest.num_people())
    print(openspacetest.remaining_seats())
    openspacetest.store()
    late1 = None
    while late1 != 'nobody':
        late1 = str(input('Add the name of 1 person who is late:\n If there is nobody to add enter nobody: '))
        if len(late1) > 0:
            print(openspacetest.late(late1))
            print(openspacetest.num_people())
            print(openspacetest.remaining_seats())
if __name__ == "__main__":
    main()