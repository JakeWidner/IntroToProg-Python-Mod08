# Employee Performance Ratings Management System

This project is a Python application designed to manage employee performance ratings efficiently. It utilizes object-oriented programming (OOP) principles, ensuring a modular and maintainable codebase. The project is split into multiple Python modules, each responsible for handling a specific aspect of the application, from data management to user interaction.

Note: ChatGPT was used to generate this ReadMe. Edits were made.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
  - [data_classes.py](#data_classespy)
  - [processing_classes.py](#processing_classespy)
  - [presentation_classes.py](#presentation_classespy)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Employee Performance Ratings Management System is built to simplify the process of recording, storing, and retrieving employee performance data. By following a well-structured OOP approach, the system is both easy to extend and maintain.

## Features

- **Object-Oriented Design**: The application is designed with modularity and reusability in mind.
- **Data Persistence**: Employee data is stored in a JSON file, `EmployeeRatings.json`, ensuring that data is retained across sessions.
- **User Interaction**: The application provides a user-friendly command-line interface for managing employee ratings.
- **Automated Testing**: Unit tests are provided for each major component, ensuring reliability and robustness.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/JakeWidner/IntroToProg-Python-Mod08.git
   cd IntroToProg-Python-Mod08
2. **Install Dependencies**:
   Ensure you have Python installed. If not, download and install Python from [here](https://www.python.org/downloads/).

3. **Run the Application**:
   ```bash
   python main.py
   
## Usage

The program starts with a welcome message and then presents a menu with options to:
1. Add a new employee rating.
2. View all employee ratings.
3. Save ratings to the JSON file.
4. Exit the application.

Simply follow the on-screen prompts to manage employee ratings.

## Modules

### data_classes.py

This module defines the core data structures used in the application.

- **`Person` Class**:
  - **Attributes**:
    - `first_name` (str): The first name of the person.
    - `last_name` (str): The last name of the person.
  - **Methods**:
    - `__init__(self, first_name, last_name)`: Constructor method to initialize the `Person` object with a first and last name.
    - `__str__(self)`: Returns a formatted string representation of the `Person` object.

- **`Employee` Class**:
  - Inherits from `Person`.
  - **Attributes**:
    - `employee_id` (int): A unique identifier for the employee.
    - `rating` (float): The performance rating of the employee.
  - **Methods**:
    - `__init__(self, employee_id, first_name, last_name, rating)`: Constructor method to initialize the `Employee` object with an ID, name, and rating.
    - `__str__(self)`: Returns a formatted string representation of the `Employee` object.

### processing_classes.py

This module is responsible for handling data persistence and processing.

- **`FileProcessor` Class**:
  - **Methods**:
    - `read_employee_data_from_file(file_name, employee_data)`: Reads employee data from a JSON file and returns a list of `Employee` objects.
    - `save_employee_data_to_file(file_name, employee_data)`: Saves the list of `Employee` objects to a JSON file.

### presentation_classes.py

This module handles the user interface and interaction.

- **`IO` Class**:
  - **Methods**:
    - `output_menu(menu)`: Displays a menu to the user.
    - `input_menu_choice()`: Collects and returns the user's menu selection.
    - `input_employee_data(employee_data)`: Prompts the user to enter new employee data, adds it to the existing data, and returns the updated list.
    - `output_employee_data(employee_data)`: Displays the list of employee data to the user.

- **Constants**:
  - `WELCOME`: A string containing the welcome message displayed when the application starts.
  - `MENU`: A string containing the main menu options.
  - `EXIT_MSG`: A string containing the message displayed when the application exits.

## Testing

Automated tests are provided in separate test modules:

- **`test_data_classes.py`**: Tests for the `Person` and `Employee` classes to ensure correct instantiation and string representation.
- **`test_processing_classes.py`**: Tests for the `FileProcessor` class, focusing on reading from and writing to the JSON file.
- **`test_presentation_classes.py`**: Tests for the `IO` class, validating menu output, data input, and employee data display.

Run the tests using the following command:
```bash
python -m unittest discover
