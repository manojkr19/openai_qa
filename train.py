import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb

# Generate synthetic data
np.random.seed(42)
X = np.random.randn(1000, 10)
Y = (np.sum(X, axis=1) + np.random.randn(1000) > 0).astype(int)

# Split the data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Define models and their configurations
models = [
    {
        'name': 'Logistic Regression',
        'model': tf.keras.Sequential([tf.keras.layers.Dense(1, input_dim=10, activation='sigmoid')]),
        'fit': lambda model, X, Y: model.compile(optimizer='adam', loss='binary_crossentropy') or model.fit(X, Y, epochs=50, batch_size=10, verbose=0),
        'predict': lambda model, X: (model.predict(X) > 0.5).astype(int)
    },
    {
        'name': 'Neural Network',
        'model': tf.keras.Sequential([
            tf.keras.layers.Dense(64, input_dim=10, activation='relu'),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ]),
        'fit': lambda model, X, Y: model.compile(optimizer='adam', loss='binary_crossentropy') or model.fit(X, Y, epochs=50, batch_size=10, verbose=0),
        'predict': lambda model, X: (model.predict(X) > 0.5).astype(int)
    },
    {
        'name': 'XGBoost',
        'model': xgb.XGBClassifier(),
        'fit': lambda model, X, Y: model.fit(X, Y),
        'predict': lambda model, X: model.predict(X)
    },
    {
        'name': 'RandomForest',
        'model': RandomForestClassifier(),
        'fit': lambda model, X, Y: model.fit(X, Y),
        'predict': lambda model, X: model.predict(X)
    }
]

# Iterate over models and print their performance
for model_config in models:
    model = model_config['model']
    model_config['fit'](model, X_train, Y_train)
    
    Y_pred = model_config['predict'](model, X_test)
    accuracy = accuracy_score(Y_test, Y_pred)
    f1 = f1_score(Y_test, Y_pred)
    
    print(f"Model: {model_config['name']}")
    print(f"Accuracy: {accuracy * 100:.2f}%")
    print(f"F1 Score: {f1:.2f}")
    print("-" * 50)

# Based on the printed results, you can pick the model with the highest accuracy and F1 score.