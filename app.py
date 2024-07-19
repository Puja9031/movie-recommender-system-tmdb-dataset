import pandas as pd
import pickle
import streamlit as st
import requests
from tenacity import retry, stop_after_attempt, wait_fixed, RetryError

# Fetch poster function with retry logic
@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def fetch_poster(movie_id):
    try:
        response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=850b1529d7d143cc13fd5f8d07db5138&language=en-US')
        response.raise_for_status()  # Raise an HTTPError if the response code was unsuccessful
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f'http://image.tmdb.org/t/p/w500/{poster_path}'
        else:
            return "No poster available"
    except requests.exceptions.RequestException as e:
        raise RetryError(f"An error occurred: {e}")

# Title of the Streamlit app
st.title('🎬 Movie Recommender System')

# Load the movies dictionary and similarity data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies_df = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommend function to get movie recommendations and posters
def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended = []
    recommended_movie_posters = []
    for i in movie_list:
        movie_id = movies_df.iloc[i[0]].movie_id
        recommended.append(movies_df.iloc[i[0]].title)
        try:
            recommended_movie_posters.append(fetch_poster(movie_id))
        except RetryError as e:
            recommended_movie_posters.append("An error occurred fetching poster")

    return recommended, recommended_movie_posters


# Select box for movie selection
selected_movie_name = st.selectbox(
    "Which movie suggestions are you looking for?",
    movies_df['title'].values
)

# Button to get recommendations
if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    # Display recommended movies and posters
    cols = st.columns(5)

    for col, name, poster in zip(cols, names, posters):
        with col:
            st.markdown(f"#### {name}")
            if "An error occurred" in poster:
                st.error(poster)
            else:
                st.image(poster)




# Add some spacing and footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            color: black;
            text-align: center;
            padding: 10px;
        }
    </style>
    <div class="footer">
        <p>Developed by PUJA</p>
    </div>
""", unsafe_allow_html=True)