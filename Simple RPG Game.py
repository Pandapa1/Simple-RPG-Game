import random


class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, enemy):
        damage = random.randint(1, self.attack_power)
        enemy.health -= damage
        return damage

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self):
        self.player = None

    def choose_character(self):
        print("Choose your character:")
        print("1. Warrior (Health: 100, Attack: 15)")
        print("2. Mage (Health: 80, Attack: 20)")
        print("3. Archer (Health: 70, Attack: 25)")
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            self.player = Character("Warrior", 100, 15)
        elif choice == "2":
            self.player = Character("Mage", 80, 20)
        elif choice == "3":
            self.player = Character("Archer", 70, 25)
        else:
            print("Invalid choice!")
            self.choose_character()

    def start_battle(self):
        enemy = Character("Goblin", 50, 10)
        print(f"A wild {enemy.name} appears!")
        while self.player.is_alive() and enemy.is_alive():
            print(f"\nYour health: {self.player.health}, Enemy health: {enemy.health}")
            action = input("Choose action: (1) Attack (2) Run: ")
            if action == "1":
                damage = self.player.attack(enemy)
                print(f"You dealt {damage} damage!")
                if enemy.is_alive():
                    enemy_damage = enemy.attack(self.player)
                    print(f"The {enemy.name} dealt {enemy_damage} damage!")
            elif action == "2":
                print("You ran away!")
                break
            else:
                print("Invalid action!")

        if self.player.is_alive():
            print("You won!")
        else:
            print("You were defeated!")


# Usage Example
game = Game()
game.choose_character()
game.start_battle()
