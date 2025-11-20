# Initial Findings

## Goals
Going into this project, I was not sure how well playlists would naturally cluster, especially with so many of them. To figure out if clustering would be successful, I did some
basic embedding and clustering on a small sample of the playlists. I did this to answer the following questions:
1. Do natural clusters exist?
2. How difficult is it to make sense of a cluster? In other words, can the clusters be described without using the playlist embeddings?
3. How much of an impact does the size of the data have on methods used?

## Exploration
In order to quickly answer the questions above and to better inform further analysis, I did the following:
1. Sample 1% (1000) of the playlists to be used in exploration
2. Create a weighted bipartite where nodes are playlists and artists and edges connect an artist to a playlist with the number of times that artist appears on that playlist
3. Use Node2Vec to create embeddings for the playlists (and artists)
4. Clustered the playlists with K Means Clustering using only the discovered latent features
5. Identified the type of playlist each cluster represented using the playlist names

I did the same thing with an unweighted playlist-song graph as well, but the silhouette score of the clusters was worse. I also think focusing on artists is more interesting that songs.

## Results
<img width="783" height="654" alt="Screenshot 2025-11-19 at 10 32 06 PM" src="https://github.com/user-attachments/assets/f66c58dc-eec6-4218-99a9-85de009878d1" />

Results were contradictory. The best K (19) resulted in a silhouette score of ~0.05. Additionally, as depicted in the above graph visualizing the clusters, seperation was generally not high.
However, a manual analysis of the playlists in each cluster revealed that clustering was seemingly successful: 
clusters for latin playlists, country playlists, disney playlists, christmas playlists, korean playlists, and worship playlists  
were discovered, with other clusters being similar, although less so than those aforementioned.

To answer the target questions:
1. Natural clusters exist!
2. Labeling clusters based on playlist names moderately successful.
3. The data is massive and greatly impacts the methods used for embedding and clustering.

## Next Steps
This exploration was incredibly insightful. I now have many ideas about how I want to further this analysis:
1. Find other ways to embed the playlists. Examples include Collaborative Fitlering. Node2Vec is too slow for any decent sample size. Compare the quality of their embeddings.
2. Explore various clustering techniques, especially hierarchical clustering and Leiden's algorithm. Compare the quality of the clusters created.
3. Create text-based features to reduce the cardinality of playlist names, allowing for more precise labeling of clusters.
4. In addition to 3, find the artists and tracks that are key to each "playlist genre"
5. Finally, cluster more playlists!
6. Bonus: Do the same analysis for artists!
