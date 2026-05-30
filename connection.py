import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:Arti%40123@localhost:5432/customer_behavior"
)

df = pd.read_csv("customer_shopping_behavior.csv")

# Clean column names
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')
df = df.rename(columns={
    'purchase_amount_(usd)': 'purchase_amount'
})

# Create age_group
labels = ['young Adult', 'Adult', 'Middle-aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels=labels)

# Create purchase_frequency_days
frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)

# Drop column
df = df.drop('promo_code_used', axis=1)

# Upload
df.to_sql('customer', engine, if_exists='replace', index=False)

print("Data uploaded successfully!")