
result = client['sample_mflix']['theaters'].aggregate([
    {
        '$match': {
            'location.address.city': 'California'
        }
    }, {
        '$count': 'amount'
    }
])


# ----------------------------------------------------------
result = client['sample_airbnb']['listingsAndReviews'].aggregate([
    {
        '$sort': {
            'bedrooms': -1
        }
    }, {
        '$limit': 1
    }, {
        '$project': {
            'name': 1
        }
    }
])

# ----------------------------------------------------------

result = client['sample_airbnb']['listingsAndReviews'].aggregate([
    {
        '$match': {
            'number_of_reviews': {
                '$gte': 50
            }
        }
    }, {
        '$sort': {
            'review_scores.review_scores_rating': -1
        }
    }, {
        '$limit': 1
    }, {
        '$project': {
            'name': 1
        }
    }
])