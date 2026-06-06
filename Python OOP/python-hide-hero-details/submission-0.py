class SuperHero:
    MAX_HEALTH: int = 100
    MIN_HEALTH: int = 0
    MAX_POWER_LEVEL: int = 10
    MIN_POWER_LEVEL: int = 1

    def __init__(self, name: str, health: int, power_level: int):
        self.name = name
        self._health = health
        self._power_level = power_level
    
    def get_health(self) -> int:
        return self._health

    def get_power_level(self) -> int:
        return self._power_level

    def get_name(self) -> str:
        return self.name

    def set_health(self, health: int) -> None:
        if health > self.MAX_HEALTH:
            print(
                "You can't set the health to more than "
                f"{self.MAX_HEALTH}"
            )
        elif health < self.MIN_HEALTH:
            print(
                "You can't set the health to less than "
                f"{self.MIN_HEALTH}"
            )
        else:
            self._health = health

    def set_power_level(self, power_level: int) -> None:
        if power_level > self.MAX_POWER_LEVEL:
            print(
                "You can't set the power level to more than "
                f"{self.MAX_POWER_LEVEL}"
            )
        elif power_level < self.MIN_POWER_LEVEL:
            print(
                "You can't set the power level to less than "
                f"{self.MIN_POWER_LEVEL}"
            )
        else:
            self._power_level = power_level


super_hero = SuperHero("Batman", 80, 9)

print(super_hero.get_health()) # this should print 80
super_hero.set_health(110) # this should print You can't set the health to more than 100
super_hero.set_health(-10) # this should print You can't set the health to less than 100
super_hero.set_health(70)

print(super_hero.get_power_level()) # this should print 9
super_hero.set_power_level(11) # this should print You can't set the power level to more than 10
super_hero.set_power_level(0) # this should print You can't set the power level to less than 1
super_hero.set_power_level(7)



# TODO: print the hero's attributes
print(
    f"{super_hero.get_name()} has {super_hero.get_health()} health and"
    f" {super_hero.get_power_level()} power level"
)