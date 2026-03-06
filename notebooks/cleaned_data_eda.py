import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set visual style
sns.set_theme(style="whitegrid", palette="viridis")
plt.rcParams['figure.figsize'] = (12, 8)

def run_cleaned_eda():
    """
    Perform EDA on the cleaned Netflix titles dataset.
    """
    # 1. Load the dataset
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, '..', 'data', 'clean_netflix_titles.csv')
    
    if not os.path.exists(data_path):
        print(f"Error: Cleaned dataset not found at {data_path}. Please run data_cleaning.py first.")
        return

    print("Loading cleaned dataset...")
    df = pd.read_csv(data_path)
    
    # Create visualizations folder
    viz_dir = os.path.join(current_dir, '..', 'visualizations')
    if not os.path.exists(viz_dir):
        os.makedirs(viz_dir)
        print(f"Created folder: {viz_dir}")

    # --- 2. Content Type Analysis ---
    print("\n--- Performing Content Type Analysis ---")
    plt.figure(figsize=(10, 6))
    type_counts = df.drop_duplicates(subset=['show_id'])['type'].value_counts()
    sns.barplot(x=type_counts.index, y=type_counts.values, hue=type_counts.index, palette=['#E50914', '#221F1F'], legend=False)
    plt.title('Number of Movies vs TV Shows (Unique Titles)', fontsize=16)
    plt.xlabel('Content Type', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.savefig(os.path.join(viz_dir, 'content_type_bar.png'))
    print("Saved: content_type_bar.png")

    # --- 3. Content Growth Over Time ---
    print("\n--- Performing Growth Analysis ---")
    plt.figure(figsize=(12, 6))
    # Drop duplicates to avoid counting exploded rows as new titles
    growth_data = df.drop_duplicates(subset=['show_id'])
    growth_counts = growth_data.groupby('year_added').size()
    growth_counts.plot(kind='line', marker='o', color='#E50914', linewidth=2)
    plt.title('Netflix Content Added Over the Years', fontsize=16)
    plt.xlabel('Year Added', fontsize=12)
    plt.ylabel('Number of Titles', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.savefig(os.path.join(viz_dir, 'content_growth_line.png'))
    print("Saved: content_growth_line.png")

    # --- 4. Top Genres ---
    print("\n--- Performing Genre Analysis ---")
    plt.figure(figsize=(12, 8))
    top_genres = df['listed_in'].value_counts().head(10)
    sns.barplot(x=top_genres.values, y=top_genres.index, hue=top_genres.index, palette='rocket', legend=False)
    plt.title('Top 10 Genres on Netflix', fontsize=16)
    plt.xlabel('Count (including exploded roles)', fontsize=12)
    plt.ylabel('Genre', fontsize=12)
    plt.savefig(os.path.join(viz_dir, 'top_genres_hbar.png'))
    print("Saved: top_genres_hbar.png")

    # --- 5. Top Countries ---
    print("\n--- Performing Country Analysis ---")
    plt.figure(figsize=(12, 8))
    top_countries = df[df['country'] != 'Unknown']['country'].value_counts().head(10)
    sns.barplot(x=top_countries.values, y=top_countries.index, hue=top_countries.index, palette='mako', legend=False)
    plt.title('Top 10 Countries Producing Netflix Content', fontsize=16)
    plt.xlabel('Count (including collaborative productions)', fontsize=12)
    plt.ylabel('Country', fontsize=12)
    plt.savefig(os.path.join(viz_dir, 'top_countries_bar.png'))
    print("Saved: top_countries_bar.png")

    # --- 6. Ratings Distribution ---
    print("\n--- Performing Ratings Distribution Analysis ---")
    plt.figure(figsize=(12, 6))
    rating_counts = df.drop_duplicates(subset=['show_id'])['rating'].value_counts()
    sns.barplot(x=rating_counts.index, y=rating_counts.values, hue=rating_counts.index, palette='magma', legend=False)
    plt.title('Distribution of Content Ratings on Netflix', fontsize=16)
    plt.xlabel('Rating', fontsize=12)
    plt.ylabel('Number of Titles', fontsize=12)
    plt.xticks(rotation=45)
    plt.savefig(os.path.join(viz_dir, 'ratings_distribution_bar.png'))
    print("Saved: ratings_distribution_bar.png")

    # --- 7. Print Key Insights ---
    print("\n" + "="*30)
    print("      KEY INSIGHTS")
    print("="*30)
    
    unique_df = df.drop_duplicates(subset=['show_id'])
    total_titles = len(unique_df)
    movies_pc = (len(unique_df[unique_df['type'] == 'Movie']) / total_titles) * 100
    tv_pc = (len(unique_df[unique_df['type'] == 'TV Show']) / total_titles) * 100
    
    common_genre = df['listed_in'].value_counts().idxmax()
    top_country = df[df['country'] != 'Unknown']['country'].value_counts().idxmax()

    print(f"1. Most Common Genre: {common_genre}")
    print(f"2. Top Content Producer: {top_country}")
    print(f"3. Content Mix:")
    print(f"   - Movies: {movies_pc:.2f}%")
    print(f"   - TV Shows: {tv_pc:.2f}%")
    print("="*30)
    
    print("\nEDA Completed! Check the 'visualizations/' folder for the results.")

if __name__ == "__main__":
    run_cleaned_eda()
