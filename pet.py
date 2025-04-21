import time
import random

class Pet:
    def __init__(self, name, species="Dog"):
        # Initialize attributes
        self.name = name
        self.species = species
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        """Feed the pet: reduce hunger and increase happiness."""
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        time.sleep(1)
        food = random.choice(["🍖 bone", "🍗 chicken", "🍣 sushi", "🍌 banana"])
        print(f"{self.name} enjoyed a delicious {food}!")

    def sleep(self):
        """Let the pet sleep: increase energy."""
        self.energy = min(10, self.energy + 5)
        time.sleep(1)
        print(f"{self.name} is snoring peacefully 💤💤.")

    def play(self):
        """Play with the pet: reduce energy, increase happiness and hunger."""
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            toy = random.choice(["🧸 teddy", "🎾 ball", "🪁 kite"])
            time.sleep(1)
            print(f"You played with {self.name} using a {toy}. So fun!")
        else:
            print(f"{self.name} is too tired to play 😴.")

    def bath(self):
        """Give your pet a bath: refreshes mood."""
        self.happiness = min(10, self.happiness + 1)
        time.sleep(1)
        print(f"🛁 {self.name} is squeaky clean and smells amazing!")

    def train(self, trick):
        """Teach the pet a new trick."""
        if trick in self.tricks:
            print(f"{self.name} already knows '{trick}' 🤓.")
        else:
            self.tricks.append(trick)
            time.sleep(1)
            print(f"{self.name} learned a new trick: '{trick}' 🏅!")

    def show_tricks(self):
        """Display learned tricks."""
        if not self.tricks:
            print(f"{self.name} hasn't learned any tricks yet 😢.")
        else:
            print(f"\n{self.name}'s Tricks:")
            for i, trick in enumerate(self.tricks, 1):
                print(f"  {i}. 🐾 {trick}")

    def get_status(self):
        """Display pet's current status."""
        print(f"\n📋 {self.name} the {self.species}'s Status:")
        print(f"  🍽 Hunger: {self.hunger}/10")
        print(f"  ⚡ Energy: {self.energy}/10")
        print(f"  😺 Happiness: {self.happiness}/10")
        print(f"  🧠 Tricks: {', '.join(self.tricks) if self.tricks else 'None yet'}")
        time.sleep(1)
