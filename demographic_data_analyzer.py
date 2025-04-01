import pandas as pd

def analyze_demographic_data(filepath):
    # Load dataset
    df = pd.read_csv(filepath)
    
    # 1. Count of each race
    race_count = df['race'].value_counts()
    
    # 2. Average age of men
    average_age_men = df[df['sex'] == 'Male']['age'].mean()
    
    # 3. Percentage with Bachelor's degree
    percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100
    
    # 4 & 5. Percentage of people with and without advanced education earning >50K
    advanced_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    high_income = df['salary'] == '>50K'
    
    higher_edu_rich = (df[advanced_edu & high_income].shape[0] / df[advanced_edu].shape[0]) * 100
    lower_edu_rich = (df[~advanced_edu & high_income].shape[0] / df[~advanced_edu].shape[0]) * 100
    
    # 6. Minimum hours per week
    min_hours = df['hours-per-week'].min()
    
    # 7. Percentage earning >50K among minimum hour workers
    min_hour_workers = df[df['hours-per-week'] == min_hours]
    rich_min_hour_workers = (min_hour_workers['salary'] == '>50K').mean() * 100
    
    # 8. Country with highest % earning >50K
    country_stats = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean() * 100)
    top_country = country_stats.idxmax()
    top_country_percentage = country_stats.max()
    
    # 9. Most popular occupation in India earning >50K
    india_high_earners = df[(df['native-country'] == 'India') & high_income]
    top_india_occupation = india_high_earners['occupation'].mode()[0]
    
    return {
        "Race Count": race_count,
        "Average Age of Men": average_age_men,
        "Percentage with Bachelors": percentage_bachelors,
        "Higher Education >50K": higher_edu_rich,
        "Lower Education >50K": lower_edu_rich,
        "Min Work Hours": min_hours,
        "Rich Min Hour Workers %": rich_min_hour_workers,
        "Top Country": top_country,
        "Top Country %": top_country_percentage,
        "Top Occupation in India": top_india_occupation
    }

# Example usage:
# result = analyze_demographic_data('your_dataset.csv')
# print(result)
