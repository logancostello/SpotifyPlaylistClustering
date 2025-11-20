import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

K_CLUSTERS = 19

playlist_embeddings = pd.read_parquet("playlist_embeddings.parquet")

scaler = StandardScaler()
features_scaled = scaler.fit_transform(playlist_embeddings[[f"emb_{i}" for i in range(0, 64)]])

kmeans = KMeans(n_clusters=K_CLUSTERS, random_state=42, n_init=10)
playlist_embeddings["cluster"] = kmeans.fit_predict(features_scaled)

sil_score = silhouette_score(features_scaled, playlist_embeddings["cluster"])
print(f"Silhouette Score for K={K_CLUSTERS}: {sil_score:.4f}")

playlist_embeddings.to_parquet("playlist_embeddings.parquet")