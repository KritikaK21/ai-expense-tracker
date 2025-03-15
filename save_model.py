import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Sample data
data = {
    'Text': [
        'I spent 500 on groceries',
        'Paid 1000 for rent',
        'Bought clothes for 2000',
        'Movie tickets 800',
        'Paid electricity bill 1500',
        'Bus pass 500',
        'Bought medicine for 600',
        'Dinner for 1200',
        'Netflix subscription 500',
        'New shoes for 3000'
    ],
    'Category': [
        'Groceries',
        'Rent',
        'Shopping',
        'Entertainment',
        'Bills',
        'Transport',
        'Medical',
        'Food',
        'Entertainment',
        'Shopping'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Vectorize the Text
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['Text'])

# Labels
y = df['Category']

# Train the Model
model = MultinomialNB()
model.fit(X, y)

# ✅ Save model
with open('expense_categorizer_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)
print("✅ Model saved as 'expense_categorizer_model.pkl'")

# ✅ Save vectorizer
with open('expense_vectorizer.pkl', 'wb') as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)
print("✅ Vectorizer saved as 'expense_vectorizer.pkl'")
