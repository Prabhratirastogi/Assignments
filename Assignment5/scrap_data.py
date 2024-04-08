import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the IMDb page
url = "https://www.imdb.com/chart/top/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Fetch the HTML content
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# List to store movie titles, years, and ratings
movie_title = []
year = []
rating = []

# Find all the movie entries
movie_data = soup.findAll('li', attrs={'class': 'ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent'})[:20]

# Extract movie titles, years, and ratings
for store in movie_data:
    # Extract title
    name_element = store.find('h3', class_='ipc-title__text')
    if name_element:
        name = name_element.text.strip()
        movie_title.append(name)

    # Extract year
    year_element = store.find('span', class_='sc-b0691f29-8 ilsLEX cli-title-metadata-item')
    if year_element:
        year_text = year_element.text.strip()
        year.append(year_text)

    # Extract rating
    rating_element = store.find('span', class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating')
    if rating_element:
        rating_text = rating_element.text.strip()
        rating_value = rating_text.split()[0]
        rating.append(rating_value)

#  create a DataFrame from the extracted data
df = pd.DataFrame({
    'Title': movie_title,
    'Year': year,
    'Rating': rating
})


# Save the DataFrame to a CSV file
df.to_csv('top_20_movies.csv', index=False)

print("Data saved to top_20_movies.csv")


# Calculate the average rating
average_rating = df['Rating'].astype(float).mean()
print(f"Average Rating of Top 20 Movies: {average_rating:.2f}")
