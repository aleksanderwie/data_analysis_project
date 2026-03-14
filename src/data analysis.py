import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def uploading_data():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(BASE_DIR, '..', 'Data', 'manufacturing.csv')
    df = pd.read_csv(csv_path)
    return df



def run_exploratory_analysis(df):
    print("\n--- INFORMATIONS ---")
    print(df.info())
    print("\n--- DESCRIPTIVE STATISTICS ---")
    print(df.describe())
    print("\n--- MISSING DATA ---")
    print(df.isna().sum())
    print("\n--- PIERWSZE 5 WIERZCHÓW ---")
    print(df.head())
    

def plot_vizualization(df):
    '''Boxplot for temperature '''
    plt.figure(figsize=(10,4))
    sns.boxplot(x=df['Temperature (°C)'])
    plt.title('Temperature Distribution - Checking for Outliers')
    plt.show()

    '''Histogram for all numeric columns '''
    df.hist(figsize=(12,10), bins=20, color='skyblue', edgecolor='black')
    plt.suptitle('Rozkłady wszystkich parametrów')
    plt.show()

    '''Scatterplot: Temperature vs Quality Rating'''
    plt.figure(figsize=(8,5))
    sns.scatterplot(data=df, x = 'Temperature (°C)', y = 'Quality Rating')
    plt.title('Temperature vs Quality Rating')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Quality Rating')
    plt.show()

    '''KDE plot: Pressure vs Quality Rating '''
    plt.figure(figsize=(8,5))
    sns.kdeplot(x=df['Pressure (kPa)'], y=df['Quality Rating'], fill=True, cmap='Blues')
    plt.title('Pressure vs Quality Rating')
    plt.xlabel('Pressure (kPa)')
    plt.ylabel('Quality Rating')
    plt.show()

    '''Correlation heatmap'''
    sns.heatmap(df.corr(), annot=True, cmap='YlGnBu')
    plt.title('Correlation Heatmap')
    plt.show()

    '''Spearman correlation for selected columns'''
    print("--- SPEARMAN CORRELATION ---")
    spearman_corr = df[['Temperature (°C)', 'Material Fusion Metric']].corr(method='spearman')
    print("Spearman correlation:\n", spearman_corr)

# ==========================================
# MAIN PROGRAM LOOP 
# ==========================================

if __name__ == "__main__":
    try:
        df = uploading_data()
        run_exploratory_analysis(df)
        plot_vizualization(df)
        print("\nAnalysis succesful")
    except Exception as e:
        print(f"an unexpected error occurred {e}")