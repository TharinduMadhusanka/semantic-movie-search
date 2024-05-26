# semantic-movie-search TMDB Top Movies

This Streamlit app allows you to search for top movies from TMDB and displays detailed information about them, including links to their YTS pages if available.

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/TharinduMadhusanka/semantic-movie-search.git
    cd tmdb_top_movies
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file in the project root** and add your TMDB API key:
    ```bash
    echo "TMDB_API_KEY=your_tmdb_api_key" > .env
    ```
    Replace `your_tmdb_api_key` with your actual TMDB API key. You can create an API key by registering on the [TMDB website](https://www.themoviedb.org/).

5. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

## Usage

- Enter a query in the text input field.
- Select the number of movies to display.
- Select the minimum release year.
- Click the "Search" button to view the results.

## Project Structure

- `app.py`: Main application code.
- `TMDB.py`: Contains the `api_response` function to fetch data from TMDB API.
- `YTS_url.py`: Contains the `get_movie_page_url` function to get the YTS movie page URL.
- `requirements.txt`: Lists the dependencies.
- `.gitignore`: Specifies files and directories to ignore.
- `README.md`: Provides an overview and instructions on how to run the project.

## Database (Optional)

You can create your own vector database for storing and querying movie embeddings using ChromaDB. If you don't want to create a new database, the app can still run without it.

## License

This project is licensed under the MIT License.
