# ✅ Import libraries
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

# ✅ Load dataset
data = pd.read_csv('expenses.csv')

# ✅ Check dataset
print("Sample Data:\n", data.head())

# ✅ Split into input (X) and output (y)
X = data['Text']  # Input sentences
y = data['Category']  # Expense categories

# ✅ Convert text to numeric vectors
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# ✅ Train Naive Bayes model on ALL data (since small dataset)
model = MultinomialNB()
model.fit(X_vectorized, y)

print("\n✅ Model trained successfully!")

# ✅ Test on new example sentences
test_sentences = [
    "Paid 400 for medicines",
    "Spent 3000 on clothes",
    "Ordered pizza for 800",
    "Movie night tickets 1200",
    "Electricity bill 2000",
    "Bus pass 500"
]

# ✅ Vectorize test sentences
test_vectors = vectorizer.transform(test_sentences)

# ✅ Predict categories
predictions = model.predict(test_vectors)

# ✅ Show predictions
print("\n✅ Sample Predictions:")
for sentence, prediction in zip(test_sentences, predictions):
    print(f"'{sentence}' ➡️ {prediction}")
