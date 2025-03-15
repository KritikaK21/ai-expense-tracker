import pickle

# ✅ Load the saved model
with open('expense_categorizer_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# ✅ Load the saved vectorizer
with open('expense_vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

print("\n✅ Model and Vectorizer loaded successfully!")

# ✅ Test the model with new expenses
test_sentences = [
    "Paid 400 for medicines",
    "Spent 3000 on clothes",
    "Ordered pizza for 800",
    "Electricity bill 2000",
    "Bus pass 500"
]

# ✅ Convert test sentences to vectors
test_vectors = vectorizer.transform(test_sentences)

# ✅ Predict categories
predictions = model.predict(test_vectors)

# ✅ Print the predictions
print("\n✅ Predictions from Loaded Model:")
for sentence, prediction in zip(test_sentences, predictions):
    print(f"'{sentence}' ➡️ {prediction}")
