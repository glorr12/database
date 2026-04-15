# Requires the PyMongo package.
# https://api.mongodb.com/python/current
client = MongoClient('mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich')
filter={
    'ContactName': 'Sven Ottlieb'
}
project={
    '_id': 0,
    'ContactName': 1,
    'City': 1
}
result = client['ich']['customers'].find(
  filter=filter,
  projection=project
)
# -------------------------------------------------------
# Requires the PyMongo package.
# https://api.mongodb.com/python/current
client = MongoClient('mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich')
filter={}
sort=list({
    'age': -1
}.items())
limit=1

result = client['ich']['US_Adult_Income'].find(
  filter=filter,
  sort=sort,
  limit=limit
)

# -------------------------------------------------------
# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich')
filter={
    'age': 90
}

result = client['ich']['US_Adult_Income'].find(
  filter=filter
)

# -------------------------------------------------------
# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich')
filter={
    'education': ' IT-career-hub'
}
project={
    'education': 1
}

result = client['ich']['US_Adult_Income'].find(
  filter=filter,
  projection=project
)
# -------------------------------------------------------
# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich')
filter={
    'age': {
        '$gte': 20,
        '$lte': 30
    }
}

result = client['ich']['US_Adult_Income'].find(
  filter=filter
)
