import logging

def setup_logger() -> None:
    """
    Configures the application logger.
    Saves all logs to a file and formats them professionally with a timestamp.
    """
    logging.basicConfig(
        filename="my_application.log", 
        level=logging.DEBUG, # Captures EVERYTHING from DEBUG all the way up to CRITICAL
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S" # Adds a clean date/time format
    )

def division_calculator() -> None:
    """A safe division calculator that logs all user interactions and errors."""
    
    # INFO: Normal application behavior
    logging.info("Application started. User entered the division calculator.")
    print("--------- Professional Division Calculator ---------")
    
    try:
        # DEBUG: Great for seeing the raw data exactly as it was typed
        a_input = input("Enter number 'a': ")
        logging.debug(f"Raw input for 'a': '{a_input}'")
        a = float(a_input) # We use float instead of int to allow decimals!
        
        b_input = input("Enter number 'b': ")
        logging.debug(f"Raw input for 'b': '{b_input}'")
        b = float(b_input)
        
    except ValueError:
        # WARNING: The user did something wrong (typed text instead of numbers), 
        # but we caught it, so the program doesn't completely crash.
        print("❌ Invalid input! Please enter numbers only.")
        logging.warning("User entered non-numeric data. Calculation aborted.")
        return

    # ERROR: A specific rule was violated
    if b == 0:
        print("❌ Error: Cannot divide by zero.")
        logging.error(f"Attempted division by zero (a={a}). Operation aborted.")
        return

    # If we made it this far, do the math!
    try:
        result = a / b
        print(f"✅ Result: {a} / {b} = {result}")
        
        # INFO: Recording a successful operation
        logging.info(f"Successful calculation: {a} / {b} = {result}")
        
    except Exception as e:
        # CRITICAL: A catch-all for massive, unexpected crashes
        print("💥 A critical system error occurred!")
        logging.critical(f"Unexpected crash during calculation: {e}", exc_info=True)

def main() -> None:
    # 1. Start the logger
    setup_logger()
    
    # 2. Run the application
    division_calculator()
    
    # 3. Log that the app is closing, adding a visual divider line in the log file
    logging.info("Application closed.\n" + "-"*50)
    print("\n📝 Log saved to 'my_application.log'. Open it in a text editor to see the results!")

if __name__ == "__main__":
    main()