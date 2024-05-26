import chromadb
from chromadb.utils import embedding_functions
import streamlit as st
from TMDB import api_response
from YTS_url import get_movie_page_url

# Initialize ChromaDB client and collection
chroma_client = chromadb.PersistentClient(path="tmdbtopmovies")
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="models")
collection = chroma_client.get_or_create_collection(name="movies_collection", embedding_function=sentence_transformer_ef)


# Streamlit UI
st.title("TMDB semantic Movie search")
query = st.text_input("Enter your query here:")
col3, col4 = st.columns([1, 1])
with col3:
    n_movies = st.slider("Select number of movies to display:", 1, 20,3)
with col4:
    min_year = st.slider("Select minimum release year:", 1900, 2025, 1900)


@st.cache_data(show_spinner=False)
def search_movie(query, n_movies, min_year):
    return collection.query(query_texts=[query], n_results=n_movies, where={"release_year": {"$gte": min_year}})

if st.button("Search"):

    results = search_movie(query, n_movies, min_year)

    for i, result in enumerate(results["metadatas"][0]):
        movie_id = results['ids'][0][i]
        api_data = api_response(movie_id)
        if not api_data:
            st.write("Error fetching data for movie:", result['title'])
            continue
        imdb_url = api_data["imdb_url"] if "imdb_url" in api_data else None
        tmdb_url = f"https://www.themoviedb.org/movie/{movie_id}"
        yts_url = get_movie_page_url(result['title']) 

        st.markdown(f"### [{result['title']}]({tmdb_url})")
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(api_data['poster_url'], width=300)
        with col2:
            st.markdown(f"**Genres:** {(result['genres'])}")
            st.markdown(f"**Release Year:** {result['release_year']}")
            st.markdown(f"**Runtime:** {result['runtime']} minutes")
            st.markdown(f"**Overview:** {results['documents'][0][i]}")
            if imdb_url:
                st.markdown(f"**[IMDB]({imdb_url})**")
            if yts_url:
                st.markdown(f"**[YTS]({yts_url})**")
        st.markdown("---")
