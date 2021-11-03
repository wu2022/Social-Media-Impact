from weibo_import import sina2
from datetime import datetime, timedelta
import numpy as np
import pandas as pd


### Copy data
sina1 = sina2.copy(deep=True)

### Create posts release date
# sina1['crawl_date'] = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d') #Today
sina1['crawl_date'] = pd.to_datetime(sina1['crawl_date']).dt.date

### Unify Names
names = {'古驰': 'Gucci',
         '路易威登': 'Louis Vuitton',
         '芬迪': 'Fendi',
         '爱马仕': 'Hermes'}

for old, new in names.items():
    for i in sina1['search_keyword'].index:
        if sina1['search_keyword'][i] == old:
            sina1['search_keyword'][i] = new

sina1['search_keyword'] = sina1['search_keyword'].str.title()

### Remove Duplicate
columns = ['user_id', 'user_name', 'user_age', 'user_sex', 'industry_type', 'friend_link',
           'user_head_url', 'user_country', 'user_follow', 'post_url', 'post_id', 'post_content',
           'post_topic', 'post_like_num', 'post_forward_num', 'post_comment_num', 'post_time',
           'search_keyword', 'user_tag', 'post_comment', 'user_info', 'platform_certification',
           'platform_source', 'post_user_url', 'crawl_date']

dat1 = pd.DataFrame(columns=columns)
for i in np.unique(sina1['search_keyword']):
    rows = np.where(sina1['search_keyword'] == i)
    rows = rows[0].tolist()
    dat = sina1.iloc[rows,].drop_duplicates(subset=['post_id'])
    dat1 = dat1.append(dat, sort=False)

sina1 = dat1.copy(deep=True)

### Remove Punctuations
sina1['post_topic'] = sina1['post_topic'].str.replace('[^\w\s]', '')

### Lowercase
sina1["post_topic"] = sina1["post_topic"].str.lower()

### Word Frequency
# sina1.post_topic.str.split(expand=True).stack().value_counts()
