from weibo_preprocessing import sina1
from sqlalchemy import create_engine

# Change charset to utf8mb4
engine = create_engine(
    str(r"mysql+mysqldb://%s:" + '%s' + "@%s/%s?charset=utf8mb4") % ('root', 'Ss.768754763', '115.28.187.85',
                                                                     'bi_db'))
sina1.to_sql(name='social_media', con=engine, if_exists='append', index=False)
sina1.to_sql(name='social_media_backup', con=engine, if_exists='append', index=False)

