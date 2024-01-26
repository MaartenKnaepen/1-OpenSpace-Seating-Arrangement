
from src.openspace import OpenSpace

def main():
    numseats = int(input('How many seats per table?'))
    lonely = bool(input('Can people sit alone? (yes=True, no=False)'))
    openspacetest = OpenSpace(numseats, lonely)
    openspacetest.organize()
    print(openspacetest.display())
    openspacetest.store()

if __name__ == "__main__":
    main()

