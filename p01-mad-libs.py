while True:
    print("Welcome to Mad Libs! Please provide the following words:")
    name = input("Name: ")
    place = input("Place: ")
    verb = input("Verb: ")
    adjective = input("Adjective: ")
    animal = input("Animal: ")
    number = input("Number: ")
    print("\nHere's your Mad Libs story:\n")
    print(f"Once upon a time, {name} went to {place} and {verb} with a {adjective} {animal}. It was the best day ever, with {number} people watching!")

    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.strip().lower() != "yes":
        print("Thanks for playing Mad Libs! Goodbye!")
        break
