import pandas as pd
import duckdb as db
import networkx as nx
from node2vec import Node2Vec

NUM_PLAYLISTS = 1000

contents = pd.read_parquet("../data/parquet/playlist_contents.parquet")
playlist_meta = pd.read_parquet("../data/parquet/playlist_metadata.parquet")
track_meta = pd.read_parquet("../data/parquet/track_metadata.parquet")

playlist_meta = playlist_meta[playlist_meta["pid"] < NUM_PLAYLISTS]

sampled_playlists = playlist_meta[playlist_meta["pid"] < NUM_PLAYLISTS]
data = contents.merge(sampled_playlists[["pid", "num_tracks"]], on="pid", how="inner")
data = data.merge(track_meta[["track_uri", "artist_uri"]], on="track_uri", how="inner")

artist_edges = db.sql("SELECT pid AS source, artist_uri AS target, COUNT(*) AS weight FROM data GROUP BY pid, artist_uri").df()

G = nx.from_pandas_edgelist(
    artist_edges,
    source="source",
    target="target",
    edge_attr="weight",
    create_using=nx.Graph()
)

node2vec = Node2Vec(
    G,
    dimensions=64,
    walk_length=20,
    num_walks=100,
    p=1.0,
    q=0.5,
    weight_key='weight',
    workers=8
)

model = node2vec.fit(window=5, min_count=1)

nodes = [str(n) for n in G.nodes()]
emb_matrix = [model.wv[n] for n in nodes]
dim = len(emb_matrix[0])
columns = [f"emb_{i}" for i in range(dim)]

emb_df = pd.DataFrame(emb_matrix, index=nodes, columns=columns).reset_index()
emb_df = emb_df.rename(columns={"index": "node"})

playlist_embs = emb_df[emb_df["node"].isin(sampled_playlists["pid"].astype(str))]
artist_embs = emb_df[~emb_df["node"].isin(sampled_playlists["pid"].astype(str))]

playlist_embs.to_parquet("./playlist_embeddings.parquet", index=False)
artist_embs.to_parquet("./artist_embeddings.parquet", index=False)
