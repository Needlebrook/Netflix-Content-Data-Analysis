import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
df = pd.read_csv("netflix_dataset.csv")
# Remove duplicates
df.drop_duplicates(inplace=True)
# Drop rows missing crucial fields
df.dropna(subset=['type', 'title', 'release_year'], inplace=True)
# Fill remaining missing values with 'Unknown'
df.fillna('Unknown', inplace=True)

print(len(df))
print("no. of movies",len(df[df['type']=='Movie']))
print("no. of TV Shows",len(df[df['type']=='TV Show']))
# Make sure 'listed_in' column has no missing values
genre_series = df['listed_in'].dropna().str.split(', ').explode()

# Count how many times 'Drama' appears
drama_count = (genre_series == 'Dramas').sum()

print(f"Number of titles tagged with Dramas: {drama_count}")


# Count how many times 'Drama' appears
drama_count = (genre_series == 'International Movies').sum()

print(f"Number of titles tagged with International Movies: {drama_count}")

# Count how many times 'Comedy' appears
drama_count = (genre_series == 'Comedies').sum()

print(f"Number of titles tagged with comedies: {drama_count}")


plt.figure(figsize=(5,7))
sns.countplot(data=df, x='type', palette='colorblind')
plt.title('Distribution of Content Types on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()

countries_series = df['country'].dropna().str.split(',')
# Flatten the list and strip whitespace
all_countries = countries_series.explode().str.strip()
# Count and plot
top_countries = all_countries.value_counts().head(20)
plt.figure(figsize=(10,5))
top_countries.plot(kind='barh', color='violet')
plt.title('Top 20 Countries by Content Count')
plt.xlabel('Number of Titles')
plt.gca().invert_yaxis()
plt.show()

genre_series = df['listed_in'].str.split(', ').explode()
top_genres = genre_series.value_counts().head(15)
plt.figure(figsize=(10,4))
sns.barplot(x=top_genres.values, y=top_genres.index, palette='Set1')
plt.title('Top 15 Genres on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Genre')
plt.show()

plt.figure(figsize=(12,6))
df['release_year'].value_counts().sort_index().plot(kind='line',
marker='*')
plt.title('Number of Titles Released Each Year')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.grid(True)
plt.show()

top_ratings = df['rating'].value_counts().head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_ratings.index, y=top_ratings.values,
palette='cool')
plt.title('Top Content Ratings on Netflix')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()

movies = df[df['type'] == 'Movie'].copy()
movies['duration'] = movies['duration'].str.replace(' min', '')
movies['duration'] = pd.to_numeric(movies['duration'],
errors='coerce')
plt.figure(figsize=(10,5))
sns.histplot(movies['duration'].dropna(), bins=30, kde=True,
color='coral')
plt.title('Distribution of Movie Durations')
plt.xlabel('Duration (minutes)')
plt.ylabel('Frequency')
plt.show()

tv_shows = df[df['type'] == 'TV Show'].copy()
tv_shows['duration'] = tv_shows['duration'].str.replace(' Season', '')
tv_shows['duration'] = tv_shows['duration'].str.replace('s', '')
tv_shows['duration'] = pd.to_numeric(tv_shows['duration'],
errors='coerce')
plt.figure(figsize=(10,5))
sns.countplot(x='duration', data=tv_shows, palette='deep')
plt.title('Distribution of Number of Seasons in TV Shows')
plt.xlabel('Number of Seasons')
plt.ylabel('Number of Shows')
plt.show()

valid_directors = df[df['director'] != 'Unknown']
directors_series = valid_directors['director'].str.split(', ').explode()
top_directors = directors_series.value_counts().head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=top_directors.values, y=top_directors.index,
palette='mako')
plt.title('Top 10 Directors on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Director')
plt.show()

valid_cast = df[df['cast'] != 'Unknown']
cast_series = valid_cast['cast'].str.split(', ').explode()
top_cast = cast_series.value_counts().head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_cast.values, y=top_cast.index, palette='coolwarm')
plt.title('Top 10 Most Frequent Cast Members on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Actor/Actress')
plt.show()