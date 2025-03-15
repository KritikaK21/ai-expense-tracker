import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

# ✅ Load the service account key
cred = credentials.Certificate('serviceAccountKey.json')

# ✅ Load the database URL from firebase-config.json
with open('firebase-config.json') as f:
    config = json.load(f)

# ✅ Initialize the Firebase app
firebase_admin.initialize_app(cred, {
    'databaseURL': config['databaseURL']  # Loaded dynamically
})

# ✅ Reference to 'expense' node
ref = db.reference('expense')

# ✅ Take user input for dynamic data
expense_type = input("Enter expense type (e.g., food, transport): ")
expense_amount = input("Enter expense amount: ")
expense_date = input("Enter date (YYYY-MM-DD): ")

# ✅ Create data dictionary
data = {
    'type': expense_type,
    'amount': expense_amount,
    'date': expense_date
}

# ✅ Push data to Firebase
ref.push(data)
print("✅ Expense added successfully!")

# ✅ Function to read and display expenses
def read_expenses():
    expenses = ref.get()  # Get all data from 'expense' node
    if expenses:
        print("\n📊 Your Expense Records:")
        for key, value in expenses.items():
            print(f"- Type: {value['type']}, Amount: {value['amount']}, Date: {value['date']}")
    else:
        print("\n❌ No expenses found.")

# ✅ Call the function to display expenses
read_expenses()
