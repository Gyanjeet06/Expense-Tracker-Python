# QUICK START GUIDE - Personal Expense Tracker

## Setup (First Time)

### Step 1: Install Python Dependencies

Before running the project, open Command Prompt, PowerShell, or the VS Code terminal in the project folder and run:

```bash
pip install -r requirements.txt
```

### Step 2: Run the Application

```bash
python main.py
```

---

## First Time Usage

### Adding Your First Expense

Follow these simple steps to add your first expense:

1. Run the application using `python main.py`
2. Select **1. Add an Expense** from the menu.
3. Enter a date or press **Enter** to use today's date.
4. Choose an expense category.
5. Enter the amount spent.
6. Add a short description if needed.
7. The expense will be added to the system.

### Example Session

```text
PERSONAL EXPENSE TRACKER
========================
...menu...
Enter your choice (1-8): 1

--- Add Expense ---

Enter date (YYYY-MM-DD) or press Enter for today:
(Press Enter to use today's date)

Available categories:
1. Food
2. Transport
3. Entertainment
4. Utilities
5. Healthcare
6. Shopping
7. Other

Select category (1-7) or enter custom: 1

Enter amount: $50
Enter description (optional): Grocery shopping

✓ Expense added successfully.
```

---

## Common Tasks

### Task 1: View All Expenses

* Select **2. View All Expenses**
* Displays all recorded expenses in a table
* Expenses are sorted by date
* Shows the total amount spent

### Task 2: Check Your Spending Report

* Select **3. Generate Report**
* View your total spending
* Check spending by category
* See the highest and lowest expenses
* Review the average expense amount

### Task 3: Visualize Your Spending

* Select **4. Visualize Expenses**
* Generates a pie chart showing category-wise spending
* Generates a bar chart for comparison
* Saves the chart as `expense_chart.png`

### Task 4: Find Expenses in a Category

* Select **6. Filter by Category**
* Choose a category from the list
* View all expenses under that category
* Check the total spent in that category

### Task 5: Find Expenses in a Date Range

* Select **7. Filter by Date Range**
* Enter a start date
* Enter an end date
* View expenses recorded during that period

### Task 6: Remove an Expense

* Select **5. Delete an Expense**
* Review the displayed expenses
* Enter the corresponding row number
* The selected expense will be removed

### Task 7: Save and Exit

* Select **8. Save and Exit**
* All expenses will be saved automatically
* The application will close safely

---

## File Descriptions

| File                | Purpose                        |
| ------------------- | ------------------------------ |
| `main.py`           | Main application file          |
| `requirements.txt`  | Required Python packages       |
| `README.md`         | Detailed project documentation |
| `QUICKSTART.md`     | Quick setup and usage guide    |
| `expenses.csv`      | Stores expense records         |
| `expense_chart.png` | Generated expense charts       |

---

## Data Storage

* **Location:** `expenses.csv`
* **Format:** CSV (Comma-Separated Values)
* **Fields:** Date, Category, Amount, Description
* **Saved When:** You select "Save and Exit"
* **Loaded When:** The application starts

### Sample expenses.csv

```csv
date,category,amount,description
2024-06-04,Food,50.0,Groceries
2024-06-03,Transport,20.0,Taxi Fare
2024-06-02,Entertainment,30.0,Movie Tickets
```

---

## Troubleshooting

### Problem: "Module 'matplotlib' not found"

**Solution:**

```bash
pip install matplotlib
```

### Problem: Invalid Date Format

**Solution:**
Use the format:

```text
YYYY-MM-DD
```

Example:

```text
2024-06-04
```

### Problem: No Expenses Showing

**Solution:**
Add at least one expense before trying to view reports or charts.

### Problem: CSV File Errors

**Solution:**
Avoid editing the CSV file manually. Use the application menu to add or remove records.

### Problem: Charts Not Displaying

**Solution:**

1. Verify that matplotlib is installed.
2. Check that you have permission to create files in the project folder.

---

## Tips & Tricks

### Best Practices

* Record expenses regularly.
* Use clear category names.
* Add descriptions for better tracking.
* Review reports periodically.
* Keep a backup of your expense data.

### Useful Tips

* Create custom categories when needed.
* Use date filters to review monthly or weekly expenses.
* Generate charts to understand spending patterns.
* Save your work before closing the application.

### Analysis Ideas

* Compare spending across different months.
* Identify categories where most money is spent.
* Track personal spending habits over time.
* Create a monthly budget based on previous reports.

---

## Keyboard Shortcuts & Tips

* Press **Enter** to use today's date.
* Press **Ctrl + C** to close the application if needed.
* Use numeric values when selecting menu options.
* Double-check dates before submitting them.

---

## Example Workflow

### Week 1

1. Add expenses daily.
2. Review expenses at the end of the week.
3. Identify any unnecessary spending.

### Month End

1. Generate a report.
2. Review category-wise spending.
3. Create charts for visualization.
4. Plan your budget for the next month.

### Quarterly

1. Compare spending trends across months.
2. Review overall financial habits.
3. Adjust spending categories if necessary.

---

## Next Steps

1. Install the required dependencies.
2. Run the application.
3. Add your first expense.
4. Explore the reports section.
5. Generate charts and visualizations.
6. Save your data before exiting.

---

## Getting Help

* Review the menu options carefully.
* Check the README.md file for detailed information.
* Follow the input formats shown by the application.
* Read any error messages displayed on the screen for guidance.

---

Start tracking your expenses and keep a clear record of your spending.

For additional details, refer to the README.md file.
