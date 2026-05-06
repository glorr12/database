/**
 * _id: The id of the group.
 * fieldN: The first field name.
 */
{
  _id: null,
  average_age: {
    $avg: "$age"
  }
}

# ------------------------------------------------


db.getCollection('orders_Igor').aggregate(
  [{ $count: 'sold' }],
  { maxTimeMS: 60000, allowDiskUse: true }
);
# ------------------------------------------------


[
    {
        '$match': {
            'product': 'Apple'
        }
    }, {
        '$count': 'apple_orders'
    }
]

# ------------------------------------------------

client = MongoClient('mongodb://ich_editor:verystrongpassword@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich_edit')
filter={}
project={
    'id': 1,
    '_id': 0
}
sort=list({
    'amount': -1
}.items())
limit=3

result = client['ich_edit']['orders_Igor'].find(
  filter=filter,
  projection=project,
  sort=sort,
  limit=limit
)


# ------------------------------------------------


client = MongoClient('mongodb://ich_editor:verystrongpassword@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich_edit')
filter={
    'city': 'Berlin'
}

result = client['ich_edit']['orders_Igor'].find(
  filter=filter
)

# ------------------------------------------------

client = MongoClient('mongodb://ich_editor:verystrongpassword@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich_edit')
result = client['ich_edit']['orders_Igor'].aggregate([
    {
        '$match': {
            'city': {
                '$in': [
                    'Berlin', 'Madrid'
                ]
            }
        }
    }, {
        '$match': {
            'product': 'Apple'
        }
    }, {
        '$group': {
            '_id': None,
            'total_count': {
                '$sum': 1
            },
            'total_amount': {
                '$sum': '$amount'
            }
        }
    }
])
# ------------------------------------------------

client = MongoClient('mongodb://ich_editor:verystrongpassword@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich_edit')
result = client['ich_edit']['orders_Igor'].aggregate([
    {
        '$group': {
            '_id': '$customer',
            'total': {
                '$sum': '$amount'
            }
        }
    }
])

# ------------------------------------------------


client = MongoClient('mongodb://ich_editor:verystrongpassword@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich_edit')
result = client['ich_edit']['orders_Igor'].aggregate([
    {
        '$match': {
            'customer': 'Olga'
        }
    }, {
        '$group': {
            '_id': '$city'
        }
    }
])