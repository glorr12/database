{
    'writers': {from pymongo import MongoClient

client = MongoClient('mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich')
filter={
    'writers': {
        '$size': 3
    },
    'directors': {
        '$size': 2
    }
}

result = client['ich']['imdb'].find(
  filter=filter
)
# -------------------------

client = MongoClient('mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich')
filter={
    'vin': 'WME4530421Y135045'
}
project={
    'final_address': 1,
    'final_date': 1,
    'final_time': 1
}
sort=list({
    'final_date': -1
}.items())
limit=1

result = client['ich']['bookings'].find(
  filter=filter,
  projection=project,
  sort=sort,
  limit=limit
)
# -------------------------

client = MongoClient('mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich')
result = client['ich']['bookings'].aggregate([
    {
        '$match': {
            'final_fuel': 0
        }
    }, {
        '$count': 'count' #30
    }
])

# -------------------------


client = MongoClient('mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich')
filter={}
project={
    'plate': 1,
    'vin': 1,
    'distance': -1,
    '_id': 0
}
sort=list({
    'distance': -1
}.items())
limit=1

result = client['ich']['bookings'].find(
  filter=filter,
  projection=project,
  sort=sort,
  limit=limit
)

# -------------------------

client = MongoClient('mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich')
result = client['ich']['imdb'].aggregate([
    {
        '$match': {
            'cast': 'Brad Pitt'
        }
    }, {
        '$addFields': {
            'ratingNum': {
                '$convert': {
                    'input': '$imdb.rating',
                    'to': 'double',
                    'onError': -1,
                    'onNull': -1
                }
            }
        }
    }, {
        '$sort': {
            'ratingNum': -1
        }
    }, {
        '$limit': 1
    }, {
        '$project': {
            '_id': 0,
            'title': 1,
            'year': 1,
            'imdb.rating': 1
        }
    }
])
# --------------------

