import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def load_and_preprocess_data(filepath):
    df = pd.read_csv(filepath)
    
    # Add 'overweight' column
    df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)
    df['overweight'] = (df['BMI'] > 25).astype(int)
    df.drop(columns=['BMI'], inplace=True)
    
    # Normalize cholesterol and glucose
    df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
    df['gluc'] = (df['gluc'] > 1).astype(int)
    
    return df

def draw_cat_plot(df):
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    g = sns.catplot(x='variable', y='total', hue='value', col='cardio', kind='bar', data=df_cat)
    fig = g.fig
    return fig

def draw_heat_map(df):
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]
    
    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', cmap='coolwarm', ax=ax)
    return fig

# Example usage:
# df = load_and_preprocess_data('medical_examination.csv')
# cat_plot = draw_cat_plot(df)
# heat_map = draw_heat_map(df)
# cat_plot.show()
# heat_map.show()
