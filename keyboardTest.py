import keyboard as kb


def keysEvent(e):
    print(f"Key {e} pressed")
    if e == 'e':
        print("You pressed the 'e' key!")
        input("Press Enter to continue...")  # Wait for user input before continuing

kb.on_press(lambda e: keysEvent(e.name))  # Print the name of the key pressed
kb.wait('esc')  # Wait until 'esc' is pressed to exit the program