import pandas as pd
import matplotlib.pyplot as plt

table_of_shows = pd.read_csv("imdb_top_1000.csv")
# print(dataframe.head())
# print(table_of_shows.describe())
# my_df=pd.DataFrame({table_of_shows})
# print(my_df)
# print(type(table_of_shows))

brief_df = table_of_shows[['Series_Title', 'Genre', 'Director', 'IMDB_Rating']].copy()


# print(brief_df)
# print((brief_df[pd.isnull(brief_df.Series_Title)]))


def check_missing_values():
    if "Empty DataFrame" in brief_df[pd.isnull(brief_df.Series_Title)]:
        print("there is empty data in Series_Title column")
    elif "Empty DataFrame" in brief_df[pd.isnull(brief_df.Genre)]:
        print("there is empty data in Genre column")
    elif "Empty DataFrame" in brief_df[pd.isnull(brief_df.Director)]:
        print("there is empty data in Director column")
    elif "Empty DataFrame" in brief_df[pd.isnull(brief_df.IMDB_Rating)]:
        print("there is empty data in IMDB_Rating column ")
    else:
        print("missing values checked : no empty data")


#  missing_Series_Title=brief_df[pd.isnull(brief_df.Series_Title)]
# missing_Series_Title=brief_df[pd.isnull(brief_df.Series_Title)]
# missing_Series_Title=brief_df[pd.isnull(brief_df.Series_Title)]


brief_df['Genre'] = brief_df['Genre'].str.split(', ')
df_exploded = brief_df.explode('Genre')
genre_counts = df_exploded['Genre'].value_counts()
most_popular_genre = genre_counts.idxmax()

check_missing_values()
print("____________________________________________")
print("most popular genre is: " + most_popular_genre)
print("____________________________________________")
genre_counts_df = pd.DataFrame({'Genre': genre_counts.index, 'Count': genre_counts.values})
print(genre_counts_df)
genre_counts_df = genre_counts_df.sort_values('Count', ascending=False)



director_avg_ratings = brief_df.groupby('Director')['IMDB_Rating'].mean()
director_ratings_df = pd.DataFrame({'Director': director_avg_ratings.index, 'IMDB_Rating': director_avg_ratings.values})
director_ratings_df = director_ratings_df.sort_values('IMDB_Rating', ascending=False)
top_10_directors = director_ratings_df.head(10)



plt.figure(figsize=(12, 6))
plt.bar(genre_counts_df['Genre'], genre_counts_df['Count'])
plt.xlabel('Genre')
plt.ylabel('Count')
plt.title('Most Popular Genres of Movies/TV Shows')
plt.xticks(rotation=45)


plt.figure(figsize=(12, 6))
plt.bar(top_10_directors['Director'], top_10_directors['IMDB_Rating'])
plt.xlabel('Director')
plt.ylabel('IMDB Rating')
plt.title('Top 10 Directors based on IMDB Rating of Movies/TV Shows')
plt.xticks(rotation=45)
plt.show()







