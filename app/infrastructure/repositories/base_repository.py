from app.infrastructure import mongo


class BaseRepository:
    def __init__(self, collection_name):
        self.collection_name = collection_name

    @property
    def collection(self):
        if not hasattr(mongo, 'db') or mongo.db is None:
            raise RuntimeError("MongoDB instance is not initialized")
        return mongo.db[self.collection_name]

    @property
    def db(self):
        return mongo.db

    def get_next_sequence(self, name):
        sequence_document = self.db.counters.find_one_and_update(
            {'_id': name},
            {'$inc': {'sequence_value': 1}},
            return_document=True,
            upsert=True
        )
        return sequence_document['sequence_value']
