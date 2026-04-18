import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import joblib
import os

# Create directories
os.makedirs('data', exist_ok=True)
os.makedirs('models', exist_ok=True)
os.makedirs('outputs', exist_ok=True)

def generate_data():
    print("Generating Pattern-based HR Data...")
    np.random.seed(42)
    n = 1000
    
    # Feature generation
    years_exp = np.random.randint(1, 15, n)
    projects = np.random.randint(1, 10, n)
    attendance = np.random.randint(60, 100, n)
    training_score = np.random.randint(40, 100, n)
    
    # Logical scoring for high accuracy
    score = (projects * 0.4) + (attendance * 0.3) + (training_score * 0.3)
    
    performance_score = []
    for s in score:
        if s > 55:
            performance_score.append(2) # High
        elif s > 40:
            performance_score.append(1) # Medium
        else:
            performance_score.append(0) # Low
        
    df = pd.DataFrame({
        'years_exp': years_exp,
        'projects': projects,
        'attendance': attendance,
        'training_score': training_score,
        'performance_score': performance_score
    })
    
    df.to_csv('data/employee_data.csv', index=False)
    return df

if __name__ == "__main__":
    # Load and Prepare Data
    df = generate_data()
    X = df.drop('performance_score', axis=1)
    y = df['performance_score']
    
    # Split Dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Model Training
    print("Training Random Forest Model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Predictions and Evaluation
    y_pred = model.predict(X_test)
    print(f"\n✅ Accuracy: {accuracy_score(y_test, y_pred)*100:.2f}%")
    print("\n📋 Classification Report:\n", classification_report(y_test, y_pred))
    
    # Save Artifacts
    joblib.dump(model, 'models/perf_model.pkl')
    
    # Generate Visualization
    plt.figure(figsize=(8,6))
    sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, cmap='Blues', fmt='d')
    plt.title('Performance Prediction - Confusion Matrix')
    plt.savefig('outputs/result_graph.png')
    
    print("\n✅ Success! Dataset, Model, and Graph are ready.")
    plt.savefig('outputs/result_graph.png')
                # Generate Visualization
    plt.figure(figsize=(8,6))
    sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, cmap='Blues', fmt='d')
    plt.title('Performance Prediction - Confusion Matrix')
    
    
    plt.savefig('outputs/result_graph.png') 
    
    
    plt.show() 
    
    print("\n✅ Success! Dataset, Model, and Graph are ready.")