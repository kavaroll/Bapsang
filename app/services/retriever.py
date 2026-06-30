from app.db.chroma import get_collection


class Retriever:

    def __init__(self):
        self.collection = get_collection()

    def search(self, query, k=5):

        result = self.collection.query(
            query_texts=[query],
            n_results=k,
        )

        return result["documents"][0]