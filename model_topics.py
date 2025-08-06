def generate_super_cluster_labels(df, cluster_col='super_cluster', label_col='cluster_label', top_n=3):
    super_cluster_labels = {}
    for super_cluster_id in df[cluster_col].unique():
        if super_cluster_id == -1:
            # Keep unclustered as a fixed label
            super_cluster_labels[super_cluster_id] = "Unclustered"
            continue
        
        sub_labels = df[df[cluster_col] == super_cluster_id][label_col].tolist()
        # Combine all labels into one text
        combined_text = ' '.join(sub_labels).lower()
        # Remove stopwords & split
        words = [w for w in re.findall(r'\w+', combined_text) if w not in ENGLISH_STOP_WORDS]
        # Get top N keywords
        most_common = [w for w, _ in Counter(words).most_common(top_n)]
        # Join them as a label
        super_cluster_labels[super_cluster_id] = ' '.join(most_common)
    
    # Assign back to df
    df['super_cluster_label'] = df[cluster_col].map(super_cluster_labels)
    return df, super_cluster_labels
