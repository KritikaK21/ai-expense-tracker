import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

# ✅ Load dataset
data = pd.read_csv('expenses.csv')

# ✅ Check data
print("Sample Data:\n", data.head())

# ✅ Split dataset into text and category
X = data['Text']  # Input text
y = data['Category']  # Output category (label)

# ✅ Convert text to vectors (Bag of Words)
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# ✅ Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

print("✅ Data Preprocessed and Ready for Training")

from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# ✅ Initialize the model (Naive Bayes Classifier)
model = MultinomialNB()

# ✅ Train the model
model.fit(X_train, y_train)

# ✅ Predict on test data
y_pred = model.predict(X_test)

# ✅ Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy * 100:.2f}%")

# ✅ Test model on new data (Optional)
test_sentences = ["Paid 400 for medicines", "Spent 3000 on clothes", "Ordered pizza for 800"]
test_vectors = vectorizer.transform(test_sentences)
predictions = model.predict(test_vectors)

print("\n✅ Sample Predictions:")
for sentence, prediction in zip(test_sentences, predictions):
    print(f"'{sentence}' ➡️ {prediction}")
