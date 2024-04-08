import pandas as pd

# Read the csv file

df = pd.read_csv('data.csv')

# Calculate the avg age

avg_age = df['age'].mean()
average_age = round(avg_age, 2)

# Find the most common domain name

df['domain'] = df['email'].apply(lambda x: x.split('@')[1])
most_common_domain = df['domain'].value_counts().idxmax()

print(f'Average Age: {average_age}')
print(f'Most Common Domain: {most_common_domain}')