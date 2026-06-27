# Personal Expense Tracker

A simple command-line application developed in Python to help users record, manage, and analyze their daily expenses. The project allows users to store expense records, generate reports, and visualize spending patterns through charts.

## Features

### Phase 1: Basic Operations

* Add new expenses with date, category, amount, and description
* View all recorded expenses in a structured table format
* Easy-to-use menu-driven interface
* Input validation and error handling

### Phase 2: Data Management

* Automatically saves expenses to a CSV file (`expenses.csv`)
* Loads previously saved expenses when the application starts
* Maintains data between sessions

### Phase 3: Reports and Analysis

* Calculate total spending
* View spending by category with percentage distribution
* Identify the highest and lowest expenses
* Calculate average expense amount
* Filter expenses by category
* Filter expenses by date range

### Phase 4: Data Visualization

* Generate a pie chart showing expense distribution
* Generate a bar chart for category-wise spending
* Save charts as image files (`expense_chart.png`)
* Visualize spending patterns for better analysis

### Additional Features

* Delete existing expenses
* Add optional descriptions for each expense
* Create custom expense categories
* Comprehensive error handling
* User-friendly date input system

## Installation

### Step 1: Download the Project

Download or clone the project files to your computer.

### Step 2: Install Dependencies

Open Command Prompt, PowerShell, or the VS Code terminal and run:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

```bash
python main.py
```

### Menu Options

#### 1. Add an Expense

Create a new expense record by entering:

* Date
* Category
* Amount
* Optional description

#### 2. View All Expenses

Displays all recorded expenses in a table format, sorted by date.

#### 3. Generate Report

Provides an overview of:

* Total spending
* Category-wise spending
* Highest expense
* Lowest expense
* Average expense

#### 4. Visualize Expenses

Creates:

* Pie chart showing expense distribution
* Bar chart showing spending by category

#### 5. Delete an Expense

Allows users to remove an expense record from the system.

#### 6. Filter by Category

Displays expenses belonging to a selected category.

#### 7. Filter by Date Range

Displays expenses recorded between two selected dates.

#### 8. Save and Exit

Saves all records and closes the application.

## Data Storage

Expense records are stored in the `expenses.csv` file.

CSV Structure:

```csv
date,category,amount,description
2024-06-04,Food,50.0,Groceries
2024-06-03,Transport,20.0,Taxi Fare
```

The file is automatically loaded when the application starts and updated whenever data is saved.

## Example Usage

```text
PERSONAL EXPENSE TRACKER
========================
1. Add an Expense
2. View All Expenses
3. Generate Report
4. Visualize Expenses
5. Delete an Expense
6. Filter by Category
7. Filter by Date Range
8. Save and Exit
========================

Enter your choice (1-8): 1

--- Add Expense ---

Enter date (YYYY-MM-DD) or press Enter for today:
Select category (1-7): 1
Enter amount: $45.50
Enter description (optional): Lunch at Restaurant

Expense added successfully.
```

## Project Structure

```text
Expense_tracker/
├── main.py
├── requirements.txt
├── README.md
├── QUICKSTART.md
├── expenses.csv
└── expense_chart.png
```

## Technologies Used

* Python 3.x
* CSV Module
* Datetime Module
* Matplotlib
* Collections Module
* OS Module

## Key Components

### Main Functions

1. `load_expenses()` – Loads expense records from the CSV file
2. `save_expenses()` – Saves expense records to the CSV file
3. `add_expense()` – Adds a new expense with validation
4. `view_expenses()` – Displays all expenses
5. `generate_report()` – Creates spending reports
6. `visualize_expenses()` – Generates charts and graphs
7. `delete_expense()` – Removes an expense record
8. `filter_by_category()` – Filters expenses by category
9. `filter_by_date()` – Filters expenses by date range
10. `main_menu()` – Controls the main application workflow

## Data Structure

Each expense is stored as a dictionary:

```python
{
    'date': '2024-06-04',
    'category': 'Food',
    'amount': 45.50,
    'description': 'Lunch at Restaurant'
}
```

## Error Handling

The application includes validation for:

* Incorrect date formats
* Invalid amount entries
* Negative or zero amounts
* File reading and writing issues
* CSV-related errors
* Invalid menu selections

## Sample Categories

* Food
* Transport
* Entertainment
* Utilities
* Healthcare
* Shopping
* Other
* Custom Categories

## Tips for Use

* Use the correct date format: `YYYY-MM-DD`
* Add descriptions to make records easier to understand later
* Review reports regularly to monitor spending habits
* Generate charts to visualize where money is being spent
* Keep a backup copy of the CSV file if needed

## Future Enhancements

Possible improvements for future versions:

* Monthly and yearly reports
* Budget planning and alerts
* PDF report generation
* Data backup and restore functionality
* Expense editing feature
* Multi-user support
* Web or mobile application version

## Requirements

* Python 3.6 or above
* Matplotlib

The following modules are included with Python:

* csv
* datetime
* collections
* os

## Support

If you encounter any issues:

* Check the error message displayed on the screen
* Verify that Python is installed correctly
* Ensure that matplotlib is installed
* Confirm that the application has permission to read and write files

## Author

Personal Expense Tracker Project

Developed as part of a Python learning and project-based internship program.

---

This project demonstrates the use of Python programming concepts such as file handling, data management, user input validation, reporting, and data visualization in a practical real-world application.
