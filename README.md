&emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp;[![logo](https://github.com/petrarkaselin/song_recommender/blob/main/ironhack_logo.png)](https://github.com/petrarkaselin/song_recommender/blob/main/ironhack_logo.png)

# Song Recommender
Our **Song Recommender** app is like your personal music matchmaker! Just tell us a song and artist you love, and we'll handpick five more tracks that we think you'll absolutely adore. It's all about making your music journey more personalized and enjoyable!

![cover](https://github.com/petrarkaselin/song_recommender/blob/main/presentation/cover.jpg)

### Team:
##### &emsp;   Alice De Ghetto
##### &emsp;   Noelia Oriola Escobar
##### &emsp;   Olabisi Matthew
##### &emsp;   Tatyana Tarasova
###
#### Goal
The goal of the project was to create a presentation visualizing how the algorithm works that the data analysts created during a project. The presentation played off of the scenario of a pitch meeting with investors to secure funding for the app.

![front_vs_back](https://github.com/petrarkaselin/song_recommender/blob/main/presentation/front_vs_back.jpg)
#### Object
To create an algorithm that takes the user's song and fetches the song's audio features from Spotify over the unique song ID. As an output the algorithm gives back recommendations from the chosen database.
#### Criteria for recommendations:
- Songs that are actually similar to the ones they picked from an acoustic point of view.
- Songs that are popular around the world right now, independently from their tastes.

#### Datasets
- Top 100 Songs from Billboard
- 2500 Songs 

![dataset](https://github.com/petrarkaselin/song_recommender/blob/main/presentation/dataset.jpg)

#### Methods:
- Data collection:
    - HTML - WebScraping
    - Spotify's API
- Unsupervised machine learning:
    - UMAP Dimensionality Reduction
    - K-Means Clustering 
- Front-end development:
    - Steamlit

#### Workflow of the app
**Step 1** A user inputs a song title and an artist (partial input is also accepted). 

![step_1](https://github.com/petrarkaselin/song_recommender/blob/main/presentation/step_1.jpg)

**Step 2** The algorithm checks if there are songs with the same title, it can be a song with the same title but different artist, or another version of the same songs. User gets a list with 5 of these songs, they can choose a song from the list or get another set of songs.

![step_2](https://github.com/petrarkaselin/song_recommender/blob/main/presentation/step_2.jpg)

**Step 3** The user gets a link to the song, based on recommendations mentioned before. If the user's song is one of the Top 100, then a recommended song will also be from the same list. Otherwise the recommended song will be from the larger dataset.

![step_3](https://github.com/petrarkaselin/song_recommender/blob/main/presentation/step_3.jpg)

Song Recommender app not only offers a personalized and enjoyable music discovery experience but also represents the culmination of a comprehensive data analysis project. The goal was to create an algorithm that not only fetches song audio features from Spotify but also provides recommendations based on acoustic similarities and global popularity. Leveraging datasets from Billboard's Top 100 Songs and a collection of 2500 songs, our algorithm, employing techniques like UMAP Dimensionality Reduction and K-Means Clustering, ensures that the suggestions align with the user's preferences.

![cover_2](https://github.com/petrarkaselin/song_recommender/blob/main/presentation/cover_2.jpg)
