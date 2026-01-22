import pandas as pd

def hello_data():
    # Création d'un dataset simple 
    data = {
        'Etudiant': ['Toi', 'Moi', 'Lui'],
        'Note': [20, 18, 12],
        'Matiere': ['Docker', 'Docker', 'Docker']
    }
    
    # Création du DataFrame (le tableau)
    df = pd.DataFrame(data)
    
    print("--- HELLO DATA ---")
    print(df)
    print("------------------")

if __name__ == "__main__":
    hello_data()