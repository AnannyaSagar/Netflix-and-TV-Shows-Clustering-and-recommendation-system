
import pickle
import streamlit as st
import requests
import pandas as pd
import pickle as pkl

movies = pickle.load(open(r'movies_dict.pkl','rb'))
movies = pd.DataFrame(movies)
#print(movies.columns)
movie_names = movies["title"].values
# movie_names = movies["title"].values
#print(movie_names)


similarity = pickle.load(open(r'similarity.pkl','rb'))

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    #recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        #movie_id = movies.iloc[i[0]].show_id
        #recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names#recommended_movie_posters



st.header('Movie Recommender System')
option = st.selectbox(
    'Select a movie',
    (movie_names))

st.write('You selected:', option)

# if st.button('Recommend'):
#     st.write(option)

if st.button('Recommend') :
    recommendations = recommend (option)
    for i in recommendations:
        st.write(i)


