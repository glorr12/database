
filter={}
sort=list({
    'Danceability': -1,
    'Energy': -1
}.items())
limit=1

result = client['ich']['Spotify_Youtube'].find(
  filter=filter,
  sort=sort,
  limit=limit
)


# -----------------------------------------------------


filter={
    'Album_type': {
        '$ne': 'compilation'
    }
}
sort=list({
    'Duration_ms': -1
}.items())
limit=1

result = client['ich']['Spotify_Youtube'].find(
  filter=filter,
  sort=sort,
  limit=limit
)
# -----------------------------------------------------

result = client['ich']['Spotify_Youtube'].aggregate([
    {
        '$group': {
            '_id': '$Album',
            'track_count': {
                '$sum': 1
            }
        }
    }, {
        '$sort': {
            'track_count': -1
        }
    }, {
        '$limit': 1
    }
])
# -----------------------------------------------------

filter={}
project={
    'Views': 1
}
sort=list({
    'Stream': -1
}.items())
limit=1

result = client['ich']['Spotify_Youtube'].find(
  filter=filter,
  projection=project,
  sort=sort,
  limit=limit
)
