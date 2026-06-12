# Professional Division Calculator with Logging

## Overview

This project is a Python-based division calculator designed with professional logging and exception handling practices.
The application safely performs division operations while recording all important events, errors, and user interactions into a log file.

The project demonstrates:

* Logging in Python
* Exception handling
* Input validation
* File-based log management
* Debugging practices used in real-world applications

---

## Features

* Accepts decimal and integer inputs
* Prevents crashes using exception handling
* Detects invalid user input
* Handles division-by-zero safely
* Stores logs with timestamps
* Uses multiple logging levels:

  * DEBUG
  * INFO
  * WARNING
  * ERROR
  * CRITICAL

---

## Technologies Used

* Python 3
* Built-in `logging` module

---

## Project Structure

```bash
project/
│
├── keylogger.py
├── my_application.log
└── README.md
```

---

## Logging Levels Used

| Level    | Purpose                        |
| -------- | ------------------------------ |
| DEBUG    | Stores raw user input          |
| INFO     | Tracks normal application flow |
| WARNING  | Logs invalid user actions      |
| ERROR    | Logs division by zero          |
| CRITICAL | Logs unexpected crashes        |

---

## Example Log Output

```text
2026-06-12 20:15:01 - INFO - Application started.
2026-06-12 20:15:05 - DEBUG - Raw input for 'a': '10'
2026-06-12 20:15:08 - DEBUG - Raw input for 'b': '2'
2026-06-12 20:15:08 - INFO - Successful calculation: 10 / 2 = 5.0
```

---

## Concepts Learned

* Python logging configuration
* Error handling using try-except
* Safe user input validation
* Professional debugging techniques
* Writing structured application logs

---

## Future Improvements

* Add support for more mathematical operations
* Create a GUI version
* Export logs to CSV
* Add colored terminal output
* Implement user authentication

---

## Educational Purpose

This project was developed for learning and internship practice purposes to understand how professional applications manage logs, debugging, and runtime errors.
