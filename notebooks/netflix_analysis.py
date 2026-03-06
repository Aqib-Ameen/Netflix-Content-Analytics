#Load Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set visual style
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams['figure.figsize'] = (12, 8)

def run_eda():
    # 1. Load Dataset
    # Get the directory where the script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, '..', 'data', 'netflix_titles.csv')
    df = pd.read_csv(data_path)
    print("Dataset Loaded Successfully!")
    print(f"Shape: {df.shape}")
    
    # 2. Data Cleaning
    print("\n--- Data Cleaning ---")
    # Handling missing values for EDA
    df['director'] = df['director'].fillna('Unknown')
    df['cast'] = df['cast'].fillna('Unknown')
    df['country'] = df['country'].fillna(df['country'].mode()[0])
    df['date_added'] = df['date_added'].fillna(df['date_added'].mode()[0])
    df['rating'] = df['rating'].fillna(df['rating'].mode()[0])

    # Convert date_added to datetime
    df['date_added'] = pd.to_datetime(df['date_added'].str.strip())
    df['year_added'] = df['date_added'].dt.year
    df['month_added'] = df['date_added'].dt.month_name()

    print("Missing values handled and dates converted.")

    # 3. Exploratory Analysis & Visualization
    if not os.path.exists('../images'):
        os.makedirs('../images')

    # A. Distribution of Movies vs TV Shows
    plt.figure(figsize=(8, 6))
    df['type'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['#E50914', '#221F1F'])
    plt.title('Distribution of Netflix Content Types')
    plt.ylabel('')
    plt.savefig('../images/content_distribution.png')
    print("Saved: content_distribution.png")

    # B. Content added over years
    plt.figure(figsize=(12, 6))
    content_by_year = df.groupby(['year_added', 'type']).size().unstack().fillna(0)
    content_by_year.plot(kind='line', marker='o')
    plt.title('Content Added Over Years')
    plt.xlabel('Year Added')
    plt.ylabel('Count')
    plt.savefig('../images/content_over_years.png')
    print("Saved: content_over_years.png")

    # C. Top 10 Countries with Content
    plt.figure(figsize=(12, 6))
    top_countries = df['country'].value_counts().head(10)
    sns.barplot(x=top_countries.values, y=top_countries.index, hue=top_countries.index, palette='viridis', legend=False)
    plt.title('Top 10 Countries by Content Count')
    plt.xlabel('Count')
    plt.savefig('../images/top_countries.png')
    print("Saved: top_countries.png")

    # D. Ratings distribution
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x='rating', order=df['rating'].value_counts().index, hue='type', palette='magma')
    plt.title('Distribution of Content Ratings')
    plt.xticks(rotation=45)
    plt.savefig('../images/ratings_distribution.png')
    print("Saved: ratings_distribution.png")

    # E. Top Genres
    plt.figure(figsize=(12, 6))
    genres = df['listed_in'].str.split(', ').explode().value_counts().head(10)
    sns.barplot(x=genres.values, y=genres.index, hue=genres.index, palette='rocket', legend=False)
    plt.title('Top 10 Genres on Netflix')
    plt.xlabel('Count')
    plt.savefig('../images/top_genres.png')
    print("Saved: top_genres.png")

    print("\nEDA Completed! Visualizations saved in 'images/' folder.")

if __name__ == "__main__":
    run_eda()