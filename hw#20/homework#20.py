import re
from pymongo import MongoClient

{
    'borough': 'Staten Island',
    'name': re.compile(r"pizza(?i)")
}

result = client['sample_data']['restaurants'].find(
  filter=filter
)


# -------------------------------------------

result = client['sample_data']['restaurants'].aggregate([
    {
        '$project': {
            '_id': 0,
            'name': 1,
            'grades.score': {
                '$avg': '$grades.score'
            }
        }
    }, {
        '$sort': {
            'grades.score': -1
        }
    }, {
        '$limit': 5
    }
])