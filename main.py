import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

EXPENSES_FILE = "expenses.csv"

def load_expenses():
    """Load expenses from CSV file"""
    expenses = []
    if os.path.exists(EXPENSES_FILE):
        try:
            with open(EXPENSES_FILE, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        expenses.append({
                            'date': row['date'],
                            'category': row['category'],
                            'amount': float(row['amount']),
                            'description': row.get('description', '')
                        })
                    except (ValueError, KeyError):
                        continue
        except Exception as e:
            print(f"Error loading expenses: {e}")
    return expenses


def save_expenses(expenses):
    """Save expenses to CSV file"""
    try:
        with open(EXPENSES_FILE, 'w', newline='') as file:
            fieldnames = ['date', 'category', 'amount', 'description']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for expense in expenses:
                writer.writerow(expense)
        print("✓ Expenses saved successfully!")
    except Exception as e:
        print(f"Error saving expenses: {e}")


def add_expense(expenses):
    """Add a new expense to the list"""
    try:
        print("\n--- Add Expense ---")
        
        # Get date
        while True:
            date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
            if date_input == "":
                date = datetime.now().strftime('%Y-%m-%d')
                break
            try:
                datetime.strptime(date_input, '%Y-%m-%d')
                date = date_input
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD")
        
        # Get category
        categories = ['Food', 'Transport', 'Entertainment', 'Utilities', 'Healthcare', 'Shopping', 'Other']
        print("\nAvailable categories:")
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")
        
        while True:
            try:
                cat_choice = int(input("Select category (1-7) or enter custom: "))
                if 1 <= cat_choice <= 7:
                    category = categories[cat_choice - 1]
                    break
                else:
                    print("Invalid choice. Please enter 1-7")
            except ValueError:
                category = input("Enter custom category: ").strip()
                if category:
                    break
                print("Category cannot be empty")
        
        # Get amount
        while True:
            try:
                amount = float(input("Enter amount: $"))
                if amount > 0:
                    break
                else:
                    print("Amount must be positive")
            except ValueError:
                print("Invalid amount. Please enter a number")
        
        # Get description
        description = input("Enter description (optional): ").strip()
        
        expense = {
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
        }
        expenses.append(expense)
        print(f"✓ Expense added: ${amount} for {category} on {date}")
        
    except Exception as e:
        print(f"Error adding expense: {e}")

def view_expenses(expenses):
    """Display all expenses"""
    if not expenses:
        print("\n--- View Expenses ---")
        print("No expenses recorded yet.")
        return
    
    print("\n--- All Expenses ---")
    print(f"{'Date':<12} {'Category':<15} {'Amount':<10} {'Description':<20}")
    print("-" * 60)
    
    for expense in sorted(expenses, key=lambda x: x['date'], reverse=True):
        date = expense['date']
        category = expense['category']
        amount = f"${expense['amount']:.2f}"
        description = expense['description'][:20] if expense['description'] else "---"
        print(f"{date:<12} {category:<15} {amount:<10} {description:<20}")
    
    total = sum(exp['amount'] for exp in expenses)
    print("-" * 60)
    print(f"{'TOTAL':<12} {'':<15} ${total:.2f}")

def generate_report(expenses):
    """Generate expense reports"""
    if not expenses:
        print("\n--- Generate Report ---")
        print("No expenses to report.")
        return
    
    print("\n--- Expense Report ---")
    
    # Total spending
    total_spending = sum(exp['amount'] for exp in expenses)
    print(f"\nTotal Spending: ${total_spending:.2f}")
    
    # Spending by category
    category_spending = defaultdict(float)
    for expense in expenses:
        category_spending[expense['category']] += expense['amount']
    
    print("\n--- Spending by Category ---")
    print(f"{'Category':<15} {'Amount':<10} {'Percentage':<10}")
    print("-" * 35)
    
    for category, amount in sorted(category_spending.items(), key=lambda x: x[1], reverse=True):
        percentage = (amount / total_spending) * 100 if total_spending > 0 else 0
        print(f"{category:<15} ${amount:>8.2f} {percentage:>8.1f}%")
    
    # Highest and lowest expense
    if expenses:
        highest = max(expenses, key=lambda x: x['amount'])
        lowest = min(expenses, key=lambda x: x['amount'])
        print(f"\nHighest Expense: ${highest['amount']:.2f} ({highest['category']} on {highest['date']})")
        print(f"Lowest Expense: ${lowest['amount']:.2f} ({lowest['category']} on {lowest['date']})")
        print(f"Average Expense: ${total_spending / len(expenses):.2f}")

def visualize_expenses(expenses):
    """Create visualizations of expenses"""
    if not expenses:
        print("\n--- Visualize Expenses ---")
        print("No expenses to visualize.")
        return
    
    category_spending = defaultdict(float)
    for expense in expenses:
        category_spending[expense['category']] += expense['amount']
    
    print("\n--- Generating Visualizations ---")
    
    # Create pie chart
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Pie chart
    categories = list(category_spending.keys())
    amounts = list(category_spending.values())
    colors = plt.cm.Set3(range(len(categories)))
    
    ax1.pie(amounts, labels=categories, autopct='%1.1f%%', colors=colors, startangle=90)
    ax1.set_title('Expense Distribution by Category')
    
    # Bar chart
    ax2.bar(categories, amounts, color=colors)
    ax2.set_xlabel('Category')
    ax2.set_ylabel('Amount ($)')
    ax2.set_title('Spending by Category')
    plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    plt.tight_layout()
    plt.savefig('expense_chart.png', dpi=100, bbox_inches='tight')
    print("✓ Chart saved as 'expense_chart.png'")
    plt.show()

# Delete expense
def delete_expense(expenses):
    """Delete an expense"""
    if not expenses:
        print("No expenses to delete.")
        return
    
    view_expenses(expenses)
    try:
        index = int(input("\nEnter the row number to delete (counting from bottom): ")) - 1
        sorted_expenses = sorted(expenses, key=lambda x: x['date'], reverse=True)
        
        if 0 <= index < len(sorted_expenses):
            deleted = sorted_expenses[index]
            expenses.remove(deleted)
            print(f"✓ Deleted: ${deleted['amount']:.2f} for {deleted['category']} on {deleted['date']}")
        else:
            print("Invalid row number")
    except ValueError:
        print("Invalid input")

def filter_by_category(expenses):
    """Filter expenses by category"""
    if not expenses:
        print("No expenses to filter.")
        return
    
    categories = set(exp['category'] for exp in expenses)
    print("\nAvailable categories:")
    cat_list = sorted(list(categories))
    for i, cat in enumerate(cat_list, 1):
        print(f"{i}. {cat}")
    
    try:
        choice = int(input("Select category: ")) - 1
        if 0 <= choice < len(cat_list):
            selected_category = cat_list[choice]
            filtered = [exp for exp in expenses if exp['category'] == selected_category]
            
            print(f"\n--- Expenses in {selected_category} ---")
            print(f"{'Date':<12} {'Amount':<10} {'Description':<20}")
            print("-" * 42)
            
            total = 0
            for expense in sorted(filtered, key=lambda x: x['date'], reverse=True):
                date = expense['date']
                amount = f"${expense['amount']:.2f}"
                description = expense['description'][:20] if expense['description'] else "---"
                print(f"{date:<12} {amount:<10} {description:<20}")
                total += expense['amount']
            
            print("-" * 42)
            print(f"Total in {selected_category}: ${total:.2f}")
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid input")

def filter_by_date(expenses):
    """Filter expenses by date range"""
    if not expenses:
        print("No expenses to filter.")
        return
    
    try:
        start_date = input("Enter start date (YYYY-MM-DD): ").strip()
        end_date = input("Enter end date (YYYY-MM-DD): ").strip()
        
        datetime.strptime(start_date, '%Y-%m-%d')
        datetime.strptime(end_date, '%Y-%m-%d')
        
        filtered = [exp for exp in expenses if start_date <= exp['date'] <= end_date]
        
        if not filtered:
            print("No expenses found in this date range.")
            return
        
        print(f"\n--- Expenses from {start_date} to {end_date} ---")
        print(f"{'Date':<12} {'Category':<15} {'Amount':<10} {'Description':<20}")
        print("-" * 60)
        
        total = 0
        for expense in sorted(filtered, key=lambda x: x['date'], reverse=True):
            date = expense['date']
            category = expense['category']
            amount = f"${expense['amount']:.2f}"
            description = expense['description'][:20] if expense['description'] else "---"
            print(f"{date:<12} {category:<15} {amount:<10} {description:<20}")
            total += expense['amount']
        
        print("-" * 60)
        print(f"Total: ${total:.2f}")
    except ValueError:
        print("Invalid date format or input")


def main_menu():
    """Main menu"""
    expenses = load_expenses()
    
    while True:
        print("\n" + "="*50)
        print("  PERSONAL EXPENSE TRACKER")
        print("="*50)
        print("1.  Add an Expense")
        print("2.  View All Expenses")
        print("3.  Generate Report")
        print("4.  Visualize Expenses (Charts)")
        print("5.  Delete an Expense")
        print("6.  Filter by Category")
        print("7.  Filter by Date Range")
        print("8.  Save and Exit")
        print("="*50)
        
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            generate_report(expenses)
        elif choice == '4':
            visualize_expenses(expenses)
        elif choice == '5':
            delete_expense(expenses)
        elif choice == '6':
            filter_by_category(expenses)
        elif choice == '7':
            filter_by_date(expenses)
        elif choice == '8':
            save_expenses(expenses)
            print("\n✓ Thank you for using Personal Expense Tracker!")
            print("✓ Your expenses have been saved.")
            break
        else:
            print("Invalid choice. Please enter 1-8")

if __name__ == "__main__":
    main_menu()
