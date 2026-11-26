class Fighter:
    def __init__(self, name: str, health: int, damage_per_attack: int):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Ім'я бійця має бути непорожнім рядком")
        self.__name = name
        self.set_health(health)
        self.set_damage(damage_per_attack)
        print(f"Створено бійця: {self.__name}")

    def __del__(self):
        print(f"Бійця {self.__name} знищено")

    def get_name(self) -> str:
        return self.__name

    def get_health(self) -> int:
        return self.__health

    def get_damage(self) -> int:
        return self.__damage_per_attack

    def set_health(self, health: int):
        if not isinstance(health, int) or isinstance(health, bool) or health < 0:
            raise ValueError("Здоров'я має бути цілим невід'ємним числом (>= 0)")
        self.__health = health

    def set_damage(self, damage: int):
        if not isinstance(damage, int) or isinstance(damage, bool) or damage <= 0:
            raise ValueError("Урон має бути цілим додатним числом (> 0)")
        self.__damage_per_attack = damage

    def is_alive(self) -> bool:
        return self.__health > 0

    def take_damage(self, damage: int):
        if not isinstance(damage, int) or isinstance(damage, bool) or damage < 0:
            raise ValueError("Отримана шкода має бути цілим невід'ємним числом (>= 0)")
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0

    def info(self):
        print(f"Ім'я: {self.__name}, Здоров'я: {self.__health}, Урон: {self.__damage_per_attack}")


class Fight:
    def __init__(self, fighter1: Fighter, fighter2: Fighter):
        if not isinstance(fighter1, Fighter) or not isinstance(fighter2, Fighter):
            raise TypeError("Обидва учасники бою мають бути об'єктами класу Fighter")
        self.__fighter1 = fighter1
        self.__fighter2 = fighter2
        print(f"\nБій між {fighter1.get_name()} та {fighter2.get_name()} розпочато!")

    def __del__(self):
        print("Бій завершено і об'єкт Fight знищено")

    def get_winner(self) -> str:
        f1 = self.__fighter1
        f2 = self.__fighter2

        print("\n--- Початок бою ---")
        f1.info()
        f2.info()
        print()

        turn = 0

        while f1.is_alive() and f2.is_alive():
            if turn == 0:
                damage = f1.get_damage()
                f2.take_damage(damage)
                print(f"{f1.get_name()} атакує {f2.get_name()} на {damage} шкоди. "
                      f"Здоров'я {f2.get_name()}: {f2.get_health()}")
            else:
                damage = f2.get_damage()
                f1.take_damage(damage)
                print(f"{f2.get_name()} атакує {f1.get_name()} на {damage} шкоди. "
                      f"Здоров'я {f1.get_name()}: {f1.get_health()}")

            turn = 1 - turn

        print("\n--- Кінець бою ---")

        if f1.is_alive():
            winner = f1.get_name()
        else:
            winner = f2.get_name()

        print(f"Переможець: {winner}")
        return winner


def main():
    hero = Fighter("Артур", 100, 25)
    enemy = Fighter("Мордред", 90, 30)

    print("\nІнформація про бійців перед боєм:")
    hero.info()
    enemy.info()

    battle = Fight(hero, enemy)
    winner_name = battle.get_winner()
    print(f"\nРезультат бою: переміг {winner_name}")

    print("\n" + "="*50)
    print("Другий бій")

    warrior = Fighter("Спартак", 120, 20)
    gladiator = Fighter("Максимус", 110, 22)

    fight2 = Fight(warrior, gladiator)
    winner2 = fight2.get_winner()
    print(f"\nРезультат другого бою: переміг {winner2}")


if __name__ == "__main__":
    main()