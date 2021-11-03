import pandas as pd
from Preprocessing import sina1
import numpy as np

columns = ["brand", "release_date", "social_media", "mentions", "total_comments", "totoal_forwards", "total_likes",
           "num_male", "num_female"]

stat_sina = pd.DataFrame(columns=columns)

stat_sina['brand'] = ["Fendi", "Lane Crawford", "Louis Vuitton", "Gucci", "Hermes"]
stat_sina['release_date'] = sina1['release_date']
stat_sina['social_media'] = sina1['source_platform']

for i in range(5):
    stat_sina.loc[i, 'mentions'] = len(np.where(sina1['search'] == stat_sina.loc[i, 'brand'])[0].tolist())

# print(fifa[['scaled_sliding_tackle', 'scaled_aggression', 'cluster_labels']].groupby('cluster_labels').mean())

