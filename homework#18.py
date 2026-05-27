from pymongo import MongoClient

client = MongoClient('mongodb+srv://igorfishkov1991_db_user:EP300847@cluster0.ovy4u8e.mongodb.net/')
result = client['sample_airbnb']['listingsAndReviews'].aggregate([
    {
        '$match': {
            'address.market': {
                '$in': [
                    'Oahu', 'Maui', 'The Big Island', 'Kauai'
                ]
            }
        }
    }, {
        '$group': {
            '_id': None,
            'avg_price': {
                '$avg': '$price'
            }
        }
    }
])


# ---------------------------------------------------



from pymongo import MongoClient


client = MongoClient('mongodb+srv://igorfishkov1991_db_user:EP300847@cluster0.ovy4u8e.mongodb.net/')
result = client['sample_mflix']['movies'].aggregate([
    {
        '$match': {
            'imdb.rating': {
                '$gt': 8
            },
            'year': {
                '$gte': 2015,
                '$lte': 2023
            }
        }
    }, {
        '$sort': {
            'imdb.rating': -1
        }
    }, {
        '$limit': 1
    }
])