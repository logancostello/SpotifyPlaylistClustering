# EDA Summary

## Data
The dataset is the Spotify Million Playlist dataset, including their metadata (time, number of edits, etc) and the songs on the playlist (track name, track duration, album name, and artist name).
The dataset comes from a challenge published by Spotify where participants must build a model that accepts playlists as inputs and recommends tracks to add to the playlist. 
The data is no longer officially public, but can be found at [this Kaggle dataset](https://www.kaggle.com/datasets/himanshuwagh/spotify-million). 
A formal description of the original challenge can be found [here](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge).

While participating in the challenge seems fun and challenging, I am primarily interested in using this data to discover clusters of tracks, albums, and artists. 
I've always been interested in assigning genres to music, and I've struggled with it myself when building a website that shows users statistics about their listening habits on Spotify. 
However, genres are limited: they only account for the sonic similarity between music. I'm interested in discovering other ways that music is similar. 
For example, what songs have similar emotional appeal, what songs are typically played in a particular setting, and what songs are related in ways we would expect. 
The same questions (and many more) equally apply to artists and albums as well.

With the million playlists, I plan on using the graph of playlists, artists, albums, and tracks to learn latent features that describe each. 
Those features will then be used to cluster the music. The clusters will be analyzed for logic and sanity, but more importantly to see what interesting similarities exist.

## Discoveries
<img width="868" height="547" alt="image" src="https://github.com/user-attachments/assets/f583d6c4-0073-4777-bf3a-e1a8aa53ff4b" />

It appears that the number of tracks per playlist follows a log normal distribution peaking at around 30 tracks. Interestingly there are spikes in frequency at nice, round numbers such as 50, 100, etc.
Note that there are no playlists with 0 songs and that the number of tracks abrubtlty cuts off at 250. Both of these are likely because the data is currated and sampled by Spotify, but there is a single playlist with >250 tracks.
I confirmed this was in the original data and not a bug with my preprocessing. This graph demonstrates that most playlists have a decent number of tracks on them, and thus reasonably accurate latent features should be able to be discovered for them.

<img width="850" height="547" alt="image" src="https://github.com/user-attachments/assets/f97018de-5e8b-4838-8b3e-5ce47cb1ab01" />

Not surprisingly, it appears that as the number of tracks on a playlist increases, the number of artists on a playlist increases. This demonstrates that playlists tend to have diverse tracks, at least in terms of artists.
The curve at the higher track numbers is interesting to me, as artist diversity seems to be forced for the playlists with few artists and artist repeats also seems to be forced for the playlists with many artists.
Further understanding this relationship would be interesting and possibly useful for clustering playlists.

<img width="872" height="528" alt="image" src="https://github.com/user-attachments/assets/4fc0e29c-5d2a-4005-b041-a1904a5d7905" />

While I don't know what is considered sparse for big data, this data appears to be vary sparse. The playlist-artist adjacency matrix is less sparse however, so clustering on artists might be more successful that tracks or albums. 
Understanding, addressing, and working with this sparsity will be important for discovering latent features.

## Issues and Open Questions

One problem discovered above is the sparisty of the data. While it cannot be improved, it will need to be considered when choosing ways to embed the graph.

Another problem is the amount of missing data desired for building features. For example, one feature one might want is album length. 
Since not every song on the album is guarenteed to be in the million playlists, this information cannot be properly computed. Solutions include dealing with it, or using the Spotify API to query for the missing data. Neither option is desirable.

Finally, there is the problem of outliers. 
Almost every relationship that was not visualized followed a power-law distribution. Songs exceeded 2 hours (podcasts, sleep sounds), artists had thousands of albums (Mozart), and playlists had hundreds of repeated songs. 
Finding ways to properly handle these outliers will be important moving forward.


