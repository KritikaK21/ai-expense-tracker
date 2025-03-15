import json
import firebase_admin
from firebase_admin import credentials, firestore
import pickle
import os

# ------------------ Firebase Setup -------------------

# Initialize Firebase Admin SDK only once
if not firebase_admin._apps:
    cred = credentials.Certificate('serviceAccountKey.json')
    firebase_admin.initialize_app(cred)

# Initialize Firestore DB
db = firestore.client()

# ------------------ Load Model and Vectorizer -------------------

# Load trained ML model
with open('expense_categorizer_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load vectorizer
with open('expense_vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# ------------------ Lambda Handler -------------------

def lambda_handler(event, context):
    try:
        # Parse input data
        body = event  # Direct event input for local testing
        expense_text = body.get('text')
        amount = body.get('amount')
        date = body.get('date')
        
        # Check required fields
        if not expense_text or not amount or not date:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Invalid input. Please provide text, amount, and date.'})
            }

        # Predict category using ML model
        text_vector = vectorizer.transform([expense_text])
        predicted_category = model.predict(text_vector)[0]

        # Prepare data to store
        data = {
            'text': expense_text,
            'amount': amount,
            'date': date,
            'category': predicted_category
        }

        # Store in Firebase Firestore under "expenses" collection
        db.collection('expenses').add(data)

        # Return success response
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Expense stored successfully!',
                'category': predicted_category
            })
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'message': f'Internal server error: {str(e)}'})
        }

# ------------------ Local Simulation (Run when executing index.py directly) -------------------

if __name__ == "__main__":
    # Simulated event (like Lambda test input)
    test_event = {
        "text": "Bought medicine for 600",
        "amount": "600",
        "date": "2025-03-13"
    }

    # Simulate Lambda context (empty here)
    context = {}

    # Call Lambda function and print response
    response = lambda_handler(test_event, context)
    print("\n✅ Lambda Function Output:")
    print(json.dumps(response, indent=4))
