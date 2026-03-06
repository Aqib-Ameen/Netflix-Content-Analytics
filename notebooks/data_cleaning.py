import pandas as pd
import numpy as np
import os

def clean_preprocess_netflix():
    """
    Clean and preprocess the Netflix titles dataset for data analytics.
    """
    # 1. Load the dataset
    # Robust path handling to run from project root or notebook directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, '..', 'data', 'netflix_titles.csv')
    
    print("Loading dataset...")
    df = pd.read_csv(data_path)
    
    # 2. Check dataset shape and column information
    print(f"\nDataset Shape: {df.shape}")
    print("\nColumn Information:")
    print(df.info())
    
    # 3. Handle missing values
    print("\nIdentifying missing values...")
    print(df.isnull().sum())
    
    print("\nReplacing missing values...")
    df['director'] = df['director'].fillna("Unknown")
    df['cast'] = df['cast'].fillna("Unknown")
    df['country'] = df['country'].fillna("Unknown")
    df['rating'] = df['rating'].fillna("Not Rated")
    
    # 4. Convert date_added to datetime
    print("Converting 'date_added' to datetime...")
    df['date_added'] = pd.to_datetime(df['date_added'].str.strip())
    
    # 5. Create new columns: year_added and month_added
    print("Extracting 'year_added' and 'month_added'...")
    df['year_added'] = df['date_added'].dt.year.astype('Int64') # Int64 handles NaNs if any remain
    df['month_added'] = df['date_added'].dt.month_name()
    
    # 6. Clean categorical columns: listed_in (genre)
    print("Cleaning and exploding 'listed_in'...")
    df['listed_in'] = df['listed_in'].str.split(',')
    df = df.explode('listed_in')
    df['listed_in'] = df['listed_in'].str.strip()
    
    # 7. Clean country column: Split and explode
    print("Cleaning and exploding 'country'...")
    df['country'] = df['country'].str.split(',')
    df = df.explode('country')
    df['country'] = df['country'].str.strip()
    
    # 8. Remove duplicate records
    print(f"Duplicates before removal: {df.duplicated().sum()}")
    df = df.drop_duplicates()
    print(f"Shape after cleaning and exploding: {df.shape}")
    
    # 9. Display summary statistics and the first 10 rows
    print("\nSummary Statistics:")
    print(df.describe(include='all'))
    
    print("\nFirst 10 Rows of Cleaned Dataset:")
    print(df.head(10))
    
    # 10. Save the cleaned dataset
    output_path = os.path.join(current_dir, '..', 'data', 'clean_netflix_titles.csv')
    df.to_csv(output_path, index=False)
    print(f"\nCleaned dataset saved as: {output_path}")

if __name__ == "__main__":
    clean_preprocess_netflix()
