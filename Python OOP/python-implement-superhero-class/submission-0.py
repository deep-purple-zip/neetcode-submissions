class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int) -> None:
        # TODO: Initialize the superhero's attributes here
        self.name = name
        self.power = power
        self.health = health


# TODO: Create Superhero instances
batman: SuperHero = SuperHero(name="Batman", power="Intelligence", health=100)
superman: SuperHero = SuperHero(name="Superman", power="Strength", health=150)

# TODO: Print out the attributes of each superhero
for super_hero in (batman, superman):
    print(super_hero.name)
    print(super_hero.power)
    print(super_hero.health)