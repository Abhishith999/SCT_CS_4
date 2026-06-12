import tkinter as tk
import logging

def setup_logger() -> None:
    """Configures the logger to save tracked keys to a file."""
    logging.basicConfig(
        filename="key_tracker.log", 
        level=logging.INFO, 
        format="%(asctime)s - KEY PRESSED: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

def on_key_press(event) -> None:
    """
    This is the Listener Function. 
    Every time a key is pressed while the window is active, this catches it.
    """
    key_pressed = event.keysym
    
    # Log the key to our file
    logging.info(f"[{key_pressed}]")
    
    # Print it to the terminal so you can see it working
    print(f"Tracked key: {key_pressed}")

def main() -> None:
    # 1. Start the logger
    setup_logger()
    print("--- Safe Key Tracker Started ---")
    print("A window will open. Click on the window and start typing.")
    print("Close the window to stop tracking.")
    
    # 2. Create the application window
    root = tk.Tk()
    root.title("SkillCraft Key Tracker")
    root.geometry("400x200") # Width x Height
    
    # Add an instruction label
    instruction = tk.Label(
        root, 
        text="Click here and start typing to track keys.\nLogs are saved to 'key_tracker.log'", 
        font=("Arial", 12)
    )
    instruction.pack(expand=True)
    
    # 3. Bind the keyboard to the listener function
    root.bind("<Key>", on_key_press)
    
    # 4. Keep the window running
    root.mainloop()
    
    print("\nTracker closed. Check 'key_tracker.log' for the results!")

if __name__ == "__main__":
    main()