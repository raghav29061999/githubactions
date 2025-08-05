import pandas as pd
import numpy as np
import re
import string
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.manifold import TSNE
from sentence_transformers import SentenceTransformer
import hdbscan

# ------------------------------
# Second-level clustering using cluster labels
# ------------------------------
def process_cluster_labels(df):
    # Step 1: Take unique cluster labels
    unique_labels = df['cluster_label'].unique().tolist()
    
    # Step 2: Embed cluster labels
    embedder = EmbeddingModel()
    label_embeddings = embedder.encode(unique_labels)
    
    # Step 3: Reduce dimensions using t-SNE (for better separability)
    reduced_embeddings = reduce_dimensions_tsne(label_embeddings)
    
    # Step 4: Cluster again (super-clusters)
    super_clusters = cluster_issues(reduced_embeddings)
    
    # Step 5: Map super-cluster IDs back to original dataframe
    label_to_super = dict(zip(unique_labels, super_clusters))
    df['super_cluster'] = df['cluster_label'].map(label_to_super)
    
    return df, unique_labels, super_clusters, reduced_embeddings

# ------------------------------
# Visualization for cluster labels
# ------------------------------
def plot_super_clusters(unique_labels, reduced_embeddings, super_clusters):
    plt.figure(figsize=(8,6))
    for cluster in set(super_clusters):
        idx = [i for i, c in enumerate(super_clusters) if c == cluster]
        plt.scatter(reduced_embeddings[idx,0], reduced_embeddings[idx,1], label=f"SuperCluster {cluster}", alpha=0.7)
        for i in idx:
            plt.text(reduced_embeddings[i,0], reduced_embeddings[i,1], unique_labels[i], fontsize=9)
    plt.legend()
    plt.title("t-SNE Super-Clusters of Cluster Labels")
    plt.show()


# Assume df already has: issue, cleaned, cluster, cluster_label
df, unique_labels, super_clusters, reduced_embeddings = process_cluster_labels(df)

# Visualize super-clusters
plot_super_clusters(unique_labels, reduced_embeddings, super_clusters)
print(df[['issue', 'cluster', 'cluster_label', 'super_cluster']])

