from ins_import import ins2
from datetime import datetime, timedelta
import numpy as np
import pandas as pd

### Copy data
ins1 = ins2.copy(deep=True)

### Create posts release date
# ins1['release_date'] = datetime.strftime(datetime.now() - timedelta(1),'%Y-%m-%d')  #Today
ins1['crawl_date'] = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')


### Remove Punctuations
ins1['post_topic'] = ins1['post_topic'].str.replace('[^\w\s]', '')

### Lowercase
ins1["post_topic"] = ins1["post_topic"].str.lower()

### Word Frequency
# sina1.post_topic.str.split(expand=True).stack().value_counts()

###
