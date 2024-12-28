import pygame

# Function to take input and play a sound
def input_with_sound(prompt):
    user_input = input(prompt)  # Get user input

    if user_input == "sos":
        pygame.mixer.init()  # Initialize the mixer module
        pygame.mixer.music.load("path/to/your/sound/file")  # Load the sound file
        pygame.mixer.music.play(-1)  # Play the sound in a loop (-1 for infinite)

        while True:
            x = input("Pause?: ")
            if x.lower() == "yes":
                pygame.mixer.music.stop()  # Stop the sound
                break
            elif x.lower() == "no":
                continue
            else:
                print("Invalid input. Type 'yes' to stop or 'no' to continue.")
    else:
        print("Invalid input.")

# Example usage
input_with_sound("Enter something: ")
