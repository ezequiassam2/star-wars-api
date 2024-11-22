from bson import ObjectId

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

def to_object_id(film_id):
    return ObjectId(film_id)