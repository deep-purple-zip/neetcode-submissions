class Pet:
    """Represent a pet with a name and species."""

    def __init__(self, name: str, species: str) -> None:
        """
        Initialize a Pet instance.

        Parameters
        ----------
        name : str
            The name of the pet.
        species : str
            The species of the pet.
        """
        self.name = name
        self.species = species


# Do not modify below this line
my_pet = Pet("Fluffy", "cat")
print(f"My pet is a {my_pet.species} named {my_pet.name}")
