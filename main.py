import pet
import time

# Loading animation

def loading(action, petName=""):
    print(f"{petName} is {action}ing", end="")
    for _ in range(3):
        print(".", end="")
        time.sleep(0.5)
    print("")

# Introduction
print("==============================================")
print("🎮 Welcome to the Pet Simulator!")
print("Create a pet, care for it, and teach it tricks!")
print("==============================================")
name = input("Enter your pet's name: ")
species = input("What kind of pet is it? (e.g., Dog, Cat, Dragon): ")
userPet = pet.Pet(name, species)

print("==============================================")
print(f"🎉 You have adopted a {species} named {userPet.name}!")

# Menu loop
while True:
    print("\n==============================================")
    print("What would you like to do?")
    print("1. 🍗 Feed")
    print("2. 🎾 Play")
    print("3. ✍️  Teach a Trick")
    print("4. 📊 Check Status")
    print("5. 😴 Sleep")
    print("6. 🧼 Give a Bath")
    print("7. 🎓 Show Tricks")
    print("8. 🚪 Exit")
    print("==============================================")

    try:
        userChoice = int(input("Choose (1-8): "))
        if userChoice < 1 or userChoice > 8:
            raise ValueError
    except ValueError:
        print("❌ Invalid input. Please choose a number between 1 and 8.")
        continue

    if userChoice == 1:
        loading("feed", userPet.name)
        userPet.eat()
    elif userChoice == 2:
        loading("play", userPet.name)
        userPet.play()
    elif userChoice == 3:
        trick = input("🧠 Enter a trick to teach: ")
        if not trick.isalpha() or len(trick) < 3 or len(trick) > 20:
            print("❗ Trick must be 3-20 letters.")
            continue
        loading("teach", userPet.name)
        userPet.train(trick)
    elif userChoice == 4:
        userPet.get_status()
    elif userChoice == 5:
        loading("sleep", userPet.name)
        userPet.sleep()
    elif userChoice == 6:
        loading("bath", userPet.name)
        userPet.bath()
    elif userChoice == 7:
        userPet.show_tricks()
    elif userChoice == 8:
        print(f"👋 Bye-bye from {userPet.name} the {userPet.species}!")
        break

print("Exiting the Pet Simulator", end="")
for _ in range(3):
    print(".", end="")
    time.sleep(1)
print(" Done!")
