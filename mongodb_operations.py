from pymongo import MongoClient
from bson.objectid import ObjectId

class MongoDBOperation:
    import environment
    
    def __init__(self, uri=environment.DB_URI, db_name=environment.DB_NAME, collection_name=environment.DB_COLLECTION_NAME):
        try:
            self.client = MongoClient(uri)
            self.db = self.client.get_database(db_name)
            self.collection = self.db.get_collection(collection_name)
        except Exception as e:
            print(f"Error occurred while connecting to the database: {e}")
            raise

    def add_record(self, record):
        try:
            self.collection.insert_one(record)
        except Exception as e:
            print(f"Error occurred while adding record: {e}")
            raise

    def remove_record(self, record_id):
        try:
            self.collection.delete_one({'_id': ObjectId(record_id)})
        except bson.errors.InvalidId:
            print(f"Invalid ObjectId: {record_id}")
            raise
        except Exception as e:
            print(f"Error occurred while removing record: {e}")
            raise

    def update_record(self, record_id, updates):
        try:
            self.collection.update_one({'_id': ObjectId(record_id)}, {'$set': updates})
        except bson.errors.InvalidId:
            print(f"Invalid ObjectId: {record_id}")
            raise
        except Exception as e:
            print(f"Error occurred while updating record: {e}")
            raise

    def view_all_records(self):
        try:
            return [record for record in self.collection.find()]
        except Exception as e:
            print(f"Error occurred while retrieving all records: {e}")
            raise

    def view_specific_record(self, filters):
        try:
            return [record for record in self.collection.find(filters)]
        except Exception as e:
            print(f"Error occurred while retrieving specific record: {e}")
            raise