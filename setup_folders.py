import os

# Define the project directory structure
project_name = "Employee-Performance-Predictor"
folders = [
    'data',         # To store CSV/Raw data
    'notebooks',    # For Jupyter Notebook experiments
    'src',          # For main Python scripts
    'models',       # To save the trained .pkl models
    'outputs',      # For generated graphs and CSV results
    'images'        # For GitHub documentation screenshots
]

files = {
    'requirements.txt': 'pandas\nnumpy\nscikit-learn\nmatplotlib\nseaborn\njoblib',
    'README.md': '# Employee Performance Predictor\nThis project predicts employee performance levels using ML.',
    '.gitignore': 'models/*.pkl\ndata/*.csv\n__pycache__/\n.env'
}

def create_structure():
    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Directory created: {folder}")

    # Create initial files
    for filename, content in files.items():
        with open(filename, 'w') as f:
            f.write(content)
        print(f"File created: {filename}")

if __name__ == "__main__":
    create_structure()