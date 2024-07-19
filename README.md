### Project Description: Movie Recommender System

**Overview:**
The Movie Recommender System is a web application built using Streamlit that provides movie recommendations based on user input. It leverages a pre-trained similarity model to suggest movies similar to a selected title and fetches movie posters from The Movie Database (TMDb) API to enhance the user experience.

**Features:**

1. **Movie Recommendations:**
   - Users can select a movie title from a dropdown menu.
   - Upon selection, the app recommends movies similar to the chosen title using a similarity matrix.
   - The recommendations are based on a precomputed similarity model that evaluates how closely related different movies are.

2. **Poster Fetching:**
   - For each recommended movie, the app retrieves and displays a poster image.
   - The app includes a retry mechanism to handle errors while fetching posters from the TMDb API, ensuring a smoother user experience even when network issues occur.

3. **User Interface:**
   - The app features an intuitive interface where users can interact with a simple dropdown menu to choose a movie and a button to trigger recommendations.
   - Recommended movies and their posters are displayed in a grid format, making it easy for users to browse through suggestions.

4. **Error Handling:**
   - Includes robust error handling with retry logic to manage network-related issues when fetching movie posters.
   - Displays appropriate error messages if a poster cannot be fetched, maintaining a user-friendly experience.

5. **Footer:**
   - A fixed footer at the bottom of the page credits the developer, ensuring the project’s contributions are acknowledged.

**Technical Stack:**
- **Streamlit:** For building the web application interface.
- **Pandas:** For handling movie data.
- **Pickle:** For loading precomputed data such as movie details and similarity matrices.
- **Requests:** For making API calls to fetch movie posters.
- **Tenacity:** For implementing retry logic to handle API request failures.

**Usage:**
 To use the app, simply select a movie from the dropdown menu and click the "Recommend" button.
- The app will then display a list of similar movies along with their posters.

**Conclusion:**
This Movie Recommender System offers a user-friendly way to discover new movies based on your preferences, with visually appealing poster images to enhance the overall experience. It combines data science with practical web development to provide a valuable tool for movie enthusiasts.

### OUTPUT


![m1](https://github.com/user-attachments/assets/6e706c40-9597-4679-a228-00c3ce229306)
![m2](https://github.com/user-attachments/assets/c5b167c9-5817-427e-9eb1-3e0484361bc4)
![m3](https://github.com/user-attachments/assets/fcb1d684-bb40-4cb9-8319-c30a6b8d5c6c)
![m4](https://github.com/user-attachments/assets/5e132768-071d-4d78-a4c1-9cfda2e8c52d)
