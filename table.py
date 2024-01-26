class Table:
    """
    Represents a table with a specified capacity and associated seats.

    Methods:
    - has_free_spot: Checks if there is at least one available spot at the table.
    - assign_seat: Assigns a name to an available seat at the table.
    - capacity_left: Returns the number of available seats at the table.
    """
    def __init__(self, capacity):
        """
        Initializes a Table object with a specified capacity.
        """
        self.seats = [Seat() for i in range(capacity)]
        self.capacity = capacity

    def has_free_spot(self):
        """
        Checks if there is at least one available spot at the table.
        """
        if any(seat.is_free() for seat in self.seats):
            return 'There is at least 1 spot available at this table'
        else:
            return "This table is at maximum capacity"

    def assign_seat(self, name):
        """
        Assigns a name to an available seat at the table.
        """
        for seat in self.seats:
            if seat.is_free():
                seat.set_occupant(name)
                return f'{name} is now sitting on a seat!'
        return 'No available seats'

    def capacity_left(self):
        """
        Returns the number of available seats at the table.
        """
        return f"{sum(seat.is_free() for seat in self.seats)} seats left at this table"
    
    def __repr__(self) -> str:
        return f"This is a table"


class Seat:
    """
    Represents a seat at a table, with occupant information and availability status.
    
    - is_free: Checks if the seat is available.
    - set_occupant: Sets the occupant of the seat if it is free.
    - remove_occupant: Removes the occupant from the seat if the seat is occupied.
    """
    def __init__(self, occupant=None, free=True):
        """
        Initializes a Seat object with optional occupant and availability status.
        """
        self.occupant = occupant
        self.free = free

    def is_free(self):
        """
        Checks if the seat is available.
        """
        return self.free

    def set_occupant(self, name):
        """
        Sets the occupant on the seat if it is free.
        """
        if self.is_free():
            self.occupant = name
            self.free = False
            return f'{name} is now sitting on this seat'
        else:
            return f'This seat is already occupied by {self.occupant}'

    def remove_occupant(self, name):
        """
        Removes the occupant from the seat if the seat is occupied.
        """
        if not self.is_free() and self.occupant == name:
            self.free = True
            self.occupant = None
            return f'{name} was removed from this seat'
        else:
            return f'The seat is already free or not occupied by {name}'

    def __repr__(self) -> str:
        return f"This is a seat"
