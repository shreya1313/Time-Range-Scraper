from google_search import GoogleSearch
import datetime
from calendar import monthrange
import json

search = GoogleSearch()

pd_result = {}


YEAR = 2018
for month in range(1, 13):
    no_days = monthrange(YEAR, month)
    START_DATE = datetime.datetime(YEAR, month, 1, 0, 0)
    END_DATE = datetime.datetime(YEAR, month, no_days[1], 0, 0)
    data = search.filter_by_time(
        'python developer', START_DATE,
        END_DATE, 10
    )
    data = list(filter(lambda x: 'jobs' not in x, data))
    pd_result.update({START_DATE.strftime("%b"): data})


with open('next_page_pd.json', 'w') as f:
    json.dump(pd_result, f)
