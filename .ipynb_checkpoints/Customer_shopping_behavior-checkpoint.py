import pandas as pd  #import pandas
df=pd.read_csv("customer_shopping_behavior.csv")   #read csv file

print(df.head())                                    #display from top by default 5
print(df.info())                                    #display all columes and there data type

print(df.describe(include='all'))                                #to check summury statictics

print(df.isnull().sum())                                         #to check how many null values are present

df['Review Rating']=df.groupby('Category')['Review Rating'].transform(lambda x:x.fillna(x.median()))
print(df.isnull().sum())  


df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
df=df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
print(df.columns)

#create column age_group

labels=['young Adult','Adult','Middle-aged','Senior']
df['age_group']=pd.qcut(df['age'], q=4 ,labels=labels)
print(df[['age','age_group']].head(10))

#purchase frequency days column

frequency_mapping={
    'Fortnightly':14,
    'Weekly':7,
    'Monthly':30,
    'Quarterly':90,
    'Bi-Weekly':14,
    'Annually':365,
    'Every 3 Months':90
}

df['purchase_frequency_days']=df['frequency_of_purchases'].map(frequency_mapping)

print(df[['purchase_frequency_days','frequency_of_purchases']].head(10))

print(df[['discount_applied','promo_code_used']].head(10))

#print(df['discount_applied']==df['promo_code_used']).all()

df=df.drop('promo_code_used',axis=1)
print(df.columns)