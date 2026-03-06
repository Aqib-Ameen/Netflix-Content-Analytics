# Netflix Content Analytics Dashboard

![Project Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![Project Category](https://img.shields.io/badge/Category-Data%20Analytics-E50914?style=for-the-badge&logo=netflix)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PowerBI](https://img.shields.io/badge/PowerBI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)

## Project Overview
![Overview Badge](https://img.shields.io/badge/Section-Project%20Overview-blue?style=flat-square)

The **Netflix Content Analytics Dashboard** is a comprehensive data analytics project designed to uncover deep insights into Netflix's vast library of movies and TV shows. By leveraging Python for robust data preprocessing and advanced visualization tools, this project identifies significant trends in content production, global distribution, and audience demographics.

The primary goal is to provide a clear, data-driven narrative of how Netflix has evolved as a global streaming leader and where its content strategy is currently focused.

---

## Business Problem
![Business Problem Badge](https://img.shields.io/badge/Section-Business%20Problem-red?style=flat-square)

As the streaming industry becomes increasingly competitive, understanding content trends is crucial. This analysis addresses key strategic questions:
- **Growth Strategy**: How has the volume of content added to the platform evolved over the last decade?
- **Global Footprint**: Which countries are the leading contributors to Netflix's library, and where is the growth emerging?
- **Content Mix**: What is the current balance between Movies and TV Shows, and how is this ratio shifting?
- **Genre Dominance**: Which genres consistently dominate the platform and provide the most variety for users?
- **Audience Targeting**: How is content categorized across different maturity ratings?

---

## Dataset Information
![Dataset Info Badge](https://img.shields.io/badge/Section-Dataset%20Information-orange?style=flat-square)

The project utilizes the **Netflix Movies and TV Shows** dataset, sourced from [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows).

**Key Features:**
- `title`: Name of the movie or TV show.
- `type`: Category of the content (Movie or TV Show).
- `director`: Director(s) of the content.
- `cast`: Actors involved in the production.
- `country`: Country where the content was produced.
- `date_added`: Date the content was added to Netflix.
- `release_year`: The actual release year of the item.
- `rating`: TV rating or movie rating (e.g., TV-MA, PG-13).
- `listed_in`: Genres the content belongs to.

---

## Tools & Technologies
![Tech Stack Badge](https://img.shields.io/badge/Section-Tools%20%26%20Technologies-lightgrey?style=flat-square)

- **Programming**: Python (v3.x)
- **Data Manipulation**: Pandas, NumPy
- **Visualizations (Python)**: Matplotlib, Seaborn
- **Business Intelligence**: Power BI / Tableau (Dashboarding)
- **Version Control**: GitHub
- **Environment**: Visual Studio Code / Jupyter Notebooks

---

## Project Workflow
![Workflow Badge](https://img.shields.io/badge/Section-Project%20Workflow-green?style=flat-square)

1.  **Data Collection**: Importing the raw CSV dataset.
2.  **Data Cleaning**: Standardizing formats, handling missing values, and de-duplication.
3.  **Feature Engineering**: Extracting date features and normalizing multi-value columns (Exploding Genres/Countries).
4.  **Exploratory Data Analysis (EDA)**: Statistical analysis and trend identification.
5.  **Data Visualization**: Creating static charts to validate findings.
6.  **Dashboard Development**: Designing an interactive, multi-page dashboard.
7.  **Insights & Conclusions**: Summarizing business implications and strategic recommendations.

---

## Data Cleaning Process
![Cleaning Badge](https://img.shields.io/badge/Section-Data%20Cleaning-yellow?style=flat-square)

To ensure high data quality for the final dashboard, several preprocessing steps were performed:
- **Missing Value Handling**: Replaced nulls in `director`, `cast`, and `country` with "Unknown" and `rating` with "Not Rated".
- **Date Formatting**: Converted `date_added` into a standardized `datetime` format.
- **Derived Features**: Created `year_added` and `month_added` columns for time-series analysis.
- **Data Normalization**: Split and exploded the `listed_in` (genres) and `country` columns so that collaborative productions and multi-genre titles are accurately represented in granular counts.
- **Whitespace Trimming**: Standardized all string entries for clean categorical analysis.

---

## Exploratory Data Analysis
![EDA Badge](https://img.shields.io/badge/Section-Exploratory%20Data%20Analysis-purple?style=flat-square)

Our analysis revealed several foundational trends across the platform.

### 1. Content Distribution (Movies vs TV Shows)
Approximate distribution shows that **69.6%** of content are Movies, while **30.4%** are TV Shows.
![Content Type Distribution](visualizations/content_type_bar.png)

### 2. Content Growth Over Time
A massive surge in content additions was observed starting from **2016**.
![Content Growth](visualizations/content_growth_line.png)

### 3. Top 10 Genres
**International Movies**, **Dramas**, and **Comedies** rank as the most frequent categories.
![Top Genres](visualizations/top_genres_hbar.png)

### 4. Regional Production Leaders
The **United States** leads in production, followed by **India** and the **United Kingdom**.
![Top Countries](visualizations/top_countries_bar.png)

### 5. Ratings Distribution
Analysis of content ratings showing the volume of items categorized by maturity levels.
![Ratings Distribution](visualizations/ratings_distribution_bar.png)

---

## Dashboard Features
![Dashboard Badge](https://img.shields.io/badge/Section-Dashboard%20Features-brightgreen?style=flat-square)

The final BI dashboard (linked in `/dashboard`) includes:
- **KPI Overview**: Real-time stats for Total Titles, Total Movies, and Total TV Shows.
- **Growth Analysis**: Dynamic line charts showing content addition trends.
- **Global Map**: Interactive geographic distribution of content production.
- **Rating Matrix**: Visualization of content distribution across audience maturity levels.
- **Advanced Filtering**: Slice data by Year, Genre, Country, and Type.

---

## Key Insights
![Insights Badge](https://img.shields.io/badge/Section-Key%20Insights-important?style=flat-square)

- **The Netflix Surge**: Content acquisition increased exponentially between 2016 and 2019, reflecting Netflix's aggressive push for original content.
- **Global Diversity**: While the US is the leader, International content is the fastest-growing segment, highlighting Netflix's "local-to-global" strategy.
- **The Shift to TV**: While Movies have a higher total count, the acquisition rate of TV Shows has increased significantly in recent years.
- **Genre Powerhouse**: Dramas and International titles represent the core pillars of the Netflix library.

---

## Project Folder Structure
![Folders Badge](https://img.shields.io/badge/Section-Folder%20Structure-informational?style=flat-square)

```text
Netflix-Content-Analytics/
│
├── data/                       # Raw and Cleaned datasets
│   ├── netflix_titles.csv
│   └── clean_netflix_titles.csv
├── notebooks/                  # Python scripts and EDA logic
│   ├── data_cleaning.py
│   ├── netflix_analysis.py
│   └── cleaned_data_eda.py
├── dashboard/                  # Power BI / Tableau project files
│   └── Netflix_Dashboard.pbix (Placeholder)
├── visualizations/             # High-resolution charts from final analysis
├── images/                     # Screenshots and banner assets
└── README.md                   # Project documentation
```

---

## Dashboard Preview
![Preview Badge](https://img.shields.io/badge/Section-Dashboard%20Preview-9ff?style=flat-square)

---

## How to Run This Project
![Run Badge](https://img.shields.io/badge/Section-How%20to%20Run-success?style=flat-square)

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/Netflix-Content-Analytics.git
    ```
2.  **Install Dependencies**:
    ```bash
    pip install pandas numpy matplotlib seaborn
    ```
3.  **Clean & Process Data**:
    ```bash
    python notebooks/data_cleaning.py
    ```
4.  **Generate Visuals**:
    ```bash
    python notebooks/cleaned_data_eda.py
    ```
5.  **Open Dashboard**:
    Load `data/clean_netflix_titles.csv` into Power BI or open the `.pbix` file in the `dashboard/` folder.

---

## Future Improvements
![Future Badge](https://img.shields.io/badge/Section-Future%20Improvements-blueviolet?style=flat-square)

- **Advanced NLP**: Performing Sentiment Analysis on the `description` column to identify tonal trends.
- **Machine Learning**: Implementing a Recommendation System based on genre and cast.
- **Predictive Analytics**: Time-series forecasting to predict future content acquisition targets.

---

## Conclusion
![Conclusion Badge](https://img.shields.io/badge/Section-Conclusion-blue?style=flat-square)

This project demonstrates the full lifecycle of a data analytics workflow—from raw data intake and rigorous cleaning to sophisticated visualization and strategic insight generation. The results provide a clear roadmap of Netflix’s content evolution and strategic priorities.

---

**Aqib Ameen**
- [LinkedIn](https://www.linkedin.com/in/aqib-ameen)


---
*Disclaimer: This project is for educational purposes and uses publicly available data from Kaggle.*
