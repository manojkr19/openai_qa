import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score

# Sample data
data = pd.DataFrame({
    'client_id': [1, 2, 1, 3],
    'sector': ['Tech', 'Health', 'Tech', 'Finance'],
    'rating': ['buy', 'sell', 'hold', 'buy'],
    'prev_rating': ['hold', 'buy', 'sell', 'hold'],
    'price': [150, 120, 130, 140],
    'prev_price': [140, 125, 135, 130],
    'traded': [1, 0, 1, 0]
})

# Features and target
X = data.drop('traded', axis=1)
y = data['traded']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing
numeric_features = ['price', 'prev_price']
numeric_transformer = StandardScaler()

categorical_features = ['client_id', 'sector', 'rating', 'prev_rating']
categorical_transformer = OneHotEncoder(drop='first')

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Model
model = Pipeline(steps=[('preprocessor', preprocessor),
                        ('classifier', LogisticRegression())])

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print(f"F1 Score: {f1_score(y_test, y_pred):.2f}")
